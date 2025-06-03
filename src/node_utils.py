import re
from textnode import TextNode, TextType


def split_nodes_delimeter(old_nodes, delimeter, text_type):
    new_nodes = []
    for node in old_nodes:
        split_nodes_text = node.text.split(delimeter)
        i = -1
        for split_node_text in split_nodes_text:
            i += 1
            if not split_node_text:
                continue

            if i % 2 == 0:
                new_nodes.append(TextNode(split_node_text, node.text_type))
            else:
                new_nodes.append(TextNode(split_node_text, text_type))
    return new_nodes


def extract_markdown_images(text):
    images = re.findall(r"\!\[([^\]]*)\]\(([^\)]*)\)", text)
    return images


def extract_markdown_links(text):
    links = re.findall(r"(?<!\!)\[([^\]]*)\]\(([^\)]*)\)", text)
    return links


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        extracted = extract_markdown_images(node.text)
        if len(extracted) == 0:
            new_nodes.append(node)
            continue

        remaining_text = node.text
        for alt, url in extracted:
            split = remaining_text.split(f"![{alt}]({url})", maxsplit=1)
            if len(split) != 2:
                raise ValueError("Invalid image")
            if split[0] != "":
                new_nodes.append(TextNode(split[0], TextType.TEXT))

            new_nodes.append(TextNode(alt, TextType.IMAGE, url))
            remaining_text = split[1]

        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        extracted = extract_markdown_links(node.text)
        if len(extracted) == 0:
            new_nodes.append(node)
            continue

        remaining_text = node.text
        for text, url in extracted:
            split = remaining_text.split(f"[{text}]({url})", maxsplit=1)
            if len(split) != 2:
                raise ValueError("Invalid link")
            if split[0] != "":
                new_nodes.append(TextNode(split[0], TextType.TEXT))
            new_nodes.append(TextNode(text, TextType.LINK, url))
            remaining_text = split[1]

        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimeter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimeter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimeter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes


