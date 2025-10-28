from .type_enums import BlockType

def markdown_to_blocks(markdown) -> list:
    split_strings = markdown.split("\n\n")
    block_strings = []
    for i in range(len(split_strings)):
        string = split_strings[i].strip()
        if string != "" and not string.isspace():
            block_strings.append(string)
    return block_strings


def block_to_block_type(block) -> BlockType:
    pound_symbol_count = 0
    quote_symbol_count = 0
    dash_symbol_count = 0
    ordered_num_count = 0
    ordered_num = 1
    newline_block = block.split("\n")

    for i in range(0, len(block)):
        char = block[i]
        next_char = block[i + 1]

        if char == "#":
            pound_symbol_count += 1
        if next_char != "#":
            break

    for newline in newline_block:
        if newline.startswith(">"):
            quote_symbol_count += 1
        if newline.startswith("- "):
            dash_symbol_count += 1
        if newline.startswith(f"{ordered_num}. "):
            ordered_num_count += 1
            ordered_num += 1

    if (1 <= pound_symbol_count < 7 and next_char == " "):
        return BlockType.HEADING, pound_symbol_count
    if quote_symbol_count == len(newline_block):
        return BlockType.QUOTE      
    if dash_symbol_count == len(newline_block):
        return BlockType.UNORDERED_LIST
    if ordered_num_count == len(newline_block):
        return BlockType.ORDERED_LIST
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    if block.startswith("\n> "):
        return BlockType.QUOTE
    else:
        return BlockType.PARAGRAPH
    
# print(markdown_to_blocks("""
# This is **bolded** paragraph
# text in a p
# tag here

# This is another paragraph with _italic_ text and `code` here

# """))