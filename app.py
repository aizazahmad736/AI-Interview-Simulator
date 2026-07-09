
from voice import speak
from speech import record_answer
import streamlit as st
from interview.interviewer import generate_question, evaluate_answer

st.set_page_config(
    page_title="AI Interview Simulator",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Interview Simulator")
st.write("Practice interviews powered by Gemini AI.")

# ------------------------
# Session State
# ------------------------
if "started" not in st.session_state:
    st.session_state.started = False

if "question" not in st.session_state:
    st.session_state.question = ""

if "question_no" not in st.session_state:
    st.session_state.question_no = 1

if "score" not in st.session_state:
    st.session_state.score = 0

if "evaluation" not in st.session_state:
    st.session_state.evaluation = ""

if "answered" not in st.session_state:
    st.session_state.answered = False

if "role" not in st.session_state:
    st.session_state.role = ""

if "difficulty" not in st.session_state:
    st.session_state.difficulty = ""

if "name" not in st.session_state:
    st.session_state.name = ""


# ------------------------
# User Inputs
# ------------------------

if not st.session_state.started:

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

    if st.button("Start Interview"):

        if name.strip() == "":
            st.warning("Please enter your name.")

        else:

            st.session_state.started = True
            st.session_state.name = name
            st.session_state.role = role
            st.session_state.difficulty = difficulty

            st.session_state.question = generate_question(
                role,
                difficulty
            )

            st.rerun()


# ------------------------
# Interview Screen
# ------------------------

if st.session_state.started:

    st.success(f"Welcome, {st.session_state.name}!")

    st.subheader(
        f"Question {st.session_state.question_no} / 5"
    )

    st.write(st.session_state.question)

        st.write("### 🎤 Answer the Question")

    voice_answer = record_answer()

    if voice_answer:
        st.success("✅ Voice recognized successfully!")
        st.write("**Transcript:**")
        st.write(voice_answer)

    answer = st.text_area(
        "Or type your answer here",
        value=voice_answer if voice_answer else "",
        key=f"answer_{st.session_state.question_no}"
    )

   
    st.write("### 🎤 Answer the Question")

voice_answer = record_answer()



    if not st.session_state.answered:

        if st.button("Submit Answer"):

            if answer.strip() == "":
                st.warning("Please enter your answer.")

            else:

                with st.spinner("Evaluating answer..."):

                    feedback = evaluate_answer(
                        st.session_state.question,
                        answer
                    )

                st.session_state.evaluation = feedback
                st.session_state.score += 10
                st.session_state.answered = True

                st.rerun()

    else:

        st.subheader("AI Feedback")

        st.write(st.session_state.evaluation)

        if st.session_state.question_no < 5:

            if st.button("Next Question"):

                st.session_state.question_no += 1

                st.session_state.question = generate_question(
                    st.session_state.role,
                    st.session_state.difficulty
                )

                st.session_state.evaluation = ""
                st.session_state.answered = False

                st.rerun()

        else:

            st.success("🎉 Interview Completed!")

            st.subheader("Final Result")

            st.write(
                f"Total Score: {st.session_state.score} / 50"
            )

            percentage = (st.session_state.score / 50) * 100

            st.write(f"Percentage: {percentage:.0f}%")

            if percentage >= 80:
                st.balloons()
                st.success("Excellent Performance!")
            elif percentage >= 60:
                st.info("Good Job! Keep Practicing.")
            else:
                st.warning("Needs Improvement.")

            if st.button("Restart Interview"):

                for key in list(st.session_state.keys()):
                    del st.session_state[key]

                st.rerun()