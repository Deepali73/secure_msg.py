import streamlit as st
import uuid
import json
import os

DATA_FILE = "user_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Initialize session state
if "user_data" not in st.session_state:
    st.session_state.user_data = load_data()
if "current_user" not in st.session_state:
    st.session_state.current_user = ""
if "message_sent" not in st.session_state:
    st.session_state.message_sent = False
if "login_attempted" not in st.session_state:
    st.session_state.login_attempted = False

st.title("🔐 Secure Message Portal")
st.markdown("""
Login with a username to generate your API key and send secure messages.
""")

username = st.text_input("Enter your username:", key="username_input")
login_clicked = st.button("Login")

if login_clicked and username:
    st.session_state.login_attempted = True
    st.session_state.current_user = username

    if username not in st.session_state.user_data:
        st.session_state.user_data[username] = {
            "api_key": str(uuid.uuid4()),
            "messages": []
        }
        save_data(st.session_state.user_data)
        st.success("New user created and API key generated.")

if st.session_state.login_attempted and st.session_state.current_user:
    user_info = st.session_state.user_data[st.session_state.current_user]

    st.sidebar.markdown(f"### Welcome, **{st.session_state.current_user}**")
    st.sidebar.text_input("Your API Key:", value=user_info["api_key"], key="api_key_display")

    if st.session_state.message_sent:
        msg_input = st.text_input("Enter your message:", value="", key="message_input_clear")
        api_input = st.text_input("Enter your API key:", value="", key="api_key_input_clear")
        st.session_state.message_sent = False
    else:
        msg_input = st.text_input("Enter your message:", key="message_input")
        api_input = st.text_input("Enter your API key:", key="api_key_input")

    if st.button("Send Message"):
        if api_input.strip() == user_info["api_key"]:
            if msg_input.strip():
                st.session_state.user_data[st.session_state.current_user]["messages"].append(msg_input.strip())
                save_data(st.session_state.user_data)
                st.success("Message sent successfully!")
                st.session_state.message_sent = True
                st.query_params.clear()
            else:
                st.warning("Please enter a message.")
        else:
            st.error("Invalid API key!")

    if user_info["messages"]:
        st.markdown("### 📝 Message History")
        for idx, msg in enumerate(user_info["messages"], 1):
            st.markdown(f"**{idx}.** {msg}")
else:
    st.info("Please enter your username and click the login button to begin.")