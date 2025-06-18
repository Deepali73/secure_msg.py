# 🔐 Secure Message Portal

A secure, Streamlit-based messaging platform that allows users to generate unique API keys, send private messages, and view their message history—all stored locally in a JSON file.

## 🚀 Features

- **User Login**: Enter a username to login or register.
- **Automatic API Key Generation**: New users are issued a UUID-based API key.
- **Persistent Storage**: All user data (API keys and messages) are saved in a local `user_data.json` file.
- **Secure Messaging**: Only users with a valid API key can send messages.
- **Message History**: Logged-in users can see a list of their sent messages.
- **Session Awareness**: Recognizes returning users and displays their API key in the sidebar.
- **Clean UI**: Clears input blocks after message sending for better usability.

## 🧪 How It Works

1. **Login**:
   - Enter a unique username.
   - If it's your first time, the system generates and shows your API key.
   - If you're a returning user, your existing API key is loaded.

2. **Send Message**:
   - Type your message.
   - Enter your API key to validate identity.
   - On success, the message is saved under your profile.

3. **Data Storage**:
   - All user credentials and messages are stored in `user_data.json` in the same directory.
