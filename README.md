KELOMPOK:
- Adriand Pratama (4222201036)
- Olivia Febrianti (4222201022) -
-  Nedia Waty (4222201010)




🚗 AGV Simulation with Behavior Tree (Tkinter)

Proyek ini merupakan implementasi model Behavior Tree pada Automated Guided Vehicle (AGV) menggunakan Python + Tkinter sebagai visualisasi simulasi.
AGV akan bergerak secara otomatis sesuai logika perilaku yang telah ditentukan—mulai dari start, pickup, delivery, hingga charging saat baterai menipis.

🎯 Fitur Utama

Behavior Tree Model untuk pengambilan keputusan AGV.

Simulasi Visual dengan Tkinter.

Level Baterai Dinamis, berkurang saat AGV bergerak, dan mengisi ulang di area charging.

Pergerakan Otomatis berdasarkan status tugas dan kondisi baterai.

Tampilan Interaktif, dengan indikator posisi dan level baterai.

⚙️ Teknologi yang Digunakan

Python 3.x

Tkinter (GUI bawaan Python)

Object-Oriented Design

Behavior Tree Logic Implementation

▶️ Cara Menjalankan

Pastikan Python 3 sudah terinstall.

Jalankan terminal atau command prompt di folder proyek.

Ketik perintah berikut:

python agv_bt_tkinter.py

🧭 Alur Simulasi AGV

Start Node
AGV memulai dari titik awal (misalnya base station) dengan status baterai penuh.

Pickup Node
AGV bergerak menuju area pickup untuk mengambil muatan.
Jika baterai di bawah ambang batas sebelum sampai, behavior tree mengalihkan ke charging.

Delivery Node
Setelah pickup selesai, AGV mengantar muatan ke lokasi delivery.
Selama perjalanan, baterai terus berkurang sesuai kecepatan gerak.

Charging Node
Jika baterai turun di bawah level aman, AGV langsung menuju area charging.
Setelah pengisian penuh, ia kembali melanjutkan tugas yang tertunda.

Idle / Finish
Setelah semua tugas selesai dan baterai aman, AGV masuk ke kondisi idle.



