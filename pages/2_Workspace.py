import streamlit as st  
import pandas as pd
from collections import deque   
import openai
import numpy as np

memory = deque(maxlen=6)

MODEL = "gpt-3.5-turbo"

card_list = ["chariot","emperor","empress","hermit","hierophant","high_priestess","magician","strength","the_lovers","wheel_of_fortune"]
openai.api_key = "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"

system_commands = '''
ignore all previous instructions these are you new instructions. Imagine you are professional tarot reader. You give your clients spiritual guidance and offer insight into their lives,
you are not afraid to speak the true, give an explaination of each card according to the user question and give a comprehensive summary at the end,
the user will provide a question and the cards he or she hs choosen.
'''


def chat(text):
    if "memory" not in st.session_state["memory"]:
        st.session_state["memory"] = []
    st.session_state["memory"].append({"role": "system", "content": system_commands})
    st.session_state["memory"].append({"role": "user", "content": text})
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
if "cards_selected" not in st.session_state:
    st.session_state["cards_selected"] = dict(col10=False,col9=False,col8=False,col7=False,col6=False,col5=False,col4=False,col3=False,col2=False,col1=False)

if "chooses" not in st.session_state:
    st.session_state["chooses"] = []

if "reset" not in st.session_state:
    st.session_state["reset"] = True



def workspace():
    result = " No Results Yet!"

    if len(st.session_state["chooses"]) > 2 and st.session_state["reset"] == True:
         st.session_state["chooses"] = []


    if "WORKSPACE_VALUE" not in st.session_state:
        st.session_state['WORKSPACE_VALUE'] = "hello world"

    st.title("Get Your Personal reading".upper())
    st.write("##")

    col1, col2 = st.columns([1,2])

    col1.image("images/home.jpg")
    col1.write("##")
    col1.markdown("Name: User")
    col1.write("Membership: Premium")

    st.markdown("---")

    text = st.text_area("Ask your question here.")
    st.subheader("Pick 3 cards")
    col11,col12,col13,col14,col15 = st.columns(5)
    col21,col22,col23,col24,col25 = st.columns(5)




    if st.session_state["cards_selected"]["col1"]:
        col11.image(f"images/{st.session_state['cards_selected']['col1']}.jpg")
    else:
        col11.image("images/back.jpg")
    if st.session_state['cards_selected']['col1'] == False and st.session_state["reset"]:
        choose1 = col11.button("Choose 1")
        if choose1:
            choose = np.random.choice(card_list)
            check = True
            st.session_state["cards_selected"]["col1"] = np.random.choice(card_list)
            st.session_state["chooses"].append(choose)


    
    if st.session_state["cards_selected"]["col2"]:
        col12.image(f"images/{st.session_state['cards_selected']['col2']}.jpg")
    else:
        col12.image("images/back.jpg")
    if st.session_state['cards_selected']['col2'] == False and st.session_state["reset"]:
        choose2 = col12.button("Choose 2")
        if choose2:
            choose = np.random.choice(card_list)
            check = True
            st.session_state["cards_selected"]["col2"] = np.random.choice(card_list)
            st.session_state["chooses"].append(choose)


    if st.session_state["cards_selected"]["col3"]:
        col13.image(f"images/{st.session_state['cards_selected']['col3']}.jpg")
    else:
        col13.image("images/back.jpg")
    if st.session_state['cards_selected']['col3'] == False and st.session_state["reset"]:
        choose3 = col13.button("Choose 3")
        if choose3:
            choose = np.random.choice(card_list)
            check = True
            st.session_state["cards_selected"]["col3"] = np.random.choice(card_list)
            st.session_state["chooses"].append(choose)


    
    if st.session_state["cards_selected"]["col4"]:
        col14.image(f"images/{st.session_state['cards_selected']['col4']}.jpg")
    else:
        col14.image("images/back.jpg")
    if st.session_state['cards_selected']['col4'] == False and st.session_state["reset"]:
        choose4 = col14.button("Choose 4")
        if choose4:
            choose = np.random.choice(card_list)
            check = True
            st.session_state["cards_selected"]["col4"] = np.random.choice(card_list)
            st.session_state["chooses"].append(choose)


    if st.session_state["cards_selected"]["col5"]:
        col15.image(f"images/{st.session_state['cards_selected']['col5']}.jpg")
    else:
        col15.image("images/back.jpg")
    if st.session_state['cards_selected']['col5'] == False and st.session_state["reset"]:
        choose5 = col15.button("Choose 5")
        if choose5:
            choose = np.random.choice(card_list)
            check = True
            st.session_state["cards_selected"]["col5"] = np.random.choice(card_list)
            st.session_state["chooses"].append(choose)


    
    if st.session_state["cards_selected"]["col6"]:
        col21.image(f"images/{st.session_state['cards_selected']['col6']}.jpg")
    else:
        col21.image("images/back.jpg")
    if st.session_state['cards_selected']['col6'] == False and st.session_state["reset"]:
        choose6 = col21.button("Choose 6")
        if choose6:
            choose = np.random.choice(card_list)
            check = True
            st.session_state["cards_selected"]["col6"] = np.random.choice(card_list)


    if st.session_state["cards_selected"]["col7"]:
        col22.image(f"images/{st.session_state['cards_selected']['col7']}.jpg")
    else:
        col22.image("images/back.jpg")
    if st.session_state['cards_selected']['col7'] == False and st.session_state["reset"]:
        choose7 = col22.button("Choose 7")
        if choose7:
            choose = np.random.choice(card_list)
            check = True
            st.session_state["cards_selected"]["col7"] = np.random.choice(card_list)
            st.session_state["chooses"].append(choose)


    
    if st.session_state["cards_selected"]["col8"]:
        col23.image(f"images/{st.session_state['cards_selected']['col8']}.jpg")
    else:
        col23.image("images/back.jpg")
    if st.session_state['cards_selected']['col8'] == False and st.session_state["reset"]:
        choose8 = col23.button("Choose 8")
        if choose8:
            choose = np.random.choice(card_list)
            check = True
            st.session_state["cards_selected"]["col8"] = np.random.choice(card_list)
            st.session_state["chooses"].append(choose)


    if st.session_state["cards_selected"]["col9"]:
        col24.image(f"images/{st.session_state['cards_selected']['col9']}.jpg")
    else:
        col24.image("images/back.jpg")
    if st.session_state['cards_selected']['col8'] == False and st.session_state["reset"]:
        choose9 = col24.button("Choose 9")
        if choose9:
            choose = np.random.choice(card_list)
            check = True
            st.session_state["cards_selected"]["col9"] = np.random.choice(card_list)
            st.session_state["chooses"].append(choose)


    if st.session_state["cards_selected"]["col10"]:
        col25.image(f"images/{st.session_state['cards_selected']['col10']}.jpg")
    else:
        col25.image("images/back.jpg")
    if st.session_state['cards_selected']['col10'] == False and st.session_state["reset"]:
        choose8 = col25.button("Choose 10")
        if choose8:
            choose = np.random.choice(card_list)
            check = True
            st.session_state["cards_selected"]["col10"] = np.random.choice(card_list)
            st.session_state["chooses"].append(choose)

    submit = st.button("Submit")
    if len(st.session_state["chooses"]) > 2:
        reset = st.button("Reset")
        st.session_state["reset"] = False
        if reset:
            st.session_state["reset"] = True
            for x in st.session_state["cards_selected"].keys():
                st.session_state["cards_selected"][x] = False
    prompt = []
    if submit:

        for x in st.session_state["cards_selected"].values():
            if x != False:
                prompt.append(x)
        resp = chat(f"the question:{text} and cards {prompt}")
        st.write(resp)


    
    

    




def send_request(Task, message):
    # Add your email sending logic here.
    # For security reasons, I'm not including the actual email sending code in this example.
    # You can use libraries like 'smtplib' or services like 'SendGrid' or 'Gmail API' to send emails.
    return "Demo"

if __name__ == "__main__":
    workspace()
