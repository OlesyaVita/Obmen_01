from tkinter import *
from tkinter import messagebox as mb
import requests
import json
from tkinter import ttk


def update_c_label(event):
    code = combobox.get()
    name = cur[code]
    c_label.config(text=name)


def exchange():
    code = combobox.get()

    if code:
        try:
            response = requests.get(f'https://open.er-api.com/v6/latest/{code}')
            response.raise_for_status()
            data = response.json()
            if code in data["rates"]:
                exchange_rate = data["rates"][code]
                c_name = cur[code]
                mb.showinfo("Курс обмена", f"Курс: {exchange_rate:.2f} {c_name} за 1 доллар.")
            else:
                mb.showerror("Ошибка", f"Валюта {code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}.")
    else:
        mb.showwarning("Внимание!", "Введите код валюты!")

cur = {
    "RUB": "Российский рубль",
    "USD": "Американский доллар",
    "EUR": "Евро",
    "JPY": "Японская йена",
    "GBP": "Британский фунт стерлингов",
    "AUD": "Австралийский доллар",
    "CAD": "Канадский доллар",
    "CHF": "Швейцарский франк",
    "CNY": "Китайский юань",
    "KZT": "Казахстанский тенге",
    "UZS": "Узбекский сум"
}


window = Tk()
window.title("Курсы обмена валют")
window.geometry("360x300")

Label(text="Выберите код валюты").pack(padx=10, pady=10)

combobox = ttk.Combobox(values=list(cur.keys()))
combobox.pack(padx=10, pady=10)
combobox.bind("<<ComboboxSelected>>", update_c_label)

c_label = ttk.Label()
c_label.pack(padx=10, pady=10)

Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)

window.mainloop()
