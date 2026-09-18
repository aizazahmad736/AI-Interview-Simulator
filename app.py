"""
AI Interview Simulator
Streamlit Application Entry Point
"""

import streamlit as st
from config import is_api_key_configured, GEMINI_API_KEY
from interview.interviewer import generate_question, evaluate_answer
from interview.resume_parser import extract_text_from_file, parse_resume_content
from interview.report_generator import generate_pdf_report

# =========================================================
# 1. Page Configuration
# =========================================================
st.set_page_config(
    page_title="AI Interview Simulator",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
<style>
    .main-title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #1E3A8A;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        font-size: 1.05rem;
        color: #4B5563;
        margin-bottom: 1.5rem;
    }
    .question-card {
        background-color: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-left: 5px solid #2563EB;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 20px;
        font-size: 1.15rem;
        font-weight: 500;
        color: #0F172A;
    }
    .stMetric {
        background-color: #F8FAFC;
        padding: 10px;
        border-radius: 8px;
        border: 1px solid #E2E8F0;
    }
</style>
""", unsafe_allow_html=True)

# =========================================================
# 2. Session State Initialization
# =========================================================
if "screen" not in st.session_state:
    st.session_state.screen = "setup"

if "candidate_name" not in st.session_state:
    st.session_state.candidate_name = ""

if "role" not in st.session_state:
    st.session_state.role = "Python Developer"

if "difficulty" not in st.session_state:
    st.session_state.difficulty = "Mid-Level"

if "num_questions" not in st.session_state:
    st.session_state.num_questions = 5

if "current_q_idx" not in st.session_state:
    st.session_state.current_q_idx = 1

if "current_question" not in st.session_state:
    st.session_state.current_question = ""

if "current_feedback" not in st.session_state:
    st.session_state.current_feedback = None

if "qa_history" not in st.session_state:
    st.session_state.qa_history = []

if "total_score" not in st.session_state:
    st.session_state.total_score = 0

if "resume_skills" not in st.session_state:
    st.session_state.resume_skills = []

if "custom_api_key" not in st.session_state:
    st.session_state.custom_api_key = ""

# =========================================================
# 3. Sidebar Configuration
# =========================================================
with st.sidebar:
    st.image("https://img.icons8.com/color/96/artificial-intelligence.png", width=64)
    st.title("Interview Hub")
    
    # API Key Configuration
    has_key = is_api_key_configured(st.session_state.custom_api_key)
    if has_key:
        st.success("🟢 AI Engine: Gemini Active")
    else:
        st.warning("🟡 AI Engine: Offline Mode (Fallback Question Bank)")
        
    with st.expander("🔑 Gemini API Settings"):
        custom_key = st.text_input(
            "Enter Gemini API Key",
            value=st.session_state.custom_api_key,
            type="password",
            help="Free key from https://aistudio.google.com/"
        )
        if custom_key != st.session_state.custom_api_key:
            st.session_state.custom_api_key = custom_key
            st.rerun()
            
    st.divider()
    st.caption("AI Interview Simulator v2.0 &bull; Built with Streamlit & Gemini")
    
    if st.session_state.screen != "setup":
        if st.button("🔄 Reset Interview", use_container_width=True):
            for k in ["screen", "candidate_name", "current_q_idx", "current_question", "current_feedback", "qa_history", "total_score", "resume_skills"]:
                if k in st.session_state:
                    del st.session_state[k]
            st.rerun()

# =========================================================
# 4. Screen 1: Interview Setup
# =========================================================
if st.session_state.screen == "setup":
    st.markdown('<div class="main-title">🤖 AI Interview Simulator</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Practice realistic job interviews tailored to your target role, difficulty, and resume.</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 2], gap="large")
    
    with col1:
        st.subheader("📋 Candidate & Role Configuration")
        name_input = st.text_input("Your Full Name", value=st.session_state.candidate_name, placeholder="e.g. Alex Johnson")
        
        role_options = [
            "Python Developer",
            "Machine Learning Engineer",
            "Data Analyst",
            "Frontend Developer",
            "Full Stack Developer",
            "HR & Behavioral"
        ]
        selected_role = st.selectbox("Target Job Role", role_options, index=role_options.index(st.session_state.role) if st.session_state.role in role_options else 0)
        
        diff_col, count_col = st.columns(2)
        with diff_col:
            selected_diff = st.selectbox("Experience Level", ["Junior", "Mid-Level", "Senior"], index=1)
        with count_col:
            selected_count = st.select_slider("Number of Questions", options=[3, 5, 7, 10], value=st.session_state.num_questions)
            
        st.divider()
        start_btn = st.button("🚀 Start Interview Session", type="primary", use_container_width=True)
        
    with col2:
        st.subheader("📄 Resume Personalization (Optional)")
        st.info("Upload your resume (PDF or TXT) so the AI can extract your technical skills and customize questions to your experience!")
        
        uploaded_resume = st.file_uploader("Upload Resume", type=["pdf", "txt"], help="Supported: PDF and TXT")
        if uploaded_resume is not None:
            raw_text = extract_text_from_file(uploaded_resume)
            parsed = parse_resume_content(raw_text)
            st.session_state.resume_skills = parsed.get("skills", [])
            
            if st.session_state.resume_skills:
                st.success(f"Extracted {len(st.session_state.resume_skills)} skills from resume!")
                st.pills("Detected Skills", st.session_state.resume_skills[:12], selection_mode="multi")
            else:
                st.warning("Resume uploaded, but no common tech keywords were detected. Standard questions will be used.")

    if start_btn:
        if not name_input.strip():
            st.warning("Please enter your name to proceed.")
        else:
            st.session_state.candidate_name = name_input.strip()
            st.session_state.role = selected_role
            st.session_state.difficulty = selected_diff
            st.session_state.num_questions = selected_count
            st.session_state.current_q_idx = 1
            st.session_state.qa_history = []
            st.session_state.total_score = 0
            st.session_state.current_feedback = None
            
            with st.spinner("Generating your first interview question..."):
                st.session_state.current_question = generate_question(
                    role=selected_role,
                    difficulty=selected_diff,
                    question_no=1,
                    previous_qa=[],
                    resume_skills=st.session_state.resume_skills,
                    custom_api_key=st.session_state.custom_api_key
                )
            st.session_state.screen = "interview"
            st.rerun()

# =========================================================
# 5. Screen 2: Active Interview Runner
# =========================================================
elif st.session_state.screen == "interview":
    # Metrics Row
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Candidate", st.session_state.candidate_name)
    m2.metric("Target Role", st.session_state.role)
    m3.metric("Difficulty", st.session_state.difficulty)
    m4.metric("Score", f"{st.session_state.total_score} / {(st.session_state.current_q_idx - 1) * 10 if st.session_state.current_q_idx > 1 else 0}")
    
    # Progress
    progress_val = (st.session_state.current_q_idx - 1) / st.session_state.num_questions
    st.progress(progress_val, text=f"Question {st.session_state.current_q_idx} of {st.session_state.num_questions}")
    
    st.markdown(f"### 🎙️ Question #{st.session_state.current_q_idx}")
    st.markdown(f'<div class="question-card">{st.session_state.current_question}</div>', unsafe_allow_html=True)
    
    # TTS voice reader using Web Speech API
    tts_html = f"""
    <button onclick="window.speechSynthesis.cancel(); const u = new SpeechSynthesisUtterance('{st.session_state.current_question.replace("'", "\\'")}'); window.speechSynthesis.speak(u);"
            style="background-color:#2563EB; color:white; border:none; padding:8px 16px; border-radius:6px; font-weight:600; cursor:pointer; margin-bottom:15px;">
        🔊 Read Question Aloud
    </button>
    """
    st.components.v1.html(tts_html, height=45)
    
    if st.session_state.current_feedback is None:
        user_answer = st.text_area(
            "Your Answer:",
            height=180,
            placeholder="Structure your answer clearly. Explain concepts, design decisions, and real-world considerations...",
            key=f"ans_input_{st.session_state.current_q_idx}"
        )
        
        if st.button("Submit Answer 🚀", type="primary", use_container_width=True):
            if not user_answer.strip():
                st.warning("Please type your answer before submitting.")
            else:
                with st.spinner("AI Interviewer is analyzing your response..."):
                    feedback = evaluate_answer(
                        question=st.session_state.current_question,
                        answer=user_answer,
                        role=st.session_state.role,
                        difficulty=st.session_state.difficulty,
                        custom_api_key=st.session_state.custom_api_key
                    )
                    
                score = feedback.get("score", 5)
                st.session_state.total_score += score
                st.session_state.current_feedback = feedback
                
                # Save to history
                st.session_state.qa_history.append({
                    "question_no": st.session_state.current_q_idx,
                    "question": st.session_state.current_question,
                    "answer": user_answer,
                    "evaluation": feedback
                })
                st.rerun()
    else:
        # Display AI Feedback Card
        fb = st.session_state.current_feedback
        score = fb.get("score", 0)
        
        score_color = "#059669" if score >= 8 else ("#D97706" if score >= 5 else "#DC2626")
        st.markdown(f"""
        <div style="background-color:#F0FDF4; border:1px solid #BBF7D0; border-left:5px solid {score_color}; border-radius:8px; padding:15px; margin-bottom:15px;">
            <h3 style="color:{score_color}; margin:0;">AI Evaluation &bull; Score: {score} / 10</h3>
        </div>
        """, unsafe_allow_html=True)
        
        fc1, fc2 = st.columns(2)
        with fc1:
            st.success(f"**Strengths:**\n\n{fb.get('strengths')}")
        with fc2:
            st.warning(f"**Areas for Improvement:**\n\n{fb.get('improvements')}")
            
        with st.expander("💡 Recommended Ideal Answer"):
            st.info(fb.get("ideal_answer"))
            
        st.divider()
        if st.session_state.current_q_idx < st.session_state.num_questions:
            if st.button("Next Question ➡️", type="primary", use_container_width=True):
                st.session_state.current_q_idx += 1
                st.session_state.current_feedback = None
                with st.spinner("Generating next question..."):
                    st.session_state.current_question = generate_question(
                        role=st.session_state.role,
                        difficulty=st.session_state.difficulty,
                        question_no=st.session_state.current_q_idx,
                        previous_qa=st.session_state.qa_history,
                        resume_skills=st.session_state.resume_skills,
                        custom_api_key=st.session_state.custom_api_key
                    )
                st.rerun()
        else:
            if st.button("🎉 Complete & View Scorecard", type="primary", use_container_width=True):
                st.session_state.screen = "result"
                st.rerun()

# =========================================================
# 6. Screen 3: Final Assessment & PDF Report
# =========================================================
elif st.session_state.screen == "result":
    max_possible = st.session_state.num_questions * 10
    percentage = (st.session_state.total_score / max_possible * 100) if max_possible > 0 else 0
    
    if percentage >= 80:
        st.balloons()
        verdict = "Outstanding Performance! You demonstrate strong technical expertise."
        verdict_type = st.success
    elif percentage >= 60:
        verdict = "Proficient! Solid foundation with a few growth areas."
        verdict_type = st.info
    else:
        verdict = "Developing. Good effort, but recommend focused practice on core technical concepts."
        verdict_type = st.warning
        
    st.markdown('<div class="main-title">🏆 Interview Results & Scorecard</div>', unsafe_allow_html=True)
    verdict_type(f"**{verdict}**")
    
    # Overview Metrics
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Candidate", st.session_state.candidate_name)
    c2.metric("Target Role", st.session_state.role)
    c3.metric("Final Score", f"{st.session_state.total_score} / {max_possible}")
    c4.metric("Percentage", f"{percentage:.1f}%")
    
    st.divider()
    
    # PDF Download Button
    pdf_bytes = generate_pdf_report(
        candidate_name=st.session_state.candidate_name,
        role=st.session_state.role,
        difficulty=st.session_state.difficulty,
        total_score=st.session_state.total_score,
        max_score=max_possible,
        qa_history=st.session_state.qa_history
    )
    
    dl_col, new_col = st.columns([1, 1])
    with dl_col:
        st.download_button(
            label="📥 Download Full Assessment Report (PDF)",
            data=pdf_bytes,
            file_name=f"Interview_Report_{st.session_state.candidate_name.replace(' ', '_')}.pdf",
            mime="application/pdf",
            type="primary",
            use_container_width=True
        )
    with new_col:
        if st.button("🔄 Start Another Interview", use_container_width=True):
            st.session_state.screen = "setup"
            st.session_state.current_q_idx = 1
            st.session_state.qa_history = []
            st.session_state.total_score = 0
            st.session_state.current_feedback = None
            st.rerun()
            
    st.subheader("📝 Detailed Question-by-Question Review")
    for item in st.session_state.qa_history:
        q_no = item.get("question_no")
        q_text = item.get("question")
        ans_text = item.get("answer")
        eval_dict = item.get("evaluation", {})
        score_val = eval_dict.get("score", 0)
        
        with st.expander(f"Question #{q_no} &bull; Score: {score_val}/10 — {q_text[:70]}..."):
            st.markdown(f"**Question:** {q_text}")
            st.markdown(f"**Your Answer:**\n\n> {ans_text}")
            st.markdown(f"**Strengths:** {eval_dict.get('strengths')}")
            st.markdown(f"**Areas for Improvement:** {eval_dict.get('improvements')}")
            st.markdown(f"**Ideal Reference Answer:**\n\n{eval_dict.get('ideal_answer')}")
