from markdown_to_blocks import markdown_to_blocks
from markdown_blocks import block_to_block_type 
from markdown_blocks import BlockType
from htmlnode import HTMLNode, LeafNode, ParentNode


def markdown_to_html(markdown):
    blocks_list = markdown_to_blocks(markdown)

    htmlnode_from_block(blocks_list)














def htmlnode_from_block(blocks_list):
    # types = {"paragraph": BlockType.PARAGRAPH,
    #          "heading": BlockType.HEADING,
    #          "code": BlockType.CODE,
    #          "quote": BlockType.QUOTE,
    #          "unordered list": BlockType.UNORDERED_LIST,
    #          "ordered list":  BlockType.ORDERED_LIST,}
    
    for block in blocks_list:
        block_type, heading_num = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            new_node = HTMLNode("p", block)

        elif block_type == BlockType.HEADING:
            new_node = HTMLNode(f"h{heading_num}", block)

        elif block_type == BlockType.CODE:
            new_node = HTMLNode("code", block)

        elif block_type == BlockType.QUOTE:
            new_node = HTMLNode("quoteblock", block)

        elif block_type == BlockType.UNORDERED_LIST:
            new_node = HTMLNode("ul", block)

        elif block_type == BlockType.ORDERED_LIST:
            new_node = HTMLNode("ol", block)


def text_to_children(text):
    pass