import tkinter as tk
import random


class ClickCounterUp:
    def __init__(self, master):
        self.master = master
        self.master.title('Click Counter')
        self.count = 0
        self.label = tk.Label(master, text=f'Count: {self.count}')
        self.label.pack(pady=10)
        self.but = tk.Button(master, text='Click!', command=self.increment)
        self.but.pack(pady=10)
        self.resbut = tk.Button(master,text='Reset', command=self.reset)
        self.resbut.pack(pady=5, padx=200)
        self.extbut = tk.Button(master, text='Exit', command=self.exit)
        self.extbut.pack(pady=10)
        self.minbut = tk.Button(master, text='Decrease', command=self.decrease)
        self.minbut.pack(pady=10)
        self.uploadbtn = tk.Button(master, text='Upload', command=self.upload)
        self.uploadbtn.pack()
        self.save = tk.Button(master, text='Save', command=self.save).pack()
        self.strcount = str(self.count)
        self.master.geometry('500x500')
    def increment(self):
        self.count +=1
        self.label.config(text=f'Count: {self.count}')
    def reset(self):
        self.count = 0
        self.label.config(text=f'Count: {self.count}')
    def exit(self):
        root.destroy()
    def decrease(self):
        if self.count == 0:
            self.label.config(text=f'error')
        else:
            self.count -=1
        self.label.config(text=f'Count: {self.count}')
    def upload(self):
        with open('test.txt','r',encoding='utf-8') as f:
            content = f.read()
            self.count = int(content)
            self.label.config(text=f'Count: {self.count}')          
    def save(self):
        with open('test.txt', 'w', encoding='utf-8') as f:
            f.write(str(self.count))
class ClickCouterUp1(ClickCounterUp):
    def __init__(self, master):
        super().__init__(master)
        self.colors = ['red', 'blue', 'green', 'orange', 'yellow', 'purple']
    def increment(self):
        super().increment()
        new_color = random.choice(self.colors)
        self.but.config(bg=new_color)







class ClickCOuterUp2(ClickCouterUp1):
    def stepper(self):
        step = self.inp.get()
        print(step)
        print(self.count)
        self.count += int(step)
    def __init__(self, master):
        super().__init__(master)
        self.inp = tk.Entry(master, width=10)
        self.inp.pack()
        #self.btn = tk.Button(master, command=self.stepper)
        #self.inpbtn.pack()
        self.but.config(command=self.stepper)
        self.label.config(text=f'Count: {self.count}')

















if __name__ == '__main__':
    root = tk.Tk()  
    app = ClickCOuterUp2(root)
    root.mainloop()
