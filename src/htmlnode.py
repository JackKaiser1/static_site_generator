
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

    def to_html(self):
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

            


# grandchild_node = LeafNode("b", "grandchild")
# child_node = ParentNode("span", [grandchild_node])
# parent_node = ParentNode("div", [child_node])
# print(parent_node.to_html())
                
# child_node = LeafNode(tag="span", value="child", props={"color": "red"})
# parent_node = ParentNode(tag="div", children=[child_node], props={"href": "www.boot.dev"})

# print(parent_node.to_html())



















        