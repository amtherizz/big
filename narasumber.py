import spacy

nlp = spacy.load("xx_ent_wiki_sm")  # Model multibahasa

def get_named_entities(text):
    doc = nlp(text)
    return [ent.text for ent in doc.ents if ent.label_ == "PER"]
print(get_named_entities("""

      Rabu, 2 Juli 2025 - 14:50:23 PM

Tentang Kami      Login
Logo

PT. Borneo Grafika Pariwara

Jl. Kapt Pierre Tendean, RT 02 No 9, Kelurahan Bontang Baru
Kecamatan Bontang, Kota Bontang, Kaltim - 75311

    HOME
    KALTIM
    POLITIK
    EKBIS
    NASIONAL
    ADVERTORIAL
    HUMANIORA
    HUKUM & KRIMINAL
    INFOGRAFIS

    Network

    Home
    Humaniora
    Profil 

Siswa SMPN 1 Bontang Kemal Sabet Juara 1 Nasional di Ajang Lomba Gambar Peta; Wakili Indonesia ke Kanada
Profil - M Rifki
11 April 2025
 
0 Comments
SHARE
Siswa SMPN 1 Bontang Kemal Sabet Juara 1 Nasional di Ajang Lomba Gambar Peta; Wakili Indonesia ke Kanada Kemal Al Arif Istiyono pelajar SMP Negeri 1 Bontang memamerkan hasil karya lukisnya yang mengantarnya menjadi juara pertama lomba gambar peta BIG. (Ist-Klik Kaltim)

BONTANG- Peserta didik SMP Negeri 1 Bontang Kemal Al Arif Istiyono berhasil menorehkan prestasi memukau. Dia sukses menjuarai lomba menggambar tingkat nasional yang diadakan oleh Badan Informasi Geospasial Republik Indonesia pada Maret 2025 lalu. 

Karya lukisnya berhasil memukau para juri hingga dinobatkan menjadi juara pertama kategori D di tingkat nasional. Ke depan karyanya akan kembali diperlombakan di ajang internasional  Gambar Peta Internasional Barbara Petchenik Award Cartographic Conference of The International Cartographic Association yang akan diselenggarakan di Kanada, 18–22 Agustus 2025.

Keahlian melukis Kemal sudah sedari dini terlihat, putra Dwi Bakti Istiyono ini memang gemar menggambar sejak duduk di bangku Sekolah Dasar (SD). 

Dari hasil karya sang putra Kemal berhasil menyabet beberapa trofi penghargaan dari berbagai tingkatan. Mulai lomba tingkat sekolah, kota, provinsi ataupun nasional. 

Baca Juga:
Mangkrak Setahun karena Kontraktor Tak Becus, Pembangunan SMP Negeri 1 Bontang Akhirnya Dilanjutkan Tahun Ini
Guru dan Murid SMP Negeri 1 Bontang Raih Prestasi Nasional, Didaulat Jadi Sahabat Inspiratif dan Sobat Bintang

"Alhamdulillah ini prestasi yang gemilang dari anak kami. Memang dia senang dan gemar menggambar. Belajarnya pun otodidak," ucap Dwi.

Sekolah Support

Prestasi demi prestasi yang diraih oleh putranya tak terlepas dari dukungan pihak Sekolah SMP Negeri 1 Bontang. Dwi bercerita dimana informasi lomba dari Badan Geospasial RI mengadakan lomba tingkat nasional secara online dari sang guru anak. 

Usai dapat informasi itu sang ayah menyiapkan peralatan gambar. Kemudian mengambil gawai untuk dipakai merekam dari nol proses menggambar. 

Setelah itu file itu dikirim dan berhasil mendapatkan juara peringkat pertama. Kepada sang anak darah seni pun mengalir. 

Dwi mengaku sang anak gemar melihat hasil potretnya. Karena Dwi gemar mencari tempat estetik untuk sekedar mencari foto. 

"Kalau saya memang senang foto. Nah anak saya mungkin darah seninya ke bidang menggambar. Jadi saya juga support," sambungnya. 

Pihak sekolah pun sangat mendukung peserta didiknya untuk mengembangksn potensi diluar akademik. Dwi berharap sang anak bisa mencatatkan prestasi gemilang di ajang perlombaan internasional. 

Curiculum Vitae (CV) 

Nama : Kemal Al Arif Istiyono
 Usia :  13 tahun
Asal sekolah : SMP Negeri 1 Siswa VIII
Putra dari : Dwi Bakti Istiyono

Prestasi yang berhasil diraih :

-Juara 2 , Lomba menggambar tingkat SD di Dinas Perpustakaan dan Kearsipan Kota Bontang, 2022

-Juara 1, Lomba gambar bucketive KFC Bontang, 2022

-Juara 2, Lomba menggambar Bontang Hijau tingkat SD di Lembah Permai, 2023

-Juara1, Lomba menggambar tingkat SD HUT Kota Bontang ke 24, Dinas Perpustakaan dan Kearsipan Kota Bontang 2023 

-Juara 1, Lomba menggambar tingkat SD
Fashion & Acoustic Competition Bontang 2023

-Juara 1, Lomba menggambar tingkat SD
Student Expo Bontang 2023

-Juara1 FLS2N cabang gambar bercerita tingkat SD, Dinas Pendidikan Kota Bontang 2023

-Juara1 FLS2N cabang gambar bercerita tingkat SD, Dinas Pendidikan Provinsi Kalimantan Timur 2023

-Juara 2, Lomba Cipta Karya Maskot KPU Bontang pada pemilihan walikota dan wakil walikota Bontang 2024

-Juara 1 Lomba menggambar tingkat SD "Road to Hari Konservasi Alam Nasional" Balai Taman Nasional Kutai, Bontang 2024

-Juara 2 Lomba melukis Bea Cukai Bontang pada hari peringatan Bea Cukai ke 78 thn 2024

-Terpilih 12 karya terbaik 2024, "Draw and Drive Your Imagination with DVCI" Mercedes Benz, PT. Daimler Commercial Vehicles Indonesia 

-Juara 3 Desain Ilustrasi Digital tingkat SMP. Lomba Seni Sanasini 2024 PKT Bontang 

-Juara 1 Kategori D (13-15 tahun) Lomba Gambar Peta Anak Nasional 2025 . Badan Geospasial Republik Indonesia dan menjadi salah satu terbaik pilihan juri yang akan mewakili Indonesia dalam Lomba Gambar Peta Internasional Barbara Petchenik Award di ajang International Cartographic Conference of The International Cartographic Association yang akan diselenggarakan di Kanada, 18-22 Agustus 2025.

Ikuti berita-berita terkini dari klikkaltim.com dengan mengetuk suka di halaman Facebook kami berikut ini:
TAG:

PRESTASI SISWA BONTANG ANAK BONTANG BERPRESTASI SMP NEGERI 1 BONTANG KEMAL AL ARIF ISTIYONO SISWA BERPRESTASI
SHARE
BERITA TERKAIT

    Mangkrak Setahun karena Kontraktor Tak Becus, Pembangunan SMP Negeri 1 Bontang Akhirnya Dilanjutkan Tahun Ini
    Guru dan Murid SMP Negeri 1 Bontang Raih Prestasi Nasional, Didaulat Jadi Sahabat Inspiratif dan Sobat Bintang
    Tinjau Proyek Mangkrak SMP Negeri 1 Bontang, Dewan Sayangkan Gedung Baru Bisa Dilanjutkan 2025
    Proyek Gagal Rampung; Siswa SMPN 1 Bontang Giliran Pakai Ruang Kelas, Jam Belajar Dikurangi



TINGGALKAN KOMENTAR
Terpopuler!

    Mulai 2026 Tak Ada Lagi Loker; Disnaker Bontang Langsung Salurkan Pekerja ke Perusahaan
    1
    Mulai 2026 Tak Ada Lagi Loker; Disnaker Bontang Langsung Salurkan Pekerja ke Perusahaan
    Bontang    4261 Kali    2 hari lalu
    2
    Raup Untung Rp 19 Miliar dari Deposito Tahun Lalu; Pemkot Bakal Jajal Kembali Deposito 2025
    Bontang    3852 Kali    5 hari lalu
    3
    3 Bulan Belum Jalan; Akhirnya Kontraktor Mulai Garap Proyek Drainase Rp 22 Miliar di Pisangan, Material Dipesan dari Surabaya
    Bontang    3325 Kali    5 hari lalu
    4
    Ribut-Ribut Anggaran Hibah Atlet Rp 11 Miliar Tak Cair; Mantan Kadisporapar-Ekraf Angkat Bicara
    Bontang    2573 Kali    5 hari lalu
    5
    Pulau Beras Basah Jorok dan Kumuh; Terpal Disewakan Rp 100 Ribu, Sampah Berserakan hingga Nihil PAD
    Bontang    2344 Kali    2 hari lalu

Hubungi Kami
PT. Borneo Grafika Pariwara
Jl. Kapt Pierre Tendean, RT 02 No 9, Kelurahan Bontang Baru
Kecamatan Bontang, Kota Bontang
Kaltim - Indonesia, Kode Pos 75311
Telp: (0548) 3036317 - PIC: Markiyanto (0822-1479-3556)
Ikuti Kami
Official Partner
Suara.com
Tentang Kami Info Iklan Disclaimer Kode Etik Syarat & Ketentuan Kebijakan Privasi
Logo Putih
2025 © PT Borneo Grafika Pariwara. All Right Reserved.
"""))