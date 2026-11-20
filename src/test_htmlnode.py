import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode( 
            props = {"href": "https://www.google.com"} 
        
        )

        self.assertEqual(
            node.props_to_html(), 
            ' href="https://www.google.com"'
            
        )

    def test_tag(self):
        node = HTMLNode(tag="a")
        self.assertEqual(node.tag, "a")

    def test_value(self):
        node = HTMLNode(value="Hello")
        self.assertEqual(node.value, "Hello")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual( parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>",)


