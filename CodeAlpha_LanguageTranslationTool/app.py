import io
import streamlit as st
from deep_translator import GoogleTranslator

try:
    from gtts import gTTS
except ImportError:
    gTTS = None

st.set_page_config(
    page_title="Language Translator",
    page_icon="🌍",
    layout="centered"
)

st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.st-emotion-cache-1plm4a3 { display: none; }
h1 a, h2 a, h3 a { display: none !important; }
</style>
""", unsafe_allow_html=True)

st.title("🌍 Language Translator")
st.markdown("### Translate text seamlessly")

LANGUAGES = {
    "English": "en",
    "Urdu": "ur",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Chinese (Simplified)": "zh-CN"
}

text_input = st.text_area("Enter text to translate:", height=150)

col1, col2 = st.columns(2)
with col1:
    source_lang = st.selectbox("Source Language", list(LANGUAGES.keys()))
with col2:
    target_lang = st.selectbox("Target Language", list(LANGUAGES.keys()), index=5)

if st.button("Translate Text", type="primary"):
    if not text_input.strip():
        st.warning("Please enter some text to translate.")
    elif source_lang == target_lang:
        st.info("Source and target languages are identical.")
    else:
        try:
            target_code = LANGUAGES[target_lang]
            translator = GoogleTranslator(
                source=LANGUAGES[source_lang],
                target=target_code
            )
            translated_text = translator.translate(text_input)

            st.success("Translation:")
            st.text_area("Output", translated_text, height=150)
            
            st.caption("Copy the text below:")
            st.code(translated_text, language=None)

            if gTTS:
                try:
                    tts = gTTS(text=translated_text, lang=target_code)
                    audio_fp = io.BytesIO()
                    tts.write_to_fp(audio_fp)
                    st.audio(audio_fp, format='audio/mp3')
                except Exception as e:
                    st.error(f"Text-to-Speech error: {e}")
            else:
                st.warning("Text-to-Speech is unavailable. Install gTTS via pip.")

        except Exception as e:
            st.error("Translation failed. Please try again.")
