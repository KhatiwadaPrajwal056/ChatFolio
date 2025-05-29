import os
import streamlit as st
from dotenv import load_dotenv
from engine.rag_engine import load_pdf_text, chunk_text, embed_chunks_nomic, retrieve_similar_chunks
from engine.booking_tool import BookingFormTool
import google.generativeai as genai

os.environ["STREAMLIT_WATCHER_TYPE"] = "none"

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL")

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel(model_name=GEMINI_MODEL)

st.set_page_config(page_title="📄 Chat with PDF + RAG & Booking", layout="centered")
st.title("📄 Chat with PDF + Booking Appointment")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if "booking_tool" not in st.session_state:
    st.session_state.booking_tool = None
if "booking_active" not in st.session_state:
    st.session_state.booking_active = False

if uploaded_file and "chunks" not in st.session_state:
    os.makedirs("docs", exist_ok=True)
    with open("docs/temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.session_state.file_uploaded = True
    st.session_state.embedding_pending = True

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant that answers based on the provided document context. You are also able to book appointments and call the customer. If asked about different question not related to the document and appointment you just need to chat based on the query not the context of the document."}
    ]

for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if st.session_state.get("embedding_pending", False):
    with st.spinner("📄 Reading and Embedding..."):
        full_text = load_pdf_text("docs/temp.pdf")
        chunks = chunk_text(full_text)
        embeddings = embed_chunks_nomic(chunks)
        st.session_state.chunks = chunks
        st.session_state.embeddings = embeddings
        st.session_state.embedding_pending = False
        st.success("✅ Document ready!")

if "chunks" in st.session_state and "embeddings" in st.session_state:

    user_input = st.chat_input("Ask about the document or request a call/appointment...")

    if user_input:
        st.chat_message("user").markdown(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})

        if st.session_state.booking_active:
            tool = st.session_state.booking_tool
            valid, error_msg = tool.validate_and_store(user_input)

            with st.chat_message("assistant"):
                if valid:
                    if tool.is_complete():
                        summary = tool.get_summary()
                        st.markdown(summary)
                        st.session_state.booking_active = False
                        st.session_state.booking_tool = None
                        st.session_state.messages.append({"role": "assistant", "content": summary})
                    else:
                        next_q = tool.get_next_question()
                        st.markdown(next_q)
                        st.session_state.messages.append({"role": "assistant", "content": next_q})
                else:
                    st.markdown(error_msg)
                    st.session_state.messages.append({"role": "assistant", "content": error_msg})

        else:
            lower_input = user_input.lower()
            if any(kw in lower_input for kw in ["call me", "book appointment", "schedule appointment", "make appointment", "contact me"]):
                st.session_state.booking_tool = BookingFormTool()
                st.session_state.booking_active = True
                first_q = st.session_state.booking_tool.get_next_question()

                with st.chat_message("assistant"):
                    st.markdown(f"Sure! Let's get your booking details.\n\n{first_q}")
                    st.session_state.messages.append({"role": "assistant", "content": first_q})

            else:
        
                with st.chat_message("assistant"):
                    with st.spinner("Thinking..."):
                        related_chunks = retrieve_similar_chunks(
                            user_input,
                            st.session_state.chunks,
                            st.session_state.embeddings,
                            top_k=3
                        )
                        context = "\n".join(related_chunks)

                        try:
                            response = model.generate_content(
                                    f"""The following document content may help:

                                {context}

                                Q: {user_input}
                                A:
                                 If asked about different question not related to the document and appointment you just need to chat based on the query not the context of the document.
                                 Your response need to be on point and relevant to the query.
                                Response for appointment booking example:
                                ✅ Your appointment is booked!

                                📅 Booking Details:
                                • Name: Prajwal
                                • Phone: +9779741
                                • Email: Khatiwada@gmail.com
                                • Date: 2029-01-01
                                
                                """
                                )

                            print(response)
                            answer = response.text.strip()
                        except Exception as e:
                            st.error(f"Error calling Gemini API: {e}")
                            answer = "Sorry, I could not generate an answer at this time."

                        st.markdown(answer)
                        st.session_state.messages.append({"role": "assistant", "content": answer})
