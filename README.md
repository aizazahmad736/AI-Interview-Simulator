
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red?logo=streamlit)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-blue?logo=google)
![License](https://img.shields.io/badge/License-MIT-green)


# 🤖 AI Interview Simulator

A simple web app that generates mock interview questions tailored to a chosen job role and difficulty level, powered by Google's Gemini API and built with Streamlit.with user friendly interface and well designed as well

## Features

- 🎯 **Role-based questions** — choose from Python Developer, Machine Learning Engineer, Data Analyst, Frontend Developer, or HR Interview
- 📊 **Difficulty levels** — Beginner, Intermediate, or Advanced
- ⚡ **AI-generated questions** — uses the Gemini API to generate a fresh interview question on demand
- 🖥️ **Clean, simple UI** — built with Streamlit, no frontend setup required

## Tech Stack

- **Frontend/UI:** Streamlit
- **AI Model:** Google Gemini (`google-generativeai`)
- **Language:** Python
- **Config:** `python-dotenv` for environment variables

## Getting Started

### Prerequisites

- Python 3.9+
- A [Google Gemini API key](https://ai.google.dev/)

### Installation

1. Clone the repo
   ```bash
   git clone https://github.com/aizazahmad736/AI-Interview-Simulator.git
   cd AI-Interview-Simulator
   ```

2. Create a virtual environment (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables

   Create a `.env` file in the project root:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

### Running the app

```bash
streamlit run app.py
```

Then open the local URL Streamlit prints (usually `http://localhost:8501`) in your browser.

## Usage

1. Enter your name
2. Select the interview role you want to practice for
3. Select a difficulty level
4. Click **Start Interview** to generate your question

## Project Structure

```
AI-Interview-Simulator/
├── app.py              # Streamlit app entry point
├── config.py           # Loads GEMINI_API_KEY from .env
├── requirements.txt    # Python dependencies
└── interview/
    └── interviewer.py  # Question generation logic (Gemini API calls)
```

> **Note:** `interview/interviewer.py` contains the `generate_question()` function that `app.py` depends on — make sure this module exists in your local copy before running the app.

## Roadmap

Some dependencies (`PyPDF2`, `reportlab`) are already included for planned features:

- [ ] Resume upload & parsing to personalize questions
- [ ] Multi-question interview sessions (not just one question)
- [ ] AI-scored feedback on answers
- [ ] Downloadable PDF interview report

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to open a PR or issue on the [GitHub repo](https://github.com/aizazahmad736/AI-Interview-Simulator).

## License

Add your preferred license here (e.g., MIT).

## Future Improvements

- Add more AI-generated interview questions
- Add user authentication
- Add interview performance analytics
- Add support for multiple programming languages
- Improve speech recognition accuracy