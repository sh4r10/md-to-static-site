
from blocks import block_to_block_type, markdown_to_blocks


def main():
    md = """
# This is a heading

###### This is a heading

This is a not a ###  heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item

"""

    blocks = markdown_to_blocks(md)
    for block in blocks:
        print("-----------------")
        print(block)
        print(block_to_block_type(block))
        print("-----------------")


main()
