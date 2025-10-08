import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import xml.etree.ElementTree as ET


class PenguinTableApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Redactor BETA")
        self.root.geometry("800x500")

        # Кнопка открытия файла
        btn_open = tk.Button(root, text="Open XML", command=self.open_xml)
        btn_open.pack(pady=10)

        # Таблица
        self.tree = ttk.Treeview(root, show='headings')
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Полоса прокрутки
        scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def open_xml(self):
        path = filedialog.askopenfilename(
            title="Open XML",
            filetypes=[("XML файлы", "*.xml")]
        )
        if not path:
            return

        try:
            tree = ET.parse(path)
            root_elem = tree.getroot()

            # Определяем колонки по первому пингвину
            if len(root_elem) == 0:
                messagebox.showinfo("Инфо", "Файл пустой!")
                return

            first_penguin = root_elem[0]
            columns = [child.tag for child in first_penguin]

            # Настраиваем таблицу
            self.tree["columns"] = columns
            for col in columns:
                self.tree.heading(col, text=col.capitalize())
                self.tree.column(col, width=100, anchor='center')

            # Очищаем старые данные
            for item in self.tree.get_children():
                self.tree.delete(item)

            # Заполняем строки
            for penguin in root_elem:
                values = [child.text or "" for child in penguin]
                self.tree.insert("", "end", values=values)

        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось прочитать XML:\n{e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = PenguinTableApp(root)
    root.mainloop()
