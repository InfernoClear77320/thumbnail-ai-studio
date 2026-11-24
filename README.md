# 🖼️ Thumbnail AI Studio

Turn a video idea into thumbnail concepts, overlay text, title ideas, and image-generation prompts.

Thumbnail AI Studio is a beginner-friendly Python + Streamlit app for creators who want help planning clear, compelling thumbnails for YouTube and other short-form platforms.

## Features

- Generate 1–5 distinct thumbnail concepts
- Choose platform, audience, language, and visual style
- Get composition notes, overlay text, title ideas, and image prompts
- Edit and download concepts as TXT or Markdown
- Add your own program download URL to activate the in-app download button
- Keep API keys out of source code

> This starter generates thumbnail concepts and prompts. It does not create the final image file itself.

## Run locally

Requirements: Python 3.10+ and an API key for a model available through the OpenAI API.

```bash
git clone https://github.com/YOUR-USERNAME/thumbnail-ai-studio.git
cd thumbnail-ai-studio
python -m venv .venv
```

Activate the environment, then install:

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

Copy `.env.example` to `.env` and fill in your values:

```env
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-4.1-mini
PROGRAM_DOWNLOAD_URL=https://your-program-download-link
```

Run the app:

```bash
streamlit run app.py
```

## Add your program download link

The app includes a **Download the program** button. It is intentionally disabled until you add your own link.

Set `PROGRAM_DOWNLOAD_URL` in your local `.env` file or Streamlit Secrets. Replace the example URL with the actual URL where you host your program or downloadable build.

For Streamlit Community Cloud, add these under **App settings → Secrets**:

```toml
OPENAI_API_KEY = "your_api_key_here"
OPENAI_MODEL = "gpt-4.1-mini"
PROGRAM_DOWNLOAD_URL = "https://your-real-download-link"
```

Use a direct downloadable URL if you want the button to start a download immediately. A normal website URL will open that page instead.

## Deploy

1. Push this repository to GitHub.
2. Deploy it through [Streamlit Community Cloud](https://share.streamlit.io/).
3. Select `app.py`.
4. Add the API key and program download URL in Secrets.
5. Deploy the app.

Hosting may have a free tier; API usage may cost money.

## Security

- Never commit `.env` or `.streamlit/secrets.toml`.
- Never paste API keys into public issues or screenshots.
- User prompts are sent to the configured AI provider.
- Do not enter confidential information.

## License

MIT.
