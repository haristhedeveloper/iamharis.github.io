import streamlit as st

def main():
    # Get user input using Streamlit widgets
    name = st.text_input("Enter your name:")
    age = st.number_input("Enter your age:")
    gender = st.selectbox("Select your gender:", options=["Male", "Female", "Other"])

    # Display the message
    st.write(f"Your name is {name}, your age is {age}, and you are {gender}.")

if __name__ == "__main__":
    main()
