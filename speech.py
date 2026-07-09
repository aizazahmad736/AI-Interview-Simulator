from streamlit_mic_recorder import mic_recorder
import speech_recognition as sr
import tempfile
import os

def record_answer():
    audio = mic_recorder(
        start_prompt="🎤 Start Recording",
        stop_prompt="⏹ Stop Recording",
        key="mic"
    )

    if audio is None:
        return ""

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    temp_file.write(audio["bytes"])
    temp_file.close()

    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(temp_file.name) as source:
            audio_data = recognizer.record(source)

        text = recognizer.recognize_google(audio_data)

    except Exception as e:
        print(e)
        text = ""

    finally:
        os.remove(temp_file.name)

    return text