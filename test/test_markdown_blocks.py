import unittest
import sys

# sys.path.append("src")

# from src import markdown_blocks

from src.markdown_blocks import BlockType, block_to_block_type

class TestMarkdownBlocks(unittest.TestCase):

    def test_paragraph_to_blocktype(self):
        paragraph = "This is some plain text"
        self.assertEqual(block_to_block_type(paragraph), BlockType.PARAGRAPH)

    def test_fail_paragraph_to_blocktype(self):
        paragraph = "## This is actually a heading"
        self.assertNotEqual(block_to_block_type(paragraph), BlockType.PARAGRAPH)

    def test_heading_to_blocktype(self):
        heading = "###### This is a heading"
        self.assertEqual(block_to_block_type(heading), (BlockType.HEADING, 6))

    def test_fail_heading_to_blocktype(self):
        heading = "######### This is not a heading"
        self.assertNotEqual(block_to_block_type(heading), BlockType.HEADING)

    def test_code_to_blocktype(self):
        code = "```This is a code block```"
        self.assertEqual(block_to_block_type(code), BlockType.CODE)

    def test_fail_code_to_blocktype(self):
        code = "This is not a code block```"
        self.assertNotEqual(block_to_block_type(code), BlockType.CODE)

    def test_quote_to_blocktype(self):
        quote = (
"""> This is a quote line
> this is another quote line
> this is a third quote line""")
        self.assertEqual(block_to_block_type(quote), BlockType.QUOTE)

    def test_fail_quote_to_blocktype(self):
        quote = (
"""> This is a quote line
this is not a quote line
> this is a third quote line""")
        self.assertNotEqual(block_to_block_type(quote), BlockType.QUOTE)

    def test_unordered_to_blocktype(self):
        unordered_list = (
"""- Here is an item
- here is another item 
- here is a third item""")
        self.assertEqual(block_to_block_type(unordered_list), BlockType.UNORDERED_LIST)

    def test_fail_unordered_to_blocktype(self):
        unordered_list = (
"""Here is an item
- here is another item 
- here is a third item""")
        self.assertNotEqual(block_to_block_type(unordered_list), BlockType.UNORDERED_LIST)

    def test_ordered_to_blocktype(self):
        ordered_list = (
"""1. Item 
2. Item
3. Item""")
        self.assertEqual(block_to_block_type(ordered_list), BlockType.ORDERED_LIST)

    def test_fail_ordered_to_blocktype(self):
        ordered_list = (
"""1. Item 
Item
3. Item""")
        self.assertNotEqual(block_to_block_type(ordered_list), BlockType.ORDERED_LIST)

    