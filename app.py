import streamlit as st
from backend import chatbot, retrieve_all_threads
from langchain_core.messages import HumanMessage
import uuid

# **************************************** utility functions *************************

def generate_thread_id():
    return uuid.uuid4()

def reset_chat():
    thread_id = generate_thread_id()
    st.session_state['thread_id'] = thread_id
    add_thread(st.session_state['thread_id'])
    st.session_state['message_history'] = []

def add_thread(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)

def load_conversation(thread_id):
    """Safely load conversation for a given thread ID."""
    state = chatbot.get_state(config={'configurable': {'thread_id': thread_id}})
    if hasattr(state, "values") and "messages" in state.values:
        return state.values["messages"]
    return []  # return empty if no messages yet

def get_conversation_title(thread_id):
    """Get or create a title for the conversation."""
    if thread_id in st.session_state['thread_titles']:
        return st.session_state['thread_titles'][thread_id]
    
    messages = load_conversation(thread_id)
    if messages:
        first_msg = messages[0].content
        title = (first_msg[:25] + '...') if len(first_msg) > 25 else first_msg
    else:
        title = "Untitled Chat"
    
    st.session_state['thread_titles'][thread_id] = title
    return title


# **************************************** Session Setup ******************************
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()

if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = retrieve_all_threads()

if 'thread_titles' not in st.session_state:
    st.session_state['thread_titles'] = {}

add_thread(st.session_state['thread_id'])

# **************************************** Sidebar Styling ****************************
st.markdown("""
    <style>
        .chat-btn {
            display: flex;
            align-items: center;
            background-color: transparent;
            border: none;
            text-align: left;
            padding: 8px 12px;
            width: 100%;
            color: white;
            font-size: 14px;
            border-radius: 6px;
            cursor: pointer;
            transition: background 0.2s ease;
        }
        .chat-btn:hover {
            background-color: #374151;
        }
        .active-chat {
            background-color: #4b5563 !important;
        }
        .chat-icon {
            margin-right: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# **************************************** Sidebar UI *********************************

st.sidebar.title('GuideAI🤖')

if st.sidebar.button('➕ New Chat'):
    reset_chat()

st.sidebar.header('📂 My Conversations')

for thread_id in st.session_state['chat_threads'][::-1]:
    title = get_conversation_title(thread_id)
    is_active = (thread_id == st.session_state['thread_id'])
    button_label = f"💬 {title}"
    
    if st.sidebar.button(button_label, key=f"chat-{thread_id}"):
        st.session_state['thread_id'] = thread_id
        messages = load_conversation(thread_id)
        temp_messages = [
            {'role': 'user' if isinstance(msg, HumanMessage) else 'assistant', 'content': msg.content}
            for msg in messages
        ]
        st.session_state['message_history'] = temp_messages

# **************************************** Main Chat UI *******************************
# Load existing messages
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

# Chat input
user_input = st.chat_input('Type here...')

if user_input:
    # Add user message
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)

    #CONFIG = {'configurable': {'thread_id': st.session_state['thread_id']}}
    CONFIG = {
        "configurable": {"thread_id": st.session_state["thread_id"]},
        "metadata": {
            "thread_id": st.session_state["thread_id"]
        },
        "run_name": "chat_turn",
    }
    # Get AI response
    with st.chat_message('assistant'):
        ai_message = st.write_stream(
            message_chunk.content for message_chunk, metadata in chatbot.stream(
                {'messages': [HumanMessage(content=user_input)]},
                config=CONFIG,
                stream_mode='messages'
            )
        )

    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})