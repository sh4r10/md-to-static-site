import unittest
from node_utils import extract_markdown_images, extract_markdown_links, split_nodes_delimeter
from textnode import TextNode, TextType


class TestTextNodeDelimiterSplit(unittest.TestCase):
    def test_code_split(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimeter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes,
                              [
                                TextNode("This is text with a ", TextType.TEXT),
                                TextNode("code block", TextType.CODE),
                                TextNode(" word", TextType.TEXT)
                              ])


    def test_bold_split(self):
        node = TextNode("This is *text* with a *bold* word", TextType.TEXT)
        new_nodes = split_nodes_delimeter([node], "*", TextType.BOLD)
        self.assertEqual(new_nodes,
                              [
                                TextNode("This is ", TextType.TEXT),
                                TextNode("text", TextType.BOLD),
                                TextNode(" with a ", TextType.TEXT),
                                TextNode("bold", TextType.BOLD),
                                TextNode(" word", TextType.TEXT)
                              ])


    def test_italic_split(self):
        node1 = TextNode("_This_ is _text_ with some _italic_ words",
                        TextType.TEXT)
        new_nodes = split_nodes_delimeter([node1], "_", TextType.ITALIC)
        self.assertEqual(new_nodes,
                         [
                            TextNode("This", TextType.ITALIC),
                            TextNode(" is ", TextType.TEXT),
                            TextNode("text", TextType.ITALIC),
                            TextNode(" with some ", TextType.TEXT),
                            TextNode("italic", TextType.ITALIC),
                            TextNode(" words", TextType.TEXT)
                         ])


    def test_multiple_bold_split(self):
        node_a = TextNode("This is *text* with a *bold* word", TextType.TEXT)
        node_b = TextNode("And another *bolded* text with a *bold* word",
                        TextType.TEXT)
        new_nodes = split_nodes_delimeter([node_a, node_b], "*", TextType.BOLD)
        self.assertEqual(new_nodes,
                         [
                            TextNode("This is ", TextType.TEXT),
                            TextNode("text", TextType.BOLD),
                            TextNode(" with a ", TextType.TEXT),
                            TextNode("bold", TextType.BOLD),
                            TextNode(" word", TextType.TEXT),
                            TextNode("And another ", TextType.TEXT),
                            TextNode("bolded", TextType.BOLD),
                            TextNode(" text with a ", TextType.TEXT),
                            TextNode("bold", TextType.BOLD),
                            TextNode(" word", TextType.TEXT)
                         ])

class TestImageAndLinkExtraction(unittest.TestCase):
    def test_image_extraction(self):
        matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")],
                             matches)

    def test_double_image_extraction(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        actual_result = extract_markdown_images(text)
        expected_result = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(actual_result, expected_result)


    def test_link_extraction(self):
        matches = extract_markdown_links(
        "This is text with a link [shariq.xyz](https://shariq.xyz)"
        )
        self.assertListEqual([("shariq.xyz", "https://shariq.xyz")], matches)


    def test_link_extraction_with_image(self):
        matches = extract_markdown_links(
            """
                This is text with a link [shariq.xyz](https://shariq.xyz),
                don't match the image ![image](src/main.png)"
            """
        )
        self.assertListEqual([("shariq.xyz", "https://shariq.xyz")],
                             matches)

    def test_image_extraction_with_link(self):
        matches = extract_markdown_images(
            """
                This is text with a link [shariq.xyz](https://shariq.xyz),
                only match the image ![image](src/main.png)"
            """
        )
        self.assertListEqual([("image", "src/main.png")],
                             matches)



if __name__ == "__main__":
    unittest.main()
