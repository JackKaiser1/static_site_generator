import unittest
from src.markdown_to_html import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        md = "# Hello"
        self.assertEqual(extract_title(md), "Hello")

    def test_extract_title_fail(self):
        md = "### Header 3"
        self.assertRaises(Exception, extract_title, md) 