
def markdown_to_blocks(markdown):
    split_strings = markdown.split("\n\n")
    block_strings = []
    for i in range(len(split_strings)):
        string = split_strings[i].strip()
        if string != "" and not string.isspace():
            block_strings.append(string)
    return block_strings

# print(markdown_to_blocks("""
# - This is the first list item in a list block
# - This is a list item
# - This is another list item"""))