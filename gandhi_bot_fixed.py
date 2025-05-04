import streamlit as st

# Sidebar for API key
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/d/d1/Mahatma-Gandhi%2C_studio%2C_1931.jpg", width=150)
    st.title("Gandhi Bot")
    st.markdown("Ask the Mahatma for wisdom.")
    openai_api_key = st.text_input("Enter your OpenAI API key", type="password")

# Set API key
if openai_api_key:
    openai.api_key = openai_api_key
else:
    st.warning("Please enter your OpenAI API key to continue.")
    st.stop()

import openai
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Gandhi Bot - Wisdom from the Mahatma",
    page_icon="🕊️",
    layout="wide"
)

# CSS for styling
st.markdown("""
<style>
    .chat-message {
        padding: 1rem;
        border-radius: 0.8rem;
        margin-bottom: 1rem;
        display: flex;
        flex-direction: row;
        align-items: flex-start;
    }
    .chat-message.user {
        background-color: #f0f2f6;
    }
    .chat-message.bot {
        background-color: #e9f7ef;
    }
    .chat-message .avatar {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        object-fit: cover;
        margin-right: 1rem;
    }
    .chat-message .message {
        flex-grow: 1;
    }
    .stTextInput input {
        border-radius: 0.5rem;
    }
    h1, h2 {
        color: #3e6b48;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar for API key
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/7/7a/Mahatma-Gandhi%2C_studio%2C_1931.jpg", width=200)
    st.title("Gandhi Bot")
    st.markdown("Talk to a chatbot embodying the wisdom of Mahatma Gandhi")

    # API key input
    api_key = st.text_input("Enter your OpenAI API key:", type="password")
    st.caption("Your API key is not stored and is only used to communicate with OpenAI's API.")

    # Additional information
    st.markdown("---")
    st.markdown("### About Mahatma Gandhi")
    st.markdown("""
    Mohandas Karamchand Gandhi (1869-1948) was an Indian lawyer, anti-colonial nationalist, and political ethicist who employed nonviolent resistance to lead the successful campaign for India's independence from British rule.

    He inspired movements for civil rights and freedom across the world.
    """)

    st.markdown("---")
    st.markdown("Created with Streamlit and OpenAI")
    st.caption(f"© {datetime.now().year}")

# Main chat interface
st.title("🕊️ Gandhi Bot - Wisdom from the Mahatma")
st.markdown("Ask any question and receive answers inspired by Gandhi's philosophy and wisdom")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Namaste! I am a digital representation of Mahatma Gandhi's thoughts and principles. How may I help you on your path to truth and non-violence today?"}
    ]

# Display chat messages
for message in st.session_state.messages:
    if message["role"] == "user":
        with st.container():
            st.markdown(f"""
            <div class="chat-message user">
                <img class="avatar" src="https://www.svgrepo.com/show/496494/profile-circle.svg">
                <div class="message">{message["content"]}</div>
            </div>
            """, unsafe_allow_html=True)
    else:
        with st.container():
            st.markdown(f"""
            <div class="chat-message bot">
                <img class="avatar" src="https://upload.wikimedia.org/wikipedia/commons/7/7a/Mahatma-Gandhi%2C_studio%2C_1931.jpg">
                <div class="message">{message["content"]}</div>
            </div>
            """, unsafe_allow_html=True)

# Function to generate response from OpenAI
def generate_response(prompt, api_key):
    if not api_key:
        return "Please enter your OpenAI API key in the sidebar to continue our conversation."

    try:
        # Initialize the OpenAI client with the provided API key
        client = # Removed incorrect OpenAI client instantiation

        # Prepare the conversation history
        conversation = []
        for message in st.session_state.messages:
            conversation.append({"role": message["role"], "content": message["content"]})

        # Add the system message to guide the model
        conversation.insert(0, {
            "role": "system",
            "content": """You are Mahatma Gandhi, speaking with wisdom, compassion, and simplicity.
            Embody Gandhi's philosophy of non-violence (ahimsa), truth (satya), and self-reliance (swadeshi).
            Speak in a gentle, thoughtful manner, occasionally using Indian terms and references to your life experiences.
            Your responses should reflect Gandhi's moral values, his spirituality that transcends religious boundaries,
            and his practical approach to social and political issues. When appropriate, include quotes that Gandhi actually said.
            Keep responses concise yet profound."""
        })

        # Add the user's prompt
        conversation.append({"role": "user", "content": prompt})

        # Call the OpenAI API with the GPT-4.5 model
        response = client.chat.completions.create(
            model="gpt-4.1-nano",
            messages=conversation,
            max_tokens=500,
            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"I apologize, but there was an error communicating with OpenAI: {str(e)}"

# User input area
with st.container():
    with st.form(key="message_form", clear_on_submit=True):
        user_input = st.text_area("Your message:", key="user_input", height=100)
        submit_button = st.form_submit_button("Send")

    if submit_button and user_input:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Get assistant response
        with st.spinner("Gandhi is contemplating..."):
            response = generate_response(user_input, api_key)

        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

        # Force a rerun to update the UI with the new messages
        st.rerun()
