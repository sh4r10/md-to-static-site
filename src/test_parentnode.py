import unittest

from leafnode import LeafNode
from parentnode import ParentNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_grandchildren_parent_props(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node], {"class": "text-xl"})
        self.assertEqual(
            parent_node.to_html(),
            "<div class=\"text-xl\"><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_grandchildren_child_props(self):
        grandchild_node = LeafNode("b", "grandchild", {"class": "text-xl"})
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b class=\"text-xl\">grandchild</b></span></div>",
        )

    def test_to_html_with_no_children(self):
        with self.assertRaises(ValueError):
            parent_node = ParentNode("div",[]) 
            parent_node.to_html()


    def test_to_html_with_no_tag(self):
        with self.assertRaises(ValueError):
            child_node = LeafNode("", "hello")
            parent_node = ParentNode("",[child_node]) 
            parent_node.to_html()


if __name__ == "__main__":
    unittest.main()
