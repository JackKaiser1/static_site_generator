
from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        current = text
        images = extract_markdown_images(text)

        if len(images) == 0:
            new_nodes.append(node)
            continue

        for image in images:
            sections = current.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise Exception("Not valid Markdown")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            current = sections[1]
        if current != "":
            new_nodes.append(TextNode(current, TextType.TEXT))
    return new_nodes




def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        current = text 
        links = extract_markdown_links(text)

        if len(links) == 0:
            new_nodes.append(node)
            continue

        for link in links:
            sections = current.split(f"[{link[0]}]({link[1]})")
            if len(sections) != 2:
                raise Exception("Not valid Markdown")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            current = sections[1]
        if current != "":
            new_nodes.append(TextNode(current, TextType.TEXT))
    return new_nodes
    


# print(split_nodes_link([TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)]))