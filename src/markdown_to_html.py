from .markdown_blocks import block_to_block_type, markdown_to_blocks
from .htmlnode import HTMLNode, LeafNode, ParentNode
from .text_to_node import text_to_textnodes, text_node_to_html_node
from .textnode import TextNode
from .type_enums import BlockType, TextType


def markdown_to_html_node(markdown) -> ParentNode:
    blocks_list = markdown_to_blocks(markdown)
    return htmlnode_from_block(blocks_list)


def htmlnode_from_block(blocks_list):
    all_children = []
    for block in blocks_list:
        result = block_to_block_type(block)
        if isinstance(result, tuple):
            block_type, heading_num = result
        else:
            block_type = result



        # if block_type == BlockType.HEADING:
        #     heading_num = block_to_block_type(block)

        if block_type == BlockType.CODE:
            block = "".join(block.split("```"))
            block = block.removeprefix("\n")
        if block_type != BlockType.CODE:
            block = " ".join(block.split())
            children = text_to_children(block)
        if block_type == BlockType.HEADING:
            block = block.removeprefix("#" * heading_num + " ")
        if block_type == BlockType.QUOTE:
            block = " ".join(block.split())
            block = "\n".join(block.split(">"))
            block = block.removeprefix("\n")
        if block_type == BlockType.UNORDERED_LIST:
            block = " ".join(block.split("- "))


            # print(block)

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
            if children == None:
                all_children.append(LeafNode("ul", block))
            else:
                all_children.append(ParentNode("ul", children))

        elif block_type == BlockType.ORDERED_LIST:
            if children == None:
                all_children.append(LeafNode("ol", block))
            else:
                all_children.append(ParentNode("ol", children))

    return ParentNode("div", all_children)


def text_to_children(text):
    textnode_list = text_to_textnodes(text)
    if textnode_list == [TextNode(text, TextType.TEXT)]:
        return None
    child_list = []
    for node in textnode_list:
        child_list.append(text_node_to_html_node(node))
    return child_list


    


# md = """
# This is **bolded** paragraph
# text in a p
# tag here

# This is another paragraph with _italic_ text and `code` here

# """
# html = markdown_to_html_node(md)
# print(html.to_html())