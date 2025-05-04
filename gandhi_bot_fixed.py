import streamlit as st
import openai

# Sidebar input
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/d/d1/Mahatma-Gandhi%2C_studio%2C_1931.jpg", width=150)
    st.title("Gandhi Bot")
    st.markdown("Ask the Mahatma for wisdom.")
    openai_api_key = st.text_input("Enter your OpenAI API key", type="password")

# Stop app if API key is not entered
if not openai_api_key:
    st.warning("Please enter your OpenAI API key to continue.")
    st.stop()

# Set API key
openai.api_key = openai_api_key

# App input/output
st.header("Chat with Gandhi 🕊️")
user_input = st.text_area("You:", height=100)

if st.button("Ask"):
    if user_input:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are Mahatma Gandhi. Answer with wisdom, humility, and non-violence."},
                    {"role": "user", "content": user_input}
                ]
            )
            message = response["choices"][0]["message"]["content"]
            st.markdown("**Gandhi:** " + message)
        except Exception as e:
            st.error(f"I apologize, but there was an error communicating with OpenAI: {e}")
    else:
        st.warning("Please type a message to ask Gandhi.")