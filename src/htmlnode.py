from functools import reduce

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        raise NotImplementedError


    def props_to_html(self):
        return reduce(lambda acc, p: f"{acc} {p[0]}=\"{p[1]}\"",
                      self.props.items(), "")


    def __repr__(self):
       return f"{self.tag} {self.props_to_html()}" 

