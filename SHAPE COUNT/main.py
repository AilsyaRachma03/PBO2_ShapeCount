import wx
import noname
import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="pbo")
cursor = conn.cursor()


class PDashbord(noname.panel_dashbord):
    def __init__(self, parent):
        noname.panel_dashbord.__init__(self, parent.panel_utama)
        self.parent = parent
        self.SetSize(parent.GetSize())

    def persegi_keliling(self, event):
        self.parent.show_panel_KPer()

    def persegi_luas(self, event):
        self.parent.show_panel_LPer()

    def persegi_panjang_keliling(self, event):
        self.parent.show_panel_KPerPanjang()

    def persegi_panjang_luas(self, event):
        self.parent.show_panel_LPerPanjang()

    def lingkaran_keliling(self, event):
        self.parent.show_panel_KLingkaran()

    def lingkaran_keliling_luas(self, event):
        self.parent.show_panel_LLingkaran()

    def segitiga_keliling(self, event):
        self.parent.show_panel_KSegitiga()

    def segitiga_keliling_luas(self, event):
        self.parent.show_panel_LSegitiga()

    def belah_ketupat_keliling(self, event):
        self.parent.show_panel_KBB()

    def belah_ketupat_luas(self, event):
        self.parent.show_panel_LKBB()

    def trapesium_keliling(self, event):
        self.parent.show_panel_KTrapesium()

    def trapesium_keliling_luas(self, event):
        self.parent.show_panel_LTrapesium()

    def layang_keliling(self, event):
        self.parent.show_panel_KLayang()

    def layang_keliling_luas(self, event):
        self.parent.show_panel_LLayang()

    def jajar_genjang_keliling(self, event):
        self.parent.show_panel_KJajar()

    def jajar_genjang_keliling_luas(self, event):
        self.parent.show_panel_LJajar()

    def kubus_luas(self, event):
        self.parent.show_panel_LPKubus()

    def kubus_volume(self, event):
        self.parent.show_panel_VKubus()

    def balok_luas(self, event):
        self.parent.show_panel_LPBalok()

    def balok_volume(self, event):
        self.parent.show_panel_VBalok()

    def prisma_segitiga_luas(self, event):
        self.parent.show_panel_LPPriTiga()

    def prisma_segitiga_volume(self, event):
        self.parent.show_panel_VPriTiga()

    def prisma_segiempat_luas(self, event):
        self.parent.show_panel_LPPriEmpat()

    def prisma_segiempat_volume(self, event):
        self.parent.show_panel_VPPriEmpat()

    def kerucut_luas(self, event):
        self.parent.show_panel_LPKerucut()

    def kerucut_volume(self, event):
        self.parent.show_panel_VKerucut()

    def bola_luas(self, event):
        self.parent.show_panel_LPBola()

    def bola_volume(self, event):
        self.parent.show_panel_VBola()

    def limas_segiempat_LuasP(self, event):
        self.parent.show_panel_LPLEmpat()

    def limas_segiempat_volume(self, event):
        self.parent.show_panel_VLEMPAT()

    def tabung_luas(self, event):
        self.parent.show_panel_LPTabung()

    def tabung_volume(self, event):
        self.parent.show_panel_VTabung()

    def tombol_bang_datar(self, event):
        self.parent.show_panel_katalog_datar()

    def tombol_bang_ruang(self, event):
        self.parent.show_panel_katalog_ruang()

    def tombol_bang_datar1(self, event):
        self.parent.show_panel_spesi_datar()

    def tombol_bang_ruang1(self, event):
        self.parent.show_panel_spesi_ruang()

    def tombol_buka_catatan(self, event):
        self.parent.show_panel_catatan()

    def tombol_logout(self, event):
        self.parent.show_panel_login()

class tampilan_Catatan(noname.panel_catatan):
    id_catatan = ''
    row_id = ''

    def __init__(self, parent):
        noname.panel_catatan.__init__(self, parent.panel_utama)
        self.parent = parent
        self.tampil()

    def set_id_catatan(self, id):
        self.id_catatan = id

    def set_row_id(self, id):
        self.row_id = id

    def get_id_catatan(self):
        return self.id_catatan

    def get_row_id(self):
        return self.row_id

    def select_cell_tabel(self, event):
        row = event.GetRow()
        self.lihat_isi(row)

    def lihat_isi(self, row):
        deadline_pr = self.tabel_catatan.GetCellValue(row, 0)
        isi_catatan = self.tabel_catatan.GetCellValue(row, 1)

        self.query = "SELECT id_catatan FROM catatan where deadline='{}' and catatan_pr='{}'".format(deadline_pr, isi_catatan)
        cursor.execute(self.query)
        id_cat = cursor.fetchone()

        if id_cat is not None:
            self.set_id_catatan(id_cat[0])

        if row is not None:
            self.set_row_id(row)

        self.input_deadline.SetValue(deadline_pr)
        self.input_cat.SetValue(isi_catatan)

    def tombol_catatan_edit(self, event):
        deadline_pr = self.input_deadline.GetValue()
        isi_catatan = self.input_cat.GetValue()

        id_cat = self.get_id_catatan()

        if deadline_pr != "" and isi_catatan != "":
            query = "UPDATE catatan SET deadline = %s, catatan_pr = %s WHERE id_catatan = %s"
            value = (deadline_pr, isi_catatan, id_cat)
            cursor.execute(query, value)
            conn.commit()
        else:
            wx.MessageBox('Masukkan Data Dengan Lengkap')

    def tombol_catatan_tambah(self, event):
        deadline_pr = self.input_deadline.GetValue()
        isi_catatan = self.input_cat.GetValue()
        id_cat = self.get_id_catatan()

        if deadline_pr != "" and isi_catatan != "":
            self.query = 'INSERT INTO catatan (deadline, catatan_pr) values (%s, %s)'
            self.value = (deadline_pr, isi_catatan)
            cursor.execute(self.query, self.value)
            conn.commit()
            self.parent.show_panel_catatan()
        else:
            wx.MessageBox('Masukkan Data Dengan Lengkap')

    def tampil(self):
        query = 'SELECT deadline, catatan_pr FROM catatan'
        cursor.execute(query)
        hasil = cursor.fetchall()
        for a in hasil:
            self.tabel_catatan.AppendRows(1)

        for b in range(2):
            a = 0
            for row in hasil:
                self.tabel_catatan.SetCellValue(a, b, str(row[b]))
                a = a + 1

    def tombol_catatan_res(self, event):
        query = 'SELECT deadline, catatan_pr FROM catatan'
        cursor.execute(query)
        hasil = cursor.fetchall()
        for a in hasil:
            self.tabel_catatan.AppendRows(1)

        for b in range(2):
            a = 0
            for row in hasil:
                self.tabel_catatan.SetCellValue(a, b, str(row[b]))
                a = a + 1

    def tombol_catatan_del(self, event):
        id_cat = self.get_id_catatan()
        row_id = self.get_row_id()

        query = "DELETE FROM catatan WHERE id_catatan = {}".format(id_cat)
        cursor.execute(query)
        conn.commit()

        self.tabel_catatan.DeleteRows(row_id)

    def tombol_catatan_kembali(self, event):
        self.parent.show_panel_dash()


class K_Bangun_Datar(noname.panel_ru_bd):
    def __init__(self, parent):
        noname.panel_ru_bd.__init__(self, parent.panel_utama)
        self.parent = parent
        self.tampilkan_katalog_datar()
        self.SetSize(parent.GetSize())

    def tampilkan_katalog_datar(self):
        query = 'SELECT t2.nama_bangun, t1.r_keliling, t1.r_luas FROM b_datar t1 INNER JOIN bangun t2 ON t1.id_bangun = t2.id_bangun'
        cursor.execute(query)
        hasil = cursor.fetchall()

        for b in range(3):
            a = 0
            for row in hasil:
                self.grid_datar.SetCellValue(a, b, str(row[b]))
                a = a + 1

    def klik_kembali_datar(self, event):
        self.parent.show_panel_dash()


class K_Bangun_Ruang(noname.panel_ru_ruang):
    def __init__(self, parent):
        noname.panel_ru_ruang.__init__(self, parent.panel_utama)
        self.parent = parent
        self.tampilkan_katalog_ruang()
        self.SetSize(parent.GetSize())

    def tampilkan_katalog_ruang(self):
        query = 'SELECT t2.nama_bangun, t1.luas_p, t1.volume FROM b_ruang t1 INNER JOIN bangun t2 ON t1.id_bangun = t2.id_bangun'
        cursor.execute(query)
        hasil = cursor.fetchall()

        for b in range(3):
            a = 0
            for row in hasil:
                self.grid_ruang.SetCellValue(a, b, str(row[b]))
                a = a + 1

    def klik_kembali_ruang(self, event):
        self.parent.show_panel_dash()


class S_Bangun_Datar(noname.panel_spe_bd):
    def __init__(self, parent):
        noname.panel_spe_bd.__init__(self, parent.panel_utama)
        self.parent = parent
        self.tampilkan_spesi_datar()
        self.SetSize(parent.GetSize())

    def tampilkan_spesi_datar(self):
        query = 'SELECT t2.nama_bangun, t1.sisi, t1.sudut, t1.simetri_putar, t1.diagonal FROM s_datar t1 INNER JOIN bangun t2 ON t1.id_bangun = t2.id_bangun'
        cursor.execute(query)
        hasil = cursor.fetchall()

        for b in range(5):
            a = 0
            for row in hasil:
                self.grid_spe_datar.SetCellValue(a, b, str(row[b]))
                a = a + 1

    def klik_kembali_datar_spek(self, event):
        self.parent.show_panel_dash()


class S_Bangun_Ruang(noname.panel_spe_bruang):
    def __init__(self, parent):
        noname.panel_spe_bruang.__init__(self, parent.panel_utama)
        self.parent = parent
        self.tampilkan_spesi_ruang()
        self.SetSize(parent.GetSize())

    def tampilkan_spesi_ruang(self):
        query = 'SELECT t2.nama_bangun, t1.sisi, t1.rusuk, t1.sudut, t1.d_sisi, t1.d_ruang, t1.bdg_diagonal FROM s_ruang t1 INNER JOIN bangun t2 ON t1.id_bangun = t2.id_bangun'
        cursor.execute(query)
        hasil = cursor.fetchall()

        for b in range(7):
            a = 0
            for row in hasil:
                self.grid_spe_ruang.SetCellValue(a, b, str(row[b]))
                a = a + 1

    def klik_kembali_ruang_spek(self, event):
        self.parent.show_panel_dash()


class PLogin(noname.m_gin):
    def __init__(self, parent):
        noname.m_gin.__init__(self, parent.panel_utama)
        self.parent = parent
        self.SetSize(parent.GetSize())

    def tombol_login(self, event):
        user = self.input_username.GetValue()
        passwd = self.input_password.GetValue()

        self.query = "SELECT * FROM shape where username='{}' and password='{}'".format(user, passwd)
        cursor.execute(self.query)
        hasil = cursor.fetchone()

        if hasil is not None and len(hasil) > 0:
            wx.MessageBox("Selamat Login Berhasil", "Informasi", wx.OK | wx.ICON_INFORMATION)
            print("Selamat Login Berhasil")
            self.parent.show_panel_dash()
        else:
            wx.MessageBox("Login Gagal", "Silahkan masukkan username dan password lagi!", wx.OK | wx.ICON_ERROR)
            print("Login Gagal")

    def tombol_daftar(self, event):
        dlg = Reg(None)
        dlg.ShowModal()

    def keluar_daf(self, event):
        self.Destroy()


class Reg(noname.D_af):
    def __init__(self, parent):
        noname.D_af.__init__(self, parent)

    def tombol_daftar(self, event):
        nama = self.d_nama.GetValue()
        alamat = self.d_alamat.GetValue()
        email = self.d_email.GetValue()
        user = self.d_username.GetValue()
        passwd = self.d_password.GetValue()

        if nama != "" and alamat != "" and email != "" and user != "" and passwd != "":
            self.query = 'INSERT INTO shape (nama, alamat, email, username, password) VALUES (%s, %s, %s, %s, %s)'
            self.value = (nama, alamat, email, user, passwd)
            cursor.execute(self.query, self.value)
            conn.commit()
            mdlg = wx.MessageDialog(None, 'Apakah Data sudah Benar ?', 'Konfirmasi',
                                    wx.YES_NO | wx.ICON_QUESTION)  # message dialog buat objek
            kodeDialog = mdlg.ShowModal()
            print('kodeDialog :', kodeDialog)
            if kodeDialog == wx.ID_YES:
                print('yes di klik')
                self.Destroy()
            else:
                print('No diklik')
        else:
            wx.MessageBox('Masukkan Data Dengan Lengkap')

    def t_masuk(self, event):
        self.Hide()

    def keluar_daf(self, event):
        self.Destroy()


# KALKULATOR BANGUN DATAR
# PERSEGI
# Keliling
class PK_Persegi(noname.k_persegi):
    def __init__(self, parent):
        noname.k_persegi.__init__(self, parent.panel_utama)
        self.parent = parent
        self.result = float(self.hasil_kPersegi.GetLabelText())
        self.SetSize(parent.GetSize())

    def kembali_kel_persegiOnButtonClick(self, event):
        self.parent.show_panel_dash()

    def persegi_keliling_hitung(self, event):
        sisi = float(self.input_sisiPersegi.GetValue())
        self.result = 4 * sisi
        self.hasil_kPersegi.SetLabelText(str(self.result))


# Luas
class PL_Persegi(noname.l_persegi):
    def __init__(self, parent):
        noname.l_persegi.__init__(self, parent.panel_utama)
        self.parent = parent
        self.result = float(self.hasil_LPersegi.GetLabelText())
        self.SetSize(parent.GetSize())

    def kembali_luas_persegiOnButtonClick(self, event):
        self.parent.show_panel_dash()

    def persegi_luas_hitung(self, event):
        sisi = float(self.input_sisiPersegi2.GetValue())
        self.result = sisi * sisi
        self.hasil_LPersegi.SetLabelText(str(self.result))


# PERSEGI PANJANG
# Keliling
class PK_PerPanjang(noname.k_PPanjang):
    def __init__(self, parent):
        noname.k_PPanjang.__init__(self, parent.panel_utama)
        self.parent = parent
        self.SetSize(parent.GetSize())

    def kembali_kel_ppOnButtonClick(self, event):
        self.parent.show_panel_dash()

    def persegi_panjang_keliling_hitung(self, event):
        p = float(self.input_panjang_kel.GetValue())
        l = float(self.input_lebar_luas.GetValue())
        self.result = 2 * (p + l)
        self.hasil_kel_pp.SetLabelText(str(self.result))


# Luas
class PL_PerPanjang(noname.l_PPanjang):
    def __init__(self, parent):
        noname.l_PPanjang.__init__(self, parent.panel_utama)
        self.parent = parent
        self.SetSize(parent.GetSize())

    def kem_lPP(self, event):
        self.parent.show_panel_dash()

    def persegi_panjang_luas_hitung(self, event):
        p = float(self.input_p_luas_pp.GetValue())
        l = float(self.input_l_luas_pp.GetValue())
        self.result = p * l
        self.hasil_luas_pp.SetLabelText(str(self.result))


# LINGKARAN
# Keliling
class PK_Lingkaran(noname.k_lingkaran):
    def __init__(self, parent):
        noname.k_lingkaran.__init__(self, parent.panel_utama)
        self.parent = parent
        self.result = float(self.hasil_kel_lingkaran.GetLabelText())
        self.SetSize(parent.GetSize())

    def kembali_kel_lingOnButtonClick(self, event):
        self.parent.show_panel_dash()

    def lingkaran_keliling_hitung(self, event):
        d = float(self.input_diameter.GetValue())
        self.result = 3.14 * d
        self.hasil_kel_lingkaran.SetLabelText(str(self.result))


# Luas
class PL_Lingkaran(noname.l_lingkaran):
    def __init__(self, parent):
        noname.l_lingkaran.__init__(self, parent.panel_utama)
        self.parent = parent
        self.result = float(self.hasil_luas_lingkaran.GetLabelText())
        self.SetSize(parent.GetSize())

    def kembali_luas_lingOnButtonClick(self, event):
        self.parent.show_panel_dash()

    def lingkaran_luas_hitung(self, event):
        r = float(self.input_jariluas.GetValue())
        self.result = 3.14 * r * r
        self.hasil_luas_lingkaran.SetLabelText(str(self.result))


# SEGITIGA
# Keliling
class PK_Segitiga(noname.k_segitiga):
    def __init__(self, parent):
        noname.k_segitiga.__init__(self, parent.panel_utama)
        self.parent = parent
        self.result = float(self.hasil_kel_seg.GetLabelText())
        self.SetSize(parent.GetSize())

    def kembali_kel_segOnButtonClick(self, event):
        self.parent.show_panel_dash()

    def segitiga_keliling_hitung(self, event):
        a = float(self.input_sisi_a.GetValue())
        b = float(self.input_sisi_b.GetValue())
        c = float(self.input_sisi_c.GetValue())
        self.result = a + b + c
        self.hasil_kel_seg.SetLabelText(str(self.result))


# Luas
class PL_Segitiga(noname.l_segitiga):
    def __init__(self, parent):
        noname.l_segitiga.__init__(self, parent.panel_utama)
        self.parent = parent
        self.result = float(self.hasil_luas_segitiga.GetLabelText())
        self.SetSize(parent.GetSize())

    def kem_segitiga_luas(self, event):
        self.parent.show_panel_dash()

    def segitiga_luas_hitung(self, event):
        a = float(self.input_al.GetValue())
        t = float(self.input_t.GetValue())
        self.result = (a * t) / 2
        self.hasil_luas_segitiga.SetLabelText(str(self.result))


# BELAH KETUPAT
# Keliling
class PK_Belah_Ketupat(noname.k_belah_ketupat):
    def __init__(self, parent):
        noname.k_belah_ketupat.__init__(self, parent.panel_utama)
        self.parent = parent
        self.result = float(self.hasil_kel_bel.GetLabelText())
        self.SetSize(parent.GetSize())

    def kembali_kel_bbOnButtonClick(self, event):
        self.parent.show_panel_dash()

    def bb_keliling_hitung(self, event):
        a1 = float(self.input_sisi_a2.GetValue())
        b1 = float(self.input_sisi_b2.GetValue())
        c1 = float(self.input_sisi_c2.GetValue())
        d1 = float(self.input_sisi_d2.GetValue())
        self.result = a1 + b1 + c1 + d1
        self.hasil_kel_bel.SetLabelText(str(self.result))


# Luas
class PL_Belah_Ketupat(noname.l_belah_ketupat):
    def __init__(self, parent):
        noname.l_belah_ketupat.__init__(self, parent.panel_utama)
        self.parent = parent
        self.result = float(self.hasil_luas_bb.GetLabelText())
        self.SetSize(parent.GetSize())

    def kem_bb(self, event):
        self.parent.show_panel_dash()

    def bb_luas_hitung(self, event):
        diagonalA = float(self.input_diagonal_bb.GetValue())
        diagonalB = float(self.input_diagonal_bb2.GetValue())
        self.result = (diagonalA * diagonalB) / 2
        self.hasil_luas_bb.SetLabelText(str(self.result))


# TRAPESIUM
class PK_Trapesium(noname.k_trapesium):
    def __init__(self, parent):
        noname.k_trapesium.__init__(self, parent.panel_utama)
        self.parent = parent
        self.result = float(self.hasil_kel_trape.GetLabelText())
        self.SetSize(parent.GetSize())


    def kembali_kel_trapeOnButtonClick(self, event):
        self.parent.show_panel_dash()

    def trape_keliling_hitung(self, event):
        a_b = float(self.input_sisi_ab.GetValue())
        b_c = float(self.input_sisi_bc.GetValue())
        c_d = float(self.input_sisi_cd.GetValue())
        a_d = float(self.input_sisi_ad.GetValue())
        self.result = a_b + b_c + c_d + a_d
        self.hasil_kel_trape.SetLabelText(str(self.result))


class PL_Trapesium(noname.l_trapesium):
    def __init__(self, parent):
        noname.l_trapesium.__init__(self, parent.panel_utama)
        self.parent = parent
        self.result = float(self.hasil_luas_trape.GetLabelText())
        self.SetSize(parent.GetSize())

    def kembali_luas_trapeOnButtonClick(self, event):
        self.parent.show_panel_dash()

    def trape_keliling_hitung(self, event):
        sA = float(self.input_sisi_a_trape.GetValue())
        sB = float(self.input_sisi_b_trape.GetValue())
        tG = float(self.input_tinggi_trape.GetValue())
        self.result = (sA + sB) * tG / 2
        self.hasil_luas_trape.SetLabelText(str(self.result))


# LAYANG - LAYANG
# Keliling
class PK_Layang(noname.k_layang):
    def __init__(self, parent):
        noname.k_layang.__init__(self, parent.panel_utama)
        self.parent = parent
        self.result = float(self.hasil_kel_layang.GetLabelText())
        self.SetSize(parent.GetSize())

    def kembali_kel_layangOnButtonClick(self, event):
        self.parent.show_panel_dash()

    def layang_keliling_hitung(self, event):
        ab = float(self.input_sisi_ab2.GetValue())
        bc = float(self.input_sisi_bc2.GetValue())
        cd = float(self.input_sisi_cd2.GetValue())
        da = float(self.input_sisi_ad2.GetValue())
        self.result = ab + bc + cd + da
        self.hasil_kel_layang.SetLabelText(str(self.result))


# Luas
class PL_Layang(noname.l_layang):
    def __init__(self, parent):
        noname.l_layang.__init__(self, parent.panel_utama)
        self.parent = parent
        self.result = float(self.hasil_luas_layang.GetLabelText())
        self.SetSize(parent.GetSize())

    def layang_luas_tom(self, event):
        self.parent.show_panel_dash()

    def layang_luas_hitung(self, event):
        diagonal1 = float(self.input_digA_luas_layang.GetValue())
        diagonal2 = float(self.input_digb_luas_layang.GetValue())
        self.result = (diagonal1 * diagonal2) / 2
        self.hasil_luas_layang.SetLabelText(str(self.result))


# JAJAR GENJANG
# Keliling
class PK_Jajar(noname.k_jajar):
    def __init__(self, parent):
        noname.k_jajar.__init__(self, parent.panel_utama)
        self.parent = parent
        self.result = float(self.hasil_kel_Gj.GetLabelText())
        self.SetSize(parent.GetSize())

    def kembali_kel_gjOnButtonClick(self, event):
        self.parent.show_panel_dash()

    def gj_keliling_hitung(self, event):
        alas = float(self.input_sisi_alasGJ.GetValue())
        sisiM = float(self.input_sisi_miringGJ.GetValue())
        self.result = 2 * (alas + sisiM)
        self.hasil_kel_Gj.SetLabelText(str(self.result))


# Luas
class PL_Jajar(noname.l_jajar):
    def __init__(self, parent):
        noname.l_jajar.__init__(self, parent.panel_utama)
        self.parent = parent
        self.result = float(self.hasil_luas_jg.GetLabelText())
        self.SetSize(parent.GetSize())

    def kem_jg_luas(self, event):
        self.parent.show_panel_dash()

    def jg_luas_hitung(self, event):
        ajg = float(self.input_p_jg.GetValue())
        tjg = float(self.input_t_jg.GetValue())
        self.result = ajg * tjg
        self.hasil_luas_jg.SetLabelText(str(self.result))


# BANGUN RUANG --------------------------------------------------
# KUBUS
# Luas Permukaan
class LPer_Kubus(noname.LP_kubus):
    def __init__(self, parent):
        noname.LP_kubus.__init__(self, parent.panel_utama)
        self.parent = parent
        self.result = float(self.hasil_luasPermukaanKubus.GetLabelText())
        self.SetSize(parent.GetSize())

    def kembali_luasPer_kubusOnButtonClick(self, event):
        self.parent.show_panel_dash()

    def kubus_lPermukaan_hitung(self, event):
        rusukL = float(self.input_rusuk.GetValue())
        self.result = 6 * rusukL * rusukL
        self.hasil_luasPermukaanKubus.SetLabelText(str(self.result))


# Volume
class Vol_Kubus(noname.V_kubus):
    def __init__(self, parent):
        noname.V_kubus.__init__(self, parent.panel_utama)
        self.parent = parent
        self.result = float(self.hasil_volumeKubus.GetLabelText())
        self.SetSize(parent.GetSize())

    def kembali_volume_kubusOnButtonClick(self, event):
        self.parent.show_panel_dash()

    def kubus_volume_hitung(self, event):
        rusukK = float(self.input_rusuk_volume.GetValue())
        self.result = rusukK * rusukK * rusukK
        self.hasil_volumeKubus.SetLabelText(str(self.result))


# BALOK
# Luas Permukaan
class LPer_Balok(noname.LP_balok):
    def __init__(self, parent):
        noname.LP_balok.__init__(self, parent.panel_utama)
        self.parent = parent
        self.result = float(self.hasil_luasPermukaanBalok.GetLabelText())
        self.SetSize(parent.GetSize())

    def kembali_luasPer_balokOnButtonClick(self, event):
        self.parent.show_panel_dash()

    def balok_lPermukaan_hitung(self, event):
        pB = float(self.input_panjang_balok.GetValue())
        lB = float(self.input_lebar_balok.GetValue())
        tB = float(self.input_tinggi_balok.GetValue())
        self.result = 2 * ((pB * lB) + (lB * tB) + (tB * pB))
        self.hasil_luasPermukaanBalok.SetLabelText(str(self.result))


# Volume
class Vol_Balok(noname.V_balok):
    def __init__(self, parent):
        noname.V_balok.__init__(self, parent.panel_utama)
        self.parent = parent
        self.result = float(self.hasil_volumeBalok.GetLabelText())
        self.SetSize(parent.GetSize())

    def kembali_volume_balokOnButtonClick(self, event):
        self.parent.show_panel_dash()

    def balok_volume_hitung(self, event):
        pB = float(self.input_panjang_balok1.GetValue())
        lB = float(self.input_lebar_balok1.GetValue())
        tB = float(self.input_tinggi_balok1.GetValue())
        self.result = pB * lB * tB
        self.hasil_volumeBalok.SetLabelText(str(self.result))


# PRISMA SEGITIGA
# Luas Permukaan
class LPer_PriTiga(noname.LP_PSeg):
    def __init__(self, parent):
        noname.LP_PSeg.__init__(self, parent.panel_utama)
        self.parent = parent
        self.result = float(self.hasil_luasPermukaanPSegitiga.GetLabelText())
        self.SetSize(parent.GetSize())

    def kembali_luasPer_balokOnButtonClick(self, event):
        self.parent.show_panel_dash()

    def pSegitiga_lPermukaan_hitung(self, event):
        a = float(self.input_alas_prisma.GetValue())
        tA = float(self.input_tinggi_alas.GetValue())
        tP = float(self.input_tinggi_prisma.GetValue())
        bC = float(self.input_sisiBC.GetValue())
        aC = float(self.input_sisiAC.GetValue())
        self.result = (a * tA) + (a + bC + aC)
        self.hasil_luasPermukaanPSegitiga.SetLabelText(str(self.result))


# Volume
class Vol_PriTiga(noname.V_PSeg):
    def __init__(self, parent):
        noname.V_PSeg.__init__(self, parent.panel_utama)
        self.parent = parent
        self.result = float(self.hasil_volumePSegitiga.GetLabelText())
        self.SetSize(parent.GetSize())

    def kembali_volume_pSegitigaOnButtonClick(self, event):
        self.parent.show_panel_dash()

    def pSegitiga_volume_hitung(self, event):
        aPT = float(self.input_alas_pSegitiga.GetValue())
        taPT = float(self.input_tinggi_alas_pSegitiga.GetValue())
        tPT = float(self.input_tinggi_pSegitiga.GetValue())
        self.result = aPT * taPT * tPT / 2
        self.hasil_volumePSegitiga.SetLabelText(str(self.result))


# PRISMA SEGIEMPAT
# Luas Permukaan
class LPer_PriEmpat(noname.LP_PEmpat):
    def __init__(self, parent):
        noname.LP_PEmpat.__init__(self, parent.panel_utama)
        self.parent = parent
        self.result = float(self.hasil_LPSegiempat.GetLabelText())
        self.SetSize(parent.GetSize())

    def kembali_luasPer_pSegiempatOnButtonClick(self, event):
        self.parent.show_panel_dash()

    def pSegiempat_lpermukaan(self, event):
        pJ = float(self.input_panjang_pS.GetValue())
        lJ = float(self.input_lebar_pS.GetValue())
        tJ = float(self.input_tinggi_pS.GetValue())
        self.result = 2 * (pJ + lJ) + 2 * pJ * lJ * tJ
        self.hasil_LPSegiempat.SetLabelText(str(self.result))


# Volume
class Vol_PriEmpat(noname.V_PEmpat):
    def __init__(self, parent):
        noname.V_PEmpat.__init__(self, parent.panel_utama)
        self.parent = parent
        self.result = float(self.hasil_volumepSegiempat.GetLabelText())
        self.SetSize(parent.GetSize())

    def kembali_volume_pSegiempatOnButtonClick(self, event):
        self.parent.show_panel_dash()

    def pSegiempat_volume_hitung(self, event):
        pP = float(self.input_panjang4_pSegiempat.GetValue())
        lP = float(self.input_lebar4_pSegiempat.GetValue())
        tP = float(self.input_tinggi4_pSegiempat.GetValue())
        self.result = pP * lP * tP
        self.hasil_volumepSegiempat.SetLabelText(str(self.result))


# KERUCUT
# Luas Permukaan
class LPer_Kerucut(noname.LP_Kerucut):
    def __init__(self, parent):
        noname.LP_Kerucut.__init__(self, parent.panel_utama)
        self.parent = parent
        self.result = float(self.hasil_luasPermukaanKerucut.GetLabelText())
        self.SetSize(parent.GetSize())

    def kembali_luasPer_KerucutOnButtonClick(self, event):
        self.parent.show_panel_dash()

    def lpermukaan_kerucut_hitung(self, event):
        rLK = float(self.input_jari_kerucut.GetValue())
        sK = float(self.input_s_kerucut.GetValue())
        self.result = 3.14 * rLK * (sK + rLK)
        self.hasil_luasPermukaanKerucut.SetLabelText(str(self.result))


# Volume
class Vol_Kerucut(noname.V_Kerucut):
    def __init__(self, parent):
        noname.V_Kerucut.__init__(self, parent.panel_utama)
        self.parent = parent
        self.result = float(self.hasil_volumeKerucut.GetLabelText())
        self.SetSize(parent.GetSize())

    def kembali_volume_kerucutOnButtonClick(self, event):
        self.parent.show_panel_dash()

    def kerucut_volume_hitung(self, event):
        rK = float(self.input_jari_kerucut.GetValue())
        tK = float(self.input_tinggi_kerucut.GetValue())
        self.result = 2.14 * rK * rK * tK / 3
        self.hasil_volumeKerucut.SetLabelText(str(self.result))


# BOLA
# Luas Permukaan
class LPer_Bola(noname.LP_Bola):
    def __init__(self, parent):
        noname.LP_Bola.__init__(self, parent.panel_utama)
        self.parent = parent
        self.result = float(self.hasil_luasPermukaanBola.GetLabelText())
        self.SetSize(parent.GetSize())

    def kembali_luasPer_BolaOnButtonClick(self, event):
        self.parent.show_panel_dash()

    def lpermukaan_bola_hitung(self, event):
        rBola = float(self.input_jari_bola.GetValue())
        self.result = 4 * 3.14 * rBola * rBola
        self.hasil_luasPermukaanBola.SetLabelText(str(self.result))


# Volume
class Vol_Bola(noname.V_Bola):
    def __init__(self, parent):
        noname.V_Bola.__init__(self, parent.panel_utama)
        self.parent = parent
        self.result = float(self.hasil_volumeBola.GetLabelText())
        self.SetSize(parent.GetSize())

    def kembali_volume_BolaOnButtonClick(self, event):
        self.parent.show_panel_dash()

    def bola_volume_hitung(self, event):
        rusukB = float(self.input_jari_bola_2.GetValue())
        self.result = 4 * 3.14 * rusukB * rusukB * rusukB / 3
        self.hasil_volumeBola.SetLabelText(str(self.result))


# LIMAS SEGIEMPAT
# Luas Permukaan
class LPer_LEmpat(noname.LP_LEmpat):
    def __init__(self, parent):
        noname.LP_LEmpat.__init__(self, parent.panel_utama)
        self.parent = parent
        self.result = float(self.hasil_LPSegiempat.GetLabelText())
        self.SetSize(parent.GetSize())

    def kembali_luasPer_LSegiempatOnButtonClick(self, event):
        self.parent.show_panel_dash()

    def lpermukaan_LSegiempat_hitung(self, event):
        aLS = float(self.input_alas_lSegiempat.GetValue())
        tLS = float(self.input_tinggi_lSegiempat.GetValue())
        sLS = float(self.input_sisi_lSegiempat.GetValue())
        self.result = (aLS * tLS * sLS) / 3
        self.hasil_LPSegiempat.SetLabelText(str(self.result))


# Volume
class Vol_LEmpat(noname.V_LEmpat):
    def __init__(self, parent):
        noname.V_LEmpat.__init__(self, parent.panel_utama)
        self.parent = parent
        self.result = float(self.hasil_volumeLsegiempat.GetLabelText())
        self.SetSize(parent.GetSize())

    def kembali_volume_LSegiempatOnButtonClick(self, event):
        self.parent.show_panel_dash()

    def lSegiempat_volume_hitung(self, event):
        sL = float(self.input_sisi_LSegiempat.GetValue())
        tL = float(self.input_tinggi_limas_lSegiempat.GetValue())
        self.result = sL * tL / 3
        self.hasil_volumeLsegiempat.SetLabelText(str(self.result))


# TABUNG
# Luas Permukaan
class LPer_Tabung(noname.LP_Tabung):
    def __init__(self, parent):
        noname.LP_Tabung.__init__(self, parent.panel_utama)
        self.parent = parent
        self.result = float(self.hasil_luasPermukaanTabung.GetLabelText())
        self.SetSize(parent.GetSize())

    def kembali_luasPer_TabungOnButtonClick(self, event):
        self.parent.show_panel_dash()

    def lpermukaan_tabung_hitung(self, event):
        rT = float(self.input_jari_tabung.GetValue())
        tT = float(self.input_tinggi_tabung.GetValue())
        self.result = 2 * 3.14 * rT * (rT + tT)
        self.hasil_luasPermukaanTabung.SetLabelText(str(self.result))


# Volume
class Vol_Tabung(noname.V_Tabung):
    def __init__(self, parent):
        noname.V_Tabung.__init__(self, parent.panel_utama)
        self.parent = parent
        self.result = float(self.hasil_volumeTabung.GetLabelText())
        self.SetSize(parent.GetSize())

    def kembali_volume_TabungOnButtonClick(self, event):
        self.parent.show_panel_dash()

    def volume_tabung_hitung(self, event):
        rT = float(self.input_jari_tabung2.GetValue())
        tT = float(self.input_tinggi_tabung2.GetValue())
        self.result = 3.14 * rT * rT * tT
        self.hasil_volumeTabung.SetLabelText(str(self.result))


class frame_utama(noname.frame_tugas):
    def __init__(self, parent):
        noname.frame_tugas.__init__(self, parent)
        self.temp_dash = PDashbord(self)
        self.temp_login = PLogin(self)
        self.temp_KPersegi = PK_Persegi(self)
        self.temp_LPersegi = PL_Persegi(self)
        self.temp_KPerPanjang = PK_PerPanjang(self)
        self.temp_LPerPanjang = PL_PerPanjang(self)
        self.temp_KLingkaran = PK_Lingkaran(self)
        self.temp_LLingkaran = PL_Lingkaran(self)
        self.temp_KSegitiga = PK_Segitiga(self)
        self.temp_LSegitiga = PL_Segitiga(self)
        self.temp_KBB = PK_Belah_Ketupat(self)
        self.temp_LBB = PL_Belah_Ketupat(self)
        self.temp_KTrapesium = PK_Trapesium(self)
        self.temp_LTrapesium = PL_Trapesium(self)
        self.temp_KLayang = PK_Layang(self)
        self.temp_LLayang = PL_Layang(self)
        self.temp_KJajar = PK_Jajar(self)
        self.temp_LJajar = PL_Jajar(self)
        self.temp_LPKubus = LPer_Kubus(self)
        self.temp_VKubus = Vol_Kubus(self)
        self.temp_LPBalok = LPer_Balok(self)
        self.temp_VBalok = Vol_Balok(self)
        self.temp_LPPriTiga = LPer_PriTiga(self)
        self.temp_VPriTiga = Vol_PriTiga(self)
        self.temp_LPPriEmpat = LPer_PriEmpat(self)
        self.temp_VPriEmpat = Vol_PriEmpat(self)
        self.temp_LPKerucut = LPer_Kerucut(self)
        self.temp_VKerucut = Vol_Kerucut(self)
        self.temp_LPBola = LPer_Bola(self)
        self.temp_VBola = Vol_Bola(self)
        self.temp_LLEmpat = LPer_LEmpat(self)
        self.temp_VLEmpat = Vol_LEmpat(self)
        self.temp_LPTabung = LPer_Tabung(self)
        self.temp_VTabung = Vol_Tabung(self)
        self.temp_K_Datar = K_Bangun_Datar(self)
        self.temp_K_Ruang = K_Bangun_Ruang(self)
        self.temp_S_Datar = S_Bangun_Datar(self)
        self.temp_S_Ruang = S_Bangun_Ruang(self)
        self.temp_e_catatan = tampilan_Catatan(self)
        self.show_panel_login()

    def login_frameSize( self, event ):
        self.temp_dash.SetSize(self.GetSize())
        self.temp_login.SetSize(self.GetSize())
        self.temp_KPersegi.SetSize(self.GetSize())
        self.temp_LPersegi.SetSize(self.GetSize())
        self.temp_KPerPanjang.SetSize(self.GetSize())
        self.temp_LPerPanjang.SetSize(self.GetSize())
        self.temp_KLingkaran.SetSize(self.GetSize())
        self.temp_LLingkaran.SetSize(self.GetSize())
        self.temp_KSegitiga.SetSize(self.GetSize())
        self.temp_LSegitiga.SetSize(self.GetSize())
        self.temp_KBB.SetSize(self.GetSize())
        self.temp_LBB.SetSize(self.GetSize())
        self.temp_KTrapesium.SetSize(self.GetSize())
        self.temp_LTrapesium.SetSize(self.GetSize())
        self.temp_KLayang.SetSize(self.GetSize())
        self.temp_LLayang.SetSize(self.GetSize())
        self.temp_KJajar.SetSize(self.GetSize())
        self.temp_LJajar.SetSize(self.GetSize())
        self.temp_LPKubus.SetSize(self.GetSize())
        self.temp_VKubus.SetSize(self.GetSize())
        self.temp_LPBalok.SetSize(self.GetSize())
        self.temp_VBalok.SetSize(self.GetSize())
        self.temp_LPPriTiga.SetSize(self.GetSize())
        self.temp_VPriTiga.SetSize(self.GetSize())
        self.temp_LPPriEmpat.SetSize(self.GetSize())
        self.temp_VPriEmpat.SetSize(self.GetSize())
        self.temp_LPKerucut.SetSize(self.GetSize())
        self.temp_VKerucut.SetSize(self.GetSize())
        self.temp_LPBola.SetSize(self.GetSize())
        self.temp_VBola.SetSize(self.GetSize())
        self.temp_LLEmpat.SetSize(self.GetSize())
        self.temp_VLEmpat.SetSize(self.GetSize())
        self.temp_LPTabung.SetSize(self.GetSize())
        self.temp_VTabung.SetSize(self.GetSize())
        self.temp_K_Datar.SetSize(self.GetSize())
        self.temp_K_Ruang.SetSize(self.GetSize())
        self.temp_S_Datar.SetSize(self.GetSize())
        self.temp_S_Ruang.SetSize(self.GetSize())

    def show_panel_catatan(self):
        self.temp_e_catatan.Show()
        self.temp_login.Hide()
        self.temp_S_Datar.Hide()
        self.temp_S_Ruang.Hide()
        self.temp_K_Datar.Hide()
        self.temp_K_Ruang.Hide()
        self.temp_VTabung.Hide()
        self.temp_LPTabung.Hide()
        self.temp_VLEmpat.Hide()
        self.temp_LLEmpat.Hide()
        self.temp_VBola.Hide()
        self.temp_LPBola.Hide()
        self.temp_VKerucut.Hide()
        self.temp_LPKerucut.Hide()
        self.temp_VPriEmpat.Hide()
        self.temp_LPPriEmpat.Hide()
        self.temp_VPriTiga.Hide()
        self.temp_LPPriTiga.Hide()
        self.temp_VBalok.Hide()
        self.temp_LPBalok.Hide()
        self.temp_VKubus.Hide()
        self.temp_LPKubus.Hide()
        self.temp_LJajar.Hide()
        self.temp_KJajar.Hide()
        self.temp_LLayang.Hide()
        self.temp_KLayang.Hide()
        self.temp_LTrapesium.Hide()
        self.temp_KTrapesium.Hide()
        self.temp_LBB.Hide()
        self.temp_KBB.Hide()
        self.temp_KSegitiga.Hide()
        self.temp_LSegitiga.Hide()
        self.temp_LLingkaran.Hide()
        self.temp_KLingkaran.Hide()
        self.temp_LPerPanjang.Hide()
        self.temp_KPerPanjang.Hide()
        self.temp_LPersegi.Hide()
        self.temp_KPersegi.Hide()
        self.temp_dash.Hide()

    def show_panel_login(self):
        self.temp_login.Show()
        self.temp_e_catatan.Hide()
        self.temp_S_Datar.Hide()
        self.temp_S_Ruang.Hide()
        self.temp_K_Datar.Hide()
        self.temp_K_Ruang.Hide()
        self.temp_VTabung.Hide()
        self.temp_LPTabung.Hide()
        self.temp_VLEmpat.Hide()
        self.temp_LLEmpat.Hide()
        self.temp_VBola.Hide()
        self.temp_LPBola.Hide()
        self.temp_VKerucut.Hide()
        self.temp_LPKerucut.Hide()
        self.temp_VPriEmpat.Hide()
        self.temp_LPPriEmpat.Hide()
        self.temp_VPriTiga.Hide()
        self.temp_LPPriTiga.Hide()
        self.temp_VBalok.Hide()
        self.temp_LPBalok.Hide()
        self.temp_VKubus.Hide()
        self.temp_LPKubus.Hide()
        self.temp_LJajar.Hide()
        self.temp_KJajar.Hide()
        self.temp_LLayang.Hide()
        self.temp_KLayang.Hide()
        self.temp_LTrapesium.Hide()
        self.temp_KTrapesium.Hide()
        self.temp_LBB.Hide()
        self.temp_KBB.Hide()
        self.temp_KSegitiga.Hide()
        self.temp_LSegitiga.Hide()
        self.temp_LLingkaran.Hide()
        self.temp_KLingkaran.Hide()
        self.temp_LPerPanjang.Hide()
        self.temp_KPerPanjang.Hide()
        self.temp_LPersegi.Hide()
        self.temp_KPersegi.Hide()
        self.temp_dash.Hide()

    def show_panel_dash(self):
        self.temp_dash.Show()
        self.temp_e_catatan.Hide()
        self.temp_S_Datar.Hide()
        self.temp_S_Ruang.Hide()
        self.temp_K_Datar.Hide()
        self.temp_K_Ruang.Hide()
        self.temp_VTabung.Hide()
        self.temp_LPTabung.Hide()
        self.temp_VLEmpat.Hide()
        self.temp_LLEmpat.Hide()
        self.temp_VBola.Hide()
        self.temp_LPBola.Hide()
        self.temp_VKerucut.Hide()
        self.temp_LPKerucut.Hide()
        self.temp_VPriEmpat.Hide()
        self.temp_LPPriEmpat.Hide()
        self.temp_VPriTiga.Hide()
        self.temp_LPPriTiga.Hide()
        self.temp_VBalok.Hide()
        self.temp_LPBalok.Hide()
        self.temp_VKubus.Hide()
        self.temp_LPKubus.Hide()
        self.temp_LJajar.Hide()
        self.temp_KJajar.Hide()
        self.temp_LLayang.Hide()
        self.temp_KLayang.Hide()
        self.temp_LTrapesium.Hide()
        self.temp_KTrapesium.Hide()
        self.temp_LBB.Hide()
        self.temp_KBB.Hide()
        self.temp_KSegitiga.Hide()
        self.temp_LSegitiga.Hide()
        self.temp_LLingkaran.Hide()
        self.temp_KLingkaran.Hide()
        self.temp_LPerPanjang.Hide()
        self.temp_KPerPanjang.Hide()
        self.temp_LPersegi.Hide()
        self.temp_KPersegi.Hide()
        self.temp_login.Hide()

    def show_panel_spesi_datar(self):
        self.temp_S_Datar.Show()
        self.temp_e_catatan.Hide()
        self.temp_S_Ruang.Hide()
        self.temp_K_Datar.Hide()
        self.temp_K_Ruang.Hide()
        self.temp_VTabung.Hide()
        self.temp_LPTabung.Hide()
        self.temp_VLEmpat.Hide()
        self.temp_LLEmpat.Hide()
        self.temp_VBola.Hide()
        self.temp_LPBola.Hide()
        self.temp_VKerucut.Hide()
        self.temp_LPKerucut.Hide()
        self.temp_VPriEmpat.Hide()
        self.temp_LPPriEmpat.Hide()
        self.temp_VPriTiga.Hide()
        self.temp_LPPriTiga.Hide()
        self.temp_VBalok.Hide()
        self.temp_LPBalok.Hide()
        self.temp_VKubus.Hide()
        self.temp_LPKubus.Hide()
        self.temp_LJajar.Hide()
        self.temp_KJajar.Hide()
        self.temp_LLayang.Hide()
        self.temp_KLayang.Hide()
        self.temp_LTrapesium.Hide()
        self.temp_KTrapesium.Hide()
        self.temp_LBB.Hide()
        self.temp_KBB.Hide()
        self.temp_KSegitiga.Hide()
        self.temp_LSegitiga.Hide()
        self.temp_LLingkaran.Hide()
        self.temp_KLingkaran.Hide()
        self.temp_LPerPanjang.Hide()
        self.temp_KPerPanjang.Hide()
        self.temp_LPersegi.Hide()
        self.temp_KPersegi.Hide()
        self.temp_dash.Hide()
        self.temp_login.Hide()

    def show_panel_spesi_ruang(self):
        self.temp_S_Datar.Hide()
        self.temp_e_catatan.Hide()
        self.temp_S_Ruang.Show()
        self.temp_K_Datar.Hide()
        self.temp_K_Ruang.Hide()
        self.temp_VTabung.Hide()
        self.temp_LPTabung.Hide()
        self.temp_VLEmpat.Hide()
        self.temp_LLEmpat.Hide()
        self.temp_VBola.Hide()
        self.temp_LPBola.Hide()
        self.temp_VKerucut.Hide()
        self.temp_LPKerucut.Hide()
        self.temp_VPriEmpat.Hide()
        self.temp_LPPriEmpat.Hide()
        self.temp_VPriTiga.Hide()
        self.temp_LPPriTiga.Hide()
        self.temp_VBalok.Hide()
        self.temp_LPBalok.Hide()
        self.temp_VKubus.Hide()
        self.temp_LPKubus.Hide()
        self.temp_LJajar.Hide()
        self.temp_KJajar.Hide()
        self.temp_LLayang.Hide()
        self.temp_KLayang.Hide()
        self.temp_LTrapesium.Hide()
        self.temp_KTrapesium.Hide()
        self.temp_LBB.Hide()
        self.temp_KBB.Hide()
        self.temp_KSegitiga.Hide()
        self.temp_LSegitiga.Hide()
        self.temp_LLingkaran.Hide()
        self.temp_KLingkaran.Hide()
        self.temp_LPerPanjang.Hide()
        self.temp_KPerPanjang.Hide()
        self.temp_LPersegi.Hide()
        self.temp_KPersegi.Hide()
        self.temp_dash.Hide()
        self.temp_login.Hide()

    def show_panel_katalog_ruang(self):
        self.temp_K_Datar.Hide()
        self.temp_e_catatan.Hide()
        self.temp_S_Datar.Hide()
        self.temp_S_Ruang.Hide()
        self.temp_K_Ruang.Show()
        self.temp_VTabung.Hide()
        self.temp_LPTabung.Hide()
        self.temp_VLEmpat.Hide()
        self.temp_LLEmpat.Hide()
        self.temp_VBola.Hide()
        self.temp_LPBola.Hide()
        self.temp_VKerucut.Hide()
        self.temp_LPKerucut.Hide()
        self.temp_VPriEmpat.Hide()
        self.temp_LPPriEmpat.Hide()
        self.temp_VPriTiga.Hide()
        self.temp_LPPriTiga.Hide()
        self.temp_VBalok.Hide()
        self.temp_LPBalok.Hide()
        self.temp_VKubus.Hide()
        self.temp_LPKubus.Hide()
        self.temp_LJajar.Hide()
        self.temp_KJajar.Hide()
        self.temp_LLayang.Hide()
        self.temp_KLayang.Hide()
        self.temp_LTrapesium.Hide()
        self.temp_KTrapesium.Hide()
        self.temp_LBB.Hide()
        self.temp_KBB.Hide()
        self.temp_KSegitiga.Hide()
        self.temp_LSegitiga.Hide()
        self.temp_LLingkaran.Hide()
        self.temp_KLingkaran.Hide()
        self.temp_LPerPanjang.Hide()
        self.temp_KPerPanjang.Hide()
        self.temp_LPersegi.Hide()
        self.temp_KPersegi.Hide()
        self.temp_dash.Hide()
        self.temp_login.Hide()

    def show_panel_katalog_datar(self):
        self.temp_K_Datar.Show()
        self.temp_e_catatan.Hide()
        self.temp_S_Datar.Hide()
        self.temp_S_Ruang.Hide()
        self.temp_K_Ruang.Hide()
        self.temp_VTabung.Hide()
        self.temp_LPTabung.Hide()
        self.temp_VLEmpat.Hide()
        self.temp_LLEmpat.Hide()
        self.temp_VBola.Hide()
        self.temp_LPBola.Hide()
        self.temp_VKerucut.Hide()
        self.temp_LPKerucut.Hide()
        self.temp_VPriEmpat.Hide()
        self.temp_LPPriEmpat.Hide()
        self.temp_VPriTiga.Hide()
        self.temp_LPPriTiga.Hide()
        self.temp_VBalok.Hide()
        self.temp_LPBalok.Hide()
        self.temp_VKubus.Hide()
        self.temp_LPKubus.Hide()
        self.temp_LJajar.Hide()
        self.temp_KJajar.Hide()
        self.temp_LLayang.Hide()
        self.temp_KLayang.Hide()
        self.temp_LTrapesium.Hide()
        self.temp_KTrapesium.Hide()
        self.temp_LBB.Hide()
        self.temp_KBB.Hide()
        self.temp_KSegitiga.Hide()
        self.temp_LSegitiga.Hide()
        self.temp_LLingkaran.Hide()
        self.temp_KLingkaran.Hide()
        self.temp_LPerPanjang.Hide()
        self.temp_KPerPanjang.Hide()
        self.temp_LPersegi.Hide()
        self.temp_KPersegi.Hide()
        self.temp_dash.Hide()
        self.temp_login.Hide()

    def show_panel_KPer(self):
        self.temp_KPersegi.Show()
        self.temp_e_catatan.Hide()
        self.temp_S_Datar.Hide()
        self.temp_S_Ruang.Hide()
        self.temp_K_Datar.Hide()
        self.temp_K_Ruang.Hide()
        self.temp_VTabung.Hide()
        self.temp_LPTabung.Hide()
        self.temp_VLEmpat.Hide()
        self.temp_LLEmpat.Hide()
        self.temp_VBola.Hide()
        self.temp_LPBola.Hide()
        self.temp_VKerucut.Hide()
        self.temp_LPKerucut.Hide()
        self.temp_VPriEmpat.Hide()
        self.temp_LPPriEmpat.Hide()
        self.temp_VPriTiga.Hide()
        self.temp_LPPriTiga.Hide()
        self.temp_VBalok.Hide()
        self.temp_LPBalok.Hide()
        self.temp_VKubus.Hide()
        self.temp_LPKubus.Hide()
        self.temp_LJajar.Hide()
        self.temp_KJajar.Hide()
        self.temp_LLayang.Hide()
        self.temp_KLayang.Hide()
        self.temp_LTrapesium.Hide()
        self.temp_KTrapesium.Hide()
        self.temp_LBB.Hide()
        self.temp_KBB.Hide()
        self.temp_KSegitiga.Hide()
        self.temp_LSegitiga.Hide()
        self.temp_LLingkaran.Hide()
        self.temp_KLingkaran.Hide()
        self.temp_LPerPanjang.Hide()
        self.temp_KPerPanjang.Hide()
        self.temp_LPersegi.Hide()
        self.temp_login.Hide()
        self.temp_dash.Hide()

    def show_panel_LPer(self):
        self.temp_LPersegi.Show()
        self.temp_e_catatan.Hide()
        self.temp_S_Datar.Hide()
        self.temp_S_Ruang.Hide()
        self.temp_K_Datar.Hide()
        self.temp_K_Ruang.Hide()
        self.temp_VTabung.Hide()
        self.temp_LPTabung.Hide()
        self.temp_VLEmpat.Hide()
        self.temp_LLEmpat.Hide()
        self.temp_VBola.Hide()
        self.temp_LPBola.Hide()
        self.temp_VKerucut.Hide()
        self.temp_LPKerucut.Hide()
        self.temp_VPriEmpat.Hide()
        self.temp_LPPriEmpat.Hide()
        self.temp_VPriTiga.Hide()
        self.temp_LPPriTiga.Hide()
        self.temp_VBalok.Hide()
        self.temp_LPBalok.Hide()
        self.temp_VKubus.Hide()
        self.temp_LPKubus.Hide()
        self.temp_LJajar.Hide()
        self.temp_KJajar.Hide()
        self.temp_LLayang.Hide()
        self.temp_KLayang.Hide()
        self.temp_LTrapesium.Hide()
        self.temp_KTrapesium.Hide()
        self.temp_LBB.Hide()
        self.temp_KBB.Hide()
        self.temp_KSegitiga.Hide()
        self.temp_LSegitiga.Hide()
        self.temp_LLingkaran.Hide()
        self.temp_KLingkaran.Hide()
        self.temp_LPerPanjang.Hide()
        self.temp_KPerPanjang.Hide()
        self.temp_KPersegi.Hide()
        self.temp_login.Hide()
        self.temp_dash.Hide()

    def show_panel_KPerPanjang(self):
        self.temp_KPerPanjang.Show()
        self.temp_e_catatan.Hide()
        self.temp_S_Datar.Hide()
        self.temp_S_Ruang.Hide()
        self.temp_K_Datar.Hide()
        self.temp_K_Ruang.Hide()
        self.temp_VTabung.Hide()
        self.temp_LPTabung.Hide()
        self.temp_VLEmpat.Hide()
        self.temp_LLEmpat.Hide()
        self.temp_VBola.Hide()
        self.temp_LPBola.Hide()
        self.temp_VKerucut.Hide()
        self.temp_LPKerucut.Hide()
        self.temp_VPriEmpat.Hide()
        self.temp_LPPriEmpat.Hide()
        self.temp_VPriTiga.Hide()
        self.temp_LPPriTiga.Hide()
        self.temp_VBalok.Hide()
        self.temp_LPBalok.Hide()
        self.temp_VKubus.Hide()
        self.temp_LPKubus.Hide()
        self.temp_LJajar.Hide()
        self.temp_KJajar.Hide()
        self.temp_LLayang.Hide()
        self.temp_KLayang.Hide()
        self.temp_LTrapesium.Hide()
        self.temp_KTrapesium.Hide()
        self.temp_LBB.Hide()
        self.temp_KBB.Hide()
        self.temp_KSegitiga.Hide()
        self.temp_LSegitiga.Hide()
        self.temp_LLingkaran.Hide()
        self.temp_KLingkaran.Hide()
        self.temp_LPerPanjang.Hide()
        self.temp_LPersegi.Hide()
        self.temp_KPersegi.Hide()
        self.temp_login.Hide()
        self.temp_dash.Hide()

    def show_panel_LPerPanjang(self):
        self.temp_LPerPanjang.Show()
        self.temp_e_catatan.Hide()
        self.temp_S_Datar.Hide()
        self.temp_S_Ruang.Hide()
        self.temp_K_Datar.Hide()
        self.temp_K_Ruang.Hide()
        self.temp_VTabung.Hide()
        self.temp_LPTabung.Hide()
        self.temp_VLEmpat.Hide()
        self.temp_LLEmpat.Hide()
        self.temp_VBola.Hide()
        self.temp_LPBola.Hide()
        self.temp_VKerucut.Hide()
        self.temp_LPKerucut.Hide()
        self.temp_VPriEmpat.Hide()
        self.temp_LPPriEmpat.Hide()
        self.temp_VPriTiga.Hide()
        self.temp_LPPriTiga.Hide()
        self.temp_VBalok.Hide()
        self.temp_LPBalok.Hide()
        self.temp_VKubus.Hide()
        self.temp_LPKubus.Hide()
        self.temp_LJajar.Hide()
        self.temp_KJajar.Hide()
        self.temp_LLayang.Hide()
        self.temp_KLayang.Hide()
        self.temp_LTrapesium.Hide()
        self.temp_KTrapesium.Hide()
        self.temp_LBB.Hide()
        self.temp_KBB.Hide()
        self.temp_KSegitiga.Hide()
        self.temp_LSegitiga.Hide()
        self.temp_LLingkaran.Hide()
        self.temp_KLingkaran.Hide()
        self.temp_KPerPanjang.Hide()
        self.temp_LPersegi.Hide()
        self.temp_KPersegi.Hide()
        self.temp_login.Hide()
        self.temp_dash.Hide()

    def show_panel_KLingkaran(self):
        self.temp_KLingkaran.Show()
        self.temp_e_catatan.Hide()
        self.temp_S_Datar.Hide()
        self.temp_S_Ruang.Hide()
        self.temp_K_Datar.Hide()
        self.temp_K_Ruang.Hide()
        self.temp_VTabung.Hide()
        self.temp_LPTabung.Hide()
        self.temp_VLEmpat.Hide()
        self.temp_LLEmpat.Hide()
        self.temp_VBola.Hide()
        self.temp_LPBola.Hide()
        self.temp_VKerucut.Hide()
        self.temp_LPKerucut.Hide()
        self.temp_VPriEmpat.Hide()
        self.temp_LPPriEmpat.Hide()
        self.temp_VPriTiga.Hide()
        self.temp_LPPriTiga.Hide()
        self.temp_VBalok.Hide()
        self.temp_LPBalok.Hide()
        self.temp_VKubus.Hide()
        self.temp_LPKubus.Hide()
        self.temp_LJajar.Hide()
        self.temp_KJajar.Hide()
        self.temp_LLayang.Hide()
        self.temp_KLayang.Hide()
        self.temp_LTrapesium.Hide()
        self.temp_KTrapesium.Hide()
        self.temp_LBB.Hide()
        self.temp_KBB.Hide()
        self.temp_KSegitiga.Hide()
        self.temp_LSegitiga.Hide()
        self.temp_LLingkaran.Hide()
        self.temp_LPerPanjang.Hide()
        self.temp_KPerPanjang.Hide()
        self.temp_LPersegi.Hide()
        self.temp_KPersegi.Hide()
        self.temp_login.Hide()
        self.temp_dash.Hide()

    def show_panel_LLingkaran(self):
        self.temp_LLingkaran.Show()
        self.temp_e_catatan.Hide()
        self.temp_S_Datar.Hide()
        self.temp_S_Ruang.Hide()
        self.temp_K_Datar.Hide()
        self.temp_K_Ruang.Hide()
        self.temp_VTabung.Hide()
        self.temp_LPTabung.Hide()
        self.temp_VLEmpat.Hide()
        self.temp_LLEmpat.Hide()
        self.temp_VBola.Hide()
        self.temp_LPBola.Hide()
        self.temp_VKerucut.Hide()
        self.temp_LPKerucut.Hide()
        self.temp_VPriEmpat.Hide()
        self.temp_LPPriEmpat.Hide()
        self.temp_VPriTiga.Hide()
        self.temp_LPPriTiga.Hide()
        self.temp_VBalok.Hide()
        self.temp_LPBalok.Hide()
        self.temp_VKubus.Hide()
        self.temp_LPKubus.Hide()
        self.temp_LJajar.Hide()
        self.temp_KJajar.Hide()
        self.temp_LLayang.Hide()
        self.temp_KLayang.Hide()
        self.temp_LTrapesium.Hide()
        self.temp_KTrapesium.Hide()
        self.temp_LBB.Hide()
        self.temp_KBB.Hide()
        self.temp_KSegitiga.Hide()
        self.temp_LSegitiga.Hide()
        self.temp_KLingkaran.Hide()
        self.temp_LPerPanjang.Hide()
        self.temp_KPerPanjang.Hide()
        self.temp_LPersegi.Hide()
        self.temp_KPersegi.Hide()
        self.temp_login.Hide()
        self.temp_dash.Hide()

    def show_panel_KSegitiga(self):
        self.temp_KSegitiga.Show()
        self.temp_e_catatan.Hide()
        self.temp_S_Datar.Hide()
        self.temp_S_Ruang.Hide()
        self.temp_K_Datar.Hide()
        self.temp_K_Ruang.Hide()
        self.temp_VTabung.Hide()
        self.temp_LPTabung.Hide()
        self.temp_VLEmpat.Hide()
        self.temp_LLEmpat.Hide()
        self.temp_VBola.Hide()
        self.temp_LPBola.Hide()
        self.temp_VKerucut.Hide()
        self.temp_LPKerucut.Hide()
        self.temp_VPriEmpat.Hide()
        self.temp_LPPriEmpat.Hide()
        self.temp_VPriTiga.Hide()
        self.temp_LPPriTiga.Hide()
        self.temp_VBalok.Hide()
        self.temp_LPBalok.Hide()
        self.temp_VKubus.Hide()
        self.temp_LPKubus.Hide()
        self.temp_LJajar.Hide()
        self.temp_KJajar.Hide()
        self.temp_LLayang.Hide()
        self.temp_KLayang.Hide()
        self.temp_LTrapesium.Hide()
        self.temp_KTrapesium.Hide()
        self.temp_LBB.Hide()
        self.temp_KBB.Hide()
        self.temp_LSegitiga.Hide()
        self.temp_LLingkaran.Hide()
        self.temp_KLingkaran.Hide()
        self.temp_LPerPanjang.Hide()
        self.temp_KPerPanjang.Hide()
        self.temp_LPersegi.Hide()
        self.temp_KPersegi.Hide()
        self.temp_login.Hide()
        self.temp_dash.Hide()

    def show_panel_LSegitiga(self):
        self.temp_LSegitiga.Show()
        self.temp_e_catatan.Hide()
        self.temp_S_Datar.Hide()
        self.temp_S_Ruang.Hide()
        self.temp_K_Datar.Hide()
        self.temp_K_Ruang.Hide()
        self.temp_VTabung.Hide()
        self.temp_LPTabung.Hide()
        self.temp_VLEmpat.Hide()
        self.temp_LLEmpat.Hide()
        self.temp_VBola.Hide()
        self.temp_LPBola.Hide()
        self.temp_VKerucut.Hide()
        self.temp_LPKerucut.Hide()
        self.temp_VPriEmpat.Hide()
        self.temp_LPPriEmpat.Hide()
        self.temp_VPriTiga.Hide()
        self.temp_LPPriTiga.Hide()
        self.temp_VBalok.Hide()
        self.temp_LPBalok.Hide()
        self.temp_VKubus.Hide()
        self.temp_LPKubus.Hide()
        self.temp_LJajar.Hide()
        self.temp_KJajar.Hide()
        self.temp_LLayang.Hide()
        self.temp_KLayang.Hide()
        self.temp_LTrapesium.Hide()
        self.temp_KTrapesium.Hide()
        self.temp_LBB.Hide()
        self.temp_KBB.Hide()
        self.temp_KSegitiga.Hide()
        self.temp_LLingkaran.Hide()
        self.temp_KLingkaran.Hide()
        self.temp_LPerPanjang.Hide()
        self.temp_KPerPanjang.Hide()
        self.temp_LPersegi.Hide()
        self.temp_KPersegi.Hide()
        self.temp_login.Hide()
        self.temp_dash.Hide()

    def show_panel_KBB(self):
        self.temp_KBB.Show()
        self.temp_e_catatan.Hide()
        self.temp_S_Datar.Hide()
        self.temp_S_Ruang.Hide()
        self.temp_K_Datar.Hide()
        self.temp_K_Ruang.Hide()
        self.temp_VTabung.Hide()
        self.temp_LPTabung.Hide()
        self.temp_VLEmpat.Hide()
        self.temp_LLEmpat.Hide()
        self.temp_VBola.Hide()
        self.temp_LPBola.Hide()
        self.temp_VKerucut.Hide()
        self.temp_LPKerucut.Hide()
        self.temp_VPriEmpat.Hide()
        self.temp_LPPriEmpat.Hide()
        self.temp_VPriTiga.Hide()
        self.temp_LPPriTiga.Hide()
        self.temp_VBalok.Hide()
        self.temp_LPBalok.Hide()
        self.temp_VKubus.Hide()
        self.temp_LPKubus.Hide()
        self.temp_LJajar.Hide()
        self.temp_KJajar.Hide()
        self.temp_LLayang.Hide()
        self.temp_KLayang.Hide()
        self.temp_LTrapesium.Hide()
        self.temp_KTrapesium.Hide()
        self.temp_LBB.Hide()
        self.temp_KSegitiga.Hide()
        self.temp_LSegitiga.Hide()
        self.temp_LLingkaran.Hide()
        self.temp_KLingkaran.Hide()
        self.temp_LPerPanjang.Hide()
        self.temp_KPerPanjang.Hide()
        self.temp_LPersegi.Hide()
        self.temp_KPersegi.Hide()
        self.temp_login.Hide()
        self.temp_dash.Hide()

    def show_panel_LKBB(self):
        self.temp_LBB.Show()
        self.temp_e_catatan.Hide()
        self.temp_S_Datar.Hide()
        self.temp_S_Ruang.Hide()
        self.temp_K_Datar.Hide()
        self.temp_K_Ruang.Hide()
        self.temp_VTabung.Hide()
        self.temp_LPTabung.Hide()
        self.temp_VLEmpat.Hide()
        self.temp_LLEmpat.Hide()
        self.temp_VBola.Hide()
        self.temp_LPBola.Hide()
        self.temp_VKerucut.Hide()
        self.temp_LPKerucut.Hide()
        self.temp_VPriEmpat.Hide()
        self.temp_LPPriEmpat.Hide()
        self.temp_VPriTiga.Hide()
        self.temp_LPPriTiga.Hide()
        self.temp_VBalok.Hide()
        self.temp_LPBalok.Hide()
        self.temp_VKubus.Hide()
        self.temp_LPKubus.Hide()
        self.temp_LJajar.Hide()
        self.temp_KJajar.Hide()
        self.temp_LLayang.Hide()
        self.temp_KLayang.Hide()
        self.temp_LTrapesium.Hide()
        self.temp_KTrapesium.Hide()
        self.temp_KBB.Hide()
        self.temp_KSegitiga.Hide()
        self.temp_LSegitiga.Hide()
        self.temp_LLingkaran.Hide()
        self.temp_KLingkaran.Hide()
        self.temp_LPerPanjang.Hide()
        self.temp_KPerPanjang.Hide()
        self.temp_LPersegi.Hide()
        self.temp_KPersegi.Hide()
        self.temp_login.Hide()
        self.temp_dash.Hide()

    def show_panel_KTrapesium(self):
        self.temp_KTrapesium.Show()
        self.temp_e_catatan.Hide()
        self.temp_S_Datar.Hide()
        self.temp_S_Ruang.Hide()
        self.temp_K_Datar.Hide()
        self.temp_K_Ruang.Hide()
        self.temp_VTabung.Hide()
        self.temp_LPTabung.Hide()
        self.temp_VLEmpat.Hide()
        self.temp_LLEmpat.Hide()
        self.temp_VBola.Hide()
        self.temp_LPBola.Hide()
        self.temp_VKerucut.Hide()
        self.temp_LPKerucut.Hide()
        self.temp_VPriEmpat.Hide()
        self.temp_LPPriEmpat.Hide()
        self.temp_VPriTiga.Hide()
        self.temp_LPPriTiga.Hide()
        self.temp_VBalok.Hide()
        self.temp_LPBalok.Hide()
        self.temp_VKubus.Hide()
        self.temp_LPKubus.Hide()
        self.temp_LJajar.Hide()
        self.temp_KJajar.Hide()
        self.temp_LLayang.Hide()
        self.temp_KLayang.Hide()
        self.temp_LTrapesium.Hide()
        self.temp_LBB.Hide()
        self.temp_KBB.Hide()
        self.temp_KSegitiga.Hide()
        self.temp_LSegitiga.Hide()
        self.temp_LLingkaran.Hide()
        self.temp_KLingkaran.Hide()
        self.temp_LPerPanjang.Hide()
        self.temp_KPerPanjang.Hide()
        self.temp_LPersegi.Hide()
        self.temp_KPersegi.Hide()
        self.temp_login.Hide()
        self.temp_dash.Hide()

    def show_panel_LTrapesium(self):
        self.temp_LTrapesium.Show()
        self.temp_e_catatan.Hide()
        self.temp_S_Datar.Hide()
        self.temp_S_Ruang.Hide()
        self.temp_K_Datar.Hide()
        self.temp_K_Ruang.Hide()
        self.temp_VTabung.Hide()
        self.temp_LPTabung.Hide()
        self.temp_VLEmpat.Hide()
        self.temp_LLEmpat.Hide()
        self.temp_VBola.Hide()
        self.temp_LPBola.Hide()
        self.temp_VKerucut.Hide()
        self.temp_LPKerucut.Hide()
        self.temp_VPriEmpat.Hide()
        self.temp_LPPriEmpat.Hide()
        self.temp_VPriTiga.Hide()
        self.temp_LPPriTiga.Hide()
        self.temp_VBalok.Hide()
        self.temp_LPBalok.Hide()
        self.temp_VKubus.Hide()
        self.temp_LPKubus.Hide()
        self.temp_LJajar.Hide()
        self.temp_KJajar.Hide()
        self.temp_LLayang.Hide()
        self.temp_KLayang.Hide()
        self.temp_KTrapesium.Hide()
        self.temp_LBB.Hide()
        self.temp_KBB.Hide()
        self.temp_KSegitiga.Hide()
        self.temp_LSegitiga.Hide()
        self.temp_LLingkaran.Hide()
        self.temp_KLingkaran.Hide()
        self.temp_LPerPanjang.Hide()
        self.temp_KPerPanjang.Hide()
        self.temp_LPersegi.Hide()
        self.temp_KPersegi.Hide()
        self.temp_login.Hide()
        self.temp_dash.Hide()

    def show_panel_KLayang(self):
        self.temp_KLayang.Show()
        self.temp_e_catatan.Hide()
        self.temp_S_Datar.Hide()
        self.temp_S_Ruang.Hide()
        self.temp_K_Datar.Hide()
        self.temp_K_Ruang.Hide()
        self.temp_VTabung.Hide()
        self.temp_LPTabung.Hide()
        self.temp_VLEmpat.Hide()
        self.temp_LLEmpat.Hide()
        self.temp_VBola.Hide()
        self.temp_LPBola.Hide()
        self.temp_VKerucut.Hide()
        self.temp_LPKerucut.Hide()
        self.temp_VPriEmpat.Hide()
        self.temp_LPPriEmpat.Hide()
        self.temp_VPriTiga.Hide()
        self.temp_LPPriTiga.Hide()
        self.temp_VBalok.Hide()
        self.temp_LPBalok.Hide()
        self.temp_VKubus.Hide()
        self.temp_LPKubus.Hide()
        self.temp_LJajar.Hide()
        self.temp_KJajar.Hide()
        self.temp_LLayang.Hide()
        self.temp_LTrapesium.Hide()
        self.temp_KTrapesium.Hide()
        self.temp_LBB.Hide()
        self.temp_KBB.Hide()
        self.temp_KSegitiga.Hide()
        self.temp_LSegitiga.Hide()
        self.temp_LLingkaran.Hide()
        self.temp_KLingkaran.Hide()
        self.temp_LPerPanjang.Hide()
        self.temp_KPerPanjang.Hide()
        self.temp_LPersegi.Hide()
        self.temp_KPersegi.Hide()
        self.temp_login.Hide()
        self.temp_dash.Hide()

    def show_panel_LLayang(self):
        self.temp_LLayang.Show()
        self.temp_e_catatan.Hide()
        self.temp_S_Datar.Hide()
        self.temp_S_Ruang.Hide()
        self.temp_K_Datar.Hide()
        self.temp_K_Ruang.Hide()
        self.temp_VTabung.Hide()
        self.temp_LPTabung.Hide()
        self.temp_VLEmpat.Hide()
        self.temp_LLEmpat.Hide()
        self.temp_VBola.Hide()
        self.temp_LPBola.Hide()
        self.temp_VKerucut.Hide()
        self.temp_LPKerucut.Hide()
        self.temp_VPriEmpat.Hide()
        self.temp_LPPriEmpat.Hide()
        self.temp_VPriTiga.Hide()
        self.temp_LPPriTiga.Hide()
        self.temp_VBalok.Hide()
        self.temp_LPBalok.Hide()
        self.temp_VKubus.Hide()
        self.temp_LPKubus.Hide()
        self.temp_LJajar.Hide()
        self.temp_KJajar.Hide()
        self.temp_KLayang.Hide()
        self.temp_LTrapesium.Hide()
        self.temp_KTrapesium.Hide()
        self.temp_LBB.Hide()
        self.temp_KBB.Hide()
        self.temp_KSegitiga.Hide()
        self.temp_LSegitiga.Hide()
        self.temp_LLingkaran.Hide()
        self.temp_KLingkaran.Hide()
        self.temp_LPerPanjang.Hide()
        self.temp_KPerPanjang.Hide()
        self.temp_LPersegi.Hide()
        self.temp_KPersegi.Hide()
        self.temp_login.Hide()
        self.temp_dash.Hide()

    def show_panel_KJajar(self):
        self.temp_KJajar.Show()
        self.temp_e_catatan.Hide()
        self.temp_S_Datar.Hide()
        self.temp_S_Ruang.Hide()
        self.temp_K_Datar.Hide()
        self.temp_K_Ruang.Hide()
        self.temp_VTabung.Hide()
        self.temp_LPTabung.Hide()
        self.temp_VLEmpat.Hide()
        self.temp_LLEmpat.Hide()
        self.temp_VBola.Hide()
        self.temp_LPBola.Hide()
        self.temp_VKerucut.Hide()
        self.temp_LPKerucut.Hide()
        self.temp_VPriEmpat.Hide()
        self.temp_LPPriEmpat.Hide()
        self.temp_VPriTiga.Hide()
        self.temp_LPPriTiga.Hide()
        self.temp_VBalok.Hide()
        self.temp_LPBalok.Hide()
        self.temp_VKubus.Hide()
        self.temp_LPKubus.Hide()
        self.temp_LJajar.Hide()
        self.temp_LLayang.Hide()
        self.temp_KLayang.Hide()
        self.temp_LTrapesium.Hide()
        self.temp_KTrapesium.Hide()
        self.temp_LBB.Hide()
        self.temp_KBB.Hide()
        self.temp_KSegitiga.Hide()
        self.temp_LSegitiga.Hide()
        self.temp_LLingkaran.Hide()
        self.temp_KLingkaran.Hide()
        self.temp_LPerPanjang.Hide()
        self.temp_KPerPanjang.Hide()
        self.temp_LPersegi.Hide()
        self.temp_KPersegi.Hide()
        self.temp_login.Hide()
        self.temp_dash.Hide()

    def show_panel_LJajar(self):
        self.temp_LJajar.Show()
        self.temp_e_catatan.Hide()
        self.temp_S_Datar.Hide()
        self.temp_S_Ruang.Hide()
        self.temp_K_Datar.Hide()
        self.temp_K_Ruang.Hide()
        self.temp_VTabung.Hide()
        self.temp_LPTabung.Hide()
        self.temp_VLEmpat.Hide()
        self.temp_LLEmpat.Hide()
        self.temp_VBola.Hide()
        self.temp_LPBola.Hide()
        self.temp_VKerucut.Hide()
        self.temp_LPKerucut.Hide()
        self.temp_VPriEmpat.Hide()
        self.temp_LPPriEmpat.Hide()
        self.temp_VPriTiga.Hide()
        self.temp_LPPriTiga.Hide()
        self.temp_VBalok.Hide()
        self.temp_LPBalok.Hide()
        self.temp_VKubus.Hide()
        self.temp_LPKubus.Hide()
        self.temp_KJajar.Hide()
        self.temp_LLayang.Hide()
        self.temp_KLayang.Hide()
        self.temp_LTrapesium.Hide()
        self.temp_KTrapesium.Hide()
        self.temp_LBB.Hide()
        self.temp_KBB.Hide()
        self.temp_KSegitiga.Hide()
        self.temp_LSegitiga.Hide()
        self.temp_LLingkaran.Hide()
        self.temp_KLingkaran.Hide()
        self.temp_LPerPanjang.Hide()
        self.temp_KPerPanjang.Hide()
        self.temp_LPersegi.Hide()
        self.temp_KPersegi.Hide()
        self.temp_login.Hide()
        self.temp_dash.Hide()

    def show_panel_LPKubus(self):
        self.temp_LPKubus.Show()
        self.temp_e_catatan.Hide()
        self.temp_S_Datar.Hide()
        self.temp_S_Ruang.Hide()
        self.temp_K_Datar.Hide()
        self.temp_K_Ruang.Hide()
        self.temp_VTabung.Hide()
        self.temp_LPTabung.Hide()
        self.temp_VLEmpat.Hide()
        self.temp_LLEmpat.Hide()
        self.temp_VBola.Hide()
        self.temp_LPBola.Hide()
        self.temp_VKerucut.Hide()
        self.temp_LPKerucut.Hide()
        self.temp_VPriEmpat.Hide()
        self.temp_LPPriEmpat.Hide()
        self.temp_VPriTiga.Hide()
        self.temp_LPPriTiga.Hide()
        self.temp_VBalok.Hide()
        self.temp_LPBalok.Hide()
        self.temp_VKubus.Hide()
        self.temp_LJajar.Hide()
        self.temp_KJajar.Hide()
        self.temp_LLayang.Hide()
        self.temp_KLayang.Hide()
        self.temp_LTrapesium.Hide()
        self.temp_KTrapesium.Hide()
        self.temp_LBB.Hide()
        self.temp_KBB.Hide()
        self.temp_KSegitiga.Hide()
        self.temp_LSegitiga.Hide()
        self.temp_LLingkaran.Hide()
        self.temp_KLingkaran.Hide()
        self.temp_LPerPanjang.Hide()
        self.temp_KPerPanjang.Hide()
        self.temp_LPersegi.Hide()
        self.temp_KPersegi.Hide()
        self.temp_dash.Hide()
        self.temp_login.Hide()

    def show_panel_VKubus(self):
        self.temp_VKubus.Show()
        self.temp_e_catatan.Hide()
        self.temp_S_Datar.Hide()
        self.temp_S_Ruang.Hide()
        self.temp_K_Datar.Hide()
        self.temp_K_Ruang.Hide()
        self.temp_VTabung.Hide()
        self.temp_LPTabung.Hide()
        self.temp_VLEmpat.Hide()
        self.temp_LLEmpat.Hide()
        self.temp_VBola.Hide()
        self.temp_LPBola.Hide()
        self.temp_VKerucut.Hide()
        self.temp_LPKerucut.Hide()
        self.temp_VPriEmpat.Hide()
        self.temp_LPPriEmpat.Hide()
        self.temp_VPriTiga.Hide()
        self.temp_LPPriTiga.Hide()
        self.temp_VBalok.Hide()
        self.temp_LPBalok.Hide()
        self.temp_LPKubus.Hide()
        self.temp_LJajar.Hide()
        self.temp_KJajar.Hide()
        self.temp_LLayang.Hide()
        self.temp_KLayang.Hide()
        self.temp_LTrapesium.Hide()
        self.temp_KTrapesium.Hide()
        self.temp_LBB.Hide()
        self.temp_KBB.Hide()
        self.temp_KSegitiga.Hide()
        self.temp_LSegitiga.Hide()
        self.temp_LLingkaran.Hide()
        self.temp_KLingkaran.Hide()
        self.temp_LPerPanjang.Hide()
        self.temp_KPerPanjang.Hide()
        self.temp_LPersegi.Hide()
        self.temp_KPersegi.Hide()
        self.temp_dash.Hide()
        self.temp_login.Hide()

    def show_panel_LPBalok(self):
        self.temp_LPBalok.Show()
        self.temp_e_catatan.Hide()
        self.temp_S_Datar.Hide()
        self.temp_S_Ruang.Hide()
        self.temp_K_Datar.Hide()
        self.temp_K_Ruang.Hide()
        self.temp_VTabung.Hide()
        self.temp_LPTabung.Hide()
        self.temp_VLEmpat.Hide()
        self.temp_LLEmpat.Hide()
        self.temp_VBola.Hide()
        self.temp_LPBola.Hide()
        self.temp_VKerucut.Hide()
        self.temp_LPKerucut.Hide()
        self.temp_VPriEmpat.Hide()
        self.temp_LPPriEmpat.Hide()
        self.temp_VPriTiga.Hide()
        self.temp_LPPriTiga.Hide()
        self.temp_VBalok.Hide()
        self.temp_VKubus.Hide()
        self.temp_LPKubus.Hide()
        self.temp_LJajar.Hide()
        self.temp_KJajar.Hide()
        self.temp_LLayang.Hide()
        self.temp_KLayang.Hide()
        self.temp_LTrapesium.Hide()
        self.temp_KTrapesium.Hide()
        self.temp_LBB.Hide()
        self.temp_KBB.Hide()
        self.temp_KSegitiga.Hide()
        self.temp_LSegitiga.Hide()
        self.temp_LLingkaran.Hide()
        self.temp_KLingkaran.Hide()
        self.temp_LPerPanjang.Hide()
        self.temp_KPerPanjang.Hide()
        self.temp_LPersegi.Hide()
        self.temp_KPersegi.Hide()
        self.temp_dash.Hide()
        self.temp_login.Hide()

    def show_panel_VBalok(self):
        self.temp_VBalok.Show()
        self.temp_e_catatan.Hide()
        self.temp_S_Datar.Hide()
        self.temp_S_Ruang.Hide()
        self.temp_K_Datar.Hide()
        self.temp_K_Ruang.Hide()
        self.temp_VTabung.Hide()
        self.temp_LPTabung.Hide()
        self.temp_VLEmpat.Hide()
        self.temp_LLEmpat.Hide()
        self.temp_VBola.Hide()
        self.temp_LPBola.Hide()
        self.temp_VKerucut.Hide()
        self.temp_LPKerucut.Hide()
        self.temp_VPriEmpat.Hide()
        self.temp_LPPriEmpat.Hide()
        self.temp_VPriTiga.Hide()
        self.temp_LPPriTiga.Hide()
        self.temp_LPBalok.Hide()
        self.temp_VKubus.Hide()
        self.temp_LPKubus.Hide()
        self.temp_LJajar.Hide()
        self.temp_KJajar.Hide()
        self.temp_LLayang.Hide()
        self.temp_KLayang.Hide()
        self.temp_LTrapesium.Hide()
        self.temp_KTrapesium.Hide()
        self.temp_LBB.Hide()
        self.temp_KBB.Hide()
        self.temp_KSegitiga.Hide()
        self.temp_LSegitiga.Hide()
        self.temp_LLingkaran.Hide()
        self.temp_KLingkaran.Hide()
        self.temp_LPerPanjang.Hide()
        self.temp_KPerPanjang.Hide()
        self.temp_LPersegi.Hide()
        self.temp_KPersegi.Hide()
        self.temp_dash.Hide()
        self.temp_login.Hide()

    def show_panel_LPPriTiga(self):
        self.temp_LPPriTiga.Show()
        self.temp_e_catatan.Hide()
        self.temp_S_Datar.Hide()
        self.temp_S_Ruang.Hide()
        self.temp_K_Datar.Hide()
        self.temp_K_Ruang.Hide()
        self.temp_VTabung.Hide()
        self.temp_LPTabung.Hide()
        self.temp_VLEmpat.Hide()
        self.temp_LLEmpat.Hide()
        self.temp_VBola.Hide()
        self.temp_LPBola.Hide()
        self.temp_VKerucut.Hide()
        self.temp_LPKerucut.Hide()
        self.temp_VPriEmpat.Hide()
        self.temp_LPPriEmpat.Hide()
        self.temp_VPriTiga.Hide()
        self.temp_VBalok.Hide()
        self.temp_LPBalok.Hide()
        self.temp_VKubus.Hide()
        self.temp_LPKubus.Hide()
        self.temp_LJajar.Hide()
        self.temp_KJajar.Hide()
        self.temp_LLayang.Hide()
        self.temp_KLayang.Hide()
        self.temp_LTrapesium.Hide()
        self.temp_KTrapesium.Hide()
        self.temp_LBB.Hide()
        self.temp_KBB.Hide()
        self.temp_KSegitiga.Hide()
        self.temp_LSegitiga.Hide()
        self.temp_LLingkaran.Hide()
        self.temp_KLingkaran.Hide()
        self.temp_LPerPanjang.Hide()
        self.temp_KPerPanjang.Hide()
        self.temp_LPersegi.Hide()
        self.temp_KPersegi.Hide()
        self.temp_dash.Hide()
        self.temp_login.Hide()

    def show_panel_VPriTiga(self):
        self.temp_VPriTiga.Show()
        self.temp_e_catatan.Hide()
        self.temp_S_Datar.Hide()
        self.temp_S_Ruang.Hide()
        self.temp_K_Datar.Hide()
        self.temp_K_Ruang.Hide()
        self.temp_VTabung.Hide()
        self.temp_LPTabung.Hide()
        self.temp_VLEmpat.Hide()
        self.temp_LLEmpat.Hide()
        self.temp_VBola.Hide()
        self.temp_LPBola.Hide()
        self.temp_VKerucut.Hide()
        self.temp_LPKerucut.Hide()
        self.temp_VPriEmpat.Hide()
        self.temp_LPPriEmpat.Hide()
        self.temp_LPPriTiga.Hide()
        self.temp_VBalok.Hide()
        self.temp_LPBalok.Hide()
        self.temp_VKubus.Hide()
        self.temp_LPKubus.Hide()
        self.temp_LJajar.Hide()
        self.temp_KJajar.Hide()
        self.temp_LLayang.Hide()
        self.temp_KLayang.Hide()
        self.temp_LTrapesium.Hide()
        self.temp_KTrapesium.Hide()
        self.temp_LBB.Hide()
        self.temp_KBB.Hide()
        self.temp_KSegitiga.Hide()
        self.temp_LSegitiga.Hide()
        self.temp_LLingkaran.Hide()
        self.temp_KLingkaran.Hide()
        self.temp_LPerPanjang.Hide()
        self.temp_KPerPanjang.Hide()
        self.temp_LPersegi.Hide()
        self.temp_KPersegi.Hide()
        self.temp_dash.Hide()
        self.temp_login.Hide()

    def show_panel_LPPriEmpat(self):
        self.temp_LPPriEmpat.Show()
        self.temp_e_catatan.Hide()
        self.temp_S_Datar.Hide()
        self.temp_S_Ruang.Hide()
        self.temp_K_Datar.Hide()
        self.temp_K_Ruang.Hide()
        self.temp_VTabung.Hide()
        self.temp_LPTabung.Hide()
        self.temp_VLEmpat.Hide()
        self.temp_LLEmpat.Hide()
        self.temp_VBola.Hide()
        self.temp_LPBola.Hide()
        self.temp_VKerucut.Hide()
        self.temp_LPKerucut.Hide()
        self.temp_VPriEmpat.Hide()
        self.temp_VPriTiga.Hide()
        self.temp_LPPriTiga.Hide()
        self.temp_VBalok.Hide()
        self.temp_LPBalok.Hide()
        self.temp_VKubus.Hide()
        self.temp_LPKubus.Hide()
        self.temp_LJajar.Hide()
        self.temp_KJajar.Hide()
        self.temp_LLayang.Hide()
        self.temp_KLayang.Hide()
        self.temp_LTrapesium.Hide()
        self.temp_KTrapesium.Hide()
        self.temp_LBB.Hide()
        self.temp_KBB.Hide()
        self.temp_KSegitiga.Hide()
        self.temp_LSegitiga.Hide()
        self.temp_LLingkaran.Hide()
        self.temp_KLingkaran.Hide()
        self.temp_LPerPanjang.Hide()
        self.temp_KPerPanjang.Hide()
        self.temp_LPersegi.Hide()
        self.temp_KPersegi.Hide()
        self.temp_dash.Hide()
        self.temp_login.Hide()

    def show_panel_VPPriEmpat(self):
        self.temp_VPriEmpat.Show()
        self.temp_e_catatan.Hide()
        self.temp_S_Datar.Hide()
        self.temp_S_Ruang.Hide()
        self.temp_K_Datar.Hide()
        self.temp_K_Ruang.Hide()
        self.temp_VTabung.Hide()
        self.temp_LPTabung.Hide()
        self.temp_VLEmpat.Hide()
        self.temp_LLEmpat.Hide()
        self.temp_VBola.Hide()
        self.temp_LPBola.Hide()
        self.temp_VKerucut.Hide()
        self.temp_LPKerucut.Hide()
        self.temp_LPPriEmpat.Hide()
        self.temp_VPriTiga.Hide()
        self.temp_LPPriTiga.Hide()
        self.temp_VBalok.Hide()
        self.temp_LPBalok.Hide()
        self.temp_VKubus.Hide()
        self.temp_LPKubus.Hide()
        self.temp_LJajar.Hide()
        self.temp_KJajar.Hide()
        self.temp_LLayang.Hide()
        self.temp_KLayang.Hide()
        self.temp_LTrapesium.Hide()
        self.temp_KTrapesium.Hide()
        self.temp_LBB.Hide()
        self.temp_KBB.Hide()
        self.temp_KSegitiga.Hide()
        self.temp_LSegitiga.Hide()
        self.temp_LLingkaran.Hide()
        self.temp_KLingkaran.Hide()
        self.temp_LPerPanjang.Hide()
        self.temp_KPerPanjang.Hide()
        self.temp_LPersegi.Hide()
        self.temp_KPersegi.Hide()
        self.temp_dash.Hide()
        self.temp_login.Hide()

    def show_panel_LPKerucut(self):
        self.temp_LPKerucut.Show()
        self.temp_e_catatan.Hide()
        self.temp_S_Datar.Hide()
        self.temp_S_Ruang.Hide()
        self.temp_K_Datar.Hide()
        self.temp_K_Ruang.Hide()
        self.temp_VTabung.Hide()
        self.temp_LPTabung.Hide()
        self.temp_VLEmpat.Hide()
        self.temp_LLEmpat.Hide()
        self.temp_VBola.Hide()
        self.temp_LPBola.Hide()
        self.temp_VKerucut.Hide()
        self.temp_VPriEmpat.Hide()
        self.temp_LPPriEmpat.Hide()
        self.temp_VPriTiga.Hide()
        self.temp_LPPriTiga.Hide()
        self.temp_VBalok.Hide()
        self.temp_LPBalok.Hide()
        self.temp_VKubus.Hide()
        self.temp_LPKubus.Hide()
        self.temp_LJajar.Hide()
        self.temp_KJajar.Hide()
        self.temp_LLayang.Hide()
        self.temp_KLayang.Hide()
        self.temp_LTrapesium.Hide()
        self.temp_KTrapesium.Hide()
        self.temp_LBB.Hide()
        self.temp_KBB.Hide()
        self.temp_KSegitiga.Hide()
        self.temp_LSegitiga.Hide()
        self.temp_LLingkaran.Hide()
        self.temp_KLingkaran.Hide()
        self.temp_LPerPanjang.Hide()
        self.temp_KPerPanjang.Hide()
        self.temp_LPersegi.Hide()
        self.temp_KPersegi.Hide()
        self.temp_dash.Hide()
        self.temp_login.Hide()

    def show_panel_VKerucut(self):
        self.temp_VKerucut.Show()
        self.temp_e_catatan.Hide()
        self.temp_S_Datar.Hide()
        self.temp_S_Ruang.Hide()
        self.temp_K_Datar.Hide()
        self.temp_K_Ruang.Hide()
        self.temp_VTabung.Hide()
        self.temp_LPTabung.Hide()
        self.temp_VLEmpat.Hide()
        self.temp_LLEmpat.Hide()
        self.temp_VBola.Hide()
        self.temp_LPBola.Hide()
        self.temp_LPKerucut.Hide()
        self.temp_VPriEmpat.Hide()
        self.temp_LPPriEmpat.Hide()
        self.temp_VPriTiga.Hide()
        self.temp_LPPriTiga.Hide()
        self.temp_VBalok.Hide()
        self.temp_LPBalok.Hide()
        self.temp_VKubus.Hide()
        self.temp_LPKubus.Hide()
        self.temp_LJajar.Hide()
        self.temp_KJajar.Hide()
        self.temp_LLayang.Hide()
        self.temp_KLayang.Hide()
        self.temp_LTrapesium.Hide()
        self.temp_KTrapesium.Hide()
        self.temp_LBB.Hide()
        self.temp_KBB.Hide()
        self.temp_KSegitiga.Hide()
        self.temp_LSegitiga.Hide()
        self.temp_LLingkaran.Hide()
        self.temp_KLingkaran.Hide()
        self.temp_LPerPanjang.Hide()
        self.temp_KPerPanjang.Hide()
        self.temp_LPersegi.Hide()
        self.temp_KPersegi.Hide()
        self.temp_dash.Hide()
        self.temp_login.Hide()

    def show_panel_LPBola(self):
        self.temp_LPBola.Show()
        self.temp_e_catatan.Hide()
        self.temp_S_Datar.Hide()
        self.temp_S_Ruang.Hide()
        self.temp_K_Datar.Hide()
        self.temp_K_Ruang.Hide()
        self.temp_VTabung.Hide()
        self.temp_LPTabung.Hide()
        self.temp_VLEmpat.Hide()
        self.temp_LLEmpat.Hide()
        self.temp_VBola.Hide()
        self.temp_VKerucut.Hide()
        self.temp_LPKerucut.Hide()
        self.temp_VPriEmpat.Hide()
        self.temp_LPPriEmpat.Hide()
        self.temp_VPriTiga.Hide()
        self.temp_LPPriTiga.Hide()
        self.temp_VBalok.Hide()
        self.temp_LPBalok.Hide()
        self.temp_VKubus.Hide()
        self.temp_LPKubus.Hide()
        self.temp_LJajar.Hide()
        self.temp_KJajar.Hide()
        self.temp_LLayang.Hide()
        self.temp_KLayang.Hide()
        self.temp_LTrapesium.Hide()
        self.temp_KTrapesium.Hide()
        self.temp_LBB.Hide()
        self.temp_KBB.Hide()
        self.temp_KSegitiga.Hide()
        self.temp_LSegitiga.Hide()
        self.temp_LLingkaran.Hide()
        self.temp_KLingkaran.Hide()
        self.temp_LPerPanjang.Hide()
        self.temp_KPerPanjang.Hide()
        self.temp_LPersegi.Hide()
        self.temp_KPersegi.Hide()
        self.temp_dash.Hide()
        self.temp_login.Hide()

    def show_panel_VBola(self):
        self.temp_VBola.Show()
        self.temp_e_catatan.Hide()
        self.temp_S_Datar.Hide()
        self.temp_S_Ruang.Hide()
        self.temp_K_Datar.Hide()
        self.temp_K_Ruang.Hide()
        self.temp_VTabung.Hide()
        self.temp_LPTabung.Hide()
        self.temp_VLEmpat.Hide()
        self.temp_LLEmpat.Hide()
        self.temp_LPBola.Hide()
        self.temp_VKerucut.Hide()
        self.temp_LPKerucut.Hide()
        self.temp_VPriEmpat.Hide()
        self.temp_LPPriEmpat.Hide()
        self.temp_VPriTiga.Hide()
        self.temp_LPPriTiga.Hide()
        self.temp_VBalok.Hide()
        self.temp_LPBalok.Hide()
        self.temp_VKubus.Hide()
        self.temp_LPKubus.Hide()
        self.temp_LJajar.Hide()
        self.temp_KJajar.Hide()
        self.temp_LLayang.Hide()
        self.temp_KLayang.Hide()
        self.temp_LTrapesium.Hide()
        self.temp_KTrapesium.Hide()
        self.temp_LBB.Hide()
        self.temp_KBB.Hide()
        self.temp_KSegitiga.Hide()
        self.temp_LSegitiga.Hide()
        self.temp_LLingkaran.Hide()
        self.temp_KLingkaran.Hide()
        self.temp_LPerPanjang.Hide()
        self.temp_KPerPanjang.Hide()
        self.temp_LPersegi.Hide()
        self.temp_KPersegi.Hide()
        self.temp_dash.Hide()
        self.temp_login.Hide()

    def show_panel_LPLEmpat(self):
        self.temp_LLEmpat.Show()
        self.temp_e_catatan.Hide()
        self.temp_S_Datar.Hide()
        self.temp_S_Ruang.Hide()
        self.temp_K_Datar.Hide()
        self.temp_K_Ruang.Hide()
        self.temp_VTabung.Hide()
        self.temp_LPTabung.Hide()
        self.temp_VLEmpat.Hide()
        self.temp_VBola.Hide()
        self.temp_LPBola.Hide()
        self.temp_VKerucut.Hide()
        self.temp_LPKerucut.Hide()
        self.temp_VPriEmpat.Hide()
        self.temp_LPPriEmpat.Hide()
        self.temp_VPriTiga.Hide()
        self.temp_LPPriTiga.Hide()
        self.temp_VBalok.Hide()
        self.temp_LPBalok.Hide()
        self.temp_VKubus.Hide()
        self.temp_LPKubus.Hide()
        self.temp_LJajar.Hide()
        self.temp_KJajar.Hide()
        self.temp_LLayang.Hide()
        self.temp_KLayang.Hide()
        self.temp_LTrapesium.Hide()
        self.temp_KTrapesium.Hide()
        self.temp_LBB.Hide()
        self.temp_KBB.Hide()
        self.temp_KSegitiga.Hide()
        self.temp_LSegitiga.Hide()
        self.temp_LLingkaran.Hide()
        self.temp_KLingkaran.Hide()
        self.temp_LPerPanjang.Hide()
        self.temp_KPerPanjang.Hide()
        self.temp_LPersegi.Hide()
        self.temp_KPersegi.Hide()
        self.temp_dash.Hide()
        self.temp_login.Hide()

    def show_panel_VLEMPAT(self):
        self.temp_VLEmpat.Show()
        self.temp_e_catatan.Hide()
        self.temp_S_Datar.Hide()
        self.temp_S_Ruang.Hide()
        self.temp_K_Datar.Hide()
        self.temp_K_Ruang.Hide()
        self.temp_VTabung.Hide()
        self.temp_LPTabung.Hide()
        self.temp_LLEmpat.Hide()
        self.temp_VBola.Hide()
        self.temp_LPBola.Hide()
        self.temp_VKerucut.Hide()
        self.temp_LPKerucut.Hide()
        self.temp_VPriEmpat.Hide()
        self.temp_LPPriEmpat.Hide()
        self.temp_VPriTiga.Hide()
        self.temp_LPPriTiga.Hide()
        self.temp_VBalok.Hide()
        self.temp_LPBalok.Hide()
        self.temp_VKubus.Hide()
        self.temp_LPKubus.Hide()
        self.temp_LJajar.Hide()
        self.temp_KJajar.Hide()
        self.temp_LLayang.Hide()
        self.temp_KLayang.Hide()
        self.temp_LTrapesium.Hide()
        self.temp_KTrapesium.Hide()
        self.temp_LBB.Hide()
        self.temp_KBB.Hide()
        self.temp_KSegitiga.Hide()
        self.temp_LSegitiga.Hide()
        self.temp_LLingkaran.Hide()
        self.temp_KLingkaran.Hide()
        self.temp_LPerPanjang.Hide()
        self.temp_KPerPanjang.Hide()
        self.temp_LPersegi.Hide()
        self.temp_KPersegi.Hide()
        self.temp_dash.Hide()
        self.temp_login.Hide()

    def show_panel_LPTabung(self):
        self.temp_LPTabung.Show()
        self.temp_e_catatan.Hide()
        self.temp_S_Datar.Hide()
        self.temp_S_Ruang.Hide()
        self.temp_K_Datar.Hide()
        self.temp_K_Ruang.Hide()
        self.temp_VTabung.Hide()
        self.temp_VLEmpat.Hide()
        self.temp_LLEmpat.Hide()
        self.temp_VBola.Hide()
        self.temp_LPBola.Hide()
        self.temp_VKerucut.Hide()
        self.temp_LPKerucut.Hide()
        self.temp_VPriEmpat.Hide()
        self.temp_LPPriEmpat.Hide()
        self.temp_VPriTiga.Hide()
        self.temp_LPPriTiga.Hide()
        self.temp_VBalok.Hide()
        self.temp_LPBalok.Hide()
        self.temp_VKubus.Hide()
        self.temp_LPKubus.Hide()
        self.temp_LJajar.Hide()
        self.temp_KJajar.Hide()
        self.temp_LLayang.Hide()
        self.temp_KLayang.Hide()
        self.temp_LTrapesium.Hide()
        self.temp_KTrapesium.Hide()
        self.temp_LBB.Hide()
        self.temp_KBB.Hide()
        self.temp_KSegitiga.Hide()
        self.temp_LSegitiga.Hide()
        self.temp_LLingkaran.Hide()
        self.temp_KLingkaran.Hide()
        self.temp_LPerPanjang.Hide()
        self.temp_KPerPanjang.Hide()
        self.temp_LPersegi.Hide()
        self.temp_KPersegi.Hide()
        self.temp_dash.Hide()
        self.temp_login.Hide()

    def show_panel_VTabung(self):
        self.temp_VTabung.Show()
        self.temp_e_catatan.Hide()
        self.temp_S_Datar.Hide()
        self.temp_S_Ruang.Hide()
        self.temp_K_Datar.Hide()
        self.temp_K_Ruang.Hide()
        self.temp_LPTabung.Hide()
        self.temp_VLEmpat.Hide()
        self.temp_LLEmpat.Hide()
        self.temp_VBola.Hide()
        self.temp_LPBola.Hide()
        self.temp_VKerucut.Hide()
        self.temp_LPKerucut.Hide()
        self.temp_VPriEmpat.Hide()
        self.temp_LPPriEmpat.Hide()
        self.temp_VPriTiga.Hide()
        self.temp_LPPriTiga.Hide()
        self.temp_VBalok.Hide()
        self.temp_LPBalok.Hide()
        self.temp_VKubus.Hide()
        self.temp_LPKubus.Hide()
        self.temp_LJajar.Hide()
        self.temp_KJajar.Hide()
        self.temp_LLayang.Hide()
        self.temp_KLayang.Hide()
        self.temp_LTrapesium.Hide()
        self.temp_KTrapesium.Hide()
        self.temp_LBB.Hide()
        self.temp_KBB.Hide()
        self.temp_KSegitiga.Hide()
        self.temp_LSegitiga.Hide()
        self.temp_LLingkaran.Hide()
        self.temp_KLingkaran.Hide()
        self.temp_LPerPanjang.Hide()
        self.temp_KPerPanjang.Hide()
        self.temp_LPersegi.Hide()
        self.temp_KPersegi.Hide()
        self.temp_dash.Hide()
        self.temp_login.Hide()


app = wx.App()
frame = frame_utama(parent=None)
frame.Show()
app.MainLoop()