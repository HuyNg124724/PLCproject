class Node:
    pass

class Number(Node):
    def __init__(self, value:int):
        self.value = value

class BinaryOp(Node):
    def __init__(self, operator:str, left:Node, right:Node):
        self.operator = operator
        self.left = left
        self.right = right
