import tkinter as tk



class ClickCounterUp:
    def __init__(self, master):
        self.master = master
        self.master.title('Click Counter')
        self.count = 0
        self.label = tk.Label(master, text=f'Count: {self.count}')
        self.label.pack(pady=10)
        self.but = tk.Button(master, text='Click!', command=self.increment).pack(pady=20)
        self.resbut = tk.Button(master, text='Reset', command=self.reset).pack(pady=20)
        self.master.geometry('500x500')
    def increment(self):
        self.count +=1
        self.label.config(text=f'Count: {self.count}')
    def reset(self):
        self.count = 0
        self.label.config(text=f'Count: {self.count}')


        

if __name__ == '__main__':
    root = tk.Tk()
    app = ClickCounterUp(root)
    root.mainloop()