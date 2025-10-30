from textnode import TextNode
from type_enums import TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type) -> list:
    new_nodes = []
    for node in old_nodes:
        str_list = node.text.split(delimiter)

        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue 
        if len(str_list) % 2 == 0:
            raise Exception("String is not valid markdown")
        
        for i in range(len(str_list)):
            str = str_list[i]
            
            if str == "":
                continue
            elif i % 2 == 0 or i == 0:
                new_nodes.append(TextNode(str, TextType.TEXT))
            else: new_nodes.append(TextNode(str, text_type))

    return new_nodes

