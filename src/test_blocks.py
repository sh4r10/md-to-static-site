import unittest

from blocks import BlockType, block_to_block_type, markdown_to_blocks

class TestBlockSplitting(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )


    def test_markdown_empty_lines_to_blocks(self):
        md = """
This is **bolded** paragraph


    
This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line



- This is a list
- with items


                        
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )


class TestBlockToBlockType(unittest.TestCase):
    def test_headings_to_block_type(self):
        h1 = "# This is a heading"
        h6 = "###### This is a heading"
        p = "This is a not a ###  heading"
        self.assertEqual(BlockType.HEADING, block_to_block_type(h1))
        self.assertEqual(BlockType.HEADING, block_to_block_type(h6))
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(p))


    def test_code_to_block_type(self):
        code = """
        ```
            hello world
        ```
            """
        self.assertEqual(BlockType.CODE, block_to_block_type(code.strip()))


    def test_quote_to_block_type(self):
        valid_quote = """
>valid quote
>part 2
            """
        invalid_quote = """
        >valid quote
        part 2
            """
        self.assertEqual(BlockType.QUOTE,
                         block_to_block_type(valid_quote.strip()))
        self.assertNotEqual(BlockType.QUOTE,
                         block_to_block_type(invalid_quote.strip()))


    def test_ul_to_block_type(self):
        valid_list = """
- item 1
- item 2
- item3
            """
        invalid_list = """
- item 1
-item 2
- item3
            """

        self.assertEqual(BlockType.UNORDERED_LIST,
                         block_to_block_type(valid_list.strip()))
        self.assertNotEqual(BlockType.UNORDERED_LIST,
                         block_to_block_type(invalid_list.strip()))


    def test_ol_to_block_type(self):
        valid_list = """
1. item 1
2. item 2
3. item3
            """
        invalid_list = """
1. item 1
3. item 2
2. item3
            """

        self.assertEqual(BlockType.ORDERED_LIST,
                         block_to_block_type(valid_list.strip()))
        self.assertNotEqual(BlockType.ORDERED_LIST,
                         block_to_block_type(invalid_list.strip()))




if __name__ == "__main__":
    unittest.main()

