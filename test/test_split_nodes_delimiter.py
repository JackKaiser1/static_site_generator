import unittest

from src.textnode import TextNode
from src.type_enums import TextType
from src.split_nodes_delimiter import split_nodes_delimiter

class TestSplitNodes(unittest.TestCase):
    def test_raise_exception(self):
        node1 = TextNode("This is a string with **bold text in the middle", TextType.TEXT)
        self.assertRaises(Exception, split_nodes_delimiter, [node1], "**", TextType.BOLD)

    def test_non_text_passes(self):
        node1 = TextNode("**bold**", TextType.BOLD)
        self.assertEqual(split_nodes_delimiter([node1], "**", TextType.BOLD), [TextNode("**bold**", TextType.BOLD)])

    def test_split_node_bold(self):
        node1 = TextNode("This is a string with **bold** text in the middle", TextType.TEXT)

        self.assertEqual(
            
            split_nodes_delimiter([node1], "**", TextType.BOLD), 
            [TextNode("This is a string with ", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode(" text in the middle", TextType.TEXT)])
        
    def test_split_node_italic(self):
        node1 = TextNode("This is a string with _bold_ text in the middle", TextType.TEXT)

        self.assertEqual(

            split_nodes_delimiter([node1], "_", TextType.ITALIC),
            [TextNode("This is a string with ", TextType.TEXT), TextNode("bold", TextType.ITALIC), TextNode(" text in the middle", TextType.TEXT)]
        )

    def test_split_code_twice(self):
        node1 = TextNode("This is a string with `code` text in the middle", TextType.TEXT)
        node2 = TextNode("This is also a string with `code` text in the middle", TextType.TEXT)

        new_list = split_nodes_delimiter([node1, node2], "`", TextType.CODE)

        self.assertEqual(new_list, 
            [TextNode("This is a string with ", TextType.TEXT), TextNode("code", TextType.CODE), TextNode(" text in the middle", TextType.TEXT),
             TextNode("This is also a string with ", TextType.TEXT), TextNode("code", TextType.CODE), TextNode(" text in the middle", TextType.TEXT)])

    def test_split_and_not_split(self):
        node1 = TextNode("This is a string with `code` text in the middle", TextType.TEXT)
        node2 = TextNode("`more code`", TextType.CODE)

        new_list = split_nodes_delimiter([node1, node2], "`", TextType.CODE)
        
        self.assertEqual(new_list, 
            [TextNode("This is a string with ", TextType.TEXT), TextNode("code", TextType.CODE), TextNode(" text in the middle", TextType.TEXT),
             TextNode("`more code`", TextType.CODE)])

    def test_length(self):
        node1 = TextNode("This is a string with _bold_ text in the middle", TextType.TEXT)
        new_list = split_nodes_delimiter([node1], "_", TextType.ITALIC)
        self.assertEqual(len(new_list), 3)