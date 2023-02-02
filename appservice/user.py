"""
+ ------------------------------------------------ +
|  Nama Lengkap    : Muhammad Ali Pratama Putra    |
|  NIM             : 5220411416                    |
|  Prodi           : Informatika                   |
+ ------------------------------------------------ +
"""

import time
import datetime
import mysql.connector as mysql
try:
    import menu
except:
    from appservice import menu
class User():
    def __init__(self, nama, id_akun):
        self.nama = nama
        self.id_akun = id_akun
        self.status_cek_kendaraan = False
        self.id_kendaraan = 0
        self.model_kendaraan = ''
        self.nomor_kendaraan = ''
        self.status_booking = False
        self.id_booking = []
    def cek_kendaraan(self, session):
        data = session.get_data_where(self.id_akun, 'db_kendaraan', 1)
        if data == None:
            pengisian = menu.menu_user_buat_kendaraan()
            menu.savedata_load()
            session.create_data('db_kendaraan', [i for i in range(1, 4)], [self.id_akun, pengisian[0], pengisian[1]])
            menu.bool_alert(True)
            time.sleep(2)
        else:
            self.status_cek_kendaraan = True
            self.id_kendaraan = int(data[0])
            self.model_kendaraan = data[2]
            self.nomor_kendaraan = data[3]
    def cek_booking(self, session):
        if self.status_booking == False:
            data_sudah_booking = session.get_data_wheres('db_transaksi', [1], [self.id_akun], [0])
            if len(data_sudah_booking) > 0:
                self.status_booking = True
                for i in data_sudah_booking:
                    self.id_booking.append(i[0])
    def tambah_data_riwayat(self, session, id_layanan, tanggal, id_trx):
        # session.create_data('db_riwayat', [i for i in range(1, 10)], [self.id_akun, id_layanan, self.id_kendaraan, tanggal, '1', 'baru', datetime.datetime.now(), 'belum', id_trx])
        session.cursor.execute("""
                               INSERT INTO db_riwayat (id_user, id_layanan, id_kendaraan, tanggal_booking, id_mekanik, status, tanggal_aktivitas, lunas, id_trx) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                               """, (self.id_akun, id_layanan, self.id_kendaraan, tanggal, '1', 'baru', datetime.datetime.now(), 'belum', id_trx))
        session.conn.commit()
    def menu(self, session):
        while self.status_cek_kendaraan == False:
            self.cek_kendaraan(session)
        while True:
            menu.main_menu_akses(self.nama, 'user')
            pilihan = menu.main_menu_user()
            if pilihan == 5:
                session.nama_akun = ''
                session.id_akun = 0
                break
            elif pilihan == 4:
                menu.menu_user_04()
            elif pilihan == 0:
                if menu.menu_user_00_check(self.model_kendaraan, self.nomor_kendaraan) == 0:
                    data = menu.menu_user_00_create()
                    session.edit_data('db_kendaraan', [2, 3], [data[0], data[1]], 0, self.id_kendaraan)
                    self.model_kendaraan = data[0]
                    self.nomor_kendaraan = data[1]
                    menu.savedata_load()
                    menu.bool_alert(True)
                    time.sleep(2)
            elif pilihan == 1:
                self.cek_booking(session)
                if self.status_booking == True:
                    menu.menu_user_01_sudah()
                else:
                    data = session.get_data('db_layanan', [])
                    layanan = [i[1] for i in data]
                    layanan.insert(0,'Kembali')
                    index_layanan = menu.menu_user_01_pilih_layanan(layanan)
                    if len(index_layanan) > 0:
                        tanggal = str(menu.menu_user_01_pilih_hari())[1:-1].replace(', ', '-')
                        kolom_trx = session.get_column('db_transaksi')
                        kolom_riw = session.get_column('db_riwayat')
                        for il in index_layanan:
                            il = int(il)
                            session.create_dataa('db_transaksi', kolom_trx[1:], [self.id_akun, data[il][0], '1', tanggal, 'baru', 'belum'])
                            id_trx = session.get_data_sortt('db_transaksi', kolom_trx, 0, False, True)
                            session.create_dataa('db_riwayat', kolom_riw[1:], [self.id_akun, data[il][0], self.id_kendaraan, tanggal, '1', 'baru', datetime.datetime.now(), 'belum', id_trx[0]])
                        menu.savedata_load()
                        menu.bool_alert(True)
                        time.sleep(2)
            elif pilihan == 2:
                self.cek_booking(session)
                data_l = session.get_data('db_layanan', [])
                id_layanan = [i[0] for i in data_l]
                d_layanan = [i[1] for i in data_l]
                layanan = []
                tanggal_booking = []
                status = []
                for i in self.id_booking:
                    data = session.get_data_where(i, 'db_transaksi', 0)
                    layanan.append(d_layanan[id_layanan.index(data[2])])
                    tanggal_booking.append(data[4])
                    status.append(data[5])
                menu.menu_user_02(layanan, tanggal_booking, status)
            elif pilihan == 3:
                self.cek_booking(session)
                data_h = session.get_data('db_layanan', [])
                id_layanan = [i[0] for i in data_h]
                d_layanan = [i[1] for i in data_h]
                d_harga = [i[2] for i in data_h]
                layanan = []
                harga = []
                data = session.get_data_wheres('db_transaksi', [1, 6], [self.id_akun, 'belum'], [])
                for i in data:
                    layanan.append(d_layanan[id_layanan.index(i[2])])
                    harga.append(d_harga[id_layanan.index(i[2])])
                menu.menu_user_03(layanan, harga)