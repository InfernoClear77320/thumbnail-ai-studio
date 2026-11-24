# 🖼️ Thumbnail AI Studio

<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/dae5979b-7cac-41c2-bbe4-601e01f9ea3c" />

Turn a video idea into thumbnail concepts, overlay text, title ideas, and image-generation prompts.

## Download

**Download the program as a ZIP file:** [Download Thumbnail AI Studio](https://github.com/InfernoClear77320/thumbnail-ai-studio/releases/tag/AI-Studio)

The ZIP file is hosted in this GitHub repository. Replace `thumbnail-ai-studio.zip` in the link above with the exact filename of the ZIP you upload.

## Features

- Generate 1–5 distinct thumbnail concepts
- Choose a platform, audience, language, and visual style
- Get composition notes, overlay text, title ideas, and image prompts
- Edit and download concepts as TXT or Markdown
- Keep API keys out of source code

> This app generates thumbnail concepts and prompts. It does not create the final image file itself.

## Run locally

Requirements: Python 3.10+ and an OpenAI API key.

```bash
git clone https://github.com/YOUR-USERNAME/thumbnail-ai-studio.git
cd thumbnail-ai-studio
python -m venv .venv
```

Activate the environment, then install the dependencies:

**Windows PowerShell**
```powershell
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

**macOS / Linux**
```bash
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Copy `.env.example` to `.env` and add your API key:

```env
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-4.1-mini
```

Run the app:

```bash
streamlit run app.py
```

## Deploy

1. Push this repository to GitHub.
2. Deploy it through [Streamlit Community Cloud](https://share.streamlit.io/).
3. Select `app.py`.
4. Add `OPENAI_API_KEY` in Streamlit Secrets.
5. Deploy the app.

API usage may cost money.

## Security

- Never commit `.env` or `.streamlit/secrets.toml`.
- Never share API keys in public issues or screenshots.
- User prompts are sent to the configured AI provider.
- Do not enter confidential information.

## License

MIT.
