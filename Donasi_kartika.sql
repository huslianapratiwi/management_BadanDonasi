-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 08, 2021 at 05:46 AM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Donasi_kartika`
--

-- --------------------------------------------------------

--
-- Table structure for table `Badan_amal`
--

CREATE TABLE `Badan_amal` (
  `id_company` varchar(10) NOT NULL,
  `username` varchar(15) DEFAULT NULL,
  `password` varchar(15) DEFAULT NULL,
  `alamat` varchar(30) DEFAULT NULL,
  `nama` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Badan_amal`
--

INSERT INTO `Badan_amal` (`id_company`, `username`, `password`, `alamat`, `nama`) VALUES
('1', 'toolop', 'sdkartika22', 'jalan nusa bangsa', 'Donasi Kartika'),
('2', 'armortitan', 'sdkartika22', 'jalan jalan', 'Donasi Saya');

-- --------------------------------------------------------

--
-- Table structure for table `Barang`
--

CREATE TABLE `Barang` (
  `id_donasi` varchar(10) NOT NULL,
  `jumlah` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Donasi`
--

CREATE TABLE `Donasi` (
  `id_donatur` varchar(10) DEFAULT NULL,
  `id_donasi` varchar(10) NOT NULL,
  `tgl_donasi` date DEFAULT NULL,
  `id_company` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Donatur`
--

CREATE TABLE `Donatur` (
  `id_donatur` varchar(10) NOT NULL,
  `username` varchar(20) NOT NULL,
  `Password` varchar(20) NOT NULL,
  `nama` varchar(30) NOT NULL,
  `alamat` varchar(40) DEFAULT NULL,
  `no_telepon` varchar(13) DEFAULT NULL,
  `tipe` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Donatur`
--

INSERT INTO `Donatur` (`id_donatur`, `username`, `Password`, `nama`, `alamat`, `no_telepon`, `tipe`) VALUES
('1', 'toolop', 'sdkartika22', 'Jalan nusa bangsa', 'rafi', '08123', 'Personal'),
('2', 'laras23', 'sdkartika22', 'Jalan Buntu', 'Laras Nurul Aulia', '081540867030', 'Organisasi');

-- --------------------------------------------------------

--
-- Table structure for table `Jenis_Barang`
--

CREATE TABLE `Jenis_Barang` (
  `id_donasi` varchar(10) DEFAULT NULL,
  `jenis` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Kotak_amal`
--

CREATE TABLE `Kotak_amal` (
  `id_kotak` varchar(10) NOT NULL,
  `id_company` varchar(10) DEFAULT NULL,
  `id_pegawai` varchar(6) DEFAULT NULL,
  `alamat` varchar(30) DEFAULT NULL,
  `jumlah_uang` int(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Pegawai`
--

CREATE TABLE `Pegawai` (
  `id_pegawai` varchar(6) NOT NULL,
  `nama` varchar(20) NOT NULL,
  `no_telepon` varchar(13) NOT NULL,
  `tgl_masuk` date NOT NULL,
  `id_company` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Pegawai`
--

INSERT INTO `Pegawai` (`id_pegawai`, `nama`, `no_telepon`, `tgl_masuk`, `id_company`) VALUES
('110', 'Rafi Arya', '08123755778', '2018-12-23', '1'),
('111', 'Laras', '081540867030', '2012-12-23', '1'),
('112', 'Tiwi', '081234567', '2020-10-12', '1');

-- --------------------------------------------------------

--
-- Table structure for table `Penerima`
--

CREATE TABLE `Penerima` (
  `id_pegawai` varchar(6) DEFAULT NULL,
  `id_company` varchar(10) DEFAULT NULL,
  `id_penerima` varchar(10) NOT NULL,
  `nama` varchar(20) DEFAULT NULL,
  `alamat` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Ponsel_penerima`
--

CREATE TABLE `Ponsel_penerima` (
  `id_penerima` varchar(10) DEFAULT NULL,
  `nomor_hp` varchar(13) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Uang`
--

CREATE TABLE `Uang` (
  `id_donasi` varchar(10) NOT NULL,
  `jumlah_total` int(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Badan_amal`
--
ALTER TABLE `Badan_amal`
  ADD PRIMARY KEY (`id_company`);

--
-- Indexes for table `Barang`
--
ALTER TABLE `Barang`
  ADD PRIMARY KEY (`id_donasi`);

--
-- Indexes for table `Donasi`
--
ALTER TABLE `Donasi`
  ADD PRIMARY KEY (`id_donasi`),
  ADD KEY `id_donatur` (`id_donatur`),
  ADD KEY `id_company` (`id_company`);

--
-- Indexes for table `Donatur`
--
ALTER TABLE `Donatur`
  ADD PRIMARY KEY (`id_donatur`);

--
-- Indexes for table `Jenis_Barang`
--
ALTER TABLE `Jenis_Barang`
  ADD KEY `id_donasi` (`id_donasi`);

--
-- Indexes for table `Kotak_amal`
--
ALTER TABLE `Kotak_amal`
  ADD PRIMARY KEY (`id_kotak`),
  ADD KEY `id_company` (`id_company`),
  ADD KEY `id_pegawai` (`id_pegawai`);

--
-- Indexes for table `Pegawai`
--
ALTER TABLE `Pegawai`
  ADD PRIMARY KEY (`id_pegawai`),
  ADD KEY `id_company` (`id_company`);

--
-- Indexes for table `Penerima`
--
ALTER TABLE `Penerima`
  ADD PRIMARY KEY (`id_penerima`),
  ADD KEY `id_pegawai` (`id_pegawai`),
  ADD KEY `id_company` (`id_company`);

--
-- Indexes for table `Ponsel_penerima`
--
ALTER TABLE `Ponsel_penerima`
  ADD KEY `id_penerima` (`id_penerima`);

--
-- Indexes for table `Uang`
--
ALTER TABLE `Uang`
  ADD PRIMARY KEY (`id_donasi`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Barang`
--
ALTER TABLE `Barang`
  ADD CONSTRAINT `Barang_ibfk_1` FOREIGN KEY (`id_donasi`) REFERENCES `Donasi` (`id_donasi`) ON UPDATE CASCADE;

--
-- Constraints for table `Donasi`
--
ALTER TABLE `Donasi`
  ADD CONSTRAINT `Donasi_ibfk_1` FOREIGN KEY (`id_donatur`) REFERENCES `Donatur` (`id_donatur`) ON UPDATE CASCADE,
  ADD CONSTRAINT `Donasi_ibfk_2` FOREIGN KEY (`id_company`) REFERENCES `Badan_amal` (`id_company`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Jenis_Barang`
--
ALTER TABLE `Jenis_Barang`
  ADD CONSTRAINT `Jenis_Barang_ibfk_1` FOREIGN KEY (`id_donasi`) REFERENCES `Barang` (`id_donasi`) ON UPDATE CASCADE;

--
-- Constraints for table `Kotak_amal`
--
ALTER TABLE `Kotak_amal`
  ADD CONSTRAINT `Kotak_amal_ibfk_1` FOREIGN KEY (`id_company`) REFERENCES `Badan_amal` (`id_company`) ON UPDATE CASCADE,
  ADD CONSTRAINT `Kotak_amal_ibfk_2` FOREIGN KEY (`id_pegawai`) REFERENCES `Pegawai` (`id_pegawai`) ON UPDATE CASCADE;

--
-- Constraints for table `Pegawai`
--
ALTER TABLE `Pegawai`
  ADD CONSTRAINT `Pegawai_ibfk_1` FOREIGN KEY (`id_company`) REFERENCES `Badan_amal` (`id_company`) ON UPDATE CASCADE;

--
-- Constraints for table `Penerima`
--
ALTER TABLE `Penerima`
  ADD CONSTRAINT `Penerima_ibfk_1` FOREIGN KEY (`id_pegawai`) REFERENCES `Pegawai` (`id_pegawai`) ON UPDATE CASCADE,
  ADD CONSTRAINT `Penerima_ibfk_2` FOREIGN KEY (`id_company`) REFERENCES `Badan_amal` (`id_company`) ON UPDATE CASCADE;

--
-- Constraints for table `Ponsel_penerima`
--
ALTER TABLE `Ponsel_penerima`
  ADD CONSTRAINT `Ponsel_penerima_ibfk_1` FOREIGN KEY (`id_penerima`) REFERENCES `Penerima` (`id_penerima`) ON UPDATE CASCADE;

--
-- Constraints for table `Uang`
--
ALTER TABLE `Uang`
  ADD CONSTRAINT `Uang_ibfk_1` FOREIGN KEY (`id_donasi`) REFERENCES `Donasi` (`id_donasi`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
