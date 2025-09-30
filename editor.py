import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Текстовый редактор")

text_area = tk.Text(root)
text_area.pack(fill=tk.BOTH, expand=1)

root.mainloop()