"""
+ ------------------------------------------------ +
|  Nama Lengkap    : Muhammad Ali Pratama Putra    |
|  NIM             : 5220411416                    |
|  Prodi           : Informatika                   |
+ ------------------------------------------------ +
"""

import mysql.connector as mysql
import bcrypt
try:
    import config
except:
    from appservice import config
try:
    import menu
except:
    from appservice import menu

class Session():
    global mysql
    def __init__(self):
        self.host = config.config['host']
        self.user = config.config['user']
        self.passwd = config.config['password']
        self.db = config.config['database']
        self.jenis_akses = 'user'
        self.nama_akun = ''
        self.id_akun = 0
    def connect(self):
        try:
            self.conn = mysql.connect(
                host=self.host,
                user=self.user,
                passwd=self.passwd,
                database=self.db
            )
        except:
            menu.error_alert('Tidak Terkoneksi Database')
            quit()
        else:
            self.cursor = self.conn.cursor(buffered=True)
    def quit(self):
        self.conn.disconnect()
    def get_column(self, tabel: str):
        try:
            self.cursor.execute(f"""
            SHOW COLUMNS FROM {tabel}      
            """)
        except:
            menu.error_alert('Ada kesalahan read database')
            return ''
        else:
            columns = self.cursor.fetchall()
            return tuple([column[0] for column in columns])
    def get_data(self, tabel: str, index_kolom: list = [], isSingle: bool = False):
        tabel, isSingle, index_kolom = str(tabel), bool(isSingle), tuple(index_kolom)
        kolom_data = [self.get_column(tabel)[i] for i in index_kolom]
        if len(index_kolom) < 1:
            sql = f"""
            SELECT * FROM {tabel}
            """
        else:
            sql = f"""
            SELECT {str(kolom_data)[1:-1].replace("'", '')} FROM {tabel}
            """
        try:
            self.cursor.execute(sql)
        except:
            menu.error_alert('Ada kesalahan read database')
            return ''
        else:
            if isSingle == True:
                return self.cursor.fetchone()
            else:
                return self.cursor.fetchall()
    def create_data(self, tabel: str, index_kolom: list = [], values: list = [], isEncrypt: bool = False, index_enkripsi: list = []):
        kolom = [self.get_column(tabel)[i] for i in index_kolom]
        values = [str(i) for i in values]
        if isEncrypt == True:
            for i in index_enkripsi:
                values[i] = str(bcrypt.hashpw(values[i].encode('utf-8'), bcrypt.gensalt()))[2:-1]
        sql = f"""INSERT INTO {tabel} ({str(kolom)[1:-1].replace("'", '')}) VALUES ({str(values)[1:-1]})"""
        try:
            self.cursor.execute(sql)
        except:
            menu.error_alert('Ada kesalahan write database')
            return 0
        else:
            self.conn.commit()
            return 1
    def delete_data(self, tabel: str, index_kolom: list = [], values: list = [], logical: str = 'AND'):
        kolom = [self.get_column(tabel)[i] for i in index_kolom]
        values = [str(i) for i in values]
        if len(index_kolom) > 1:
            sql = f"""DELETE FROM {tabel} WHERE {str([str(f'{kolom[i]}="{values[i]}"') for i, v in enumerate(index_kolom)])[1:-1].replace(',', f' {logical}').replace("'", '')}"""
        else:
            sql = f"""DELETE FROM {tabel} WHERE {kolom[index_kolom[0]]}='{values[0]}'"""
        try:
            self.cursor.execute(sql)
        except:
            menu.error_alert('Ada kesalahan delete database')
            return 0
        else:
            self.conn.commit()
            return 1
    def edit_data(self, tabel: str, index_kolom: list = [], values: list = [], index_anchor: int = 0, value_anchor: str = '', isEncrypt: bool = False, index_enkripsi: list = []):
        kolom = [self.get_column(tabel)[i] for i in index_kolom]
        values = [str(i) for i in values]
        if isEncrypt == True:
            for i in index_enkripsi:
                values[i] = str(bcrypt.hashpw(values[i].encode('utf-8'), bcrypt.gensalt()))[2:-1]
        set_statement = [f'{kolom[i]}="{values[i]}"' for i in range(len(values))]
        sql = f"""UPDATE {tabel} SET {str(set_statement)[1:-1].replace("'", '')} WHERE {self.get_column(tabel)[index_anchor]}=\"{value_anchor}\""""
        try:
            self.cursor.execute(sql)
        except:
            menu.error_alert('Ada kesalahan write database')
            return 0
        else:
            self.conn.commit()
            return 1
    def get_data_where(self, input_string: str, tabel: str, index_kolom: int):
        kolom = self.get_column(tabel)[index_kolom]
        sql = f"""SELECT * FROM {tabel} WHERE {kolom}=\"{input_string}\""""
        try:
            self.cursor.execute(sql)
        except:
            menu.error_alert('Ada kesalahan read database')
            return ''
        else:
            return self.cursor.fetchone()
    def get_data_wheres(self, tabel: str, index_anchor: list, anchor_string: list, index_target: list, isSingle: bool = False):
        kolom = [self.get_column(tabel)[i] for i in index_anchor]
        where_statement = [f'{kolom[i]}="{anchor_string[i]}"' for i in range(len(index_anchor))]
        if len(index_target) > 0:
            select_statement = [self.get_column(tabel)[i] for i in index_target]
            sql = f"""SELECT {str(select_statement)[1:-1].replace("'", '')} FROM {tabel} WHERE {str(where_statement)[1:-1].replace(',', 'AND ').replace("'", '')}"""
        else:
            sql = f"""SELECT * FROM {tabel.replace("'", '')} WHERE {str(where_statement)[1:-1].replace(',', 'AND ').replace("'", '')}"""
        try:
            self.cursor.execute(sql)
        except:
            menu.error_alert('Ada kesalahan read database')
            return ''
        else:
            if isSingle:
                return self.cursor.fetchone()
            else:
                return self.cursor.fetchall()
    def auth(self, input_string: str, data: str, index_target: int):
        try:
            input_string = bytes(input_string, 'utf-8')
            hash_value = bytes(data[index_target], 'utf-8')
        except:
            return False
        else:
            return bcrypt.checkpw(input_string, hash_value)
    def get_data_sort(self, tabel: str, index_kolom: list = [], index_anchor: int = 0, asc: bool = True, isSingle: bool = False):
        tabel, isSingle, index_kolom = str(tabel), bool(isSingle), tuple(index_kolom)
        kolom_data = self.get_column(tabel)
        if len(index_kolom) < 1:
            sql = f"""
            SELECT * FROM {tabel} ORDER BY {kolom_data[index_anchor]} {'DESC' if asc == False else 'ASC'}
            """
        else:
            sql = f"""
            SELECT {str(kolom_data)[1:-1].replace("'", '')} FROM {tabel} ORDER BY {kolom_data[index_anchor]} {'DESC' if asc == False else ''}
            """
        try:
            self.cursor.execute(sql)
        except:
            menu.error_alert('Ada kesalahan read database')
            return ''
        else:
            if isSingle == True:
                return self.cursor.fetchone()
            else:
                return self.cursor.fetchall()
    def create_dataa(self, tabel: str, list_kolom: list = [], values: list = [], isEncrypt: bool = False, index_enkripsi: list = []):
        kolom = list_kolom
        values = [str(i) for i in values]
        if isEncrypt == True:
            for i in index_enkripsi:
                values[i] = str(bcrypt.hashpw(values[i].encode('utf-8'), bcrypt.gensalt()))[2:-1]
        sql = f"""INSERT INTO {tabel} ({str(kolom)[1:-1].replace("'", '')}) VALUES ({str(values)[1:-1]})"""
        try:
            self.cursor.execute(sql)
        except:
            menu.error_alert('Ada kesalahan write database')
            return 0
        else:
            self.conn.commit()
            return 1
    def get_data_sortt(self, tabel: str, list_kolom: list = [], index_anchor: int = 0, asc: bool = True, isSingle: bool = False):
        tabel, isSingle = str(tabel), bool(isSingle)
        kolom_data = list_kolom
        sql = f"""
            SELECT * FROM {tabel} ORDER BY {kolom_data[index_anchor]} {'DESC' if asc == False else 'ASC'}
            """
        try:
            self.cursor.execute(sql)
        except:
            menu.error_alert('Ada kesalahan read database')
            return ''
        else:
            if isSingle == True:
                return self.cursor.fetchone()
            else:
                return self.cursor.fetchall()