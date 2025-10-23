from textnode import TextNode, TextType
from htmlnode import LeafNode
from split_nodes_delimiter import split_nodes_delimiter
from split_nodes import split_nodes_image, split_nodes_link

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
    

def text_to_textnodes(text):
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

    # for node in new_nodes:
    #     print(node)
    return new_nodes
        

# print(text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"))


# text_node1 = TextNode(text = "hello", text_type = TextType.IMAGE , url = "www.boot.dev")
# new_leaf = text_node_to_html_node(text_node1)

# print(new_leaf.to_html())