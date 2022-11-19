-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2022-11-19 03:52:23
-- 伺服器版本： 10.4.22-MariaDB
-- PHP 版本： 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫: `middletest`
--

-- --------------------------------------------------------

--
-- 資料表結構 `商家db`
--

CREATE TABLE `商家db` (
  `id` int(11) NOT NULL,
  `name` text COLLATE utf8_bin NOT NULL,
  `price` int(11) NOT NULL,
  `stock` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- 傾印資料表的資料 `商家db`
--

INSERT INTO `商家db` (`id`, `name`, `price`, `stock`) VALUES
(1, '一號貨', 100, 10);

-- --------------------------------------------------------

--
-- 資料表結構 `我的購物車`
--

CREATE TABLE `我的購物車` (
  `id` int(11) NOT NULL,
  `name` text COLLATE utf8_bin NOT NULL,
  `price` int(11) NOT NULL,
  `quantity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- 傾印資料表的資料 `我的購物車`
--

INSERT INTO `我的購物車` (`id`, `name`, `price`, `quantity`) VALUES
(1, '一號貨', 100, 5);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
