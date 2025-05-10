import unittest

from textnode import TextNode, TextType

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


if __name__ == "__main__":
    unittest.main()
