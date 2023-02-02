"""
+ ------------------------------------------------ +
|  Nama Lengkap    : Muhammad Ali Pratama Putra    |
|  NIM             : 5220411416                    |
|  Prodi           : Informatika                   |
+ ------------------------------------------------ +
"""

import os
import datetime
import time
import questionary
from questionary import Style
from rich.console import Console
from rich.progress import track
from rich.panel import Panel
from rich.table import Table
try:
    import config
except:
    from appservice import config

    
console = Console(width = 90)
tema = Style(config.getStyleColor())

def clear_with_delay(seconds):
    seconds = int(seconds)
    time.sleep(seconds)
    os.system('cls')
def menu_01():
    os.system('cls')
    console.print('Selamat Datang', style='#af1d1e blink bold', justify='center')
    console.print(config.get_string('judulapp'), justify='center')
    print('')
def menu_02():
    email = questionary.text("Masukkan Email Anda", style=tema).ask()
    passwd = questionary.password("Masukkan Password Anda", style=tema).ask()
    print('')
    return [email, passwd]
def menu_03():
    nama = questionary.text("Masukkan Nama Lengkap Anda", style=tema).ask()
    email = questionary.text("Masukkan Email", style=tema).ask()
    pass1 = questionary.password("Masukkan Password", style=tema).ask()
    pass2 = questionary.password("Masukkan Konfirmasi Password", style=tema).ask()
    print('')
    return [nama, email, pass1, pass2]

def main_menu_akses(nama: str, akses: str):
    os.system('cls')
    console.print(f'Selamat Datang {nama}', style='#af1d1e blink bold', justify='center')
    console.print(f'Anda masuk sebagai {akses}', justify='center')
    print('')
def main_menu_user():
    pilihan = ('🚗 Cek Kendaraan','📅 Buat Jadwal Servis', '🔍 Lihat Status Servis','🧾 Lihat Tagihan','📍 Lihat Alamat Bengkel Kami','❌ Keluar')
    choise = pilihan.index(questionary.select(
        'Ada yang bisa kami bantu? 👋',
        choices=pilihan,
        style=tema
    ).ask())
    return choise
def menu_user_buat_kendaraan():
    os.system('cls')
    console.print('Sepertinya anda belum menambahkan data kendaraan', justify='center')
    print('')
    tipe = questionary.text("Masukkan Model Kendaraan Anda", style=tema).ask()
    plat = questionary.text("Masukkan Nomor Kendaraan Anda", style=tema).ask()
    return [tipe, plat]
def menu_user_00_create():
    os.system('cls')
    tipe = questionary.text("Masukkan Model Kendaraan Anda", style=tema).ask()
    plat = questionary.text("Masukkan Nomor Kendaraan Anda", style=tema).ask()
    return [tipe, plat]
def menu_user_00_check(model: str, plat: str):
    os.system('cls')
    pilihan = ('📝 Ubah', '⬅ Kembali')
    console.print(f'🚗 Model Kendaraan\t: {model}', style='white bold')
    console.print(f'📟 Nomor Kendaraan\t: {plat}', style='white bold')
    print('')
    return pilihan.index(questionary.select(
        'Apakah anda ingin mengubah data?',
        choices=pilihan,
        style=tema
    ).ask())
def menu_user_01_sudah():
    os.system('cls')
    console.print('Anda sudah booking', style='#673ab7 blink bold')
    print('')
    questionary.select('',choices=['⬅ Kembali'],style=tema).ask()
def menu_user_01_pilih_layanan(layanan: list):
    os.system('cls')
    return [layanan.index(i) for i in questionary.checkbox(
        '🔧 Silahkan pilih layanan servis',
        choices=layanan,
        style=tema
    ).ask()]
def menu_user_01_pilih_hari():
    os.system('cls')
    pilih_hari = ('Hari Ini', 'Besok', 'Kustom')
    pilihan = pilih_hari.index(questionary.select(
        '📆 Silahkan pilih mode tanggal',
        choices=pilih_hari,
        style=tema
    ).ask())
    hari_ini = datetime.datetime.now()
    besok = hari_ini + datetime.timedelta(1)
    if pilihan == 0:
        return [hari_ini.day, hari_ini.month, hari_ini.year]
    elif pilihan == 1:
        return [besok.day, besok.month, besok.year]
    elif pilihan == 2:
        return str(questionary.text("Masukkan Tanggal dengan format HH-BB-TTTT", style=tema).ask()).split('-')
def menu_user_02(layanan: list, tanggal_booking: list, status: list):
    os.system('cls')
    [console.print(f"[white]{layanan[i]}{'      ' if len(layanan[i]) < 15 else ''}\t[#673ab7]{tanggal_booking[i]}\t[#af1d1e][b]{status[i]}[/b]") for i in range(len(layanan))]
    print('')
    questionary.select('',choices=['⬅ Kembali'],style=tema).ask()
def menu_user_03(layanan: list, harga: list):
    os.system('cls')
    console.print('Rincian Tagihan Anda', style='#af1d1e blink bold')
    print('')
    [console.print(f"[white]{layanan[i]}{'      ' if len(layanan[i]) < 15 else ''}\t[#673ab7]Rp{harga[i]}") for i in range(len(layanan))]
    print('')
    console.print(f'Total Pembayaran: Rp{sum([int(i) for i in harga])}', style='#af1d1e blink bold')
    print('')
    questionary.select('',choices=['⬅ Kembali'],style=tema).ask()
def menu_user_04():
    os.system('cls')
    console.print('Alamat Bengkel Resmi Honda', style='#673ab7 blink bold')
    data = dict(config.get_string('alamat_bengkel')).items()
    [console.print(f"[#af1d1e][b]{i[0]}[/b]\n[white]{i[1]}") for i in data]
    print('')
    questionary.select('',choices=['⬅ Kembali'],style=tema).ask()
def main_menu_admin():
    pilihan = ('🖍 Edit Detail Servis','📅 Edit Status Tagihan', '🖨 Cetak Tagihan','🧾 Lihat Riwayat Transaksi','❌ Keluar')
    choise = pilihan.index(questionary.select(
        'Silahkan pilih fitur admin 💻',
        choices=pilihan,
        style=tema
    ).ask())
    return choise
def menu_admin_00_pilih_trx(layanan: list, status: list, id_transaksi: list):
    pilihan = ['⬅ Kembali']
    for i in range(len(layanan)):
        pilihan.append(f'{layanan[i]} | {status[i]}')
    choise = pilihan.index(questionary.select(
        'Silahkan pilih daftar booking 🔧',
        choices=pilihan,
        style=tema
    ).ask())
    if choise > 0:
        return [id_transaksi[choise - 1], status[choise - 1]]
def menu_admin_00_pilih_mekanik(mekanik: list, id_mekanik: list):
    pilihan = ['⬅ Kembali']
    for i in range(len(mekanik)):
        pilihan.append(mekanik[i])
    choise = pilihan.index(questionary.select(
        'Silahkan pilih mekanik 👷‍♂️',
        choices=pilihan,
        style=tema
    ).ask())
    if choise > 0:
        return id_mekanik[choise - 1]
def menu_admin_00_pilih_status():
    pilihan = ('⬅ Kembali', '⏱ Proses', '✔ Selesai')
    choise = questionary.select(
        'Silahkan pilih status 💻',
        choices=pilihan,
        style=tema
    ).ask()
    if choise == pilihan[1]:
        return 'proses'
    elif choise == pilihan[2]:
        return 'selesai'
def menu_admin_01(user: list):
    os.system('cls')
    return user.index(questionary.select(
        'Silahkan pilih user 🧍‍♂️',
        choices=user,
        style=tema
    ).ask())
def menu_admin_01_ubah(layanan: list, harga: list, lunas: list, id_transaksi: list):
    pilihan = ['⬅ Kembali']
    for i in range(len(layanan)):
        pilihan.append(f'{layanan[i]} | {harga[i]} | {lunas[i]}')
    choise = pilihan.index(questionary.select(
        'Silahkan ubah status pelunasan 💵',
        choices=pilihan,
        style=tema
    ).ask())
    if choise > 0:
        return [id_transaksi[choise - 1], lunas[choise - 1]]
def menu_admin_02(user: list):
    os.system('cls')
    return user.index(questionary.select(
        'Silahkan pilih user 🧍‍♂️',
        choices=user,
        style=tema
    ).ask())
def menu_admin_04(data: list):
    os.system('cls')
    table = Table(title="Riwayat Seluruh Transaksi")
    table.add_column("Email", style="cyan", no_wrap=True)
    table.add_column("Nama", style="magenta", no_wrap=True)
    table.add_column("Layanan", style="green", no_wrap=True)
    table.add_column("Mobil", style="cyan", no_wrap=True)
    table.add_column("Tanggal Booking", style="magenta", no_wrap=True)
    table.add_column("Mekanik", style="green", no_wrap=True)
    table.add_column("Status", style="cyan", no_wrap=True)
    table.add_column("Lunas", style="magenta", no_wrap=True)
    for i in data:
        i = str(i).split(' | ')
        table.add_row(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
    console.print(table, justify="center")
    print('')
    questionary.select('',choices=['⬅ Kembali'],style=tema).ask()
def pilihan_01_01():
    pilihan = ('🚗 Masuk','📖 Registrasi','❌ Keluar')
    choise = pilihan.index(questionary.select(
        'Ada yang bisa kami bantu? 👋',
        choices=pilihan,
        style=tema
    ).ask())
    return choise

def error_alert(error_msg):
    os.system('cls')
    error = Table.grid()
    error.add_row(
    Panel.fit(
        f"[white]{error_msg}",
        title="Error!",
        border_style="#af1d1e",
        padding=(2, 2)
    ))
    console.print(error)
def bool_alert(bool: bool):
    if bool:
        console.print('Berhasil', style='#673ab7 blink bold')
    else:
        console.print('Gagal', style='#af1d1e blink bold')
def login_alert(bool: bool):
    if bool:
        console.print('Berhasil', style='#673ab7 blink bold')
    else:
        console.print('Gagal', style='#af1d1e blink bold')
def register_alert(bool: bool):
    if bool:
        console.print('Berhasil Membuat Akun', style='#673ab7 blink bold')
    else:
        console.print('Gagal Membuat Akun', style='#af1d1e blink bold')
def login_load():
    for i in track(range(20), description="Autentikasi Akun..."):
        time.sleep(0.075)
def register_load():
    for i in track(range(20), description="Membuat akun anda..."):
        time.sleep(0.1)
def savedata_load():
    for i in track(range(20), description="Menyimpan data..."):
        time.sleep(0.05)
def pdf_alert():
    console.print('PDF sudah disimpan, silahkan print...', style='#673ab7 blink bold')
    print('')
    questionary.select('',choices=['⬅ Kembali'],style=tema).ask()
def menu_quit():
    os.system('cls')
    console.print('Terima Kasih', style='#af1d1e blink bold', justify='center')
def menu_akses(akses):
    os.system('cls')
    console.print(f'Mengarahkan anda ke menu {akses}', style='white blink bold', justify='center')
    time.sleep(2)