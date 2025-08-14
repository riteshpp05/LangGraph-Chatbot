## LangGraph Chatbot with Streamlit

A web-based chatbot built using **Streamlit** and **LangGraph**, powered by **Google Generative AI (gemini-1.5-flash)**.  
It supports stateful conversations with **SQLite checkpointing**, thread switching, and a simple, interactive UI.

## Features
-  Real-time chatbot with streamed responses  
-  Conversation history with thread switching  
-  Persistent state via SQLite  
-  Modular backend in `backend.py`  
-  Powered by Google's gemini-1.5-flash model  

## Installation
```bash
# Clone the repo
git clone https://github.com/riteshpp05/LangGraph-Chatbot.git
cd LangGraph-Chatbot

# Create & activate virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt
```

## Environment Setup
Create a `.env` file in the root:
```env
GOOGLE_API_KEY=your-api-key-here
```
Get the API key from [Google Cloud Console](https://console.cloud.google.com/).

## Run the App
```bash
streamlit run app.py
```
The app will open at **http://localhost:8501**.

## Project Structure
```
├── app.py          # Streamlit UI
├── backend.py      # Chatbot & thread logic
├── requirements.txt
├── .env            # Environment variables
├── chatbot.db      # SQLite conversation store
└── README.md
```

## 🛠 Troubleshooting
- **Import errors:** `pip install -r requirements.txt`  
- **API issues:** Check `.env` and API key  
- **DB issues:** Ensure `chatbot.db` is writable  


