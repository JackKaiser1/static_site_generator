from textnode import TextNode, TextType    


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue 
        
        str_list = node.text.split(delimiter)

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



# node1 = TextNode("This is a string with **bold** text in the middle", TextType.TEXT)
# # # node2 = TextNode("Bold Test this `is abold test`", TextType.TEXT)
# # # # node3 = TextNode("This is mode `codeddee` stuff", TextType.TEXT)
# print(split_nodes_delimiter([node1], "**", TextType.BOLD))
    















