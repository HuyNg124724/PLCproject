from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

from lexer_parser.lexer import CalcLexer
from lexer_parser.parser import CalcParser
from utils.history import evaluate, to_infix, History

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./ui/calculator.ui", self)

        self.history = History()
        self.lexer = CalcLexer()
        self.parser = CalcParser()

        self.button_equal.clicked.connect(self.calculate)

    def calculate(self):
        prefix_expression = self.input_text.text()
        try:
            ast = self.parser.parse(self.lexer.tokenize(prefix_expression))
            numeric_result = evaluate(ast)
            infix_result = to_infix(ast)

            self.output_lcd.display(numeric_result)
            self.statusbar.showMessage(f"Infix: {infix_result}")

            self.history.add(prefix_expression, numeric_result)
        except Exception as e:
            self.statusbar.showMessage(f"Error: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())

