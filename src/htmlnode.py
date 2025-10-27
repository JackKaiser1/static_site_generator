
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value 
        self.children = children
        self.props = props

    def to_html(self) -> Exception:
        raise NotImplementedError

    def props_to_html(self) -> str:
        prop_items = self.props.items()
        prop_str = ""

        for tag, value in prop_items:
            prop_str += f" {tag}={value}" 
        return prop_str
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, props)
        self.props = props

    def to_html(self) -> str:
        if not self.value:
            raise ValueError("LeafNode must have a value")
        elif not self.tag:
            return self.value
        else:
            if not self.props:
                return f"<{self.tag}>{self.value}</{self.tag}>"
            else:
                return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
            

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, children, props)
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self) -> str:
        inner_str = ""
        if not self.tag:
            raise ValueError("ParentNode must have a tag")
        elif not self.children:
            raise ValueError("ParentNode must have children")
        else:
            if not self.props:
                for child in self.children:
                    inner_str += child.to_html() 
                return f"<{self.tag}>{inner_str}</{self.tag}>"
            else:
                for child in self.children:
                    inner_str += child.to_html() 
                return f"<{self.tag}{self.props_to_html()}>{inner_str}</{self.tag}>"

            

        