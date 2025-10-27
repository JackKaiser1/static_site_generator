import unittest
import sys

# sys.path.append("src")

# from src import textnode, htmlnode, text_node_to_html_node

from src.textnode import TextNode, TextType
# from src.htmlnode import LeafNode, HTMLNode
from src.text_node_to_html_node import text_node_to_html_node, text_to_textnodes


class TestTextNodeToHTML(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_link(self):
        node = TextNode("This is a text node", TextType.LINK, "www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props, {"href": "www.boot.dev"})
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_image(self):
        node = TextNode("This is alt text", TextType.IMAGE, "www.image-link.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props, {"src": "www.image-link.com", "alt": "This is alt text"})
        self.assertEqual(html_node.value, " ")


class TestTextToTextNode(unittest.TestCase):
    def test_text_to_text_node(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        self.assertEqual(
            [
    TextNode("This is ", TextType.TEXT),
    TextNode("text", TextType.BOLD),
    TextNode(" with an ", TextType.TEXT),
    TextNode("italic", TextType.ITALIC),
    TextNode(" word and a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" and an ", TextType.TEXT),
    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
    TextNode(" and a ", TextType.TEXT),
    TextNode("link", TextType.LINK, "https://boot.dev"),
],
    text_to_textnodes(text)
        )
    
    def test_text_no_change(self):
        text = "This is plain text no work should be done"
        self.assertEqual(
            [TextNode(text, TextType.TEXT)],
            text_to_textnodes(text)
        )