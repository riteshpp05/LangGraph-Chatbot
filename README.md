## LangGraph Chatbot with Streamlit
This is a web-based chatbot application built with Streamlit and LangGraph, powered by Google's Generative AI (gemini-1.5-flash). The chatbot maintains conversation history using SQLite checkpointing, allowing users to start new conversations, switch between past threads, and interact in real-time via a user-friendly interface. Core backend logic is implemented in backend.py for modularity.
Features

Interactive Chat Interface: Users can type messages and receive streamed responses from the chatbot.
Conversation History: Past conversations are saved and can be revisited using unique thread IDs.
Stateful Conversations: Powered by LangGraph, with SQLite checkpointing to persist conversation states.
Sidebar Navigation: View and switch between conversation threads or start a new chat.
Google Generative AI: Leverages gemini-1.5-flash for natural language understanding and response generation.
Modular Backend: Core chatbot and thread retrieval logic are housed in backend.py.

Prerequisites

Python 3.8 or higher
A Google Cloud API key with access to the Generative AI API (set up in a .env file)
SQLite (included in Python's standard library)

Installation

Clone the Repository:
git clone <repository-url>
cd <repository-directory>


Set Up a Virtual Environment (recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:Ensure you have a requirements.txt file with the following content:
langgraph>=0.2.0
streamlit>=1.38.0
langchain-core>=0.3.0
langchain-google-genai>=1.0.10
python-dotenv>=1.0.0

Install the dependencies:
pip install -r requirements.txt


Set Up Environment Variables:Create a .env file in the project root with your Google API key:
GOOGLE_API_KEY=your-api-key-here

Obtain your API key from the Google Cloud Console.

Run the Application:Start the Streamlit app:
streamlit run app.py

The app will open in your default web browser at http://localhost:8501.


Usage

Start a New Chat: Click the "New Chat" button in the sidebar to begin a new conversation.
View Past Conversations: The sidebar lists all conversation thread IDs. Click a thread ID to load its history.
Interact with the Chatbot: Type your message in the chat input box at the bottom of the main interface. The chatbot's responses will stream in real-time.
Conversation Persistence: Conversation states are saved in a SQLite database (chatbot.db) using LangGraph's checkpointing.
Backend Logic: The backend.py module handles the LangGraph chatbot setup and thread retrieval logic.

Project Structure
├── app.py              # Main Streamlit application script
├── backend.py         # Backend logic for chatbot and thread retrieval
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (not tracked in git)
├── chatbot.db         # SQLite database for conversation checkpoints
└── README.md          # This file

Dependencies

langgraph: For stateful conversation workflows.
streamlit: For the web-based user interface.
langchain-core: For message handling and types.
langchain-google-genai: For integrating Google's Generative AI model.
python-dotenv: For loading environment variables.

Notes

Ensure your Google API key is valid and has access to the Generative AI API.
The SQLite database (chatbot.db) is created automatically when you first run the app.
The backend.py file contains the core LangGraph chatbot logic and the retrieve_all_threads function. Ensure it is in the same directory as app.py.
The chatbot uses the gemini-1.5-flash model with a temperature of 0 for deterministic responses. Adjust the temperature in backend.py if you want more creative responses.

Troubleshooting

Import Errors: Run pip install -r requirements.txt again or check your Python environment.
API Key Issues: Verify your .env file and Google API key setup.
Database Issues: Ensure chatbot.db is writable in your project directory.
Backend Issues: Ensure backend.py is correctly implemented and accessible from app.py.
Streamlit Issues: Ensure streamlit run app.py is executed from the project root.

Contributing
Contributions are welcome! Please submit a pull request or open an issue on the repository for bug reports or feature requests.
License
This project is licensed under the MIT License.