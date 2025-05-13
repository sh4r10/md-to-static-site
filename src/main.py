from node_utils import text_to_textnodes

def main():
    text = """This is **text** with an _italic_ word and a `code block` and an
    ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a
    [link](https://boot.dev)"""
    nodes = text_to_textnodes(text)
    print(nodes)


main()
