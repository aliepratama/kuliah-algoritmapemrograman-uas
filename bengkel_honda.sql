-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 17, 2023 at 03:59 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bengkel_honda`
--

-- --------------------------------------------------------

--
-- Table structure for table `db_akses`
--

CREATE TABLE `db_akses` (
  `id` int(20) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `nama` varchar(100) NOT NULL,
  `akses` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `db_akses`
--

INSERT INTO `db_akses` (`id`, `email`, `password`, `nama`, `akses`) VALUES
(13, 'user2@honda.id', '$2b$12$R5exVcX9CaV9YZ28qdU09eOCWZOlmDZUASJ0SK7UaU2Q9HPweIxIG', 'user2', 'user'),
(15, 'user1@honda.id', '$2b$12$AdlLE8ooHjMwyeWpPSp7WOB4y8jlO9BUa6.tLP1sSz2OGYNPg0YEW', 'user1', 'user'),
(16, 'admin@honda.id', '$2b$12$ZnjqUjJAC1GLtbklAXOzhOIInbPigz.AbnjGz5yEgPSmzT37RaqDW', 'admin', 'admin'),
(20, 'user3@honda.id', '$2b$12$r84dWptfYKfj2h8ucmXcjeFmaApoKXb1517LllzYUuXEiNSTgvx6.', 'user3', 'user');

-- --------------------------------------------------------

--
-- Table structure for table `db_kendaraan`
--

CREATE TABLE `db_kendaraan` (
  `id` int(20) NOT NULL,
  `id_user` int(20) NOT NULL,
  `nama_kendaraan` varchar(100) NOT NULL,
  `no_kendaraan` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `db_kendaraan`
--

INSERT INTO `db_kendaraan` (`id`, `id_user`, `nama_kendaraan`, `no_kendaraan`) VALUES
(1, 13, 'Honda Civic Turbo 2023', 'R 1234 R'),
(11, 15, 'Honda Brio 2020', 'AB 1111 BA'),
(12, 20, 'Honda Brio 2020', 'AB 1234 BA');

-- --------------------------------------------------------

--
-- Table structure for table `db_layanan`
--

CREATE TABLE `db_layanan` (
  `id` int(20) NOT NULL,
  `layanan` varchar(255) NOT NULL,
  `harga` varchar(20) NOT NULL,
  `status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `db_layanan`
--

INSERT INTO `db_layanan` (`id`, `layanan`, `harga`, `status`) VALUES
(3, 'Ganti Oli Mesin', '360000', 'ready'),
(4, 'Ganti Oli Transmisi', '125000', 'ready'),
(5, 'Minyak Rem', '30000', 'kosong'),
(6, 'Ganti Filter Oli', '45000', 'ready'),
(7, 'Ganti Busi', '90000', 'ready'),
(8, 'Ganti Filter Udara', '65000', 'ready'),
(9, 'Ganti AC Filter', '85000', 'kosong');

-- --------------------------------------------------------

--
-- Table structure for table `db_mekanik`
--

CREATE TABLE `db_mekanik` (
  `id` int(20) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `status` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `db_mekanik`
--

INSERT INTO `db_mekanik` (`id`, `nama`, `status`) VALUES
(1, 'null', 'ready'),
(2, 'Pratama', 'ready'),
(3, 'Putra', 'sibuk'),
(4, 'Alie', 'ready');

-- --------------------------------------------------------

--
-- Table structure for table `db_riwayat`
--

CREATE TABLE `db_riwayat` (
  `id` int(20) NOT NULL,
  `id_user` int(20) NOT NULL,
  `id_layanan` int(20) NOT NULL,
  `id_kendaraan` int(20) NOT NULL,
  `tanggal_booking` varchar(100) NOT NULL,
  `id_mekanik` int(20) NOT NULL,
  `status` varchar(20) NOT NULL,
  `tanggal_aktivitas` varchar(100) NOT NULL,
  `lunas` varchar(20) NOT NULL,
  `id_trx` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `db_riwayat`
--

INSERT INTO `db_riwayat` (`id`, `id_user`, `id_layanan`, `id_kendaraan`, `tanggal_booking`, `id_mekanik`, `status`, `tanggal_aktivitas`, `lunas`, `id_trx`) VALUES
(5, 13, 4, 1, '17-1-2023', 1, 'baru', '2023-01-17 19:28:59.681915', 'sudah', 13),
(6, 13, 5, 1, '17-1-2023', 1, 'selesai', '2023-01-17 19:29:06.881773', 'sudah', 14),
(7, 13, 6, 1, '17-1-2023', 2, 'selesai', '2023-01-17 19:29:35.603039', 'sudah', 15);

-- --------------------------------------------------------

--
-- Table structure for table `db_transaksi`
--

CREATE TABLE `db_transaksi` (
  `id` int(20) NOT NULL,
  `id_user` int(20) NOT NULL,
  `id_layanan` int(20) NOT NULL,
  `id_mekanik` int(20) NOT NULL,
  `tanggal_booking` varchar(50) NOT NULL,
  `status` varchar(20) NOT NULL,
  `lunas` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `db_transaksi`
--

INSERT INTO `db_transaksi` (`id`, `id_user`, `id_layanan`, `id_mekanik`, `tanggal_booking`, `status`, `lunas`) VALUES
(13, 13, 4, 2, '17-1-2023', 'selesai', 'sudah'),
(14, 13, 5, 2, '17-1-2023', 'selesai', 'sudah'),
(15, 13, 6, 2, '17-1-2023', 'selesai', 'sudah'),
(28, 20, 4, 1, '17-1-2023', 'baru', 'belum');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `db_akses`
--
ALTER TABLE `db_akses`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `db_kendaraan`
--
ALTER TABLE `db_kendaraan`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_akses` (`id_user`);

--
-- Indexes for table `db_layanan`
--
ALTER TABLE `db_layanan`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `db_mekanik`
--
ALTER TABLE `db_mekanik`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `db_riwayat`
--
ALTER TABLE `db_riwayat`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_user` (`id_user`),
  ADD KEY `id_layanan` (`id_layanan`),
  ADD KEY `id_mekanik` (`id_mekanik`),
  ADD KEY `id_kendaraan` (`id_kendaraan`),
  ADD KEY `id_trx` (`id_trx`);

--
-- Indexes for table `db_transaksi`
--
ALTER TABLE `db_transaksi`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_user` (`id_user`,`id_layanan`,`id_mekanik`),
  ADD KEY `id_mekanik` (`id_mekanik`),
  ADD KEY `id_layanan` (`id_layanan`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `db_akses`
--
ALTER TABLE `db_akses`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `db_kendaraan`
--
ALTER TABLE `db_kendaraan`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `db_layanan`
--
ALTER TABLE `db_layanan`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `db_mekanik`
--
ALTER TABLE `db_mekanik`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `db_riwayat`
--
ALTER TABLE `db_riwayat`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `db_transaksi`
--
ALTER TABLE `db_transaksi`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `db_kendaraan`
--
ALTER TABLE `db_kendaraan`
  ADD CONSTRAINT `db_kendaraan_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `db_akses` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Constraints for table `db_riwayat`
--
ALTER TABLE `db_riwayat`
  ADD CONSTRAINT `db_riwayat_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `db_akses` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `db_riwayat_ibfk_2` FOREIGN KEY (`id_kendaraan`) REFERENCES `db_kendaraan` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `db_riwayat_ibfk_4` FOREIGN KEY (`id_mekanik`) REFERENCES `db_mekanik` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `db_riwayat_ibfk_5` FOREIGN KEY (`id_layanan`) REFERENCES `db_layanan` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `db_riwayat_ibfk_6` FOREIGN KEY (`id_trx`) REFERENCES `db_transaksi` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `db_transaksi`
--
ALTER TABLE `db_transaksi`
  ADD CONSTRAINT `db_transaksi_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `db_akses` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `db_transaksi_ibfk_3` FOREIGN KEY (`id_mekanik`) REFERENCES `db_mekanik` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `db_transaksi_ibfk_4` FOREIGN KEY (`id_layanan`) REFERENCES `db_layanan` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
