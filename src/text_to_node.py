from textnode import TextNode
from type_enums import TextType
from htmlnode import LeafNode
from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_img_link import split_nodes_image, split_nodes_link

def text_to_textnodes(text) -> list:
    new_nodes = []
    node_list = [TextNode(text, TextType.TEXT)]

    if "**" in text:
        node_list = split_nodes_delimiter(node_list, "**", TextType.BOLD)
    if "_" in text:
        node_list = split_nodes_delimiter(node_list, "_", TextType.ITALIC)
    if "`" in text: 
        node_list = split_nodes_delimiter(node_list, "`", TextType.CODE)
    node_list = split_nodes_image(node_list)
    node_list = split_nodes_link(node_list)

    new_nodes.extend(node_list)

    return new_nodes


def text_node_to_html_node(text_node) -> LeafNode:
    if text_node.text_type not in TextType:
        raise Exception("Type is not in TextType")
    
    elif text_node.text_type == TextType.TEXT:
        return LeafNode(value = text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode(tag = "b", value = text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode(tag = "i", value = text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode(tag = "code", value = text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode(tag = "a", value = text_node.text, props = {"href": f"{text_node.url}"})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode(tag = "img", value = " ", props = {"src": f"{text_node.url}", "alt": f"{text_node.text}"})
    


        