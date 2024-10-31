from tkinter import *
from tkinter import messagebox as mb
import requests
import json
from tkinter import ttk

def exchange():
    code = combobox.get()

    if code:
        try:
            response = requests.get(f'https://open.er-api.com/v6/latest/{code}')
            response.raise_for_status()
            data = response.json()
            if code in data["rates"]:
                exchange_rate = data["rates"][code]
                mb.showinfo("Курс обмена", f"Курс: {exchange_rate:.2f} {code} за 1 доллар.")
            else:
                mb.showerror("Ошибка", f"Валюта {code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}.")
    else:
        mb.showwarning("Внимание!", "Введите код валюты!")


window = Tk()
window.title("Курсы обмена валют")
window.geometry("360x300")

Label(text="Выберите код валюты").pack(padx=10, pady=10)

cur =["EUR", "JPY", "GBP",  "AUD", "CAD", "CHF", "CNY", "RUB",  "KZT" ,  "UZS"]

combobox = ttk.Combobox(values=cur)
combobox.pack(padx=10, pady=10)


Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)

window.mainloop()
