# Chat with Document + Conversational Booking Bot

## Project Description

This project is a Streamlit-based chatbot designed to answer user queries based on uploaded documents and collect user information through a guided conversational form for tasks like booking appointments or scheduling calls. It leverages a Retrieval-Augmented Generation (RAG) approach to provide context-aware answers from documents and integrates a conversational tool to collect structured data with input validation.

## Features

*   **Document Question Answering:** Upload a PDF document and ask questions about its content. The chatbot uses RAG to find relevant information within the document to formulate its responses.
*   **Conversational Booking/Contact Form:** When the user indicates a desire to book an appointment or be contacted, the chatbot initiates a conversational flow to collect necessary information such as Name, Phone Number, Email, and preferred Date.
*   **Data Validation:** The conversational form includes basic validation for user inputs like email format, phone number format, and ensuring the booking date is in the future.
*   **Date Parsing:** The bot can parse date inputs in various natural language formats (e.g., "next Monday", "tomorrow", "2024-12-31") and extract a standardized `YYYY-MM-DD` format.
*   **LLM Integration:** Utilizes a Large Language Model (LLM), specifically configured for a Google Gemini model in `app.py`, for generating responses and handling the conversational flow.
*   **Streamlit Interface:** Provides an easy-to-use web interface for uploading documents and interacting with the chatbot.

## Technologies Used

*   Python
*   Streamlit
*   LangChain (implied by the request, although not explicitly used in the provided core files, the architecture follows LangChain principles with tools and agents)
*   Google Generative AI (Gemini)
*   PyPDF2
*   Sentence Transformers (for embeddings)
*   Scikit-learn (for cosine similarity)
*   python-dotenv
*   email-validator
*   dateparser

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```
2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows use `venv\Scripts\activate`
    ```
3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Set up environment variables:**
    Create a `.env` file in the root directory of the project and add the following variables:
    ```env
    GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
    GEMINI_MODEL="your_gemini_model_name" # e.g., "gemini-pro"
    EMBEDDING_MODEL="your_embedding_model_name" # e.g., "nomic-ai/nomic-embed-text-v1"
    ```
    Replace the placeholder values with your actual Google API key, desired Gemini model name, and the embedding model name.

## Usage

1.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```
2.  **Interact with the chatbot:**
    *   Open the provided URL in your web browser.
    *   Upload a PDF document.
    *   Once the document is processed, you can ask questions related to its content in the chat input.
    *   To trigger the booking/contact form, type phrases like "call me", "book an appointment", "schedule appointment", "make appointment", or "contact me".
    *   **Follow the bot's prompts:** The chatbot will guide you through collecting your details (Name, Phone, Email, Date) by asking one question at a time in the chat. Simply type your response in the chat input after each question from the bot. The bot will validate your input and ask the next question until all required information is collected.

## Use Case

This chatbot is ideal for scenarios where you need to quickly extract information from documents and also require a structured way to collect user contact or booking details.

**Example Scenario:**

Imagine a business that receives many inquiries through their website about their services and also needs to schedule appointments with potential clients. They can use this chatbot by uploading documents containing information about their services, pricing, or FAQs. Users can first ask the chatbot questions about the services based on the uploaded documents. If a user then decides they want to book a consultation or receive a call, they can simply ask the chatbot to "book an appointment" or "call me". The chatbot will then guide them through a simple conversation to collect their name, phone number, email, and preferred date for the appointment, validating each piece of information provided by the user. This streamlines both information delivery and lead collection processes.