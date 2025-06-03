import re
from blocks import BlockType, block_to_block_type, markdown_to_blocks
from node_utils import text_to_textnodes
from parentnode import ParentNode
from textnode import TextNode, TextType, text_node_to_html_node


def parse_headings(text):
    split = text.split()
    content = " ".join(split[1::])
    num_h = len(split[0])
    nodes = text_to_textnodes(content)
    children = map(text_node_to_html_node, nodes)
    return ParentNode(f"h{num_h}", list(children))


def parse_quote(text):
    lines = text.splitlines()
    nodes = []

    for line in lines:
        nodes.extend(text_to_textnodes(line[1::]))

    children = list(map(text_node_to_html_node, nodes))
    return ParentNode("blockquote", list(children))


def parse_list(text, type):
    children = []
    lines = text.splitlines()
    for line in lines:
        nodes = text_to_textnodes(" ".join(line.split()[1::]))

        conv_nodes = list(map(text_node_to_html_node, nodes))
        children.append(ParentNode("li", conv_nodes)) 

    if type == BlockType.ORDERED_LIST:
        return ParentNode("ol", children)
    else:
        return ParentNode("ul", children)


def parse_code_block(text):
    code = re.match(r"^`{3}\n(.*)`{3}$", text, re.DOTALL)
    node = TextNode(code.group(1), TextType.CODE)
    child = text_node_to_html_node(node)
    return ParentNode("pre", [child])


def parse_paragraph(text):
    split_and_strip = map(lambda l: l.strip(), text.splitlines())
    nodes = text_to_textnodes(" ".join(split_and_strip))
    children = list(map(text_node_to_html_node, nodes))
    return ParentNode("p", children)


def markdown_to_html_node(markdown):
    html_nodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.HEADING:
                html_nodes.append(parse_headings(block))
            case BlockType.QUOTE:
                html_nodes.append(parse_quote(block))
            case BlockType.UNORDERED_LIST:
                html_nodes.append(parse_list(block, block_type))
            case BlockType.ORDERED_LIST:
                html_nodes.append(parse_list(block, block_type))
            case BlockType.PARAGRAPH:
                html_nodes.append(parse_paragraph(block))
            case BlockType.CODE:
                html_nodes.append(parse_code_block(block))
            case _:
                raise ValueError("Invalid block type")
    
    if not html_nodes:
        raise Exception("Something went wrong with parsing the document")

    return ParentNode("div", html_nodes)


def extract_title(md):
    title = ""
    for line in md.splitlines():
        if line.startswith("# "):
            title = line.replace("# ", "").strip()
            break
    return title
