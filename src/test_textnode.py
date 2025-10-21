import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)


    def test_same_type(self):
        node = TextNode("This is a node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertTrue(node.text_type.value == node2.text_type.value)

    def test_diff_type(self):
        node = TextNode("This is a node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertTrue(node.text_type.value != node2.text_type.value)


    def test_same_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertTrue(node.text == node2.text)

    def test_diff_text(self):
        node = TextNode("This node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertTrue(node.text != node2.text)


    def test_url_none(self):
        node = TextNode("This is a node", TextType.BOLD)
        self.assertIsNone(node.url)
    
    def test_url_not_none(self):
        node = TextNode("This is a node", TextType.BOLD, "www.boot.dev")
        self.assertIsNotNone(node.url)

if __name__ == "__main__":
    unittest.main()