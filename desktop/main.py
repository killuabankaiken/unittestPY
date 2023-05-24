import tkinter as tk
from tkinter import messagebox
from mysql.connector import connect
import datetime

app = tk.Tk()
app.title('sad')
app.minsize(600,400)


# Задаем параметры растягивания и заполнения для ячеек таблицы
for i in range(4):
    app.columnconfigure(i, weight=1)
    app.rowconfigure(i, weight=1)

client_full_name_label = tk.Label(app, text='ФИО Клиента')
client_full_name = tk.Entry(app, width=30)
client_full_name_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
client_full_name.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

device_label = tk.Label(app, text='Устройство')
device = tk.Entry(app, width=30)
device_label.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')
device.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

service_label = tk.Label(app, text='Тип услуги')
service = tk.Entry(app, width=30)
service_label.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')
service.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')

master_label = tk.Label(app, text='Имя мастера')
master = tk.Entry(app, width=30)
master_label.grid(row=0, column=2, padx=10, pady=10, sticky='nsew')
master.grid(row=0, column=3, padx=10, pady=10, sticky='nsew')

price_label = tk.Label(app, text='Цена')
price = tk.Entry(app, width=30)
price_label.grid(row=1, column=2, padx=10, pady=10, sticky='nsew')
price.grid(row=1, column=3, padx=10, pady=10, sticky='nsew')

description_label = tk.Label(app, text='Описание')
description = tk.Entry(app, width=63)
description_label.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')
description.grid(row=4, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

def create_order():
    connection = connect(host='localhost', username='root',password='433272as' ,database='my_table')
    c = connection.cursor()
    query = "INSERT INTO my_table (client_name, device, service, master, price, description, date_created) VALUES (%s, %s, %s, %s, %s, %s, %s)"

    date_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    values =(
        client_full_name.get(),
        device.get(),
        service.get(),
        master.get(),
        price.get(),
        description.get(),
        date_now
    )
    c.execute(query,values)
    connection.commit()
    c.close()
    connection.close()
    messagebox.showinfo('Уведомление', 'Заказ успешно создан!')
submit = tk.Button(app, text='Создать заказ', width=30, height=5, command=create_order)
submit.grid(row=5, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

app.mainloop()
