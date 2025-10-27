import unittest
import sys

# sys.path.append("src")

# from src import htmlnode

from src.htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_no_value(self):
        node = LeafNode(value=None, tag="a", props={"href": "www.boot.dev"})
        self.assertRaises(ValueError, node.to_html)



class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(),"<div><span><b>grandchild</b></span></div>")

    def test_to_html_with_greatgrandchildren(self):
        great_grandchild_node = LeafNode("b", "great grandchild")
        grandchild_node = ParentNode("p", [great_grandchild_node])
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><p><b>great grandchild</b></p></span></div>")


    def test_to_html_with_children_and_props(self):
        child_node = LeafNode(tag="span", value="child", props={"color": "red"})
        parent_node = ParentNode(tag="div", children=[child_node], props={"href": "www.boot.dev"})
        self.assertEqual(parent_node.to_html(), "<div href=www.boot.dev><span color=red>child</span></div>")

    def test_to_html_with_grandchildren_and_props(self):
        grandchild_node = LeafNode(tag="b", value="grandchild")
        child_node = ParentNode(tag="span", children=[grandchild_node], props={"color": "red"})
        parent_node = ParentNode(tag="div", children=[child_node], props={"href": "www.boot.dev"})
        self.assertEqual(parent_node.to_html(),"<div href=www.boot.dev><span color=red><b>grandchild</b></span></div>")

    def test_to_html_with_greatgrandchildren_and_props(self):
        great_grandchild_node = LeafNode(tag="b", value="great grandchild")
        grandchild_node = ParentNode(tag="p", children=[great_grandchild_node], props={"href": "www.boot.dev"})
        child_node = ParentNode(tag="span", children=[grandchild_node], props={"href": "www.boot.dev"})
        parent_node = ParentNode(tag="div", children=[child_node], props={"href": "www.boot.dev"})
        self.assertEqual(parent_node.to_html(), "<div href=www.boot.dev><span href=www.boot.dev><p href=www.boot.dev><b>great grandchild</b></p></span></div>")


    def test_to_html_no_children(self):
        parent_node = ParentNode(tag="div", children=None, props={"href": "www.boot.dev"})
        self.assertRaises(ValueError, parent_node.to_html)

    def test_to_html_no_tag(self):
        child_node = LeafNode(tag="span", value="child")
        parent_node = ParentNode(tag=None, children=[child_node])
        self.assertRaises(ValueError, parent_node.to_html)