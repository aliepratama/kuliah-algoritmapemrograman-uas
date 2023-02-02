"""
+ ------------------------------------------------ +
|  Nama Lengkap    : Muhammad Ali Pratama Putra    |
|  NIM             : 5220411416                    |
|  Prodi           : Informatika                   |
+ ------------------------------------------------ +
"""

import time
import datetime
from fpdf import FPDF
try:
    import menu
except:
    from appservice import menu
class Admin():
    def __init__(self, nama, id_akun):
        self.nama = nama
        self.id_akun = id_akun
    def menu(self, session):
        while True:
            menu.main_menu_akses(self.nama, 'admin')
            pilihan = menu.main_menu_admin()
            if pilihan == 4:
                session.nama_akun = ''
                session.id_akun = 0
                break
            elif pilihan == 3:
                akses = session.get_data('db_akses', [0,1,3])
                d_akses = [i[0] for i in akses]
                layanan = session.get_data('db_layanan', [0,1])
                d_layanan = [i[0] for i in layanan]
                kendaraan = session.get_data('db_kendaraan', [0,2])
                d_kendaraan = [i[0] for i in kendaraan]
                mekanik = session.get_data('db_mekanik', [0,1])
                d_mekanik = [i[0] for i in mekanik]
                tabel = []
                for i in session.get_data('db_riwayat', []):
                    tabel.append(f'{akses[d_akses.index(i[1])][1]} | {akses[d_akses.index(i[1])][2]} | {layanan[d_layanan.index(i[2])][1]} | {kendaraan[d_kendaraan.index(i[3])][1]} | {i[4]} | {mekanik[d_mekanik.index(i[5])][1]} | {i[6]} | {i[8]}')
                menu.menu_admin_04(tabel)
            elif pilihan == 2:
                m_data = session.get_data_wheres('db_transaksi', [6], ['belum'], [1])
                m_id_akun = list(set([i[0] for i in m_data]))
                m_data_akun = session.get_data('db_akses', [])
                m_d_akun = [i[0] for i in m_data_akun]
                m_n_akun = [i[1] for i in m_data_akun]
                m_nn_akun = [i[3] for i in m_data_akun]
                m_nama_akun = [f'{m_n_akun[m_d_akun.index(m_id_akun[i])]} | {m_nn_akun[m_d_akun.index(m_id_akun[i])]}' for i in range(len(m_id_akun))]
                id_akun_pilih = m_d_akun[menu.menu_admin_02(m_nama_akun)]
                # print(f'{id_akun_pilih}')
                # import os
                # os.system('pause')
                data_h = session.get_data('db_layanan', [])
                id_layanan = [i[0] for i in data_h]
                d_layanan = [i[1] for i in data_h]
                d_harga = [i[2] for i in data_h]
                layanan = []
                harga = []
                data = session.get_data_wheres('db_transaksi', [1, 6], [id_akun_pilih, 'belum'], [])
                for i in data:
                    layanan.append(d_layanan[id_layanan.index(i[2])])
                    harga.append(d_harga[id_layanan.index(i[2])])
                tghn = FPDF()
                tghn.add_page()
                tghn.set_font('Arial', 'B', 16)
                tghn.ln(20)
                tghn.cell(40, 10, 'Tagihan Servis Mobil')
                tghn.ln(7)
                tghn.set_font('Arial', 'I', 13)
                tghn.cell(40, 10, 'Servis & Dealer Resmi Honda Yogyakarta')
                tghn.ln(20)
                for i in range(len(layanan)):
                    tghn.set_font('Arial', '', 11)
                    tghn.cell(40, 10, f"{layanan[i]}{'      ' if len(layanan[i]) < 15 else ''}\tRp{harga[i]}")
                    tghn.ln(7)
                tghn.ln(15)
                tghn.set_font('Arial', 'B', 11)
                tghn.cell(40, 10, f"Total Pembayaran: Rp{sum([int(i) for i in harga])}")
                tghn.output(f'tagihan_{id_akun_pilih}.pdf', 'F')
                menu.savedata_load()
                menu.bool_alert(True)
                menu.pdf_alert()
            elif pilihan == 1:
                m_data = session.get_data('db_transaksi', [1])
                m_id_akun = list(set([i[0] for i in m_data]))
                m_data_akun = session.get_data('db_akses', [])
                m_d_akun = [i[0] for i in m_data_akun]
                m_n_akun = [i[1] for i in m_data_akun]
                m_nn_akun = [i[3] for i in m_data_akun]
                m_nama_akun = [f'{m_n_akun[m_d_akun.index(m_id_akun[i])]} | {m_nn_akun[m_d_akun.index(m_id_akun[i])]}' for i in range(len(m_id_akun))]
                id_akun_pilih = m_d_akun[menu.menu_admin_01(m_nama_akun)]
                data_h = session.get_data('db_layanan', [])
                id_layanan = [i[0] for i in data_h]
                d_layanan = [i[1] for i in data_h]
                d_harga = [i[2] for i in data_h]
                layanan = []
                harga = []
                lunas = []
                id_transaksi = []
                data = session.get_data_wheres('db_transaksi', [1], [id_akun_pilih], [])
                for i in data:
                    layanan.append(d_layanan[id_layanan.index(i[2])])
                    harga.append(d_harga[id_layanan.index(i[2])])
                    lunas.append(i[6])
                    id_transaksi.append(i[0])
                pilih_trx = menu.menu_admin_01_ubah(layanan, harga, lunas, id_transaksi)
                if pilih_trx != None:
                    data_riwayat = session.get_data_wheres('db_riwayat', [9], [pilih_trx[0]], [0])[0][0]
                    if pilih_trx[1] == 'belum':
                        session.edit_data('db_transaksi', [6], ['sudah'], 0, pilih_trx[0])
                        session.edit_data('db_riwayat', [7, 8], [datetime.datetime.now(), 'sudah'], 0, data_riwayat)
                    else:
                        session.edit_data('db_transaksi', [6], ['belum'], 0, pilih_trx[0])
                        session.edit_data('db_riwayat', [7, 8], [datetime.datetime.now(), 'belum'], 0, data_riwayat)
                    menu.savedata_load()
                    menu.bool_alert(True)
                    time.sleep(2)
            elif pilihan == 0:
                m_data = session.get_data('db_transaksi', [1])
                m_id_akun = list(set([i[0] for i in m_data]))
                m_data_akun = session.get_data('db_akses', [])
                m_d_akun = [i[0] for i in m_data_akun]
                m_n_akun = [i[1] for i in m_data_akun]
                m_nn_akun = [i[3] for i in m_data_akun]
                m_nama_akun = [f'{m_n_akun[m_d_akun.index(m_id_akun[i])]} | {m_nn_akun[m_d_akun.index(m_id_akun[i])]}' for i in range(len(m_id_akun))]
                id_akun_pilih = m_d_akun[menu.menu_admin_01(m_nama_akun)]
                data_h = session.get_data('db_layanan', [])
                id_layanan = [i[0] for i in data_h]
                d_layanan = [i[1] for i in data_h]
                layanan = []
                status = []
                id_transaksi = []
                data = session.get_data_wheres('db_transaksi', [1], [id_akun_pilih], [])
                for i in data:
                    layanan.append(d_layanan[id_layanan.index(i[2])])
                    status.append(i[5])
                    id_transaksi.append(i[0])
                pilih_trx = menu.menu_admin_00_pilih_trx(layanan, status, id_transaksi)
                if pilih_trx != None:
                    data_riwayat = session.get_data_wheres('db_riwayat', [9], [pilih_trx[0]], [0])[0][0]
                    if pilih_trx[1] == 'baru':
                        data_mekanik = session.get_data_wheres('db_mekanik', [2], ['ready'], [])
                        id_mekanik = [i[0] for i in data_mekanik]
                        nama_mekanik = [i[1] for i in data_mekanik]
                        id_mekanik.remove(1)
                        nama_mekanik.remove('null')
                        pilih_mekanik = menu.menu_admin_00_pilih_mekanik(nama_mekanik, id_mekanik)
                        session.edit_data('db_transaksi', [3, 5], [pilih_mekanik, 'proses'], 0, pilih_trx[0])
                        session.edit_data('db_riwayat', [5, 6, 7], [pilih_mekanik, 'proses', datetime.datetime.now()], 0, data_riwayat)
                    else:
                        pilih_status = menu.menu_admin_00_pilih_status()
                        session.edit_data('db_transaksi', [5], [pilih_status], 0, pilih_trx[0])
                        session.edit_data('db_riwayat', [6, 7], [pilih_status, datetime.datetime.now()], 0, data_riwayat)
                    menu.savedata_load()
                    menu.bool_alert(True)
                    time.sleep(2)
import database
session = database.Session()
session.id_akun = '13'
session.nama_akun = 'Admin'
session.connect()
users = Admin(session.nama_akun, session.id_akun)
users.menu(session)