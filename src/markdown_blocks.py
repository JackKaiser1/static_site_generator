from enum import Enum
from collections import Counter


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"


def block_to_block_type(block):
    pound_count = 0

    for i in range(0, len(block)):
        char = block[i]
        next_char = block[i + 1]
        if char == "#":
            pound_count += 1
        if next_char != "#":
            break
    if (pound_count >= 1 
        and pound_count < 7 
        and next_char == " "):
        return BlockType.HEADING, pound_count
    
    newline_block = block.split("\n")
    quote_symbol = 0
    dash_symbol = 0
    ordered_num = 1
    ordered_num_count = 0

    for newline in newline_block:
        if newline.startswith(">"):
            quote_symbol += 1
        if newline.startswith("- "):
            dash_symbol += 1
        if newline.startswith(f"{ordered_num}. "):
            ordered_num_count += 1
            ordered_num += 1
    if quote_symbol == len(newline_block):
        return BlockType.QUOTE      
    if dash_symbol == len(newline_block):
        return BlockType.UNORDERED_LIST
    if ordered_num_count == len(newline_block):
        return BlockType.ORDERED_LIST
    
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    
    if block.startswith("\n> "):
        return BlockType.QUOTE
    
    else:
        return BlockType.PARAGRAPH
    

# print(block_to_block_type(

# """1. Codeblock
# 2. Codeblock
# 3. Codeblock 
# 4. Codeblock"""))


