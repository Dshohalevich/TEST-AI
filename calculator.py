import tkinter as tk
import math

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("300x400")
        self.resizable(False, False)

        self.expression = ""

        self.display = tk.Entry(self, font=("Arial", 20), borderwidth=2, relief="ridge", justify="right")
        self.display.pack(fill=tk.BOTH, ipadx=8, ipady=15, padx=10, pady=10)

        self._create_buttons()

    def _create_buttons(self):
        buttons = [
            ('7', lambda: self._append('7')), ('8', lambda: self._append('8')), ('9', lambda: self._append('9')), ('/', lambda: self._append('/')),
            ('4', lambda: self._append('4')), ('5', lambda: self._append('5')), ('6', lambda: self._append('6')), ('*', lambda: self._append('*')),
            ('1', lambda: self._append('1')), ('2', lambda: self._append('2')), ('3', lambda: self._append('3')), ('-', lambda: self._append('-')),
            ('0', lambda: self._append('0')), ('.', lambda: self._append('.')), ('=', self._calculate), ('+', lambda: self._append('+')),
            ('log', lambda: self._append('log(')), ('sqrt', lambda: self._append('sqrt(')), ('C', self._clear)
        ]

        rows = 5
        cols = 4
        frame = tk.Frame(self)
        frame.pack(expand=True, fill='both')

        for i, (text, cmd) in enumerate(buttons):
            row, col = divmod(i, cols)
            b = tk.Button(frame, text=text, command=cmd, font=("Arial", 14))
            b.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

        for i in range(rows):
            frame.rowconfigure(i, weight=1)
        for i in range(cols):
            frame.columnconfigure(i, weight=1)

    def _append(self, char):
        self.expression += char
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

    def _clear(self):
        self.expression = ""
        self.display.delete(0, tk.END)

    def _calculate(self):
        try:
            expr = self.expression
            expr = expr.replace('log', 'math.log')
            expr = expr.replace('sqrt', 'math.sqrt')
            result = eval(expr)
            self.expression = str(result)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)
        except Exception:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")
            self.expression = ""

if __name__ == '__main__':
    app = Calculator()
    app.mainloop()
