import unittest
import sys

# sys.path.append("src")

# from src import extract_markdown

from src.extract_markdown import extract_markdown_links, extract_markdown_images

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual(matches, [("image", "https://i.imgur.com/zjjcJKZ.png")])

    def test_extract_markdown_links(self):
        matches = extract_markdown_links("This is text with [a link](https://www.boot.dev) and another [link](https://www.youtube.com/@bootdotdev)")
        self.assertListEqual(matches, [("a link", "https://www.boot.dev"), ("link", "https://www.youtube.com/@bootdotdev")])

    def test_extract_no_image(self):
        matches = extract_markdown_images("This is text with just words!")
        self.assertListEqual(matches, [])

    def test_extract_no_link(self):
        matches = extract_markdown_links("This is text with just words!")
        self.assertListEqual(matches, [])