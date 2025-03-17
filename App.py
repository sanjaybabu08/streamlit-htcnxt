import streamlit as st
import pandas as pd
import numpy as np
import time
import json
import streamlit_lottie as st_lottie
import requests
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
from PIL import Image


img = Image.open('Lottie/HTC.png')
st.set_page_config(page_title="Building Web apps",page_icon=img, layout="centered")

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_streamlit = load_lottiefile("Lottie/Streamlit Logo Animation.json")
st.lottie(lottie_streamlit, speed=1.0, height=300, key="initial")


st.header("Agenda")
st.write("This web app is for internal purposes only. It is designed to demonstrate the use of Streamlit widgets with live code examples. The following topics will be covered in this web app:")
st.write("This app demonstrates commonly used Streamlit widgets with live code examples.")

st.write("Before we proceed. Enter your Employee ID below:")
a = st.number_input("Employee ID", min_value=1000, max_value=300000) 
my_list = [201641, 201642, 201643, 201643, 201645]
if a not in my_list:
    st.error("Employee ID not found. Please enter a valid Employee ID.")
else:
    st.balloons()
    st.title('*Building Web Applications in Python*')
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
                st.header("Web Application Development")
                st.subheader('*Introduction*')
                st.write("We interact with websites every day. Starting from social media platforms to online shopping websites, we use web applications for various purposes. Web applications are software applications that run on a web server. They are accessed through a web browser over a network, such as the Internet or an intranet.")
        with right_column:
            lottie_Website = load_lottiefile("Lottie/Website Logo Animation.json")
            st_lottie(
                lottie_Website,
                height=400,
                width=400,
            )
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            lottie_Website = load_lottiefile("Lottie/Streamlit Logo Animation.json")
            st_lottie(
                lottie_Website,
                height=200,
                width=400,
            )
        with right_column:
            st.subheader('*Streamlit*')
            st.write("Streamlit is the fastest way to build and share data apps. It is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science. In just a few lines of code, you can create interactive web apps for your projects.")
    st.header("1. Basic Input Widgets")
    st.code("""name = st.text_input("Enter your name:")
    number = st.number_input("Pick a number", min_value=0, max_value=100)
    date = st.date_input("Pick a date")
    file = st.file_uploader("Upload a file", type=["csv", "txt"])""", language="python")

    name = st.text_input("Enter your name:")
    number = st.number_input("Pick a number", min_value=0, max_value=100)
    date = st.date_input("Pick a date")
    file = st.file_uploader("Upload a file", type=["csv", "txt"])

    st.header("2. Selection Widgets")
    st.code("""option = st.selectbox("Choose an option", ["Option A", "Option B", "Option C"])
    multi_option = st.multiselect("Pick multiple", ["Apple", "Banana", "Cherry"])
    radio_choice = st.radio("Choose one", ["Yes", "No"])
    checkbox = st.checkbox("Agree to terms")""", language="python")

    option = st.selectbox("Choose an option", ["Option A", "Option B", "Option C"])
    multi_option = st.multiselect("Pick multiple", ["Apple", "Banana", "Cherry"])
    radio_choice = st.radio("Choose one", ["Yes", "No"])
    checkbox = st.checkbox("Agree to terms")

    st.header("3. Buttons & Controls")
    st.code("""if st.button("Click me!"):
        st.success("Button clicked!")

    download = st.download_button("Download Sample Data", data="Sample Text", file_name="sample.txt")""", language="python")

    if st.button("Click me!"):
        st.success("Button clicked!")

    download = st.download_button("Download Sample Data", data="Sample Text", file_name="sample.txt")

    st.header("4. Sliders & Progress Bars")
    st.code("""slider_value = st.slider("Adjust value", min_value=0, max_value=100, step=5)
    progress = st.progress(0)
    for i in range(slider_value):
        time.sleep(0.01)
        progress.progress(i + 1)""", language="python")

    slider_value = st.slider("Adjust value", min_value=0, max_value=100, step=5)
    progress = st.progress(0)
    for i in range(slider_value):
        time.sleep(0.01)
        progress.progress(i + 1)

    st.header("5. Displaying Data & Results")
    st.code("""df = pd.DataFrame(np.random.randn(10, 2), columns=["X", "Y"])
    st.dataframe(df)
    st.line_chart(df)
    st.metric("Accuracy", "92%", "+3%")""", language="python")

    df = pd.DataFrame(np.random.randn(10, 2), columns=["X", "Y"])
    st.dataframe(df)
    st.line_chart(df)
    st.metric("Accuracy", "92%", "+3%")

    st.header("6. Session State Example")
    st.code("""if "count" not in st.session_state:
        st.session_state.count = 0
    if st.button("Increase Counter"):
        st.session_state.count += 1
    st.write(f"Counter: {st.session_state.count}")""", language="python")

    if "count" not in st.session_state:
        st.session_state.count = 0
    if st.button("Increase Counter"):
        st.session_state.count += 1
    st.write(f"Counter: {st.session_state.count}")

    st.header("7. Real-Time Interactivity")
    st.code("""st.toast("Task completed!")""", language="python")
    st.toast("Task completed!")
