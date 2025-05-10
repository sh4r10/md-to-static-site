from htmlnode import HTMLNode
from textnode import TextNode, TextType


def main():
    test = HTMLNode("h1", "hello", None,
                    {"href":"http:suck.it", "target":"lol"})
    print(test)

main()
