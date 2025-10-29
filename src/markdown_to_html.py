from .markdown_blocks import block_to_block_type, markdown_to_blocks
from .htmlnode import HTMLNode, LeafNode, ParentNode
from .text_to_node import text_to_textnodes, text_node_to_html_node
from .textnode import TextNode
from .type_enums import BlockType, TextType
import re


def markdown_to_html_node(markdown) -> ParentNode:
    blocks_list = markdown_to_blocks(markdown)
    return htmlnode_from_block(blocks_list)


def htmlnode_from_block(blocks_list) -> str:
    all_children = []
    for block in blocks_list:
        result = block_to_block_type(block)
        if isinstance(result, tuple):
            block_type, heading_num = result
        else:
            block_type = result

        if block_type != BlockType.CODE:
            block = " ".join(block.split())
            children = text_to_children(block)


        if block_type == BlockType.CODE:
            block = "".join(block.split("```"))
            block = block.removeprefix("\n")
        if block_type == BlockType.HEADING:
            block = block.removeprefix("#" * heading_num + " ")
        if block_type == BlockType.QUOTE:
            block = " ".join(block.split())
            block = "\n".join(block.split(">"))
            block = block.removeprefix("\n")


        if block_type == BlockType.PARAGRAPH:
            if children == None:
                all_children.append(LeafNode("p", block))
            else:
                all_children.append(ParentNode("p", children))

        elif block_type == BlockType.HEADING:
            if children == None:
                all_children.append(LeafNode(f"h{heading_num}", block))
            else:
                all_children.append(ParentNode(f"h{heading_num}", children))

        elif block_type == BlockType.CODE:
                code_node = text_node_to_html_node(TextNode(block, TextType.CODE))
                all_children.append(ParentNode("pre", [code_node]))

        elif block_type == BlockType.QUOTE:
            if children == None:
                all_children.append(LeafNode("blockquote", block))
            else:
                all_children.append(ParentNode("blockquote", children))

        elif block_type == BlockType.UNORDERED_LIST:
            all_children.append(list_blocks(block_type, block))

        elif block_type == BlockType.ORDERED_LIST:
            all_children.append(list_blocks(block_type, block))

    return ParentNode("div", all_children)


def text_to_children(text):
    textnode_list = text_to_textnodes(text)
    if textnode_list == [TextNode(text, TextType.TEXT)]:
        return None
    child_list = []
    for node in textnode_list:
        child_list.append(text_node_to_html_node(node))
    return child_list


def list_blocks(block_type, block):
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
    


