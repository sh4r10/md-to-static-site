from enum import Enum

class TextType(Enum):
    NORMAL_TEXT = "normal text"
    BOLD_TEXT = "bold text"
    ITALIC_TEXT = "italic text"
    CODE_TEXT = "code text"
    LINK = "link"
    IMAGE = "image"



class TextNode:
    def __init__(self, text, text_type, url=None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url


    def __eq__(self, target):
        text_same = target.text == self.text
        type_same = target.text_type == self.text_type
        url_same = target.url == self.url
        return text_same and type_same and url_same


    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
