# Instalasi dan Penggunaan Bot

Ikuti langkah-langkah berikut untuk menginstal dan menjalankan bot:

| Langkah                                    | Perintah atau Keterangan                                                                 |
|-------------------------------------------|-------------------------------------------------------------------------------------------|
| **1. Clone Repositori dan Masuk ke Folder Bot** | 
|                                             | `git clone https://github.com/LFG-AAI/tomarket.git`                                      |
|                                             | `cd tomarket`                                                                            |
| **2. Buat dan Aktifkan Lingkungan Virtual** | 
|                                             | Untuk **Termux** atau **VPS**:                                                           |
|                                             | `python -m venv tomarket`                                                                |
|                                             | `source tomarket/bin/activate`                                                           |
|                                             | Untuk **VPS** dengan Python 3.x atau **Windows**:                                        |
|                                             | `python3 -m venv tomarket`                                                               |
|                                             | `source tomarket/bin/activate`                                                           |
| **3. Instal Semua Modul**                  | 
|                                             | `pip install -r requirements.txt`                                                        |
| **4. Edit Token di `tokens.txt`**          | 
|                                             | `nano tokens.txt`                                                                       |
|                                             | Paste token Anda, satu token per baris baru.<br> Simpan perubahan dengan `CTRL + X`, pilih `Y`, lalu tekan `ENTER`. |
| **5. Jalankan Bot**                       | 
|                                             | Untuk **Termux**:                                                                       |
|                                             | `python main.py`                                                                        |
|                                             | Untuk **VPS** atau **Windows**:                                                          |
|                                             | `python3 main.py`                                                                       |
| **Catatan**                               | **Pastikan untuk mengubah token Telegram dan chat ID pada `main.py`** jika Anda ingin menerima notifikasi bot ke Telegram Anda. |

Dengan mengikuti langkah-langkah di atas, bot Anda akan siap untuk dijalankan!
