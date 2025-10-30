import re
from textnode import TextNode
from type_enums import TextType


def extract_markdown_images(text) -> list[tuple]:
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text) -> list[tuple]:
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes) -> list:
    new_nodes = []

    for node in old_nodes:
        current = node.text
        images = extract_markdown_images(current)

        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if len(images) == 0:
            new_nodes.append(node)
            continue

        for image in images:
            sections = current.split(f"![{image[0]}]({image[1]})", 1)

            if len(sections) != 2:
                raise ValueError("Not a valid markdown string")
            elif sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))

            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            current = sections[1]

        if current != "":
            new_nodes.append(TextNode(current, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes) -> list:
    new_nodes = []

    for node in old_nodes:
        current = node.text
        links = extract_markdown_links(current)

        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if len(links) == 0:
            new_nodes.append(node)
            continue

        for link in links:
            sections = current.split(f"[{link[0]}]({link[1]})", 1)

            if len(sections) != 2:
                raise ValueError("Not a valid markdown string")
            elif sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))

            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            current = sections[1]

        if current != "":
            new_nodes.append(TextNode(current, TextType.TEXT))
    return new_nodes
    
