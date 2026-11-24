import unittest
from src.prompts import build_thumbnail_prompt


class ThumbnailPromptTests(unittest.TestCase):
    def test_prompt_includes_video_brief(self):
        prompt = build_thumbnail_prompt(
            topic="I tested 7 free AI tools",
            platform="YouTube",
            style="High-contrast creator thumbnail",
            audience="new creators",
            language="English",
            count=2,
        )
        self.assertIn("I tested 7 free AI tools", prompt)
        self.assertIn("new creators", prompt)
        self.assertIn("Create 2 distinct thumbnail concepts", prompt)


if __name__ == "__main__":
    unittest.main()
