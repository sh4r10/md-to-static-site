import unittest

from html_conversion import markdown_to_html_node

class TestHTMLConversion(unittest.TestCase):
    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )


    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )


    def test_single_paragraph(self):
        md = """
    This is a node that has some **bold** and _italic_ text
        """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is a node that has some <b>bold</b> and <i>italic</i> text</p></div>"
        )


    def test_ordered_list(self):
        md = """
1. This 
2. is an 
3. ordered list
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
        "<div><ol><li>This</li><li>is an</li><li>ordered list</li></ol></div>"
        )


    def test_unordered_list(self):
        md = """
- This 
- is an 
- unordered list
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
        "<div><ul><li>This</li><li>is an</li><li>unordered list</li></ul></div>"
        )


    def test_blockquote(self):
        md = """
>This is a block quote 
>it has some **bold** text
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
        "<div><blockquote>This is a block quote it has some <b>bold</b> text</blockquote></div>"
        )

    def test_headings(self):
        md = """
# This is a heading

#### This is another heading

###### And one more

######### This is not a heading
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
        "<div><h1>This is a heading</h1><h4>This is another heading</h4><h6>And one more</h6><p>######### This is not a heading</p></div>"
        )





if __name__ == "__main__":
    unittest.main()


