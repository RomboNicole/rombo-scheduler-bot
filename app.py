import streamlit as st
from schedule_bot import ScheduleBot

st.set_page_config(page_title="Rombo's Creation Bot", page_icon="📅", layout="centered")
st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)

bot = ScheduleBot()
st.title("📅 Rombo's Creation Chatbot")
st.markdown("<small><i>Karibu! I’ll help you organize your day, in Kiswahili or English.</i></small>", unsafe_allow_html=True)

with st.form("chat_form"):
    user_input = st.text_input("👤 Type your message (e.g., 'add meeting on 2025-07-05 15:30'):")
    submitted = st.form_submit_button("Send")

    if submitted and user_input:
        user_input = user_input.lower()

        if "add" in user_input:
            try:
                parts = user_input.split("on")
                event = parts[0].replace("add", "").strip()
                date = parts[1].strip()
                response = bot.add_event(event, date)
            except:
                response = "⚠️ Format error. Example: 'Add meeting on 2025-07-05 15:30'"

        elif "view" in user_input or "angalia" in user_input:
            response = bot.view_schedule()

        elif "delete" in user_input or "futa" in user_input:
            event = user_input.replace("delete", "").replace("futa", "").strip()
            response = bot.delete_event(event)

        elif "hello" in user_input or "hi" in user_input or "habari" in user_input:
            response = "👋 Hello! I can help you schedule events. Try: 'Add dentist on 2025-07-06 14:00'"

        else:
            response = "🤖 Sorry, sikuelewa. Try 'add', 'view', or 'delete' commands."

        st.markdown(f"<div class='chat-bot'>{response}</div>", unsafe_allow_html=True)
