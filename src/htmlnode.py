
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value 
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        prop_items = self.props.items()
        prop_str = ""

        for tag, value in prop_items:
            prop_str += f" {tag}={value}" 
        return prop_str
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, props)
        self.props = props

    def to_html(self):
        if not self.value:
            raise ValueError
        elif not self.tag:
            return self.value
        else:
            if not self.props:
                return f"<{self.tag}>{self.value}</{self.tag}>"
            else:
                return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
            


# node = LeafNode(tag="a", value="This is some text", props={"href": "https://www.google.com"})

# print(node.to_html())
                




















        