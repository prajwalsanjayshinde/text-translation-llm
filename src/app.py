import streamlit as st
from translator import Translator
from gtts import gTTS
import io

LANGUAGE_NAMES = {
    "ar": "Arabic", "bg": "Bulgarian", "zh": "Chinese", "cs": "Czech", "da": "Danish",
    "nl": "Dutch", "en": "English", "et": "Estonian", "fi": "Finnish", "fr": "French",
    "de": "German", "el": "Greek", "he": "Hebrew", "hi": "Hindi", "hu": "Hungarian",
    "id": "Indonesian", "it": "Italian", "ja": "Japanese", "ko": "Korean", "lv": "Latvian",
    "lt": "Lithuanian", "mk": "Macedonian", "no": "Norwegian", "pl": "Polish", "pt": "Portuguese",
    "ro": "Romanian", "ru": "Russian", "sk": "Slovak", "sl": "Slovenian", "es": "Spanish",
    "sv": "Swedish", "tr": "Turkish", "uk": "Ukrainian", "vi": "Vietnamese", "mr": "Marathi",
    "bn": "Bengali", "gu": "Gujarati", "ta": "Tamil", "te": "Telugu", "ml": "Malayalam",
    "kn": "Kannada", "pa": "Punjabi", "or": "   Odia", "as": "Assamese", "si": "Sinhala",
    "th": "Thai", "tl": "Tagalog", "ur": "Ur du", "sw": "Swahili", "ha": "Hausa",
    "yo": "Yoruba", "ig": "Igbo", "zu": "Zulu", "af": "Afrikaans", "am": "Amharic", "hy": "Armenian",   "be": "Belarusian", "bn": "Bengali", "bo": "Tibetan", "bs": "Bosnian",
    "ca": "Catalan", "eu": "Basque", "gl": "            
}

st.title("LLM Text Translator")

translator = Translator()
translator.load_model()

text = st.text_area("Enter text to translate:")
target_language = st.selectbox(
    "Select target language:",
    options=translator.supported_languages,
    format_func=lambda x: f"{LANGUAGE_NAMES.get(x, x.title())} ({x})"
)

# Use session state to store the translation
if "translated" not in st.session_state:
    st.session_state.translated = ""

if st.button("Translate"):
    if not text.strip():
        st.warning("Please enter some text to translate.")
    else:
        try:
            st.session_state.translated = translator.translate_text(text, target_language)
            st.success(f"**Translated text:**\n\n{st.session_state.translated}")
        except ValueError as e:
            st.error(str(e))

if st.session_state.translated:
    st.success(f"**Translated text:**\n\n{st.session_state.translated}")
    if st.button("🔊 Speak Translated Text"):
        # Map your language code to gTTS supported codes
        gtts_lang_map = {
            "en": "en", "fr": "fr", "de": "de", "es": "es", "it": "it", "pt": "pt",
            "ru": "ru", "hi": "hi", "ja": "ja", "ko": "ko", "zh": "zh-cn", "ar": "ar",
            "tr": "tr", "nl": "nl", "sv": "sv", "fi": "fi", "pl": "pl", "ro": "ro",
            "cs": "cs", "bg": "bg", "uk": "uk", "vi": "vi", "id": "id"
        }
        tts_lang = gtts_lang_map.get(target_language, "en")
        if st.session_state.translated.strip():
            try:
                tts = gTTS(st.session_state.translated, lang=tts_lang)
                fp = io.BytesIO()
                tts.write_to_fp(fp)
                fp.seek(0)
                st.audio(fp, format="audio/mp3")
            except Exception as e:
                st.warning(f"Could not generate audio: {e}")
        else:
            st.warning("No translated text to speak.")