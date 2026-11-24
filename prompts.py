"""Prompt builders for Thumbnail AI Studio."""


def build_thumbnail_prompt(
    *,
    topic: str,
    platform: str,
    style: str,
    audience: str,
    language: str,
    count: int = 3,
    creator: str = "",
    key_point: str = "",
    visual_notes: str = "",
) -> str:
    return f"""
You are a professional thumbnail art director and YouTube packaging strategist.
Create {count} distinct thumbnail concepts for the video below.

VIDEO BRIEF
Topic: {topic}
Platform: {platform}
Target audience: {audience}
Output language: {language}
Visual style: {style}
Creator/channel: {creator or "Not specified"}
Main takeaway: {key_point or "Choose the clearest compelling idea based on the topic."}
Visual notes: {visual_notes or "No additional notes."}

For each concept, provide:
1. A short concept name.
2. A clear composition description: main subject, background, framing, lighting, and focal point.
3. Two concise overlay text options in the requested language (aim for 2–5 words each).
4. One matching video title.
5. A detailed image-generation prompt in English. Describe visual elements and layout, not existing copyrighted characters or another creator's exact style.
6. A short readability note for mobile screens.

Guidelines:
- Make each concept meaningfully different.
- Communicate one idea at a glance; avoid clutter and tiny text.
- Use curiosity without deception, fake results, or unsupported claims.
- Do not guarantee clicks, views, or virality.
- Avoid placing important details near the outer edges.
- Keep the output practical for a creator to execute.
- If the platform is not YouTube, adapt the composition to a vertical or square format where appropriate.

Use Markdown headings and separate each concept clearly. Do not include an introduction.
""".strip()


def build_strategy_prompt(topic: str, audience: str) -> str:
    """Small helper retained for future title/packaging extensions."""
    return f"Suggest honest thumbnail angles for '{topic}' for {audience}. Avoid clickbait."
