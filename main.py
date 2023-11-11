import socket
import tkinter as tk
from socket import *
class Anekdot:
    # Инициализируем магазин шляп
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('Хотите анекдот?')
        self.win.geometry("1024x512+400+300")
        self.win.config(bg='#02b8ff')
        self.client = socket(AF_INET, SOCK_STREAM)
        self.client.connect(("127.0.0.1", 12345))
        self.shlyapu()
    # Шляпа, которую мы хотим купить
    def shlyapu(self):
        btn = tk.Button(self.win, background='#02b8ff', width=20, height=3,
                        text='Купил мужик шляпу...', font="Times 25",command=self.click)
        btn.place(relx=0.5, rely=0.5, anchor='center')
        btn.focus()
    # Покупка шляпы
    def click(self):
        self.client.send(bytes("\00", 'ascii'))
    def run(self):
        self.win.mainloop()
if __name__ == "__main__":
    app = Anekdot()
    app.run()