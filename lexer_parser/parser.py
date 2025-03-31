from sly import Parser
from .lexer import CalcLexer
from ast.nodes import Number, BinaryOp

class CalcParser(Parser):
    tokens = CalcLexer.tokens

    @_('PLUS expr expr')
    def expr(self, p):
        return BinaryOp('+', p.expr0, p.expr1)

    @_('TIMES expr expr')
    def expr(self, p):
        return BinaryOp('*', p.expr0, p.expr1)

    @_('NUMBER')
    def expr(self, p):
        return Number(p.NUMBER)

    def error(self, p):
        print(f"Syntax error at token {p}")

