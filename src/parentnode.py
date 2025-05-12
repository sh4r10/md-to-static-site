from functools import reduce
from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)


    def to_html(self):
        if not self.tag or not self.children:
            raise ValueError
        children = reduce(lambda acc, a: acc+a.to_html(), self.children, "")
        return f"<{self.tag}{self.props_to_html()}>{children}</{self.tag}>"
