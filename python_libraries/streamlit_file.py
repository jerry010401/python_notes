# STREAMLIT IS A PYTHON LIBRARY TO CREATE WEB APPS FOR DATA PROJECTS - WITHOUT NEEDING HTML,CSS AND JAVASCRIPT.
# IT TURNS YOUR PYTHON SCRIPTS INTO INTERACTIVE WEB APPS JUST BY RUNNING A SCRIPTS.

# create the simple web app:-


"""
import streamlit as st

st.title("My First Streamlit App")
st.header("Welcome to the Demo App")
st.write("This is a simple app built with Streamlit!")

name = st.text_input("What is your name?")

if name:
    st.success(f"Hello! {name}.")

age = st.slider("Select your age", 1, 100, 25)
st.write("You selected", age)

"""
# create simple calculator web app using streamlit...

import streamlit as st

from jdbc_connectivity import result

st.title("CALCULATOR APP!")

num1 = st.number_input("Enter the first number")
num2 = st.number_input("Enter the second number")
operation = st.selectbox("choose operation :",["Add","Sub","Mul","Div"])

if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Sub":
        result = num1 - num2
    elif operation == "Mul":
        result = num1 * num2
    elif operation == "Div":
        result = num1 / num2 if num2 != 0 else "Cannot divide by zero!"
    st.success(f"Result: {result}")

# run the code use to terminal - ( python -m streamlit run streamlit_file.py )




