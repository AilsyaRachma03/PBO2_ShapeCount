-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 12 Jun 2021 pada 14.09
-- Versi server: 10.4.17-MariaDB
-- Versi PHP: 7.4.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pbo`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `bangun`
--

CREATE TABLE `bangun` (
  `id_bangun` int(2) NOT NULL,
  `nama_bangun` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=ucs2;

--
-- Dumping data untuk tabel `bangun`
--

INSERT INTO `bangun` (`id_bangun`, `nama_bangun`) VALUES
(1, 'Persegi'),
(2, 'Persegi Panjang'),
(3, 'Belah Ketupat'),
(4, 'Layang-Layang'),
(5, 'Lingkaran'),
(6, 'Segitiga'),
(7, 'Trapesium'),
(8, 'Jajar Genjang'),
(9, 'Kubus'),
(10, 'Balok'),
(11, 'Prisma Segitiga'),
(12, 'Prisma Segiempat'),
(13, 'Kerucut'),
(14, 'Bola'),
(15, 'Limas Segiempat'),
(16, 'Tabung');

-- --------------------------------------------------------

--
-- Struktur dari tabel `b_datar`
--

CREATE TABLE `b_datar` (
  `id_d` int(8) NOT NULL,
  `id_bangun` int(20) NOT NULL,
  `r_keliling` varchar(30) NOT NULL,
  `r_luas` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `b_datar`
--

INSERT INTO `b_datar` (`id_d`, `id_bangun`, `r_keliling`, `r_luas`) VALUES
(1, 1, 'K = 4 x s', 'L = s x s'),
(2, 2, 'K  = 2 x (p + l)', 'L = p x l'),
(3, 3, 'K = 4 x s', 'L = ½ × d1 × d2'),
(4, 4, 'K = AB + BC + CD + DA', 'L = ½ × d1 × d2'),
(5, 5, 'K = π x d', 'L = π x r²'),
(6, 6, 'K = a + b + c', 'L = ½ x a x t'),
(7, 7, 'K = AB + BC + CD + DA', 'L = ½(d1+d2)t'),
(8, 8, 'K = 2 × (a + b)', 'L = a × t');

-- --------------------------------------------------------

--
-- Struktur dari tabel `b_ruang`
--

CREATE TABLE `b_ruang` (
  `id_b` int(8) NOT NULL,
  `id_bangun` int(20) NOT NULL,
  `luas_p` varchar(60) NOT NULL,
  `volume` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `b_ruang`
--

INSERT INTO `b_ruang` (`id_b`, `id_bangun`, `luas_p`, `volume`) VALUES
(1, 9, 'L = 6 x (s x s)', 'V =  s x s x s'),
(2, 11, 'L = Ka x t + 2 x La', 'V = Luas Alas x t'),
(3, 13, 'L = π x r x (r + s) ', 'V = 1/3 x π x r² x t'),
(4, 15, 'L = Luas Alas + Luas Segitiga Sisi Tegak', 'V = 1/3 x Luas Alas '),
(5, 10, 'L = 2 x (pl + lt + pt)', 'V = p x l x t'),
(6, 12, 'L = 2 x (pl + lt + pt)', 'V = p x l x t'),
(7, 14, 'L = 4 x π x r²', 'V = 4/3 x π x r³'),
(8, 16, 'L = 2π r t + 2π r²', 'V = π x r² x t');

-- --------------------------------------------------------

--
-- Struktur dari tabel `catatan`
--

CREATE TABLE `catatan` (
  `id_catatan` int(2) NOT NULL,
  `deadline` varchar(60) NOT NULL,
  `catatan_pr` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=ucs2;

--
-- Dumping data untuk tabel `catatan`
--

INSERT INTO `catatan` (`id_catatan`, `deadline`, `catatan_pr`) VALUES
(1, 'Senin, 14 Juni 2021', 'Tugas Matematika, Buku Paket Halaman 12'),
(2, 'Selasa, 15 Juni 2021', 'Tugas IPS, Buku Paket Halaman 17'),
(3, 'Rabu, 16 Juni 2021', 'Tugas IPA, Buku Paket Halaman 19'),
(4, 'Kamis, 17 Juni 2021', 'Tugas Bahasa Indonesia, Buku Paket Halaman 15'),
(5, 'Jum\'at, 18 Juni 2021', 'Tugas Bahasa Inggris, Buku Paket Halaman 12'),
(6, 'Senin, 21 Juni 2021', 'Tugas Basa Jawa, Buku Paket Halaman 12'),
(7, 'Selasa, 22 Juni 2021', 'Tugas Olahraga, Buku Paket Halaman 12'),
(8, 'Rabu, 23 Juni 2021', 'Tugas IPA, Buku Paket Halaman 33'),
(9, 'Kamis, 24 Juni 2021', 'Tugas Bahasa Indonesia, Buku Paket Halaman 44'),
(10, 'Jum\'at, 25 Juni 2021', 'Tugas Bahasa Indonesia, Buat Puisi'),
(14, 'Minggu, 11 Juni 2021', 'Tugas IPA, Buku Paket Halaman 12'),
(15, 'Sabtu, 12 Juni 2021', 'Tugas 12'),
(16, 'Sabtu, 12 Juni 2021', 'Tugas 2');

-- --------------------------------------------------------

--
-- Struktur dari tabel `shape`
--

CREATE TABLE `shape` (
  `id` int(6) NOT NULL,
  `nama` varchar(60) NOT NULL,
  `alamat` varchar(30) NOT NULL,
  `email` varchar(60) NOT NULL,
  `username` varchar(10) NOT NULL,
  `password` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `shape`
--

INSERT INTO `shape` (`id`, `nama`, `alamat`, `email`, `username`, `password`) VALUES
(1, 'Ahsan Hilmi', 'Tuban', 'ahsan@gmail.com', 'ahsan', 'admin'),
(2, 'Firra Andriani', 'Blitar', 'firra.andriani22@gmaill.com', 'firra1234', '1234'),
(3, 'Rachma Ailsya', 'Bojonegoro', 'RachmaCantik@gmaill.com', 'rachma', 'cantik'),
(4, 'Fitria Anggraeni', 'Blitar', 'fitria@gmail.com', 'fitria1234', 'fitria'),
(5, 'Nana Wijayanto', 'Bandung', 'nana.wijayanto@gmail.com', 'nana1234', '1234'),
(6, 'Labib Mahya', 'Banyuwangi', 'labib@gmail.com', 'labib', '1234'),
(7, 'Mas Firman', 'Jember', 'masFirma@gmail.com', 'firman1', '1234'),
(8, 'Ibnu Qomaril Huda', 'Blitar', 'ibnuqmaril@gmail.com', 'ibnu', '1234');

-- --------------------------------------------------------

--
-- Struktur dari tabel `s_datar`
--

CREATE TABLE `s_datar` (
  `id_sd` int(8) NOT NULL,
  `id_bangun` int(20) NOT NULL,
  `sisi` int(11) NOT NULL,
  `sudut` int(11) NOT NULL,
  `simetri_putar` int(11) NOT NULL,
  `diagonal` int(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `s_datar`
--

INSERT INTO `s_datar` (`id_sd`, `id_bangun`, `sisi`, `sudut`, `simetri_putar`, `diagonal`) VALUES
(1, 1, 4, 4, 4, 2),
(2, 2, 4, 4, 2, 2),
(3, 3, 4, 4, 2, 2),
(4, 4, 4, 4, 0, 2),
(5, 5, 0, 0, 0, 0),
(6, 6, 3, 3, 3, 0),
(7, 7, 4, 4, 0, 0),
(8, 8, 4, 4, 0, 2);

-- --------------------------------------------------------

--
-- Struktur dari tabel `s_ruang`
--

CREATE TABLE `s_ruang` (
  `id_sr` int(8) NOT NULL,
  `id_bangun` int(20) NOT NULL,
  `sisi` int(11) NOT NULL,
  `rusuk` int(11) NOT NULL,
  `sudut` int(11) NOT NULL,
  `d_sisi` int(11) NOT NULL,
  `d_ruang` int(11) NOT NULL,
  `bdg_diagonal` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `s_ruang`
--

INSERT INTO `s_ruang` (`id_sr`, `id_bangun`, `sisi`, `rusuk`, `sudut`, `d_sisi`, `d_ruang`, `bdg_diagonal`) VALUES
(1, 9, 6, 12, 8, 12, 4, 6),
(2, 11, 5, 9, 6, 6, 4, 5),
(3, 13, 2, 1, 1, 0, 0, 2),
(4, 15, 5, 8, 5, 2, 0, 5),
(5, 10, 6, 12, 8, 12, 4, 6),
(6, 12, 6, 12, 8, 12, 6, 6),
(7, 14, 1, 0, 0, 0, 0, 1),
(8, 16, 3, 2, 0, 0, 0, 3);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `bangun`
--
ALTER TABLE `bangun`
  ADD PRIMARY KEY (`id_bangun`);

--
-- Indeks untuk tabel `b_datar`
--
ALTER TABLE `b_datar`
  ADD PRIMARY KEY (`id_d`),
  ADD KEY `id_bangun` (`id_bangun`);

--
-- Indeks untuk tabel `b_ruang`
--
ALTER TABLE `b_ruang`
  ADD PRIMARY KEY (`id_b`),
  ADD KEY `id_bangun` (`id_bangun`);

--
-- Indeks untuk tabel `catatan`
--
ALTER TABLE `catatan`
  ADD PRIMARY KEY (`id_catatan`);

--
-- Indeks untuk tabel `shape`
--
ALTER TABLE `shape`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `s_datar`
--
ALTER TABLE `s_datar`
  ADD PRIMARY KEY (`id_sd`),
  ADD KEY `id_bangun` (`id_bangun`);

--
-- Indeks untuk tabel `s_ruang`
--
ALTER TABLE `s_ruang`
  ADD PRIMARY KEY (`id_sr`),
  ADD KEY `id_bangun` (`id_bangun`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `bangun`
--
ALTER TABLE `bangun`
  MODIFY `id_bangun` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT untuk tabel `b_datar`
--
ALTER TABLE `b_datar`
  MODIFY `id_d` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT untuk tabel `b_ruang`
--
ALTER TABLE `b_ruang`
  MODIFY `id_b` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT untuk tabel `catatan`
--
ALTER TABLE `catatan`
  MODIFY `id_catatan` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT untuk tabel `shape`
--
ALTER TABLE `shape`
  MODIFY `id` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT untuk tabel `s_datar`
--
ALTER TABLE `s_datar`
  MODIFY `id_sd` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT untuk tabel `s_ruang`
--
ALTER TABLE `s_ruang`
  MODIFY `id_sr` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `b_datar`
--
ALTER TABLE `b_datar`
  ADD CONSTRAINT `b_datar_ibfk_1` FOREIGN KEY (`id_bangun`) REFERENCES `bangun` (`id_bangun`);

--
-- Ketidakleluasaan untuk tabel `b_ruang`
--
ALTER TABLE `b_ruang`
  ADD CONSTRAINT `b_ruang_ibfk_1` FOREIGN KEY (`id_bangun`) REFERENCES `bangun` (`id_bangun`);

--
-- Ketidakleluasaan untuk tabel `s_datar`
--
ALTER TABLE `s_datar`
  ADD CONSTRAINT `s_datar_ibfk_1` FOREIGN KEY (`id_bangun`) REFERENCES `bangun` (`id_bangun`);

--
-- Ketidakleluasaan untuk tabel `s_ruang`
--
ALTER TABLE `s_ruang`
  ADD CONSTRAINT `s_ruang_ibfk_1` FOREIGN KEY (`id_bangun`) REFERENCES `bangun` (`id_bangun`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
