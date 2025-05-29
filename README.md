# Chat with Document + Conversational Booking Bot

## Project Description

This Streamlit chatbot answers user questions based on uploaded PDF documents using Retrieval-Augmented Generation (RAG). It also includes a conversational form to collect user details for tasks like booking appointments.

## Features

*   **Document Q&A:** Ask questions about uploaded PDFs.
*   **Conversational Booking:** Collect user information (Name, Phone, Email, Date) through a guided chat.
*   **Data Validation:** Basic input validation for email, phone, and date.
*   **Date Parsing:** Understands natural language dates.
*   **LLM Integration:** Uses Google Gemini for responses and conversation flow.
*   **Streamlit Interface:** Easy-to-use web interface.

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
