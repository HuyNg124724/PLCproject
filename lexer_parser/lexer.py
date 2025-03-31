from sly import Lexer

class CalcLexer(Lexer):
    tokens = { NUMBER, PLUS, TIMES }
    ignore = ' \t'

    PLUS = r'\+'
    TIMES = r'\*'

    @_(r'\d+')
    def NUMBER(self, token):
        token.value = int(token.value)
        return token

    def error(self, t):
        print(f"Illegal character '{t.value[0]}' at index {self.index}")
        self.index += 1

