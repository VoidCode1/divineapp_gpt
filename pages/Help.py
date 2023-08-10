import streamlit as st



st.set_page_config(
    page_title = "Textify",
    page_icon = ":bar_chart:)",
    layout = "wide"
    )

def help_page():
    st.title("Help and Support")
    st.subheader("We're Here to Assist You!")

    st.write("If you need any help or support regarding the Textify app, we're here to assist you. Below are some common questions and answers to help you get started. If your question is not listed below, please feel free to contact us using the form provided.")
    
    st.markdown("### Frequently Asked Questions (FAQs)")
    st.markdown("#### 1. How do I use the TarotCard AI app for personalized readings?")
    st.write("Using the TarotCard AI app is easy! Simply input your question or focus area, and the AI will generate a virtual tarot card reading for you. You'll receive insightful interpretations based on the cards drawn.")

    st.markdown("#### 2. Can the TarotCard AI app provide predictions for the future?")
    st.write("While the TarotCard AI app offers guidance and insights, it's important to remember that tarot readings are not predictive. The app provides perspectives and advice based on the cards, helping you make informed decisions.")

    st.markdown("#### 3. How accurate are the interpretations from the TarotCard AI?")
    st.write("The TarotCard AI app's interpretations are based on symbolism and traditional meanings associated with tarot cards. However, the accuracy of the interpretations can vary and should be considered as guidance rather than absolute truth.")

    st.markdown("#### 4. Is my personal information kept confidential?")
    st.write("Absolutely! We understand the importance of privacy. The TarotCard AI app respects your confidentiality, and your personal data is securely managed. We do not share your information with third parties.")

    st.markdown("#### 5. How can I provide feedback or report any concerns?")
    st.write("We value your feedback to enhance the app's experience. If you encounter any issues or have suggestions for improvement, please use the contact form below to reach out. Your input helps us make the app better!")
    st.write("---")
    st.write("##")
    
    st.markdown("### Contact Form")
    
    # Contact form fields
    with st.container():
        col_45, col_78 = st.columns([1,2])
        col_45name = col_45.text_input("Name")
        col_4email = col_45.text_input("Email")
        col_45message = col_45.text_area("Message", height=150)
    
    # Submit button
    if st.button("Submit"):
        if name and email and message:
            send_email(name, email, message)
            st.success("Thank you! Your message has been sent.")
        else:
            st.error("Please fill in all the required fields.")

def send_email(name, email, message):
    # Add your email sending logic here.
    # For security reasons, I'm not including the actual email sending code in this example.
    # You can use libraries like 'smtplib' or services like 'SendGrid' or 'Gmail API' to send emails.
    pass

if __name__ == "__main__":
    help_page()
