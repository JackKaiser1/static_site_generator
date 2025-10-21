import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_not_none(self):
        child_node = HTMLNode(tag="h1", value="Hello World")
        node = HTMLNode(tag="h1", value="Hello World", children=child_node, props={"href": "https://www.google.com", "target": "_blank",})
        self.assertTrue(node.props)

    def test_props_output(self):
        child_node = HTMLNode(tag="h1", value="Hello World")
        node = HTMLNode(tag="h1", value="Hello World", children=child_node, props={"href": "https://www.google.com", "target": "_blank",})
        self.assertIsNotNone(node.props_to_html())

    def test_has_child(self):
        child_node = HTMLNode(tag="h1", value="Hello World")
        node = HTMLNode(tag="h1", value="Hello World", children=child_node, props={"href": "https://www.google.com", "target": "_blank",})
        self.assertTrue(node.children)



class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click here!", {"href": "www.boot.dev"})
        self.assertEqual(node.to_html(), "<a href=www.boot.dev>Click here!</a>")

    def test_no_tag(self):
        node = LeafNode(value="Click here!", props={"href": "www.boot.dev"})
        self.assertEqual(node.to_html(), "Click here!")

    # def test_no_value(self):
    #     node = LeafNode(value="Click here!", tag="a", props={"href": "www.boot.dev"})
    #     self.assertTrue(ValueError)
