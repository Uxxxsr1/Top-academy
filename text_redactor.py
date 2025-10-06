import tkinter as tk
from tkinter import filedialog, messagebox

# Функция для открытия файла
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            text.delete(1.0, tk.END)  # Очищаем текстовое поле
            text.insert(tk.END, file.read())  # Вставляем текст из файла

# Функция для сохранения файла
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension="")
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get(1.0, tk.END))  # Записываем текст в файл

# Функция для выхода
def exit_app():
    if messagebox.askokcancel("Выход", "Вы уверены, что хотите выйти?"):
        root.destroy()

# Создаем основное окно
root = tk.Tk()
root.title("Текстовый редактор")

# Создаем текстовое поле
text = tk.Text(root, wrap="word")
text.pack(expand=True, fill="both")

# Создаем меню
menu_bar = tk.Menu(root)

# Меню "Файл"
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=exit_app)
menu_bar.add_cascade(label="Файл", menu=file_menu)

# Меню "Правка"
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Копировать", command=lambda: text.event_generate("<<Copy>>"))
edit_menu.add_command(label="Вставить", command=lambda: text.event_generate("<<Paste>>"))
edit_menu.add_command(label="Вырезать", command=lambda: text.event_generate("<<Cut>>"))
menu_bar.add_cascade(label="Правка", menu=edit_menu)

# Добавляем меню в окно
root.config(menu=menu_bar)

# Запуск основного цикла
root.mainloop()
