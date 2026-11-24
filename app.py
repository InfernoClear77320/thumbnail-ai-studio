from __future__ import annotations

import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

from src.prompts import build_thumbnail_prompt, build_strategy_prompt

load_dotenv()

st.set_page_config(
    page_title="Thumbnail AI Studio",
    page_icon="🖼️",
    layout="wide",
)

st.markdown("""
<style>
.stApp {background:radial-gradient(ellipse at 82% 0%,#30204f 0%,#111321 42%,#0a0b12 100%);}
.block-container {max-width:1120px;padding-top:2rem;}
.hero {padding:1.7rem 1.8rem;border:1px solid #40365f;border-radius:20px;
background:linear-gradient(120deg,rgba(25,28,53,.97),rgba(54,30,78,.92));margin-bottom:1.2rem;}
.hero h1 {margin:0;font-size:clamp(2rem,4vw,3rem);letter-spacing:-.04em;}
.hero p {color:#d0c8e5;margin:.5rem 0 0;font-size:1.05rem;}
div[data-testid="stMetric"] {background:rgba(255,255,255,.035);border:1px solid #343650;padding:12px 16px;border-radius:14px;}
div.stButton>button,div.stDownloadButton>button {border-radius:10px;font-weight:650;}
</style>
<div class="hero">
<h1>🖼️ Thumbnail AI Studio</h1>
<p>Turn a video idea into a clickable thumbnail concept, title, and image-generation prompt.</p>
</div>
""", unsafe_allow_html=True)

def get_api_key() -> str:
    key = os.getenv("OPENAI_API_KEY", "").strip()
    if not key:
        try:
            key = str(st.secrets.get("OPENAI_API_KEY", "")).strip()
        except Exception:
            key = ""
    return key

with st.sidebar:
    st.header("🎨 Studio settings")
    platform = st.selectbox("Platform", ["YouTube", "TikTok", "Instagram Reels", "Podcast"])
    style = st.selectbox("Visual style", [
        "High-contrast creator thumbnail", "Minimal and premium", "Cinematic",
        "Playful and colorful", "Clean educational", "Tech / futuristic",
        "Documentary", "Custom"
    ])
    audience = st.text_input("Target audience", "Curious viewers aged 18–34")
    language = st.selectbox("Text language", ["English", "Russian", "Spanish", "German", "French"])
    options = st.slider("Concepts to generate", 1, 5, 3)
    st.divider()
    st.caption("The app creates concepts and image prompts. It does not generate the final image in this starter version.")

left, right = st.columns([1.15, .85], gap="large")
with left:
    st.subheader("1. Describe your video")
    with st.form("thumbnail_form"):
        topic = st.text_input("Video topic", placeholder="e.g. I tested 7 free AI tools")
        creator = st.text_input("Channel or creator name (optional)")
        key_point = st.text_area("Main takeaway", placeholder="What should viewers understand at a glance?", height=90)
        reference = st.text_area("Visual notes (optional)", placeholder="Colors, objects, person/character, brand style...", height=90)
        submitted = st.form_submit_button("✨ Create thumbnail concepts", type="primary", use_container_width=True)

with right:
    st.subheader("2. What you’ll get")
    st.markdown("""
    - Thumbnail concept and composition
    - Short overlay-text options
    - Matching video title ideas
    - Image-generation prompt
    - Practical readability notes
    """)
    st.info("Good thumbnails communicate one clear idea. Keep text short and make the main subject easy to recognize.")

if submitted:
    if not topic.strip():
        st.error("Enter a video topic first.")
    else:
        key = get_api_key()
        if not key:
            st.error("OPENAI_API_KEY is missing. Add it to your environment or Streamlit Secrets; see README.md.")
        else:
            prompt = build_thumbnail_prompt(
                topic=topic.strip(), platform=platform, style=style,
                audience=audience.strip() or "General audience",
                language=language, count=options, creator=creator.strip(),
                key_point=key_point.strip(), visual_notes=reference.strip(),
            )
            try:
                with st.spinner("Designing thumbnail concepts..."):
                    client = OpenAI(api_key=key)
                    result = client.responses.create(
                        model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
                        input=prompt,
                    ).output_text.strip()
                st.session_state["concepts"] = result
                st.session_state["topic"] = topic.strip()
            except Exception as exc:
                st.error(f"Generation failed: {exc}")
                st.caption("Check your API key, account access, and network connection.")

if "concepts" in st.session_state:
    st.divider()
    st.subheader("3. Your thumbnail concepts")
    result = st.session_state["concepts"]
    st.text_area("Editable concepts", value=result, height=520, key="editable_concepts")
    final_result = st.session_state.get("editable_concepts", result)
    st.download_button(
        "⬇️ Download concepts (.txt)",
        data=final_result,
        file_name="thumbnail-concepts.txt",
        mime="text/plain",
        use_container_width=True,
    )
    st.download_button(
        "⬇️ Download concepts (.md)",
        data=final_result,
        file_name="thumbnail-concepts.md",
        mime="text/markdown",
        use_container_width=True,
    )

st.divider()
st.subheader("📦 Get the program")
st.markdown("When you publish your app or downloadable build, add its URL to `PROGRAM_DOWNLOAD_URL` in `app.py`.")
download_url = os.getenv("PROGRAM_DOWNLOAD_URL", "").strip()
if download_url and download_url.startswith(("https://", "http://")) and "PASTE_YOUR_PROGRAM_LINK_HERE" not in download_url:
    st.link_button("⬇️ Download the program", download_url, use_container_width=True)
else:
    st.button("⬇️ Download the program — add your link", disabled=True, use_container_width=True)
    st.caption("Placeholder: paste your program URL into the PROGRAM_DOWNLOAD_URL environment variable or Streamlit Secrets. The button becomes active once you add a valid URL.")

with st.expander("🔐 Privacy and API usage"):
    st.write("Your topic and instructions are sent to the configured AI provider to generate concepts. Do not include confidential information. API usage may incur charges. This starter does not store a server-side history.")

st.caption("Open-source starter · Python + Streamlit")
