import streamlit as st



st.set_page_config(
    page_title = "Divinescribe",
    layout = "wide"
    )

def contact_page():
    st.title("Contact Us")
    st.subheader("We'd Love to Hear From You!")
    
    st.write("If you have any questions, suggestions, or feedback, please feel free to reach out to us. We value your input and strive to provide the best possible user experience.")
    
    st.markdown("### Contact Information")
    st.write("Email: emucoolbuta.com")
    st.write("Phone: +260 972 864931")
    
    st.markdown("### Office Address")
    st.write("Divinescribe Inc.")
    st.write("1234 Main Street")
    st.write("City, State 12345")
    st.write("Country")
    
    st.markdown("### Social Media")
    st.write("Stay connected with us on social media for updates, news, and more!")
    st.write("Twitter: [Divinescribe](http://localhost:8501/Contact)")
    st.write("Facebook: [Divinescribe](https://www.facebook.com/DivinescribeAppOfficial)")
    st.write("Instagram: [Divinescribe](https://www.instagram.com/Divinescribe_App)")

if __name__ == "__main__":
    contact_page()