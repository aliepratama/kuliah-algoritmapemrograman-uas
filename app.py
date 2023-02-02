"""
+ ------------------------------------------------ +
|  Nama Lengkap    : Muhammad Ali Pratama Putra    |
|  NIM             : 5220411416                    |
|  Prodi           : Informatika                   |
+ ------------------------------------------------ +
"""

import time
from appservice import menu
from appservice import database
from appservice import user
from appservice import admin

session = database.Session()
session.connect()

def main_menu():
    if session.jenis_akses == 'admin':
        users = admin.Admin(session.nama_akun, session.id_akun)
    else:
        users = user.User(session.nama_akun, session.id_akun)
    menu.main_menu_akses(users.nama, session.jenis_akses)
    users.menu(session)
    del users

while True:
    menu.menu_01()
    pilihan_01 = menu.pilihan_01_01()
    if pilihan_01 == 0:
        menu.menu_01()
        login = menu.menu_02()
        data_akun = session.get_data_where(str(login[0]).lower(),'db_akses', 1)
        akses = session.auth(login[1], data_akun, 2)
        menu.login_load()
        menu.login_alert(akses)
        time.sleep(2)
        if akses:
            session.jenis_akses = data_akun[-1]
            session.nama_akun = data_akun[-2]
            session.id_akun = data_akun[0]
            menu.menu_akses(data_akun[-1])
            main_menu()
    elif pilihan_01 == 1:
        menu.menu_01()
        data = menu.menu_03()
        if bool(str(data[1]).find('@') == -1 and str(data[1]).find('.') == -1) or data[2] != data[3]:
            menu.register_alert(False)
        else:
            menu.register_load()
            menu.register_alert(True) if session.create_data('db_akses', [i for i in range(1, 5)], [str(data[1]).lower(), data[2], data[0], 'user'], True, [1]) == 1 else menu.register_alert(False)
        time.sleep(2)
        session.jenis_akses = 'user'
        session.nama_akun = data[0]
        data_akun = session.get_data_where(data[1],'db_akses', 1)
        session.id_akun = data_akun[0]
        menu.menu_akses('user')
        main_menu()
    elif pilihan_01 == 2:
        menu.menu_quit()
        menu.clear_with_delay(1)
        session.quit()
        quit()