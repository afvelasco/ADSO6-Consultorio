-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 05-11-2025 a las 01:46:58
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `consultorio06`
--
CREATE DATABASE IF NOT EXISTS consultorio06;
USE consultorio06;
-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `especialistas`
--

CREATE TABLE `especialistas` (
  `id_especialista` varchar(15) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `especialidad` varchar(25) NOT NULL,
  `foto` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `especialistas`
--

INSERT INTO `especialistas` (`id_especialista`, `nombre`, `especialidad`, `foto`) VALUES
('1006', 'Robles', 'Medico General', ''),
('1112', 'Mauricio Uriel ', 'Medico General', ''),
('1458', 'Rogelia Montoya Gonzales', 'Cardiologa', ''),
('152634', 'Jacinto Perez', 'General', ''),
('161616', 'Sandro Jimenez', 'Cirujano', ''),
('1649162648', 'uribe-chan', 'preso', ''),
('313131', 'María Paez', 'Urologa', ''),
('9876', 'Velasco', 'Cirujano', '');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pacientes`
--

CREATE TABLE `pacientes` (
  `id` varchar(15) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `celular` varchar(12) NOT NULL,
  `foto` varchar(30) NOT NULL,
  `borrado` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `pacientes`
--

INSERT INTO `pacientes` (`id`, `nombre`, `email`, `celular`, `foto`, `borrado`) VALUES
('0001', 'Jesus Creador', 'JesusQuitaPecados@gmail.com', '3011100101', '', 1),
('101010101010', 'Lionel Andres Messi Cuccittini', 'thegoat@gmail.com', '3178975466', '', 1),
('1109665705', 'OCHO', 'sebasgod@gmail.com', '3215225438', '', 1),
('11111111', 'Felipe Lotas', 'felipelotas777@gmail.com', '31313131331', 'U20250421192655.png', 1),
('1112150882', 'Jh Rodrigez Perez', 'goleado777@gmail.com', '666666666666', '', 1),
('1117017666', 'JARAMILLO, el amor de pau', 'nomegrite@gmail.com', '32424233', '', 1),
('1117017890', 'paula', 'no@gmail.com', '3233160758', '', 1),
('11316546068', 'para cuando SENALAND 2', 'senaland2@gmail.com', '32454313157', '', 1),
('1238238273', 'Pyther Parker', 'parker123@gmail.com', '3114274065', '', 1),
('13556966232', 'NUNCA', 'petroski@gmai.com', '45844666', '', 1),
('1414141414', 'Luchando los Diaz', 'jeisonramirez889@gmail.com', '3123665132', 'U20250421192921.jpg', 0),
('14544444', 'cristiano ORLANDO', 'golll@gamil.com', '545454', 'U20250421192723.jpg', 1),
('1455555', 'afvelasco', 'golll@gamil.com', '655588555', 'U20250421191705.png', 1),
('1527462728', 'POR QUE', 'juan.taborda@gmail.com', '3114274065', '', 1),
('16161616', 'NO HAY PLATA', 'CR7@email.com', '3000000', '', 1),
('16938063', 'JARAMILLO LE PRESTA', 'hernanbys@gmail.com', '3145619444', '', 1),
('18936789', 'PERO PA LLORAR', 'miltonprueba@gmail.com', '3145619444', '', 1),
('19191919191', 'Galloloko', 'kelokegalloloko@gmail.com', '3117768430', 'U20250421192722.jpg', 1),
('23262524', 'JARAMILLO BESO A PAULA', 'carlagonzales@gmail.com', '3186457854', '', 1),
('308382938', 'PRUEBAS??', 'homero@gmail.com', '3122343123', '', 1),
('313125062', 'MMM YA', 'pau@gmail.com', '3269871209', '', 1),
('31313131', 'Manuelita Saenz', 'msaenz@email.com', '3123121212', '', 1),
('34343434', 'Heriberto Jacome', 'jacome@mail.com', '3113113131', '', 1),
('3435363430', 'Andres Felipe ocoro pripra', 'paula.gon.@gmail.com', '3217765897', '', 1),
('3435363489', 'Alan, el amor de valentina', 'alan.h.paez@gmail.com', '3217765897', '', 1),
('4548895555', 'valentina, el amor de luis', '', '45669885662', '', 1),
('455555555555555', 'jacobo modul', '', '999999999999', '', 1),
('457894', 'Valentina Rangel', 'Valenrangel@email.com', '3212546978', 'U20250421192607.jpg', 1),
('57894568', 'Emili Silencio ', 'nohables@email.com', '1589754558', 'U20250421192749.jpg', 1),
('6666', 'ronaldo albeiro ocoro', 'MessiAlCali@gmail', '3333333333', '', 1),
('6666666666', 'jara puto', 'jarap@gmail.com', '000911', 'U20250421192821.jpeg', 1),
('7877787', 'NO SE QUIEN ES', 'HOLIII@gamil.com', '454545454', 'U20250421192826.jpg', 1),
('94949494', 'juan p', 'juanp@email.com', '3163163163', 'U20250421192448.jpg', 0),
('999666', 'mondongus', 'monguis@yimeil.kom', '3134645786', 'U20250421200035.bmp', 0),
('rpombo', 'Rafael Pombo', 'pombo@gmail.com', '3123121212', 'U20250303212357.jpg', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` varchar(30) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `contra` varchar(128) NOT NULL,
  `rol` int(11) NOT NULL,
  `borrado` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombre`, `contra`, `rol`, `borrado`) VALUES
('afvelasco', 'Andrés Velasco', 'd404559f602eab6fd602ac7680dacbfaadd13630335e951f097af3900e9de176b6db28512f2e000b9d04fba5133e8b1c6e8df59db3a8ab9d60be4b97cc9e81db', 0, 0);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `especialistas`
--
ALTER TABLE `especialistas`
  ADD PRIMARY KEY (`id_especialista`);

--
-- Indices de la tabla `pacientes`
--
ALTER TABLE `pacientes`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
