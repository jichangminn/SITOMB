import streamlit as st
import sqlite3
from datetime import date
import pandas as pd
from PIL import Image
import locale

# User credentials
user = "admin"
passw = "admin"

# Fungsi login
def login():
    st.title("Halaman Login")
    st.subheader("Silahkan Untuk Login Terlebih Dahulu")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username == user and password == passw:
            st.session_state["logged_in"] = True
            st.sidebar.success("Login berhasil!")
            st.experimental_rerun()  # Refresh to update the state
        else:
            st.sidebar.error("Username atau password salah.")            

# Fungsi untuk setiap halaman
def home_page():
    with st.container():
        st.subheader("Selamat datang di SITOMB :wave:")
        st.title("Sistem Informasi Soto Bogor - SITOMB")
        st.write("SITOMB merupakan sistem informasi yang dirancang untuk memudahkan pemilik UMKM Soto Mie Bogor dalam pencatatan laporan keuangannya")
        st.write('''''')

    with st.container():
        st.write("---")
        st.subheader("Sejarah Kami")
        st.write("Soto Mie Bogor adalah salah satu makanan tradisional khas Bogor yang telah lama dikenal dan disukai masyarakat. Kami mulai berjualan Soto Mie Bogor ini dengan bertujuan untuk melestarikan dan memperkenalkan kuliner tradisional Bogor. Soto Mie Bogor ini didirikan pada 10 Maret 2023  oleh Uci Sanusi dan Iskandar. Kami Biasanya buka dari jam 10 pagi sampai jam 10 malam. Berawal dari usaha kecil-kecilan di rumah, kami berharap dapat berkembang menjadi usaha yang dikenal luas dan dicintai banyak orang baik dalam negeri maupun luar negeri. Soto Mie Bogor ini memiliki ciri khas unik yang tidak dimiliki oleh soto mie lainnya seperti soto mie bogor memiliki kuah bening yang ditambahkan dengan mie dan risol didalmnya. Dengan pengelolaan yang baik, kami yakin soto mie bogor ini dapat bersaing di pasar dan menjadi salah satu makanan tradisional yang paling disukai masyarakat. Kami percaya bahwa setiap mangkuk Soto Mie Bogor yang kami sajikan bukan hanya sekedar makanan, tetapi juga sebuah warisan salah satu budaya indonesia yang harus dijaga.")
        st.write('''''')

    st.write("---")
    st.subheader("Misi Kami")
    st.write("""
    Misi kami adalah menyediakan makanan yang berkualitas dan dapat dinikmati oleh semua orang serta memberikan pelayanan terbaik kepada setiap pelanggan kami
    - Menggunakan bahan-bahan yang fresh
    - Menyajikan hidangan dengan baik
    - Memberikan pelayanan yang sama kepada setiap pelanggan
    """)

    st.write("---")
    st.subheader("Apa yang Membuat Kami Berbeda?")
    st.write("""
    1. *Resep yang unik*: Kami menggunakan resep yang berdasarkan dari keaslian soto mie bogor yang berbeda dengan soto biasa.
    2. *Bahan-Bahan yang masih fresh*: Setiap hari, kami  memastikan setiap soto mie bogor yang disajikan selalu dalam kondisi terbaik.
    3. *Pelayanan Prima*: Kami selalu siap melayani dengan senyum, sopan dan ramah tamah.
    """)

    # Informasi Produk
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("Informasi Produk")
            st.write("""
                    Kami menjual soto mie bogor yang merupakan salah satu makanan khas Nusantara yang terbilang
                    soto lengkap karena terdapat banyak bahan-bahan yang disajikan dalam satu mangkoknya.
                    Hal unik yang kami sediakan dari makanan berkuah ini adalah penyajiannya yang dilengkapi
                    dengan mi kuning, dan risol umumnya soto disajikan hanya menggunakan mi soun atau bihun.
                        """)

    Image1 = Image.open('images/sotodag.jpeg')
    Image2 = Image.open('images/soyam.jpeg')
    st.write("---")
    st.header("Produk")
    st.write('##')
    left_column, right_column = st.columns(2)
    with left_column:
        st.image(Image1, caption="Soto Mie Bogor Daging", width=500)
        st.write('##')
        st.write(''' Soto Bogor Daging yang terbuat dari bahan - bahan
                    Mie Basah, Bihun, Kol, Daging Sapi, Tomat, Bumbu Paon,
                    Bawang Goreng, Daun Daunan.''')
        st.write("---")
    with right_column:
        st.image(Image2, caption="Soto Mie Bogor Ayam", width=425)
        st.write('##')
        st.write(''' Soto Bogor Ayam yang terbuat dari bahan - bahan
                    Mie Basah, Bihun, Kol, Daging Ayam, Tomat, Bumbu Paon,
                    Bawang Goreng, Daun Daunan.''')
        st.write("---")
    with st.container():
        st.subheader("Tim Kami")
        st.write("""Kami memiliki tim yang terdiri dari 2 orang. Yang dimana setiap orang memiliki masing masing tugas yang berbeda seperti membeli bahan baku, melayani pelanggan, dan membuat soto .""")
        st.write('''''')

    with st.container():
        st.write("---")
        st.subheader("Hubungi Kami")
        st.write("""
    Kami selalu senang mendengar dari Anda! Apakah Anda memiliki pertanyaan, saran, atau sekedar ingin berbagi pengalaman menikmati Soto Mie kami, jangan ragu untuk menghubungi kami melalui:

    - *Alamat*: Jalan Raya banaran, Sekaran, Gunung Pati, Depan Five'O Barbershop, dan Samping Burketsu.
    - *Telepon*: +6282177221070
    - *Email*: SotoMieBogorUnnesgunpat@gmail.com
    """)
    st.write("---")
    st.write("""
    Terima kasih telah Mengunjungi Website ini dan saya harap bisa mengunjungi usaha kami.
             
    Salam hangat,


             






                     
    *Pemilik UMKM Soto Mie Bogor*
    """)

def transaksi_page():
    st.title("Transaksi")

    # Koneksi ke database
    conn = sqlite3.connect('Transaksion.db')
    c = conn.cursor()

    # Buat tabel jika belum ada
    c.execute('''CREATE TABLE IF NOT EXISTS information
                 (Tanggal TEXT, Keterangan TEXT, qty TEXT, Harga INTEGER)''')
    conn.commit()

    def format_rupiah(amount):
        return f"Rp {int(amount):,}".replace(",", ".")

    def form():
        st.write("Isi Data Transaksi")
        with st.form(key="information form"):
            Tanggal = st.date_input("Tanggal:")
            Keterangan = st.text_input("Keterangan:")
            qty = st.text_input("Jumlah:")
            Harga_input = st.text_input("Harga (dalam Rupiah):")
            
            submission = st.form_submit_button(label="Submit")
            
            if submission:
                # Remove dots and convert to integer
                try:
                    Harga = int(Harga_input.replace(".", ""))
                    c.execute("INSERT INTO information (Tanggal, Keterangan, qty, Harga) VALUES (?, ?, ?, ?)", (Tanggal, Keterangan, qty, Harga))
                    conn.commit()
                    st.success("Successfully submitted")
                except ValueError:
                    st.error("Harga")

    def display_data():
        c.execute("SELECT * FROM information")
        data = c.fetchall()
        df = pd.DataFrame(data, columns=['Tanggal', 'Keterangan', 'qty', 'Harga'])
        # Format Harga column
        df['Harga'] = df['Harga'].apply(format_rupiah)
        st.write(df)

    def calculate_saldo():
        c.execute("SELECT SUM(Harga) FROM information")
        saldo = c.fetchone()[0]
        if saldo is None:
            saldo = 0
        st.header(f"Saldo: {format_rupiah(saldo)}")

    def delete_data():
        row_to_delete = st.text_input("Masukkan nomor baris yang akan dihapus:")
        if st.button("Delete"):
            c.execute("DELETE FROM information WHERE rowid=?", (row_to_delete,))
            conn.commit()
            st.success("Baris berhasil dihapus")

    form()
    display_data()
    calculate_saldo()
    delete_data()
    conn.close()



def persediaan_page():
    st.title("Persediaan")

    # Koneksi ke database
    conn = sqlite3.connect('Persediaan.db')
    c = conn.cursor()

    # Buat tabel jika belum ada
    c.execute('''CREATE TABLE IF NOT EXISTS inventory
                 ("Nama Barang" TEXT, qty TEXT, Harga INTEGER)''')
    conn.commit()

    def format_rupiah(amount):
        return f"Rp {int(amount):,}".replace(",", ".")

    def form():
        st.write("Isi Data Persediaan")
        with st.form(key="inventory form"):
            nama_barang = st.text_input("Nama Barang:")
            qty = st.text_input("Jumlah:")
            harga_input = st.text_input("Harga (dalam Rupiah):")
            
            submission = st.form_submit_button(label="Submit")
            
            if submission:
                # Remove dots and convert to integer
                try:
                    harga = int(harga_input.replace(".", ""))
                    c.execute('''INSERT INTO inventory ("Nama Barang", qty, Harga) VALUES (?, ?, ?)''', (nama_barang, qty, harga))
                    conn.commit()
                    st.success("Berhasil disubmit")
                except ValueError:
                    st.error("Harga")

    def display_data():
        c.execute('SELECT * FROM inventory')
        data = c.fetchall()
        df = pd.DataFrame(data, columns=["Nama Barang", 'qty', 'Harga'])
        # Format Harga column
        df['Harga'] = df['Harga'].apply(format_rupiah)
        st.write(df)

    def calculate_total_value():
        c.execute('SELECT SUM(Harga) FROM inventory')
        total_value = c.fetchone()[0]
        if total_value is None:
            total_value = 0
        st.header(f"Total Nilai Persediaan: {format_rupiah(total_value)}")

    def delete_data():
        row_to_delete = st.text_input("Masukkan nomor baris yang akan dihapus:")
        if st.button("Delete"):
            c.execute('DELETE FROM inventory WHERE rowid=?', (row_to_delete,))
            conn.commit()
            st.success("Baris berhasil dihapus")

    form()
    display_data()
    calculate_total_value()
    delete_data()
    conn.close()

# Now you can call the persediaan_page() function in your Streamlit app


# Now you can call the persediaan_page() function in your Streamlit app

# Now you can call the persediaan_page() function in your Streamlit app

def jurnal_umum_page():
    st.title("Jurnal Umum")
    conn = sqlite3.connect('Jurnal_Umum55.db')
    c = conn.cursor()

# Create table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS information
             (Tanggal TEXT, Account TEXT, Debit REAL, Kredit REAL)''')
    conn.commit()

    def format_rupiah(amount):
        return f"Rp {amount:,.0f}".replace(",", ".")

    def form():
        st.write("Isi Data Transaksi")
    with st.form(key="information_form"):
        Tanggal = st.date_input("Tanggal:", date.today())
        Debit_Account = st.text_input("Akun Debit:")
        Debit = st.text_input("Jumlah Debit (dalam Rupiah):")
        Kredit_Account = st.text_input("Akun Kredit:")
        Kredit = st.text_input("Jumlah Kredit (dalam Rupiah):")
        submission = st.form_submit_button(label="Submit")

    if submission:
        Debit = float(Debit.replace(".", "").replace(",", ".")) if Debit else 0.0
        Kredit = float(Kredit.replace(".", "").replace(",", ".")) if Kredit else 0.0

        try:
            Debit = float(Debit)
            Kredit = float(Kredit)
            if Debit != Kredit:
                st.error("Jumlah Debit dan Kredit harus sama!")
            else:
                # Insert debit entry
                c.execute("INSERT INTO information (Tanggal, Account, Debit, Kredit) VALUES (?, ?, ?, ?)", 
                          (Tanggal, Debit_Account, Debit, 0))
                # Insert credit entry
                c.execute("INSERT INTO information (Tanggal, Account, Debit, Kredit) VALUES (?, ?, ?, ?)", 
                          (Tanggal, Kredit_Account, 0, Kredit))
                conn.commit()
                st.success("Transaksi berhasil disimpan!")
        except ValueError:
            st.error("Jumlah Debit dan Kredit harus berupa angka!")

    def display_data():
        c.execute("SELECT rowid, * FROM information")
        data = c.fetchall()
        df = pd.DataFrame(data, columns=['RowID', 'Tanggal', 'Akun', 'Debit', 'Kredit'])
        st.write(df)

    def calculate_saldo():
        c.execute("SELECT SUM(Debit), SUM(Kredit) FROM information")
        saldo = c.fetchone()
        total_debit = saldo[0] if saldo[0] is not None else 0.0
        total_kredit = saldo[1] if saldo[1] is not None else 0.0
        st.write(f"Total Debit: {format_rupiah(total_debit)}")
        st.write(f"Total Kredit: {format_rupiah(total_kredit)}")
   
    def delete_data():
        row_to_delete = st.text_input("Masukkan nomor baris yang ingin dihapus:")
        if st.button("Hapus"):
            try:
                row_to_delete = int(row_to_delete)
                c.execute("DELETE FROM information WHERE rowid=?", (row_to_delete,))
                conn.commit()
                if c.rowcount > 0:
                 st.success("Baris berhasil dihapus!")
                else:
                 st.error("Nomor baris tidak ditemukan.")
            except ValueError:
                st.error("Masukkan nomor baris yang valid.")

    form()
    display_data()
    calculate_saldo()
    delete_data()
    conn.close()

def buku_besar_page():
    st.title("Buku Besar")

    # Initialize ledgers in session state if not already present
    if 'ledgers' not in st.session_state:
        st.session_state.ledgers = {f'Account {i}': pd.DataFrame(columns=['Date', 'Description', 'Debit', 'Credit']) for i in range(1, 16)}

    st.header('Tambah Transaksi')
    def format_rupiah(amount):
               return f"Rp {amount:,.0f}".replace(",", ".")

    
    with st.form('transaction_form'):
        date = st.date_input('Tanggal')
        description = st.text_input('Deskripsi')
        account = st.selectbox('Pilih Akun', [f'Account {i}' for i in range(1, 16)])
        debit = st.number_input('Debit (Dalam Rupiah)', min_value=0.0, step=1000.0)
        credit = st.number_input('Kredit (Dalam Rupiah)', min_value=0.0, step=1000.0)
        submitted = st.form_submit_button('Tambahkan')

    if submitted:
        new_transaction = pd.DataFrame({
                'Date': [date],
                'Description': [description],
                'Debit': [debit],
                'Credit': [credit]
            })
            
            # Cek apakah debit atau credit yang harus diisi
        if debit!= 0:
                st.session_state.ledgers[account] = pd.concat([st.session_state.ledgers[account], new_transaction], ignore_index=True)
                st.success(f'Transaksi berhasil ditambahkan ke {account}!')
        elif credit!= 0:
                new_transaction['Debit'] = None
                st.session_state.ledgers[account] = pd.concat([st.session_state.ledgers[account], new_transaction], ignore_index=True)
                st.success(f'Transaksi berhasil ditambahkan ke {account}!')
        else:
                st.warning('Anda harus mengisi debit atau credit!')
    
    if st.session_state.get('ledgers'):
        st.header('Buku Besar Per Akun')

        for account, ledger in st.session_state.ledgers.items():
            st.subheader(account)

            if not ledger.empty:
                st.dataframe(ledger)

                # Form to delete transactions
                st.subheader(f'Hapus Transaksi dari {account}')

                with st.form(key=f'delete_form_{account}'):
                    transaction_index = st.number_input(f'Masukkan nomor transaksi yang ingin dihapus dari {account}', min_value=0, max_value=len(ledger)-1, step=1, key=f'delete_{account}')
                    delete_button = st.form_submit_button(f'Hapus dari {account}')

                    if delete_button:
                        st.session_state.ledgers[account] = st.session_state.ledgers[account].drop(transaction_index).reset_index(drop=True)
                        st.success(f'Transaksi berhasil dihapus dari {account}!')
            else:
                st.write(f'Belum ada transaksi di {account}.')
    else:
        st.warning("Data buku besar tidak ditemukan. Silakan tambahkan transaksi.")


   

   

def neraca_saldo_page():
    st.title("Neraca Saldo")
    if 'ledgers' not in st.session_state:
        st.warning("Data buku besar tidak ditemukan. Silakan tambahkan transaksi di halaman Buku Besar.")

    # Perhitungan saldo akhir per akun dan pembentukan neraca saldo
    balances = {'Account': [], 'Debit (Dalam Ribu Rupiah)': [], 'Credit (Dalam Ribu Rupiah)': []}

    for account, ledger in st.session_state.ledgers.items():
        total_debit = ledger['Debit'].sum()
        total_credit = ledger['Credit'].sum()
        balance = total_debit - total_credit

        balances['Account'].append(account)
        if balance >= 0:
            balances['Debit (Dalam Ribu Rupiah)'].append(balance)
            balances['Credit (Dalam Ribu Rupiah)'].append(0.0)
        else:
            balances['Debit (Dalam Ribu Rupiah)'].append(0.0)
            balances['Credit (Dalam Ribu Rupiah)'].append(abs(balance))

    # Tampilkan neraca saldo
    balance_df = pd.DataFrame(balances)
    st.dataframe(balance_df)

    # Tampilkan total debit dan kredit
    total_debit = balance_df['Debit (Dalam Ribu Rupiah)'].sum()
    total_credit = balance_df['Credit (Dalam Ribu Rupiah)'].sum()

    st.subheader('Total')
    st.write(f'Total Debit: Rp {total_debit}')
    st.write(f'Total Kredit: Rp {total_credit}')

















def laporan_keuangan_page():
    st.title("Laporan Keuangan")
    
    # Set locale to Indonesian
    locale.setlocale(locale.LC_ALL, 'id_ID')

    # Sidebar untuk input data
    st.header("Input Data")
    tgl_laporan = st.date_input("Tanggal Laporan:")
    st.subheader("Laporan Laba Rugi")
    pendapatan_usaha = st.number_input("Pendapatan Usaha (IDR):", value=0, step=1000)
    biaya_bahan_baku = st.number_input("Biaya Bahan Baku (IDR):", value=0, step=1000)
    biaya_tenaga_kerja = st.number_input("Biaya Tenaga Kerja (IDR):", value=0, step=1000)
    biaya_overhead_pabrik = st.number_input("Biaya Overhead Pabrik (IDR):", value=0, step=1000)
    biaya_operasional = st.number_input("Biaya Operasional (IDR):", value=0, step=1000)
    
    st.subheader("Laporan Perubahan Modal")
    modal_awal = st.number_input("Modal Awal (IDR):", value=0, step=1000)
    akun_privasi = st.number_input("Akun Privasi (IDR):", value=0, step=1000)
    
    st.subheader("Laporan Posisi Keuangan")
    akun_aktiva = st.number_input("Akun Aktiva (IDR):", value=0, step=1000)
    
    st.subheader("Total Kewajiban dan Modal")
    hutang_usaha = st.number_input("Hutang Usaha (IDR):", value=0, step=1000)
    
    laba_bersih = pendapatan_usaha - (biaya_bahan_baku + biaya_tenaga_kerja + biaya_overhead_pabrik + biaya_operasional)
    total_modal = modal_awal + laba_bersih - akun_privasi
    total_aset = akun_aktiva
    total_kewajiban_modal = total_modal + hutang_usaha

    # Menampilkan laporan laba rugi
    st.header("Laporan Laba Rugi")
    st.write("Pendapatan Usaha:", locale.currency(pendapatan_usaha, grouping=True))
    st.write("Biaya Bahan Baku:", locale.currency(biaya_bahan_baku, grouping=True))
    st.write("Biaya Tenaga Kerja:", locale.currency(biaya_tenaga_kerja, grouping=True))
    st.write("Biaya Overhead Pabrik:", locale.currency(biaya_overhead_pabrik, grouping=True))
    st.write("Biaya Operasional:", locale.currency(biaya_operasional, grouping=True))
    st.write("Laba Bersih:", locale.currency(laba_bersih, grouping=True))

    # Menampilkan laporan perubahan modal
    st.header("Laporan Perubahan Modal")
    st.write("Modal Awal:", locale.currency(modal_awal, grouping=True))
    st.write("Akun Privasi:", locale.currency(akun_privasi, grouping=True))
    st.write("Laba Bersih Tahun Berjalan:", locale.currency(laba_bersih, grouping=True))
    st.write("Total Modal:", locale.currency(total_modal, grouping=True))

    # Menampilkan laporan posisi keuangan
    st.header("Laporan Posisi Keuangan")
    st.write("Akun Aktiva:", locale.currency(akun_aktiva, grouping=True))
    st.write("Total Aset:", locale.currency(total_aset, grouping=True))
    st.write("Hutang Usaha:", locale.currency(hutang_usaha, grouping=True))
    st.write("Total Kewajiban dan Modal:", locale.currency(total_kewajiban_modal, grouping=True))

    data = {
        'Tanggal Laporan': [tgl_laporan],
        'Pendapatan Usaha': [pendapatan_usaha],
        'Biaya Bahan Baku': [biaya_bahan_baku],
        'Biaya Tenaga Kerja': [biaya_tenaga_kerja],
        'Biaya Overhead Pabrik': [biaya_overhead_pabrik],
        'Biaya Operasional': [biaya_operasional],
        'Modal Awal': [modal_awal],
        'Akun Privasi': [akun_privasi],
        'Laba Bersih': [laba_bersih],
        'Akun Aktiva': [akun_aktiva],
        'Hutang Usaha': [hutang_usaha],
        'Total Kewajiban dan Modal': [total_kewajiban_modal]
    }

    return data












def main():
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    selected = option_menu(
        menu_title=None,  # required
        options=["Home", "Transaksi", "Persediaan", "Jurnal Umum", "Buku Besar", "Neraca Saldo", "Laporan Keuangan", "Logout"],  # required
        icons=["house", "list", "archive", "book", "book", "balance-scale", "file-text", "key"],  # optional
        menu_icon="cast",  # optional
        default_index=0,  # optional
        orientation="horizontal",
    )

    if selected == "Home":
        home_page()
    elif selected in ["Transaksi", "Persediaan", "Jurnal Umum", "Buku Besar", "Neraca Saldo", "Laporan Keuangan"]:
        if st.session_state["logged_in"]:
            if selected == "Transaksi":
                transaksi_page()
            elif selected == "Persediaan":
                persediaan_page()
            elif selected == "Jurnal Umum":
                jurnal_umum_page()
            elif selected == "Buku Besar":
                buku_besar_page()
            elif selected == "Neraca Saldo":
                neraca_saldo_page()
            elif selected == "Laporan Keuangan":
                laporan_keuangan_page()
        else:
            st.error("Anda harus login terlebih dahulu.")
            login()
    elif selected == "Logout":
        if st.session_state["logged_in"]:
            st.session_state["logged_in"] = False
            st.sidebar.success("Logout berhasil!")
            st.experimental_rerun()
        else:
            st.sidebar.info("Anda belum login.")

    

if __name__ == "_main_":
    main()
