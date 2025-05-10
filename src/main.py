from textnode import TextNode, TextType


def main():
    test = TextNode("this is some anchor text", TextType.LINK, "https://shariq.xyz")
    print(test)

main()
