from blocks import block_to_block_type, markdown_to_blocks
from html_conversion import markdown_to_html_nodes
from leafnode import LeafNode
from node_utils import text_to_textnodes
from parentnode import ParentNode
from textnode import text_node_to_html_node

def main():
    md = """
# This is a heading

###### This is a heading

#### This is an _italic_ heading

This is a not a ###  heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

>This is a single block quote

>This is a multiline 
>block quote, tf 
>even has **bold** text

- This is the first list item in a list block
- This is a **list** item
- This is another list item

1. this is ordered
2. list 
3. wtf

Lorem ipsum dolor **sit** amet, [consectetur adipiscing elit](link.tf), sed do
![eiusmod](image.tf) tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation


"""
    print(markdown_to_html_nodes(md).to_html())


main()
