# SISTEM MANAJEMEN SERVICE BENGKEL RESMI HONDA
Nama: Muhammad Ali Pratama Putra

NIM: 5220411416

## Latar Belakang
Saya memilih tema ini karena menurut saya aplikasi ini akan sering digunakan terutama untuk bisnis bengkel baik resmi atau mandiri. Aplikasi ini dapat membantu sistem transaksi konsumen dan juga admin bengkel. Saya terinspirasi untuk memakai brand mobil Honda karena saya penggemar dari brand ini.

## Detail Sistem
Saya telah membuat rancangan sistem ini menggunakan use case diagram, yang dimana diagram ini adalah standar dari UML (Unified Modelling Language) diagram.

![](https://i.ibb.co/K62zwMx/Use-Case-Diagram1.png)

Aplikasi ini terdiri dari 2 aktor, yaitu admin dan pelanggan. Untuk fitur pelanggan terdapat tambah data kendaraan, memilih jadwal servis, melihat status servis, melihat tagihan, dan melihat alamat bengkel. Dan fitur admin terdiri dari, melihat semua riwayat, mengubah status tagihan pelanggan, mengubah status servis pelanggan dan memilih mekanik, serta dapat mencetak tagihan dalam format pdf. Kedua aktor ini melewati tahap autentikasi (login) terlebih dahulu sebelum memasuki tampilan utama aplikasi. Jika pelanggan belum memiliki akun, pelanggan dapat registrasi, dan mengakses sebagai akses pelanggan.

## Library yang digunakan
- Os (built-in)
Library ini digunakan untuk merapihkan screen.
Dokumentasi library ini dapat dilihat [disini](https://docs.python.org/3/library/os.html).

- Time (built-in)
Library ini digunakan untuk memberikan delay pada screen.
Dokumentasi library ini dapat dilihat [disini](https://docs.python.org/3/library/time.html).

- Datetime (built-in)
Library ini digunakan untuk mencetak waktu saat melakukan aktifitas pada riwayat transaksi dan membuat data tanggal untuk membuat jadwal servis.
Dokumentasi library ini dapat dilihat [disini](https://docs.python.org/3/library/datetime.html).

- Json (built-in)
Library ini digunakan untuk membaca file json pada file configuration aplikasi, dengan tujuan memudahkan pengembang untuk memodifikasi aplikasi.
Dokumentasi library ini dapat dilihat [disini](https://docs.python.org/3/library/json.html).

- Mysql.connector
Library ini digunakan untuk menghubungkan layanan mysql pada localhost dengan pemrograman python.
Dokumentasi library ini dapat dilihat [disini](https://dev.mysql.com/doc/connector-python/en/).

- Rich
Library ini digunakan untuk mengatur tampilan CLI (Command Line Interface) terlihat berwarna dan tidak membosankan.
Dokumentasi library ini dapat dilihat [disini](https://rich.readthedocs.io/en/stable/introduction.html).

- Questionary
Library ini digunakan untuk membuat menu interaktif, serta dapat membuat input jawaban user lebih mudah dipahami layaknya GUI (Graphical User Interface).
Dokumentasi library ini dapat dilihat [disini](https://questionary.readthedocs.io/en/stable/pages/installation.html).

- Bcrypt
Library ini digunakan untuk mengenkripsi password dengan metode hashing. Sehingga data sensitif pengguna lebih aman disimpan di database.
Dokumentasi library ini dapat dilihat [disini](https://pypi.org/project/bcrypt/).
- FPDF
Library ini digunakan untuk membuat struk tagihan dalam format pdf yang bisa dicetak oleh printer.
Dokumentasi library ini dapat dilihat [disini](https://pyfpdf.readthedocs.io/en/latest/).

## Database
Setelah saya mengamati sistem dan beberapa referensi, saya membuat beberpa tabel yang berhubungan dengan aplikasi ini. Saya juga sudah membuat relasi tabel data yang merupakan hal penting untuk membuat rancangan sistem.

> Saya sudah memberikan contoh database pada bengkel_honda.sql

![](https://i.ibb.co/879wt0n/a.png)

Berikut detail penjelasan mengenai tabel-tabel:
- db_akses

    Tabel ini bertujuan untuk menyimpan data akun pengguna, baik pelanggan maupun admin.
    
    ![](https://i.ibb.co/P5CsVjN/a.png)

- db_layanan

    Tabel ini bertujuan untuk menyimpan data layanan, harga, serta status yang disediakan oleh bengkel.

    ![](https://i.ibb.co/qjvg78Z/a.png)

- db_mekanik

    Tabel ini bertujuan untuk menyimpan nama mekanik dan status yang bekerja di bengkel.

    ![](https://i.ibb.co/PNL89PG/a.png)
    
- db_kendaraan

    Tabel ini bertujuan untuk menyimpan data model mobil, dan nomor kendaraan dari pelanggan. Dengan syarat, 1 pelanggan hanya dapat menyimpan 1 data mobil saja.

    ![](https://i.ibb.co/XkX9Kxd/a.png)
    
- db_transaksi

    Tabel ini bertujuan untuk menyimpan data transaksi pengguna.

    ![](https://i.ibb.co/nLsV5QV/a.png)
    
- db_riwayat

    Tabel ini bertujuan untuk menyimpan pertinggal dari data transaksi dan disediakan kolom yang lebih lengkap dibanding tabel db_transaksi.

    ![](https://i.ibb.co/tJfZm5L/a.png)

## Struktur File
Struktur file projek yang rapih dapat membuat proses pengembangan menjadi lebih mudah, berikut hasil struktur yang saya buat.

- config.json

    File ini berfungsi sebagai file konfigurasi aplikasi ini, jadi pemilik komputer bisa mengatur judul aplikasi, konfigurasi localhost, dan tema warna tampilan.

- app.py

    File ini merupakan file utama projek.

- bengkel_honda.sql

    File ini berfungsi sebagai database cadangan, ini dibutuhkan ketika menjalankan aplikasi pada komputer yang berbeda.

- appservice\config.py

    File ini mengatur jalannya config.json ke fungsi-fungsi python dan menghubungkan ke sub program lain.

- appservice\database.py

    File ini berisikan class session yang memiliki beberapa atribut mysql dan method yang menyambungkan ke layanan mysql database menggunakan paradigma OOP (Object Oriented Programming).

- appservice\menu.py

    File ini berisikan fungsi-fungsi modular tampilan/front-end yang akan berhubungan dengan jalannya proses sistem/back-end.

- appservice\admin.py

    File ini berisikan class dari actor admin. Memiliki atribut id, memiliki method yang berbeda dari pelanggan, dan berkitan dengan class session.


- appservice\user.py

    File ini berisikan class dari actor user/pelanggan. Memiliki atribut id, memiliki method yang berbeda dari admin, dan berkitan dengan class session.

## Teknis Perancangan Aplikasi
- Sebelum saya membuat aplikasi ini, saya membuat konsep dahulu dengan use case diagram, lalu saya membuat struktur database dan membuat relasi antar tabel data.

- Saya mencari beberapa referensi mengenai library built-in maupun library eksternal.

- Di projek ini saya menggunakan VE (Virtual Environment) yang mana dapat membantu kelancaran aplikasi ini dan bisa digunakan di PC manapun.

- Saya merancang aplikasi ini dengan python versi 3.11.1 dan software pengolah teks Visual Studio Code.
