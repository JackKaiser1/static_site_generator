from .textnode import TextNode
from .type_enums import TextType

def main():
    node = TextNode("hello world", TextType.BOLD, "https://www.boot.dev")
    print(node.__repr__())

main()
