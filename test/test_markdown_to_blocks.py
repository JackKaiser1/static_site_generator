import unittest

from src.markdown_blocks import markdown_to_blocks

class TestMarkDownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        text = """# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item"""
        self.assertEqual(
            markdown_to_blocks(text),
            ['# This is a heading', 'This is a paragraph of text. It has some **bold** and _italic_ words inside of it.', '- This is the first list item in a list block\n- This is a list item\n- This is another list item']
        )

    def test_markdown_to_block_extra_space(self):
        text = """# This is a heading

        



        
This is a paragraph of text. It has some **bold** and _italic_ words inside of it.







- This is the first list item in a list block
- This is a list item
- This is another list item"""
        self.assertEqual(
            markdown_to_blocks(text),
            ['# This is a heading', 'This is a paragraph of text. It has some **bold** and _italic_ words inside of it.', '- This is the first list item in a list block\n- This is a list item\n- This is another list item']
        )

    def test_markdown_to_blocks_no_newline(self):
        text = """# This is a heading
This is a paragraph of text. It has some **bold** and _italic_ words inside of it.
- This is the first list item in a list block
- This is a list item
- This is another list item"""
        self.assertEqual(
            markdown_to_blocks(text),
            ['# This is a heading\nThis is a paragraph of text. It has some **bold** and _italic_ words inside of it.\n- This is the first list item in a list block\n- This is a list item\n- This is another list item']
        )