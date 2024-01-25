import tkinter as tk
from tkinter import ttk, messagebox, Canvas
import requests
from pygame import mixer

mixer.init()  # Ses için mixer'ı başlat

def play_cash_sound():
    mixer.music.load(r"C:\Users\yigit\source\repos\live-stock-exchange-app\cash.mp3")
    mixer.music.play()

def get_latest_data():
    try:
        dolar_data = requests.get("https://www.bloomberght.com/piyasa/refdata/dolar").json()
        euro_data = requests.get("https://www.bloomberght.com/piyasa/refdata/euro").json()
        bitcoin_data = requests.get("https://www.bloomberght.com/piyasa/refdata/bitcoin").json()

        dolar_rate = dolar_data["SeriesData"][-1][1]
        euro_rate = euro_data["SeriesData"][-1][1]
        bitcoin_rate = bitcoin_data["SeriesData"][-1][1]

        return dolar_rate, euro_rate, bitcoin_rate
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Hata", f"Veri alınırken bir hata oluştu:\n{e}")
        return None, None, None

def update_labels():
    loading_label.config(text="Veriler alınıyor...", font=('Helvetica', 12, 'bold'), foreground="#FFFFFF")
    kur.update_idletasks()
    dolar_rate, euro_rate, bitcoin_rate = get_latest_data()

    if dolar_rate is not None and euro_rate is not None and bitcoin_rate is not None:
        dolar_label.config(text=f"Dolar Kuru: {dolar_rate}", foreground="#FFFFFF")
        euro_label.config(text=f"Euro Kuru: {euro_rate}", foreground="#FFFFFF")
        bitcoin_label.config(text=f"Bitcoin Dolar Kuru: {bitcoin_rate}", foreground="#FFFFFF")
        update_button.config(text="Güncellendi", state=tk.DISABLED)
        play_cash_sound()
        kur.after(1000, reset_loading_label)  # 5 saniye bekledikten sonra reset_loading_label fonksiyonunu çağır
    else:
        loading_label.config(text="Veri alınamadı", font=('Helvetica', 12), foreground="red")
        kur.after(1000, reset_loading_label)

def reset_button():
    update_button.config(text="Güncelle", state=tk.NORMAL)
    loading_label.config(text="", font=('Helvetica', 12))

def reset_loading_label():
    loading_label.config(text="", font=('Helvetica', 12))

# Ana pencere oluşturuluyor
kur = tk.Tk()
kur.title("Canlı Borsa Takip Uygulaması")
kur.geometry('400x300')
kur.resizable(0, 0)
kur.configure(bg='#121212')

style = ttk.Style()
style.configure("TFrame", background="#121212")
style.configure("TLabel", font=('Helvetica', 12), background="#121212", foreground="#FFFFFF")
style.configure("TButton", font=('Helvetica', 12), background="#263D42", foreground="#FFFFFF")

frame = ttk.Frame(kur, padding=20)
frame.pack(pady=20)

dolar_label = ttk.Label(frame, text="", font=('Helvetica', 15, 'bold'))
dolar_label.grid(row=0, column=0, pady=10, padx=10, sticky="w")

euro_label = ttk.Label(frame, text="", font=('Helvetica', 15, 'bold'))
euro_label.grid(row=1, column=0, pady=10, padx=10, sticky="w")

bitcoin_label = ttk.Label(frame, text="", font=('Helvetica', 15, 'bold'))
bitcoin_label.grid(row=2, column=0, pady=5, padx=10, sticky="w")

update_button = ttk.Button(frame, text="Güncelle", command=update_labels)
update_button.grid(row=3, column=0, pady=15)

loading_label = ttk.Label(frame, text="", font=('Helvetica', 12))
loading_label.grid(row=4, column=0, pady=10)

# Grid Konfigürasyonu
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.rowconfigure(2, weight=1)

kur.mainloop()
