# 🚗 AGV Behavior Tree Simulation (Tkinter)

Proyek ini merupakan implementasi **Behavior Tree** untuk sistem **AGV (Automated Guided Vehicle)** menggunakan **Python (Tkinter)**.  
Simulasi menampilkan perilaku AGV dalam menjalankan tugas seperti mengambil barang (*pickup*), mengirim barang (*delivery*), dan mengisi ulang baterai (*charging*) secara otomatis berdasarkan kondisi baterai.

---

## 🎯 Tujuan
Mensimulasikan **pengambilan keputusan berbasis Behavior Tree** untuk robot AGV agar mampu:
- Mengambil dan mengirim barang secara otomatis.
- Memantau kondisi baterai.
- Menghentikan tugas dan menuju stasiun pengisian saat baterai rendah.
- Melanjutkan tugas setelah baterai penuh.

---

## 🧩 Struktur Behavior Tree
```text
Root
├── Sequence: Low Battery Handler
│   ├── Condition: Battery < 20%
│   └── Action: Move to Charge → Charge Battery
└── Sequence: Main Task
    ├── Action: Move to Pickup → Pickup Item
    ├── Action: Move to Delivery → Deliver Item
🖥️ Teknologi yang Digunakan
Python 3

Tkinter untuk antarmuka dan visualisasi AGV.

Multithreading untuk simulasi non-blocking.

OOP Design untuk struktur Behavior Tree yang modular.

⚙️ Cara Menjalankan
Pastikan Python sudah terinstal (versi 3.8 atau lebih baru).

Unduh atau clone repositori ini:

bash
Salin kode
git clone https://github.com/AdriandPratama/Behavior_Tree.git
cd Behavior_Tree
Jalankan program:

bash
Salin kode
python agv_bt_tkinter.py
🎮 Fitur Simulasi
AGV bergerak otomatis antara titik pickup, delivery, dan charging.

Baterai menurun secara dinamis selama perjalanan.

Mode penyelamatan otomatis: jika baterai hampir habis, AGV tetap berjalan pelan ke stasiun pengisian.

Visual indikator baterai dengan warna:

🟢 Hijau = >50%

🟡 Kuning = 20–50%

🔴 Merah = <20%

📸 Tampilan Simulasi
Tampilan sederhana Tkinter menampilkan titik:

Pickup (oranye)

Delivery (biru muda)

Charging (hijau)

AGV ditampilkan sebagai lingkaran biru yang bergerak sesuai keputusan Behavior Tree.

