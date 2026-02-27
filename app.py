import streamlit as st
from chatbot import Chatbot

# -------------------------------------------------------
# Page Configuration
# -------------------------------------------------------
st.set_page_config(
    page_title="AI FAQ Chatbot",
    page_icon="🤖",
    layout="centered"
)

# -------------------------------------------------------
# Custom CSS Styling
# -------------------------------------------------------
st.markdown("""
    <style>
        .main {
            background-color: #f5f7fb;
        }
        .stTextInput > div > div > input {
            border-radius: 20px;
            padding: 10px 16px;
            border: 2px solid #4A90E2;
            font-size: 15px;
        }
        .chat-bubble-user {
            background-color: #4A90E2;
            color: white;
            padding: 10px 16px;
            border-radius: 18px 18px 4px 18px;
            margin: 6px 0;
            max-width: 75%;
            float: right;
            clear: both;
            font-size: 15px;
        }
        .chat-bubble-bot {
            background-color: #ffffff;
            color: #333333;
            padding: 10px 16px;
            border-radius: 18px 18px 18px 4px;
            margin: 6px 0;
            max-width: 75%;
            float: left;
            clear: both;
            font-size: 15px;
            border: 1px solid #e0e0e0;
            box-shadow: 0px 1px 3px rgba(0,0,0,0.08);
        }
        .chat-container {
            padding: 10px 0;
            overflow: hidden;
        }
    </style>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# Initialize the Chatbot and Session State
# -------------------------------------------------------

# Create the chatbot instance
bot = Chatbot(name="AIBot")

# Session state lets Streamlit remember data between reruns
# We store the full chat history here as a list of dicts
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Track if the conversation has been ended
if "chat_ended" not in st.session_state:
    st.session_state.chat_ended = False

# -------------------------------------------------------
# App Header
# -------------------------------------------------------
st.markdown("## 🤖 AI FAQ Chatbot")
st.markdown("Ask me anything about **Artificial Intelligence**, Machine Learning, Deep Learning, and more!")
st.divider()

# -------------------------------------------------------
# Display Chat History
# -------------------------------------------------------
for message in st.session_state.chat_history:
    if message["role"] == "user":
        st.markdown(
            f'<div class="chat-container"><div class="chat-bubble-user">🧑 {message["text"]}</div></div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f'<div class="chat-container"><div class="chat-bubble-bot">🤖 {message["text"]}</div></div>',
            unsafe_allow_html=True
        )

# -------------------------------------------------------
# Input Box and Send Button
# -------------------------------------------------------
st.divider()

# Show greeting if chat is empty
if not st.session_state.chat_history:
    st.info(bot.greet())

if not st.session_state.chat_ended:
    # Text input for user question
    user_input = st.text_input(
        label="Your message",
        placeholder="e.g. What is machine learning?",
        label_visibility="collapsed",
        key="user_input"
    )

    # Send button
    if st.button("Send 💬", use_container_width=True):
        if user_input.strip():
            # Get response from chatbot
            response = bot.respond(user_input)

            # Append user message and bot response to history
            st.session_state.chat_history.append({"role": "user", "text": user_input})
            st.session_state.chat_history.append({"role": "bot", "text": response})

            # If user said bye, mark chat as ended
            if bot.is_farewell(user_input):
                st.session_state.chat_ended = True

            # Rerun the app to refresh and show new messages
            st.rerun()
        else:
            st.warning("Please type a message before sending!")

else:
    st.success("Chat ended. Refresh the page to start a new conversation! 🔄")

# -------------------------------------------------------
# Sidebar — Tips for the user
# -------------------------------------------------------
with st.sidebar:
    st.markdown("### 💡 Try asking...")
    st.markdown("""
    - What is AI?
    - What is machine learning?
    - What is deep learning?
    - What is a neural network?
    - What is NLP?
    - What is reinforcement learning?
    - What is TensorFlow?
    - What is a large language model?
    - What are real world applications of AI?
    - What is overfitting?
    """)

    st.divider()
    st.markdown("### 🔄 Start Over")
    if st.button("Clear Chat", use_container_width=True):
        st.session_state.chat_history = []
        st.session_state.chat_ended = False
        st.rerun()