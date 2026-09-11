import streamlit as st
from googletrans import Translator

translator = Translator()

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌐",
    layout="centered",
)

# ---------------- Custom CSS ----------------
st.markdown("""
<style>
    @keyframes titleShake {
        0% { transform: translateX(0) rotate(0deg); }
        15% { transform: translateX(-4px) rotate(-2deg); }
        30% { transform: translateX(4px) rotate(2deg); }
        45% { transform: translateX(-3px) rotate(-1deg); }
        60% { transform: translateX(3px) rotate(1deg); }
        75% { transform: translateX(-2px) rotate(0deg); }
        100% { transform: translateX(0) rotate(0deg); }
    }

    /* Black Background */
    .stApp {
        background: linear-gradient(135deg, #000000, #0a0a0a, #151515);
    }

    .title-text {
        text-align: center;
        font-size: 2.6rem;
        font-weight: 800;
        color: #e11d74;
        margin-bottom: 0px;
        animation: titleShake 1.8s ease-in-out infinite;
        display: block;
    }

    .subtitle-text {
        text-align: center;
        color: #c2255c;
        font-size: 1rem;
        margin-bottom: 30px;
    }

    div[data-testid="stTextArea"] textarea {
        background-color: #ffffff;
        color: #7a1f42;
        border-radius: 12px;
        border: 1px solid #f193bb;
        font-size: 1rem;
    }

    div[data-baseweb="select"] > div {
        background-color: #ffffff;
        border-radius: 10px;
        border: 1px solid #f193bb;
        color: #7a1f42;
    }

    .stButton > button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        font-weight: 700;
        font-size: 1rem;
        background: linear-gradient(90deg, #ff5ca8, #e11d74);
        color: white;
        border: none;
        transition: 0.3s;
    }

    .stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 15px rgba(255, 92, 168, 0.5);
    }

    .swap-button > button {
        background: #ffffff;
        border: 1px solid #f193bb;
        height: 2.6em;
    }

    .result-box {
        background-color: #fff0f6;
        border: 1px solid #ff8fbf;
        border-radius: 12px;
        padding: 20px;
        color: #b3134f;
        font-size: 1.1rem;
        margin-top: 15px;
    }

    .char-count {
        text-align: right;
        color: #c2255c;
        font-size: 0.8rem;
    }
</style>
""", unsafe_allow_html=True)

# ---------------- Header ----------------
st.markdown(
    '<div class="title-text">🌐 Language Translation Tool</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle-text">Translate text instantly between multiple languages</div>',
    unsafe_allow_html=True
)

# ---------------- Language Options ----------------
languages = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "French": "fr",
    "Malayalam": "ml",
    "German": "de",
    "Japanese": "ja",
}

# ---------------- Session State ----------------
if "source_lang" not in st.session_state:
    st.session_state.source_lang = "English"

if "target_lang" not in st.session_state:
    st.session_state.target_lang = "Tamil"


def swap_languages():
    st.session_state.source_lang, st.session_state.target_lang = (
        st.session_state.target_lang,
        st.session_state.source_lang,
    )


# ---------------- Input ----------------
text = st.text_area(
    "Enter Text",
    height=150,
    placeholder="Type or paste your text here..."
)

st.markdown(
    f'<div class="char-count">{len(text)} characters</div>',
    unsafe_allow_html=True
)

# ---------------- Language Selectors + Swap ----------------
col1, col2, col3 = st.columns([4, 1, 4])

with col1:
    source = st.selectbox(
        "Source Language",
        list(languages.keys()),
        index=list(languages.keys()).index(
            st.session_state.source_lang
        ),
        key="source_lang",
    )

with col2:
    st.write("")
    st.write("")

    st.markdown(
        '<div class="swap-button">',
        unsafe_allow_html=True
    )

    st.button(
        "🔄",
        on_click=swap_languages,
        help="Swap languages"
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

with col3:
    target = st.selectbox(
        "Target Language",
        list(languages.keys()),
        index=list(languages.keys()).index(
            st.session_state.target_lang
        ),
        key="target_lang",
    )

# ---------------- Translate ----------------
if st.button("Translate"):
    if not text.strip():
        st.warning("⚠️ Please enter some text to translate.")

    else:
        with st.spinner("Translating..."):
            try:
                translated = translator.translate(
                    text,
                    src=languages[source],
                    dest=languages[target],
                )

                st.markdown(
                    f'<div class="result-box">{translated.text}</div>',
                    unsafe_allow_html=True,
                )

            except Exception as e:
                st.error(f"Translation failed: {e}")

# ---------------- Footer ----------------
st.markdown(
    '<div class="subtitle-text" style="margin-top:40px;">Built with Python, Streamlit & Googletrans</div>',
    unsafe_allow_html=True,
)