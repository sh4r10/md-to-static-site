import unittest

from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)


    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is another text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)


    def test_url_eq(self):
        node = TextNode("This is a link", TextType.LINK, "https://shariq.xyz")
        node2 = TextNode("This is a link", TextType.LINK, "https://shariq.xyz")
        self.assertEqual(node, node2)


    def test_url_not_eq(self):
        node = TextNode("This is a link", TextType.LINK, "https://shariq.xyz")
        node2 = TextNode("This is a different link", TextType.LINK,
                         "https://shariq.xyz")
        self.assertNotEqual(node, node2)


    def test_url_not_eq_code(self):
        node = TextNode("This is some code", TextType.CODE)
        node2 = TextNode("This is a different link", TextType.LINK,
                         "https://shariq.xyz")
        self.assertNotEqual(node, node2)


    def test_repr(self):
        node2 = TextNode("This is a link", TextType.LINK, "https://shariq.xyz")
        self.assertNotEqual("TextNode(This is a link, link, https://shariq.xyz"
                            , repr(node2))


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.to_html(), "This is a text node")


    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")
        self.assertEqual(html_node.to_html(), "<b>This is a bold node</b>")


    def test_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")
        self.assertEqual(html_node.to_html(), "<i>This is an italic node</i>")


    def test_code(self):
        node = TextNode("This is some code", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is some code")
        self.assertEqual(html_node.to_html(), "<code>This is some code</code>")


    def test_link(self):
        node = TextNode("This is a link", TextType.LINK, "https://shariq.xyz")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link")
        self.assertEqual(html_node.to_html(),
                         "<a href=\"https://shariq.xyz\">This is a link</a>")


    def test_invalid_node(self):
        node = TextNode("This is a link", "test", "https://shariq.xyz")
        with self.assertRaises(Exception):
            text_node_to_html_node(node)


if __name__ == "__main__":
    unittest.main()
