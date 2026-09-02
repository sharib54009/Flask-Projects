import streamlit as st
from Send_Emalis import Send_Emails

st.header("Contact Me")
st.write("If you have any questions or would like to get in touch, please feel free to reach out to me using the contact form below or through my email address.")

with st.form(key ="contact_form"):
    email = st.text_input("Your Email")
    raw_message = st.text_area("Your Message")
    message = f"""
    Sunject: new email from {email}
    from: {email}
    Message: {raw_message}
    """
    
    submit_button = st.form_submit_button(label="Submit")
    if submit_button:
        Send_Emails(message)
        st.info("Thank you for reaching out! Your message has been sent successfully. I will get back to you as soon as possible.")