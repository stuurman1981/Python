import tkinter as tk

class Calculator(tk.Frame):
    CANVAS_WIDTH = 600
    CANVAS_HEIGHT = 600
    buttons_list = ['C', 'CE', '<--', '/', 1, 2, 3, '*', 4, 5, 6, '-', 7, 8, 9,'+','+/-', 0, '.', '=']

    def __init__(self):
        super().__init__()
        self.pack()
        self._create_main_canvas()
        self._create_log_frame()
        self._create_entry()
        self._create_button_area()
        self.calc_act = False

    def _create_main_canvas(self):
        self.main_canvas = tk.Canvas(self,
                                     width=self.CANVAS_WIDTH,
                                     height=self.CANVAS_HEIGHT)
        self.main_canvas.pack()
        self.calculator_frame = tk.Frame(self.main_canvas,
                                   bg='#e9e9e9',
                                   bd=1)
        self.calculator_frame.place(relx=0.5,
                              relwidth=1, relheight=1,
                              anchor='n')

    def _create_log_frame(self):
        self.log_frame = tk.Frame(self.calculator_frame,
                                  bg='#e9e9e9',
                                  bd=1)
        self.log_frame.place(relx=1, rely=0.15, relwidth=1, relheight=0.2, anchor='e')
        self.log_frame.pack()
        self._create_log()

    def _create_log(self, text=None):
        self.label_row = tk.Label(self.log_frame,
                                  bg='#e9e9e9',
                                  justify='right',
                                  width=58,
                                  text=text,
                                  font=('Times', 14))
        self.label_row.place(relx=1, rely=0.15, relwidth=1, relheight=0.2, anchor='n')
        self.label_row.pack()

    def _create_entry(self):
        self.entry_row = tk.Entry(self.calculator_frame,
                                  bg = '#FFF',
                                  justify='right',
                                  width=42,
                                  font=('Times', 20))
        self.entry_row.place(relx=1, rely=0.3, relwidth=1, relheight=0.2, anchor='n')
        self.entry_row.pack()

    def _create_button_area(self):
        self.button_area = tk.Frame(self.calculator_frame, bg = '#d3d3d3')
        self.button_area.place(relx=0.5, rely=0.15, relwidth=1, relheight=1, anchor='n')
        i = 0
        for r in range(5):
            for c in range(4):
                new_button = tk.Button(self.button_area,
                                       width=2,
                                       height=1,
                                       font=('Times', 20),
                                       text=self.buttons_list[i],
                                       command=lambda x=self.buttons_list[i]: self._button_response(x))\
                    .grid(row=r, column=c, ipadx=40, ipady=20, padx=15, pady=4)
                i += 1

    def _clear_entry(self):
        self.entry_row.delete(0, 'end')

    def _clear_all(self):
        self.label_row.destroy()
        self._clear_entry()

    def _calculate(self):
        user_entry = self.entry_row.get()
        if user_entry:
            try:
                self.label_row.destroy()
                result = eval(user_entry)
                self._create_log(f'{user_entry} =')
                self.entry_row.delete(0, 'end')
                self.entry_row.insert(0, result)
            except SyntaxError:
                self._create_log("Wrong Syntax")
            except NameError:
                self._create_log("Use numbers only")

    def _posit_negat(self):
        try:
            user_entry = int(self.entry_row.get()) * (-1)
            self.entry_row.delete(0, 'end')
            self.entry_row.insert(0, user_entry)
        except ValueError:
            pass

    def _button_response(self, symbol):
        if symbol == 'C':
            self._clear_entry()
        elif symbol == 'CE':
            self._clear_all()
        elif symbol == '<--':
            user_entry = self.entry_row.get()
            self.entry_row.delete(0,'end')
            self.entry_row.insert(0, user_entry[0: len(user_entry) - 1])
            self.calc_act = False
        elif symbol == '=':
            self._calculate()
            self.calc_act = True
        elif symbol == '+/-':
            self._posit_negat()
        else:
            if self.calc_act:
                self._clear_entry()
                self.entry_row.insert(tk.INSERT, symbol)
                self.calc_act = False
            else:
                self.entry_row.insert(tk.INSERT, symbol)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Calculator")
    root.resizable(width=False, height=False)
    app = Calculator()
    app.mainloop()