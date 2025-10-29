import unittest
from src.markdown_to_html import markdown_to_html_node

class TestMarkdownToHTML(unittest.TestCase):
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


    def test_heading(self):
        md = """
##### This is a heading

This is a **bold** paragraph
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        # print(html)
        self.assertEqual(
            html,
            "<div><h5>This is a heading</h5><p>This is a <b>bold</b> paragraph</p></div>"
        )

    def test_blockquote(self):
        md = """
>This is the first line
>Second line
>Third line"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        # print(html)
        self.assertEqual(
            html,
            "<div><blockquote>This is the first line \nSecond line \nThird line</blockquote></div>"
        )

    def test_unordered_list(self):
        md = """
- This is the first line
- Second line
- Third line"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is the first line</li><li>Second line</li><li>Third line</li></ul></div>"
        )

    def test_unordered_list_children(self):
        md = """
- This is the **first** line
- Second line
- Third line"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is the <b>first</b> line</li><li>Second line</li><li>Third line</li></ul></div>"
        )

    def test_ordered_list(self):
        md = """
1. This is the first line
2. Second line
3. Third line"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is the first line</li><li>Second line</li><li>Third line</li></ol></div>"
        )

    def test_ordered_list__children(self):
        md = """
1. This is the **first** line
2. Second line
3. Third line"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is the <b>first</b> line</li><li>Second line</li><li>Third line</li></ol></div>"
        )

    def test_heading_ordered_list(self):
        md = """## Steps to Create a Markdown File

1. Open your favorite text editor.  
2. Write your content using Markdown syntax.  
3. Save it with the `.md` extension.  
4. Preview or convert it to HTML using a Markdown viewer."""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h2>Steps to Create a Markdown File</h2><ol><li>Open your favorite text editor.</li><li>Write your content using Markdown syntax.</li><li>Save it with the <code>.md</code> extension.</li><li>Preview or convert it to HTML using a Markdown viewer.</li></ol></div>"
        )