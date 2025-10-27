class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(node_1, node_2):
        if (node_1.text == node_2.text
            and node_1.text_type == node_2.text_type
            and node_1.url == node_2.url):
            return True
        return False
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


        