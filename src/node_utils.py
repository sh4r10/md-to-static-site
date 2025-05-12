import re
from textnode import TextNode


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
    images = re.findall(r"\!\[([\w\d\s\./@\:]+)\]\(([\w\d\s\./@\:]+)\)", text)
    return images


def extract_markdown_links(text):
    links = re.findall(r"(?<!\!)\[([\w\d\s\./@\:]+)\]\(([\w\d\s\./@\:]+)\)",
                       text)
    return links
