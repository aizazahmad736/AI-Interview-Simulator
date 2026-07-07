import streamlit as st
from interview.interviewer import generate_question

st.set_page_config(
    page_title="AI Interview Simulator",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Interview Simulator")
st.write("Welcome to your AI Interview Simulator!")

# User input
name = st.text_input("Enter your name")

role = st.selectbox(
    "Select Interview Role",
    [
        "Python Developer",
        "Machine Learning Engineer",
        "Data Analyst",
        "Frontend Developer",
        "HR Interview"
    ]
)

difficulty = st.selectbox(
    "Select Difficulty",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)

# Start interview
if st.button("Start Interview"):

    if name.strip() == "":
        st.warning("Please enter your name.")
    else:
        with st.spinner("Generating your interview question..."):
            question = generate_question(role, difficulty)

        st.success(f"Welcome, {name}!")

        st.subheader("📝 Interview Question")

        st.write(question)