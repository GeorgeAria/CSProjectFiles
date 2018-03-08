-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Dec 12, 2015 at 01:02 PM
-- Server version: 5.5.44-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `cs320stu02`
--

-- --------------------------------------------------------

--
-- Table structure for table `quotes`
--

CREATE TABLE IF NOT EXISTS `quotes` (
  `author` mediumtext NOT NULL,
  `quote` mediumtext NOT NULL,
  `timesViewed` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `quotes`
--

INSERT INTO `quotes` (`author`, `quote`, `timesViewed`) VALUES
('Jane Austen', 'A large income is the best recipe for happiness I ever heard of.', 3),
('Walt Whitman', 'I celebrate myself, and sing myself.', 2),
('Alan Hollinghurst', 'All families are silly in their own way.', 2),
('George Washington', 'The greatest thing about Facebook, is that you can quote something and totally make up the source.', 1),
('Rev. Martin Luther King, Jr.', 'I hate it when people quote me on the internet, claiming I said things that I never actually said.', 1),
('Count Dracula', 'Wear sunscreen.', 1),
('Abraham Lincoln', 'The trouble with quotes on the Internet is that you never know if they are genuine.', 1),
('Caesar Augustus', 'One misquote is one too many already!', 1),
('Mark Twain', 'When in doubt, attribute quotes to Mark Twain.', 3),
('Oscar Wilde', 'The fabrication of Oscar Wilde quotes is among the noblest of endeavors.', 2);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
