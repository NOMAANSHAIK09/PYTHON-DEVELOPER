import streamlit as st 
from send_email import send_email

st.header("contact us")

with st.form(key="email"):
    user_email=st.text_input("Enter the email")
    user_message=st.text_area("Your Meassage")
    message=f"""
    subject: New email from{user_email}
    From: {user_email}
    {user_message}"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("your email was sent successfully")