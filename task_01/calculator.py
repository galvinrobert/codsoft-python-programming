import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")

        self.current_input = ""
        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        result_frame = tk.Frame(self.root)
        result_frame.pack(expand=True, fill="both")

        result_label = tk.Label(result_frame, textvariable=self.result_var, font=("Arial", 24), anchor="e", bg="white", relief="sunken")
        result_label.pack(expand=True, fill="both")

        button_frame = tk.Frame(self.root)
        button_frame.pack(expand=True, fill="both")

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        row = 0
        col = 0
        for button_text in buttons:
            button = tk.Button(button_frame, text=button_text, font=("Arial", 18), command=lambda text=button_text: self.on_button_click(text))
            button.grid(row=row, column=col, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1

        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)
            button_frame.grid_rowconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == "C":
            self.current_input = ""
            self.result_var.set(self.current_input)
        elif char == "=":
            try:
                result = str(eval(self.current_input))
                self.result_var.set(result)
                self.current_input = result
            except Exception as e:
                self.result_var.set("Error")
                self.current_input = ""
        else:
            self.current_input += str(char)
            self.result_var.set(self.current_input)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
