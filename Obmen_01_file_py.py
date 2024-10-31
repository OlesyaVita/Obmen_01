from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests


def update_t_label(event):
    # Получаем полное название валюты из словаря и обновляем метку
    code = t_combobox.get()
    name = cur[code]
    t_label.config(text=name)


def update_b_label(event):
    # Получаем полное название валюты из словаря и обновляем метку
    code = b_combobox.get()
    name = cur[code]
    b_label.config(text=name)


def update_s_label(event):
    # Получаем полное название валюты из словаря и обновляем метку
    code = s_combobox.get()
    name = cur[code]
    s_label.config(text=name)


def exchange():
    b_code = b_combobox.get()
    s_code = s_combobox.get()
    t_code = t_combobox.get()

    if t_code and b_code and s_code:
        try:
            b_response = requests.get(f'https://open.er-api.com/v6/latest/{b_code}')
            b_response.raise_for_status()
            s_response = requests.get(f'https://open.er-api.com/v6/latest/{s_code}')
            s_response.raise_for_status()

            b_data = b_response.json()
            s_data = s_response.json()

            if t_code in s_data['rates'] and t_code in b_data['rates']:
                b_exchange_rate = b_data['rates'][t_code]
                s_exchange_rate = s_data['rates'][t_code]

                b_name = cur[b_code]
                t_name = cur[t_code]
                s_name = cur[s_code]
                mb.showinfo("Курс обмена", f"Курс {b_exchange_rate:.2f} {t_name} за 1 {b_name} "
                                           f"и {s_exchange_rate:.2f} {t_name} за 1 {s_name}")
            else:
                mb.showerror("Ошибка", f"Валюта {t_code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка: {e}")
    else:
        mb.showwarning("Внимание", "Выберите коды валют")


# Словарь кодов валют и их полных названий
cur = {
    "USD": "Американский доллар",
    "EUR": "Евро",
    "RUB": "Российский рубль",
    "JPY": "Японская йена",
    "GBP": "Британский фунт стерлингов",
    "AUD": "Австралийский доллар",
    "CAD": "Канадский доллар",
    "CHF": "Швейцарский франк",
    "CNY": "Китайский юань",
    "KZT": "Казахстанский тенге",
    "UZS": "Узбекский сум"
}

# Создание графического интерфейса
window = Tk()
window.title("Курс обмена валюты")
window.geometry("250x400")

Label(text="Базовая валюта:").pack(padx=10, pady=5)
b_combobox = ttk.Combobox(values=list(cur.keys()))
b_combobox.pack(padx=10, pady=5)
b_combobox.bind("<<ComboboxSelected>>", update_b_label)
b_label = ttk.Label()
b_label.pack(padx=10, pady=10)

Label(text="Вторая базовая валюта:").pack(padx=10, pady=5)
s_combobox = ttk.Combobox(values=list(cur.keys()))
s_combobox.pack(padx=10, pady=5)
s_combobox.bind("<<ComboboxSelected>>", update_s_label)
s_label = ttk.Label()
s_label.pack(padx=10, pady=10)

Label(text="Целевая валюта:").pack(padx=10, pady=5)
t_combobox = ttk.Combobox(values=list(cur.keys()))
t_combobox.pack(padx=10, pady=5)
t_combobox.bind("<<ComboboxSelected>>", update_t_label)
t_label = ttk.Label()
t_label.pack(padx=10, pady=10)

Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)

window.mainloop()
