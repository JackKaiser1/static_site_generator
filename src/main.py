# print("hello world")

from .textnode import TextNode, TextType

def main():
    node = TextNode("hello world", TextType.BOLD, "https://www.boot.dev")
    print(node.__repr__())

main()
