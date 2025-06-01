from blocks import block_to_block_type, markdown_to_blocks
from html_conversion import markdown_to_html_node
from leafnode import LeafNode
from node_utils import text_to_textnodes
from parentnode import ParentNode
from textnode import text_node_to_html_node

def main():
    md = """
# This is a heading

hi this is some `brode` sike

```
this is some shit
```

"""
    print(markdown_to_html_node(md).to_html())


main()
