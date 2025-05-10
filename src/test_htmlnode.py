import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr_props(self):
        node = HTMLNode("a", "im a link", None, 
                        {"href": "https://google.com", "target":"_blank"})
        self.assertEqual(' href="https://google.com" target="_blank"',
                         node.props_to_html()) 


    def test_props_equal(self):
        node = HTMLNode("a", "im a link", None, 
                        {"href": "https://google.com", "target":"_blank"})
        node2 = HTMLNode("a", "im a link", None, 
                        {"href": "https://google.com", "target":"_blank"})
        self.assertEqual(node.props_to_html(), node2.props_to_html())


    def test_props_not_equal(self):
        node = HTMLNode("a", "im a link", None, 
                        {"href": "https://shariq.xyz", "target":"_self"})
        node2 = HTMLNode("a", "im a link", None, 
                        {"href": "https://google.com", "target":"_blank"})
        self.assertNotEqual(node.props_to_html(), node2.props_to_html())


if __name__ == "__main__":
    unittest.main()
