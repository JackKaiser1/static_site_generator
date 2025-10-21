from textnode import TextNode, TextType
from htmlnode import LeafNode

def text_node_to_html_node(text_node):
    if text_node.text_type not in TextType:
        raise Exception("Type is not in TextType")
    
    elif text_node.text_type == TextType.TEXT:
        return LeafNode(value = text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode(tag="b", value = text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode(tag = "i", value = text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode(tag = "code", value = text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode(tag = "a", value = text_node.text, props = {"href": f"{text_node.url}"})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode(tag = "img", value = " ", props = {"src": f"{text_node.url}", "alt": f"{text_node.text}"})
    
# text_node1 = TextNode(text = "hello", text_type = TextType.IMAGE , url = "www.boot.dev")
# new_leaf = text_node_to_html_node(text_node1)

# print(new_leaf.to_html())