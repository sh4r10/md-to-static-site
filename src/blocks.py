import re
from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    blocks = map(lambda b: b.strip(), blocks)
    blocks = filter(lambda b: b != "", blocks)
    return list(blocks)


def block_to_block_type(block):
    if re.match(r"^#{1,6}\s.+", block):
        return BlockType.HEADING
    elif re.match(r"^`{3}.*`{3}$", block, re.DOTALL):
        return BlockType.CODE
    elif len(re.findall(r"^>.*", block, re.MULTILINE)) == len(block.splitlines()):
        return BlockType.QUOTE
    elif (len(re.findall(r"^-\s.*", block, re.MULTILINE)) ==
        len(block.splitlines())):
        return BlockType.UNORDERED_LIST
    elif re.match(r"^1\.\s.*", block):
        lines = block.splitlines()
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
