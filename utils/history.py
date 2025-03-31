from ast.nodes import Number, BinaryOp

class History:
    def __init__(self):
        self.entries = []

    def add(self, expression, result):
        self.entries.append((expression, result))

def evaluate(node):
    if isinstance(node, Number):
        return node.value
    elif isinstance(node, BinaryOp):
        left = evaluate(node.left)
        right = evaluate(node.right)
        return left + right if node.operator == '+' else left * right

def to_infix(node):
    if isinstance(node, Number):
        return str(node.value)
    elif isinstance(node, BinaryOp):
        return f"({to_infix(node.left)} {node.operator} {to_infix(node.right)})"


