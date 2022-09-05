import tkinter as tk
import requests
kur=tk.Tk()
kur.title("Dolar ve Euro Kurunu Öğren")
kur.geometry('500x700+50+50')
kur.resizable(0,0)

canvas=tk.Canvas(kur, height=800, width=600, bg='#10E2E9' )
canvas.pack()

def latest():
    label=tk.Label(kur, text="Dolar Kuru: "+ str(dolar[1]),fg="#263D42",font="Times 15 bold")
    label.place(x=150, y=150)
    label2=tk.Label(kur, text="Euro Kuru: "+ str(euro[1]),fg="#263D42",font="Times 15 bold")
    label2.place(x=150, y=185)
    label3=tk.Label(kur, text="Bitcoin Dolar Kuru: "+ str(bitcoin[1]),fg="#263D42",font="Times 15 bold")
    label3.place(x=150, y=220)
    

dolar1 = requests.get("https://www.bloomberght.com/piyasa/refdata/dolar").json()
euro1 = requests.get("https://www.bloomberght.com/piyasa/refdata/euro").json()
bitcoin1 = requests.get("https://www.bloomberght.com/piyasa/refdata/bitcoin").json()
dolar = dolar1["SeriesData"][-1]
euro = euro1["SeriesData"][-1]
bitcoin = bitcoin1["SeriesData"][-1]

buton=tk.Button(kur, text="Son Durum",fg="#263D42",bg="white", font="Times 15 bold",command=latest)
buton.place(x=180, y=480)

kur.mainloop()