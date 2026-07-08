import streamlit as st
import send_email
st.header("Contact Us")
with st.form(key="email_forms"):
    user_email = st.text_input("Your Email Address:")
    message = st.text_area("Your Message:")
    message=f"""\
    Subject: New email from {user_email}
    
    From: {user_email}
    {message}
    """
    button=st.form_submit_button("Submit")
    if button:
        send_email.send_email(user_email,message)
        st.info("Email sent successfully")
