import tkinter as tk

from tkinter import filedialog, messagebox



def turkce_siralamasi():

    # Türk alfabesindeki harflerin sıralaması

    return 'abcçdefgğhıijklmnoöprsştuüvyz'



def harf_sirasi(harf):

    alfabe = turkce_siralamasi()

    if harf in alfabe:

        return alfabe.index(harf)

    else:

        return None 



def sifreleme(kelime):

    alfabe = turkce_siralamasi()

    kelime = kelime.lower()

    harf_sayisi = len(kelime)

    sifreli_kelime = ""



    for harf in kelime:

        harf_siralamasi = harf_sirasi(harf)

        if harf_siralamasi is not None:

            sifre_index = (harf_siralamasi + harf_sayisi) % len(alfabe)

            sifreli_harf = alfabe[sifre_index]

            sifreli_kelime += sifreli_harf

        else:

            sifreli_kelime += harf



    return sifreli_kelime



def desifreleme(sifreli_kelime):

    alfabe = turkce_siralamasi()

    sifreli_kelime = sifreli_kelime.lower()

    harf_sayisi = len(sifreli_kelime)

    desifreli_kelime = ""



    for harf in sifreli_kelime:

        harf_siralamasi = harf_sirasi(harf)

        if harf_siralamasi is not None:

            sifre_index = (harf_siralamasi - harf_sayisi) % len(alfabe)

            desifreli_harf = alfabe[sifre_index]

            desifreli_kelime += desifreli_harf

        else:

            desifreli_kelime += harf



    return desifreli_kelime



def dosya_oku(dosya_adi):

    try:

        with open(dosya_adi, 'r', encoding='utf-8') as dosya:

            return dosya.read()

    except FileNotFoundError:

        messagebox.showerror("Hata", f"{dosya_adi} dosyası bulunamadı.")

        return None



def dosya_yaz(dosya_adi, icerik):

    with open(dosya_adi, 'w', encoding='utf-8') as dosya:

        dosya.write(icerik)



def sifreleme_islemi():

    dosya_adi = filedialog.askopenfilename(title="Şifrelenecek metin dosyasını seçin", filetypes=[("Metin Dosyası", "*.txt")])

    if dosya_adi:

        icerik = dosya_oku(dosya_adi)

        if icerik:

            sifreli_icerik = sifreleme(icerik)

            cikti_dosya_adi = filedialog.asksaveasfilename(title="Şifreli metin dosyasını kaydet", defaultextension=".txt", filetypes=[("Metin Dosyası", "*.txt")])

            if cikti_dosya_adi:

                dosya_yaz(cikti_dosya_adi, sifreli_icerik)

                messagebox.showinfo("Başarılı", f"Şifreli içerik {cikti_dosya_adi} dosyasına yazıldı.")



def desifreleme_islemi():

    dosya_adi = filedialog.askopenfilename(title="Deşifrelenecek metin dosyasını seçin", filetypes=[("Metin Dosyası", "*.txt")])

    if dosya_adi:

        icerik = dosya_oku(dosya_adi)

        if icerik:

            desifreli_icerik = desifreleme(icerik)

            cikti_dosya_adi = filedialog.asksaveasfilename(title="Deşifreli metin dosyasını kaydet", defaultextension=".txt", filetypes=[("Metin Dosyası", "*.txt")])

            if cikti_dosya_adi:

                dosya_yaz(cikti_dosya_adi, desifreli_icerik)

                messagebox.showinfo("Başarılı", f"Deşifreli içerik {cikti_dosya_adi} dosyasına yazıldı.")



def main():

    root = tk.Tk()

    root.title("Metin Dosya Şifreleme ve Deşifreleme")

    root.geometry("400x200")

    root.configure(bg='#e6e6e6')



    stil = {

        "bg": "#4a90e2",

        "fg": "white",

        "font": ("Helvetica", 14, "bold"),

        "relief": tk.RAISED,

        "bd": 3,

        "width": 20,

        "height": 2

    }



    frame = tk.Frame(root, bg='#e6e6e6')

    frame.pack(expand=True)



    sifreleme_butonu = tk.Button(frame, text="Metin Dosyasını Şifrele", **stil, command=sifreleme_islemi)

    sifreleme_butonu.grid(row=0, column=0, padx=20, pady=20)



    desifreleme_butonu = tk.Button(frame, text="Metin Dosyasını Deşifrele", **stil, command=desifreleme_islemi)

    desifreleme_butonu.grid(row=1, column=0, padx=20, pady=20)



    root.mainloop()



if __name__ == "__main__":

    main()