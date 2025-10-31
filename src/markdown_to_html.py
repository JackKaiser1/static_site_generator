from markdown_blocks import block_to_block_type, markdown_to_blocks
from htmlnode import HTMLNode, LeafNode, ParentNode
from text_to_node import text_to_textnodes, text_node_to_html_node
from textnode import TextNode
from type_enums import BlockType, TextType
import re


def markdown_to_html_node(markdown) -> ParentNode:
    all_children = []
    blocks_list = markdown_to_blocks(markdown)
    for block in blocks_list:
        html_node = htmlnode_from_block(block)
        all_children.append(html_node)
    return ParentNode("div", all_children)


def htmlnode_from_block(block) -> HTMLNode:
    result = block_to_block_type(block)
    if isinstance(result, tuple):
        block_type, heading_num = result
        block = block.removeprefix("#" * heading_num + " ")
    else:
        block_type = result

    if block_type != BlockType.CODE:
        block = " ".join(block.split())
        children = text_to_children(block)


    if block_type == BlockType.PARAGRAPH:
        if children == None:
            return LeafNode("p", block)
        else:
            return ParentNode("p", children)

    elif block_type == BlockType.HEADING:
        if children == None:
            return LeafNode(f"h{heading_num}", block)
        else:
            return ParentNode(f"h{heading_num}", children)

    elif block_type == BlockType.CODE:
        block = "".join(block.split("```")).removeprefix("\n")
        code_node = text_node_to_html_node(TextNode(block, TextType.CODE))
        return ParentNode("pre", [code_node])

    elif block_type == BlockType.QUOTE:
        block = "\n".join(block.split(">")).removeprefix("\n").strip()
        if children == None:
            return LeafNode("blockquote", block)
        else:
            return ParentNode("blockquote", children)

    elif block_type == BlockType.UNORDERED_LIST:
        return list_blocks(block_type, block)

    elif block_type == BlockType.ORDERED_LIST:
        return list_blocks(block_type, block)


def text_to_children(text) -> list[HTMLNode]:
    textnode_list = text_to_textnodes(text)
    if textnode_list == [TextNode(text, TextType.TEXT)]:
        return None
    child_list = []
    for node in textnode_list:
        child_list.append(text_node_to_html_node(node))
    return child_list


def list_blocks(block_type, block) -> ParentNode:
    if block_type == BlockType.UNORDERED_LIST:
        parent_tag = "ul"
        list_items = block.split("- ")
    elif block_type == BlockType.ORDERED_LIST:
        parent_tag = "ol"
        list_items = re.split(r"\d+\.\s", block)

    list_children = []
    for item in list_items:
        if item != "":
            item = item.strip()
            item_children = text_to_children(item)
            if not item_children:
                list_children.append(LeafNode("li", item))
            else:
                list_children.append(ParentNode("li", item_children))

    return ParentNode(parent_tag, list_children)



def extract_title(markdown):
    block_list = markdown_to_blocks(markdown)
    for block in block_list:
        if block.startswith("# "):
            return block.removeprefix("# ")
    raise Exception("No header found in markdown string")

# print(extract_title("# Hello"))





    
    


