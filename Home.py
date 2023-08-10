import streamlit as st 
import pandas as pd 
import openai
from collections import deque





st.session_state["memory"] = deque(maxlen=6)

MODEL = "gpt-3.5-turbo"

system_commands = ''' 
Ignore all previous instructions, your a an editor, your [INPUT] is OCR
have some error in

'''

def chat(text):
    st.session_state["memory"].append({"role": "user", "content": text})
    st.session_state["memory"][0] = {"role": "system", "content": system_commands}
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=list(st.session_state["memory"]),
        temperature=0,
    )
    st.session_state["memory"].append({"role": "assistant", "content": response['choices'][0]['message']['content']})
    return response['choices'][0]['message']['content']


st.set_page_config(
    page_title = "Divinescribe",
    layout = "wide"
    )

def main():
    s = 0
    st.title("Divinescribe")
    st.write("Welcome to the world of ancient wisdom and modern innovation! In an era where technology seamlessly intertwines with spirituality, we present to you the Divinescribe app. This unique platform combines the mystical insights of tarot card reading with the efficiency of AI-powered text conversion. Whether you seek guidance from the universe or the convenience of digitizing your thoughts, Divinescribe has you covered.")
    st.markdown("###")
    st.subheader("Unveiling the Tarot Cards")
    st.write("Tarot cards are more than mere pieces of art; they are keys to unlock the hidden chambers of the subconscious mind. For centuries, individuals have turned to these captivating cards for guidance, introspection, and a deeper understanding of their paths in life. Each card holds a story, a symbol, and a unique energy that resonates with the human experience.")

    st.write("The Major Arcana cards, in particular, stand as pillars of wisdom. With names like 'The Fool,' 'The Magician,' and 'The Empress,' these cards represent profound archetypes and life lessons. By drawing a card and contemplating its symbolism, individuals can gain insights into their challenges, opportunities, and personal growth journeys.")
    st.markdown("###")
    st.subheader('Embracing the Power of Divinescribe')

    st.markdown("---")

    st.image("images/home.jpg")

    st.markdown("---")
    
    st.markdown("Enter Divinescribe, your gateway to tapping into the mystical energy of tarot cards and harnessing the convenience of AI-driven innovation. Our app seamlessly combines these two realms to offer you an experience that is both enlightening and efficient."

"Through Divinescribe, you can pose your questions and intentions to the universe, and our AI-powered tarot card reading feature will provide you with interpretations and insights. By selecting a Major Arcana card, you unlock a window into your subconscious, where the symbolism and wisdom of the card illuminate your path."

"But Divinescribe doesn't stop there. Our AI text conversion feature allows you to effortlessly transform your handwritten notes or voice recordings into digital text. Imagine the ease of capturing your thoughts on-the-go and then having them digitized and organized for easy access and reference.")

    st.markdown("---")
    
    st.markdown(" Divinescribe offers a transformative experience by seamlessly blending ancient tarot card wisdom and cutting-edge AI technology. As you embark on your journey, you can frame your questions and draw a resonant Major Arcana card, allowing our AI to interpret its symbolism and provide insightful guidance. Additionally, Divinescribe streamlines creativity through AI-powered text conversion, transforming handwritten notes and voice recordings into editable text, optimizing efficiency. This app effortlessly combines mystical insights with modern efficiency, enabling you to seek cosmic guidance while also enhancing your productivity. Embrace both worlds with Divinescribe's harmonious convergence of age-old wisdom and technological innovation.")
    

    if st.button("Get started"):
        print("make url for login")
    

if __name__ == "__main__":
    main()

