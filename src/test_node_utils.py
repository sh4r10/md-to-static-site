import unittest
from node_utils import extract_markdown_images, extract_markdown_links, split_nodes_delimeter, split_nodes_image, split_nodes_link, text_to_textnodes
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
        node = TextNode("This is **text** with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimeter([node], "**", TextType.BOLD)
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
        node_a = TextNode("This is **text** with a **bold** word", TextType.TEXT)
        node_b = TextNode("And another **bolded** text with a **bold** word",
                        TextType.TEXT)
        new_nodes = split_nodes_delimeter([node_a, node_b], "**", TextType.BOLD)
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


    def test_no_delimiter_split(self):
        node = TextNode("some text that doesn't need to be split",
                        TextType.TEXT)
        new_nodes = split_nodes_delimeter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [node])

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


class TestImageAndLinkNodeSplitting(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )


    def test_split_links(self):
        node = TextNode(
            "[This is text with a link](https://i.imgur.com) and another [second link](https://i.imgur.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link", TextType.LINK, "https://i.imgur.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com"
                ),
            ],
            new_nodes,
        )

    def test_no_image_or_link(self):
        node = TextNode("some text with no links or images", TextType.TEXT)
        image_splits = split_nodes_image([node])
        link_splits = split_nodes_link([node])
        self.assertEqual(image_splits, [node])
        self.assertEqual(link_splits, [node])


    def test_multiple_images(self):
        node_a = TextNode("some text with no links or images", TextType.TEXT)
        node_b = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node_a, node_b])
        self.assertListEqual(
            [
                TextNode("some text with no links or images", TextType.TEXT),
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )


    def test_multiples_links(self):
        node_a = TextNode("some text with no links or images", TextType.TEXT)
        node_b = TextNode(
            "[This is text with a link](https://i.imgur.com) and another [second link](https://i.imgur.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node_a, node_b])
        self.assertListEqual(
            [
                TextNode("some text with no links or images", TextType.TEXT),
                TextNode("This is text with a link", TextType.LINK, "https://i.imgur.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com"
                ),
            ],
            new_nodes,
        )

    def test_non_text_images(self):
        node_a = TextNode("some text with no links or images", TextType.TEXT)
        node_b = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        node_c = TextNode("`code with an ![image](image.com)`", TextType.CODE)
        new_nodes = split_nodes_image([node_a, node_b, node_c])
        self.assertListEqual(
            [
                TextNode("some text with no links or images", TextType.TEXT),
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode("`code with an ![image](image.com)`", TextType.CODE),
            ],
            new_nodes,
        )


    def test_non_text_links(self):
        node_a = TextNode("some text with no links or images", TextType.TEXT)
        node_b = TextNode(
            "[This is text with a link](https://i.imgur.com) and another [second link](https://i.imgur.com)",
            TextType.TEXT,
        )
        node_c = TextNode("`code with a [link](shariq.xyz)`", TextType.CODE)
        new_nodes = split_nodes_link([node_a, node_b, node_c])
        self.assertListEqual(
            [
                TextNode("some text with no links or images", TextType.TEXT),
                TextNode("This is text with a link", TextType.LINK, "https://i.imgur.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com"
                ),
                TextNode("`code with a [link](shariq.xyz)`", TextType.CODE),
            ],
            new_nodes,
        )


class TestTextToTextNodesConverstion(unittest.TestCase):
    def test_all_types_conversion(self):
        text = "This is **text** with an _italic_ word and a `code block` and"\
            " an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a"\
            " [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        expected =  [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(nodes, expected)


    # TODO: Write More tests

if __name__ == "__main__":
    unittest.main()
