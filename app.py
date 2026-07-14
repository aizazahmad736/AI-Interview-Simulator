# ------------------------
# Interview Screen
# ------------------------
import st();

if st.session_state.started:

    st.success(f"Welcome, {st.session_state.name}!")

    st.subheader(f"Question {st.session_state.question_no} / 5")

    st.write(st.session_state.question)

    st.write("### ✍️ Answer the Question")

    answer = st.text_area(
        "Type your answer here",
        key=f"answer_{st.session_state.question_no}"
    )

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

            st.write(f"Total Score: {st.session_state.score} / 50")

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