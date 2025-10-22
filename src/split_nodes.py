
from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            continue

        text = node.text
        extracted_text = extract_markdown_images(text)

        text_replace = text.replace("[", "-").replace("]", "-").replace("(", "-").replace(")", "-")
        text_split = text_replace.split("-")



        # if len(text_split) % 2 == 0:
        #     raise Exception("Not valid Markdown text")

        for i in range(len(text_split)):
            str = text_split[i]

            if str == "":
                continue
            elif i % 2 == 0 or i == 0 and str not in extracted_text:
                new_nodes.append(TextNode(str, TextType.TEXT))
            else:
                new_nodes.append(TextNode(str, TextType.IMAGE, text_split[i + 2]))





    return new_nodes



def split_nodes_link(old_nodes):
    pass


print(split_nodes_image([TextNode("This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)]))