import streamlit as st
from langchain_helper import get_chat_chain

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("🤖 AI Chatbot using LangChain + Cohere")

if "chat_chain" not in st.session_state:
    st.session_state.chat_chain = get_chat_chain()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:", key="user_input")

if st.button("Send"):
    if user_input:
        response = st.session_state.chat_chain.run(user_input)
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Bot", response))
        st.rerun()  # ✅ Use this instead of experimental_rerun()

# Display chat history
for sender, msg in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"**You:** {msg}")
    else:
        st.markdown(f"**🤖 Bot:** {msg}")
