--
-- Base de données : `scuti`
--

-- ----------------------------------------------------------------------------------------------------------------

--
-- Structure de la table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `mail` varchar(255) NOT NULL,
  `auth_ticket` varchar(255) NOT NULL,
  `rank` int(11) NOT NULL DEFAULT 1,
  `credits` int(11) NOT NULL DEFAULT 100,
  `pixels` int(11) NOT NULL DEFAULT 0,
  `shells` int(11) NOT NULL DEFAULT 0,
  `look` varchar(255) NOT NULL DEFAULT 'hr-115-42.hd-190-1.ch-215-62.lg-285-91.sh-290-62',
  `gender` enum('M','F') NOT NULL,
  `motto` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `mail`, `auth_ticket`, `rank`, `credits`, `pixels`, `shells`, `look`, `gender`, `motto`) VALUES
(1, 'Tig3r', '', 'quentingarot06@gmail.com', 'sso', 1, 100, 0, 0, 'hr-115-42.hd-190-1.ch-215-62.lg-285-91.sh-290-62	', 'M', 'Scuti :p');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

-- ----------------------------------------------------------------------------------------------------------------

--
-- Structure de la table `room_models`
--

CREATE TABLE `room_models` (
  `id` varchar(100) NOT NULL,
  `door_x` int(11) NOT NULL,
  `door_y` int(11) NOT NULL,
  `door_z` double NOT NULL,
  `door_dir` int(4) NOT NULL DEFAULT 2,
  `heightmap` text NOT NULL,
  `club_only` enum('0','1') NOT NULL DEFAULT '0'
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Déchargement des données de la table `room_models`
--

INSERT INTO `room_models` (`id`, `door_x`, `door_y`, `door_z`, `door_dir`, `heightmap`, `club_only`) VALUES
('model_a', 3, 5, 0, 2, 'xxxxxxxxxxxx\r\nxxxx00000000\r\nxxxx00000000\r\nxxxx00000000\r\nxxxx00000000\r\nxxxx00000000\r\nxxxx00000000\r\nxxxx00000000\r\nxxxx00000000\r\nxxxx00000000\r\nxxxx00000000\r\nxxxx00000000\r\nxxxx00000000\r\nxxxx00000000\r\nxxxxxxxxxxxx\r\nxxxxxxxxxxxx', '0'),
('model_b', 0, 5, 0, 2, 'xxxxxxxxxxxx\r\nxxxxx0000000\r\nxxxxx0000000\r\nxxxxx0000000\r\nxxxxx0000000\r\nx00000000000\r\nx00000000000\r\nx00000000000\r\nx00000000000\r\nx00000000000\r\nx00000000000\r\nxxxxxxxxxxxx\r\nxxxxxxxxxxxx\r\nxxxxxxxxxxxx\r\nxxxxxxxxxxxx\r\nxxxxxxxxxxxx', '0'),
('model_c', 4, 7, 0, 2, 'xxxxxxxxxxxx\r\nxxxxxxxxxxxx\r\nxxxxxxxxxxxx\r\nxxxxxxxxxxxx\r\nxxxxxxxxxxxx\r\nxxxxx000000x\r\nxxxxx000000x\r\nxxxxx000000x\r\nxxxxx000000x\r\nxxxxx000000x\r\nxxxxx000000x\r\nxxxxxxxxxxxx\r\nxxxxxxxxxxxx\r\nxxxxxxxxxxxx\r\nxxxxxxxxxxxx\r\nxxxxxxxxxxxx', '0'),
('model_d', 4, 7, 0, 2, 'xxxxxxxxxxxx\r\nxxxxx000000x\r\nxxxxx000000x\r\nxxxxx000000x\r\nxxxxx000000x\r\nxxxxx000000x\r\nxxxxx000000x\r\nxxxxx000000x\r\nxxxxx000000x\r\nxxxxx000000x\r\nxxxxx000000x\r\nxxxxx000000x\r\nxxxxx000000x\r\nxxxxx000000x\r\nxxxxx000000x\r\nxxxxxxxxxxxx', '0'),
('model_e', 1, 5, 0, 2, 'xxxxxxxxxxxx\r\nxxxxxxxxxxxx\r\nxxxxxxxxxxxx\r\nxx0000000000\r\nxx0000000000\r\nxx0000000000\r\nxx0000000000\r\nxx0000000000\r\nxx0000000000\r\nxx0000000000\r\nxx0000000000\r\nxxxxxxxxxxxx\r\nxxxxxxxxxxxx\r\nxxxxxxxxxxxx\r\nxxxxxxxxxxxx\r\nxxxxxxxxxxxx', '0'),
('model_f', 2, 5, 0, 2, 'xxxxxxxxxxxx\r\nxxxxxxx0000x\r\nxxxxxxx0000x\r\nxxx00000000x\r\nxxx00000000x\r\nxxx00000000x\r\nxxx00000000x\r\nx0000000000x\r\nx0000000000x\r\nx0000000000x\r\nx0000000000x\r\nxxxxxxxxxxxx\r\nxxxxxxxxxxxx\r\nxxxxxxxxxxxx\r\nxxxxxxxxxxxx\r\nxxxxxxxxxxxx', '0'),
('model_i', 0, 10, 0, 2, 'xxxxxxxxxxxxxxxxx\r\nx0000000000000000\r\nx0000000000000000\r\nx0000000000000000\r\nx0000000000000000\r\nx0000000000000000\r\nx0000000000000000\r\nx0000000000000000\r\nx0000000000000000\r\nx0000000000000000\r\nx0000000000000000\r\nx0000000000000000\r\nx0000000000000000\r\nx0000000000000000\r\nx0000000000000000\r\nx0000000000000000\r\nx0000000000000000\r\nx0000000000000000\r\nx0000000000000000\r\nx0000000000000000\r\nx0000000000000000\r\nx0000000000000000\r\nx0000000000000000\r\nx0000000000000000\r\nx0000000000000000\r\nx0000000000000000\r\nx0000000000000000\r\nxxxxxxxxxxxxxxxxx', '0'),
('model_j', 0, 10, 0, 2, 'xxxxxxxxxxxxxxxxxxxxx\r\nxxxxxxxxxxx0000000000\r\nxxxxxxxxxxx0000000000\r\nxxxxxxxxxxx0000000000\r\nxxxxxxxxxxx0000000000\r\nxxxxxxxxxxx0000000000\r\nxxxxxxxxxxx0000000000\r\nx00000000000000000000\r\nx00000000000000000000\r\nx00000000000000000000\r\nx00000000000000000000\r\nx00000000000000000000\r\nx00000000000000000000\r\nx00000000000000000000\r\nx00000000000000000000\r\nx00000000000000000000\r\nx00000000000000000000\r\nx0000000000xxxxxxxxxx\r\nx0000000000xxxxxxxxxx\r\nx0000000000xxxxxxxxxx\r\nx0000000000xxxxxxxxxx\r\nx0000000000xxxxxxxxxx\r\nx0000000000xxxxxxxxxx\r\nxxxxxxxxxxxxxxxxxxxxx', '0'),
('model_k', 0, 13, 0, 2, 'xxxxxxxxxxxxxxxxxxxxxxxxx\r\nxxxxxxxxxxxxxxxxx00000000\r\nxxxxxxxxxxxxxxxxx00000000\r\nxxxxxxxxxxxxxxxxx00000000\r\nxxxxxxxxxxxxxxxxx00000000\r\nxxxxxxxxx0000000000000000\r\nxxxxxxxxx0000000000000000\r\nxxxxxxxxx0000000000000000\r\nxxxxxxxxx0000000000000000\r\nx000000000000000000000000\r\nx000000000000000000000000\r\nx000000000000000000000000\r\nx000000000000000000000000\r\nx000000000000000000000000\r\nx000000000000000000000000\r\nx000000000000000000000000\r\nx000000000000000000000000\r\nxxxxxxxxx0000000000000000\r\nxxxxxxxxx0000000000000000\r\nxxxxxxxxx0000000000000000\r\nxxxxxxxxx0000000000000000\r\nxxxxxxxxx0000000000000000\r\nxxxxxxxxx0000000000000000\r\nxxxxxxxxx0000000000000000\r\nxxxxxxxxx0000000000000000\r\nxxxxxxxxx0000000000000000\r\nxxxxxxxxx0000000000000000\r\nxxxxxxxxxxxxxxxxxxxxxxxxx', '0'),
('model_l', 0, 16, 0, 2, 'xxxxxxxxxxxxxxxxxxxxx\r\nx00000000000000000000\r\nx00000000000000000000\r\nx00000000000000000000\r\nx00000000000000000000\r\nx00000000000000000000\r\nx00000000000000000000\r\nx00000000000000000000\r\nx00000000000000000000\r\nx00000000xxxx00000000\r\nx00000000xxxx00000000\r\nx00000000xxxx00000000\r\nx00000000xxxx00000000\r\nx00000000xxxx00000000\r\nx00000000xxxx00000000\r\nx00000000xxxx00000000\r\nx00000000xxxx00000000\r\nx00000000xxxx00000000\r\nx00000000xxxx00000000\r\nx00000000xxxx00000000\r\nx00000000xxxx00000000\r\nxxxxxxxxxxxxxxxxxxxxx', '0'),
('model_m', 0, 15, 0, 2, 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\nxxxxxxxxxxx00000000xxxxxxxxxx\r\nxxxxxxxxxxx00000000xxxxxxxxxx\r\nxxxxxxxxxxx00000000xxxxxxxxxx\r\nxxxxxxxxxxx00000000xxxxxxxxxx\r\nxxxxxxxxxxx00000000xxxxxxxxxx\r\nxxxxxxxxxxx00000000xxxxxxxxxx\r\nxxxxxxxxxxx00000000xxxxxxxxxx\r\nxxxxxxxxxxx00000000xxxxxxxxxx\r\nxxxxxxxxxxx00000000xxxxxxxxxx\r\nxxxxxxxxxxx00000000xxxxxxxxxx\r\nx0000000000000000000000000000\r\nx0000000000000000000000000000\r\nx0000000000000000000000000000\r\nx0000000000000000000000000000\r\nx0000000000000000000000000000\r\nx0000000000000000000000000000\r\nx0000000000000000000000000000\r\nx0000000000000000000000000000\r\nxxxxxxxxxxx00000000xxxxxxxxxx\r\nxxxxxxxxxxx00000000xxxxxxxxxx\r\nxxxxxxxxxxx00000000xxxxxxxxxx\r\nxxxxxxxxxxx00000000xxxxxxxxxx\r\nxxxxxxxxxxx00000000xxxxxxxxxx\r\nxxxxxxxxxxx00000000xxxxxxxxxx\r\nxxxxxxxxxxx00000000xxxxxxxxxx\r\nxxxxxxxxxxx00000000xxxxxxxxxx\r\nxxxxxxxxxxx00000000xxxxxxxxxx\r\nxxxxxxxxxxx00000000xxxxxxxxxx\r\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', '0'),
('model_n', 0, 16, 0, 2, 'xxxxxxxxxxxxxxxxxxxxx\r\nx00000000000000000000\r\nx00000000000000000000\r\nx00000000000000000000\r\nx00000000000000000000\r\nx00000000000000000000\r\nx00000000000000000000\r\nx000000xxxxxxxx000000\r\nx000000x000000x000000\r\nx000000x000000x000000\r\nx000000x000000x000000\r\nx000000x000000x000000\r\nx000000x000000x000000\r\nx000000x000000x000000\r\nx000000xxxxxxxx000000\r\nx00000000000000000000\r\nx00000000000000000000\r\nx00000000000000000000\r\nx00000000000000000000\r\nx00000000000000000000\r\nx00000000000000000000\r\nxxxxxxxxxxxxxxxxxxxxx', '0'),
('model_g', 1, 7, 1, 2, 'xxxxxxxxxxxx\r\nxxxxxxxxxxxx\r\nxxxxxxx00000\r\nxxxxxxx00000\r\nxxxxxxx00000\r\nxx1111000000\r\nxx1111000000\r\nxx1111000000\r\nxx1111000000\r\nxx1111000000\r\nxxxxxxx00000\r\nxxxxxxx00000\r\nxxxxxxx00000\r\nxxxxxxxxxxxx\r\nxxxxxxxxxxxx\r\nxxxxxxxxxxxx\r\nxxxxxxxxxxxx', '1'),
('model_q', 10, 4, 2, 2, 'xxxxxxxxxxxxxxxxxxx\r\nxxxxxxxxxxx22222222\r\nxxxxxxxxxxx22222222\r\nxxxxxxxxxxx22222222\r\nxxxxxxxxxxx22222222\r\nxxxxxxxxxxx22222222\r\nxxxxxxxxxxx22222222\r\nx222222222222222222\r\nx222222222222222222\r\nx222222222222222222\r\nx222222222222222222\r\nx222222222222222222\r\nx222222222222222222\r\nx2222xxxxxxxxxxxxxx\r\nx2222xxxxxxxxxxxxxx\r\nx2222211111xx000000\r\nx222221111110000000\r\nx222221111110000000\r\nx2222211111xx000000\r\nxx22xxx1111xxxxxxxx\r\nxx11xxx1111xxxxxxxx\r\nx1111xx1111xx000000\r\nx1111xx111110000000\r\nx1111xx111110000000\r\nx1111xx1111xx000000\r\nxxxxxxxxxxxxxxxxxxx', '1'),
('model_o', 0, 18, 1, 2, 'xxxxxxxxxxxxxxxxxxxxxxxxx\r\nxxxxxxxxxxxxx11111111xxxx\r\nxxxxxxxxxxxxx11111111xxxx\r\nxxxxxxxxxxxxx11111111xxxx\r\nxxxxxxxxxxxxx11111111xxxx\r\nxxxxxxxxxxxxx11111111xxxx\r\nxxxxxxxxxxxxx11111111xxxx\r\nxxxxxxxxxxxxx11111111xxxx\r\nxxxxxxxxxxxxx00000000xxxx\r\nxxxxxxxxx0000000000000000\r\nxxxxxxxxx0000000000000000\r\nxxxxxxxxx0000000000000000\r\nxxxxxxxxx0000000000000000\r\nxxxxxxxxx0000000000000000\r\nxxxxxxxxx0000000000000000\r\nx111111100000000000000000\r\nx111111100000000000000000\r\nx111111100000000000000000\r\nx111111100000000000000000\r\nx111111100000000000000000\r\nx111111100000000000000000\r\nx111111100000000000000000\r\nx111111100000000000000000\r\nxxxxxxxxx0000000000000000\r\nxxxxxxxxx0000000000000000\r\nxxxxxxxxx0000000000000000\r\nxxxxxxxxx0000000000000000\r\nxxxxxxxxxxxxxxxxxxxxxxxxx', '1'),
('model_r', 10, 4, 3, 2, 'xxxxxxxxxxxxxxxxxxxxxxxxx\r\nxxxxxxxxxxx33333333333333\r\nxxxxxxxxxxx33333333333333\r\nxxxxxxxxxxx33333333333333\r\nxxxxxxxxxx333333333333333\r\nxxxxxxxxxxx33333333333333\r\nxxxxxxxxxxx33333333333333\r\nxxxxxxx333333333333333333\r\nxxxxxxx333333333333333333\r\nxxxxxxx333333333333333333\r\nxxxxxxx333333333333333333\r\nxxxxxxx333333333333333333\r\nxxxxxxx333333333333333333\r\nx4444433333xxxxxxxxxxxxxx\r\nx4444433333xxxxxxxxxxxxxx\r\nx44444333333222xx000000xx\r\nx44444333333222xx000000xx\r\nxxx44xxxxxxxx22xx000000xx\r\nxxx33xxxxxxxx11xx000000xx\r\nxxx33322222211110000000xx\r\nxxx33322222211110000000xx\r\nxxxxxxxxxxxxxxxxx000000xx\r\nxxxxxxxxxxxxxxxxx000000xx\r\nxxxxxxxxxxxxxxxxx000000xx\r\nxxxxxxxxxxxxxxxxx000000xx\r\nxxxxxxxxxxxxxxxxxxxxxxxxx', '1'),
('model_p', 0, 23, 2, 2, 'xxxxxxxxxxxxxxxxxxx\r\nxxxxxxx222222222222\r\nxxxxxxx222222222222\r\nxxxxxxx222222222222\r\nxxxxxxx222222222222\r\nxxxxxxx222222222222\r\nxxxxxxx222222222222\r\nxxxxxxx22222222xxxx\r\nxxxxxxx11111111xxxx\r\nx222221111111111111\r\nx222221111111111111\r\nx222221111111111111\r\nx222221111111111111\r\nx222221111111111111\r\nx222221111111111111\r\nx222221111111111111\r\nx222221111111111111\r\nx2222xx11111111xxxx\r\nx2222xx00000000xxxx\r\nx2222xx000000000000\r\nx2222xx000000000000\r\nx2222xx000000000000\r\nx2222xx000000000000\r\n22222xx000000000000\r\nx2222xx000000000000\r\nxxxxxxxxxxxxxxxxxxx', '1'),
('model_h', 4, 4, 1, 2, 'xxxxxxxxxxxx\r\nxxxxxxxxxxxx\r\nxxxxx111111x\r\nxxxxx111111x\r\nxxxxx111111x\r\nxxxxx111111x\r\nxxxxx111111x\r\nxxxxx000000x\r\nxxxxx000000x\r\nxxx00000000x\r\nxxx00000000x\r\nxxx00000000x\r\nxxx00000000x\r\nxxxxxxxxxxxx\r\nxxxxxxxxxxxx\r\nxxxxxxxxxxxx', '1'),
('custom_model', 0, 0, 0, 2, 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\nxxxxxxxxxxxx0000000000000xxxx\r\nxxxxxxxxxxx000000000000000xxx\r\nxxxxxxxxxx00000000000000000xx\r\nxxxxxxxxxx00000000000000000xx\r\nxxxxxxxxxx00000000000000000xx\r\nxxxxxxxxxx11111111111111111xx\r\nxxxxxxxxxx22222222222222222xx\r\nxxxxxxxxxx22222222222222222xx\r\nxxxxxxxxxx22222222222222222xx\r\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', '0'),
('the_den', 3, 22, 0, 0, '00000000xxxxxxxx\r\n0000000000000000\r\n0000000000000000\r\n000000000000xx00\r\n0000000000000000\r\n0000000000000000\r\n0000000000000000\r\nx000000000000000\r\n0000000000000000\r\n0000000000000000\r\n0000000000000000\r\n0000000000000000\r\nx000000000000000\r\nx000000000000000\r\nx000000000000000\r\nx000000000000000\r\nx000000000000000\r\nx000000000000000\r\nx000000000000000\r\nx000000000000000\r\nxxx00xxxxxxxxxxx\r\nxxx00xxxxxxxxxxx\r\nxxx00xxxxxxxxxxx\r\nGV00000000xxxxxxxx\r\n0000000000000000\r\n0000000000000000\r\n000000000000xx00\r\n0000000000000000\r\n0000000000000000\r\n0000000000000000\r\nx000000000000000\r\n0000000000000000\r\n0000000000000000\r\n0000000000000000\r\n0000000000000000\r\nx000000000000000\r\nx000000000000000\r\nx000000000000000\r\nx000000000000000\r\nx000000000000000\r\nx000000000000000\r\nx000000000000000\r\nx000000000000000\r\nxxx00xxxxxxxxxxx\r\nxxx00xxxxxxxxxxx\r\nxxx00xxxxxxxxxxx', '0'),
('model_s', 0, 3, 0, 2, 'xxxxxx\r\nx00000\r\nx00000\r\n000000\r\nx00000\r\nx00000\r\nx00000\r\nx00000', '0'),
('park_b', 11, 2, 0, 6, '0000x0000000\r\n0000xx000000\r\n000000000000\r\n00000000000x\r\n000000000000\r\n00x0000x0000', '0'),
('model_0', 0, 4, 0, 2, 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\nx00000000xx00000000xx00000000xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\nx00000000xx00000000xx00000000xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\nx00000000xx00000000xx00000000xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx0000\r\n000000000xx00000000xx00000000xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx0000\r\nx00000000xx00000000xx00000000xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx0000\r\nx00000000xx00000000xx00000000xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx0000\r\nx00000000xx00000000xx00000000xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\nx00000000xx00000000xx00000000xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', '1'),
('model_v', 0, 3, 2, 2, 'xxxxxxxxxxxxxxxxxxxx\r\nx222221111111111111x\r\nx222221111111111111x\r\n2222221111111111111x\r\nx222221111111111111x\r\nx222221111111111111x\r\nx222221111111111111x\r\nxxxxxxxx1111xxxxxxxx\r\nxxxxxxxx0000xxxxxxxx\r\nx000000x0000x000000x\r\nx000000x0000x000000x\r\nx00000000000x000000x\r\nx00000000000x000000x\r\nx000000000000000000x\r\nx000000000000000000x\r\nxxxxxxxx00000000000x\r\nx000000x00000000000x\r\nx000000x0000xxxxxxxx\r\nx00000000000x000000x\r\nx00000000000x000000x\r\nx00000000000x000000x\r\nx00000000000x000000x\r\nxxxxxxxx0000x000000x\r\nx000000x0000x000000x\r\nx000000x0000x000000x\r\nx000000000000000000x\r\nx000000000000000000x\r\nx000000000000000000x\r\nx000000000000000000x\r\nxxxxxxxxxxxxxxxxxxxx', '1'),
('model_t', 0, 3, 2, 2, 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\nx222222222222222222222222222x\r\nx222222222222222222222222222x\r\n2222222222222222222222222222x\r\nx222222222222222222222222222x\r\nx2222xxxxxx222222xxxxxxx2222x\r\nx2222xxxxxx111111xxxxxxx2222x\r\nx2222xx111111111111111xx2222x\r\nx2222xx111111111111111xx2222x\r\nx2222xx11xxx1111xxxx11xx2222x\r\nx2222xx11xxx0000xxxx11xx2222x\r\nx22222111x00000000xx11xx2222x\r\nx22222111x00000000xx11xx2222x\r\nx22222111x00000000xx11xx2222x\r\nx22222111x00000000xx11xx2222x\r\nx22222111x00000000xx11xx2222x\r\nx22222111x00000000xx11xx2222x\r\nx2222xx11xxxxxxxxxxx11xx2222x\r\nx2222xx11xxxxxxxxxxx11xx2222x\r\nx2222xx111111111111111xx2222x\r\nx2222xx111111111111111xx2222x\r\nx2222xxxxxxxxxxxxxxxxxxx2222x\r\nx2222xxxxxxxxxxxxxxxxxxx2222x\r\nx222222222222222222222222222x\r\nx222222222222222222222222222x\r\nx222222222222222222222222222x\r\nx222222222222222222222222222x\r\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', '1'),
('model_x', 0, 12, 0, 2, 'xxxxxxxxxxxxxxxxxxxx\r\nx000000000000000000x\r\nx000000000000000000x\r\nx000000000000000000x\r\nx000000000000000000x\r\nx000000000000000000x\r\nx000000000000000000x\r\nxxx00xxx0000xxx00xxx\r\nx000000x0000x000000x\r\nx000000x0000x000000x\r\nx000000x0000x000000x\r\nx000000x0000x000000x\r\n0000000x0000x000000x\r\nx000000x0000x000000x\r\nx000000x0000x000000x\r\nx000000x0000x000000x\r\nx000000x0000x000000x\r\nx000000x0000x000000x\r\nx000000xxxxxx000000x\r\nx000000000000000000x\r\nx000000000000000000x\r\nx000000000000000000x\r\nx000000000000000000x\r\nx000000000000000000x\r\nx000000000000000000x\r\nxxxxxxxxxxxxxxxxxxxx', '1'),
('model_w', 0, 3, 2, 2, 'xxxxxxxxxxxxxxxxxxxxxxxxxxx\r\nx2222xx1111111111xx11111111\r\nx2222xx1111111111xx11111111\r\n222222111111111111111111111\r\nx22222111111111111111111111\r\nx22222111111111111111111111\r\nx22222111111111111111111111\r\nx2222xx1111111111xx11111111\r\nx2222xx1111111111xx11111111\r\nx2222xx1111111111xxxx1111xx\r\nx2222xx1111111111xxxx0000xx\r\nxxxxxxx1111111111xx00000000\r\nxxxxxxx1111111111xx00000000\r\nx22222111111111111000000000\r\nx22222111111111111000000000\r\nx22222111111111111000000000\r\nx22222111111111111000000000\r\nx2222xx1111111111xx00000000\r\nx2222xx1111111111xx00000000\r\nx2222xxxx1111xxxxxxxxxxxxxx\r\nx2222xxxx0000xxxxxxxxxxxxxx\r\nx2222x0000000000xxxxxxxxxxx\r\nx2222x0000000000xxxxxxxxxxx\r\nx2222x0000000000xxxxxxxxxxx\r\nx2222x0000000000xxxxxxxxxxx\r\nx2222x0000000000xxxxxxxxxxx\r\nx2222x0000000000xxxxxxxxxxx', '1'),
('model_z', 0, 9, 0, 2, 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\nxxxxxxxxxxx00000000000000000000\r\nxxxxxxxxxxx00000000000000000000\r\nxxxxxxxxxxx00000000000000000000\r\nx00000000xx00000000000000000000\r\nx00000000xx00000000000000000000\r\nx00000000xx00000000000000000000\r\nx00000000xx00000000000000000000\r\nx00000000xx00000000000000000000\r\n000000000xx00000000000000000000\r\nx00000000xx00000000000000000000\r\nx00000000xx00000000000000000000\r\nx00000000xx00000000000000000000\r\nx00000000xx00000000000000000000\r\nx00000000xx00000000000000000000\r\nx00000000xx00000000000000000000\r\nxxxxxxxxxxx00000000000000000000\r\nxxxxxxxxxxx00000000000000000000\r\nxxxxxxxxxxx00000000000000000000\r\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', '1'),
('model_u', 0, 17, 1, 2, 'xxxxxxxxxxxxxxxxxxxxxxxx\r\nx1111100000000000000000x\r\nx1111100000000000000000x\r\nx1111100000000000000000x\r\nx1111100000000000000000x\r\nx1111100000000000000000x\r\nx1111100000000000000000x\r\nx1111100000000000000000x\r\nx1111100000000000000000x\r\nx1111100000000000000000x\r\nx1111100000000000000000x\r\nx1111100000000000000000x\r\nx1111100000000000000000x\r\nx1111100000000000000000x\r\nx1111100000000000000000x\r\nx1111100000000000000000x\r\nx1111100000000000000000x\r\n11111100000000000000000x\r\nx1111100000000000000000x\r\nx1111100000000000000000x\r\nx1111100000000000000000x\r\nx1111100000000000000000x\r\nx1111100000000000000000x\r\nx1111100000000000000000x\r\nx1111100000000000000000x\r\nx1111100000000000000000x\r\nx1111100000000000000000x\r\nx1111100000000000000000x\r\nx1111100000000000000000x\r\nx1111100000000000000000x\r\nx1111100000000000000000x\r\nx1111100000000000000000x\r\nx1111100000000000000000x\r\nx1111100000000000000000x\r\nx1111100000000000000000x\r\nxxxxxxxxxxxxxxxxxxxxxxxx', '1'),
('model_y', 0, 3, 0, 2, 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\nx00000000xx0000000000xx0000x\r\nx00000000xx0000000000xx0000x\r\n000000000xx0000000000xx0000x\r\nx00000000xx0000000000xx0000x\r\nx00000000xx0000xx0000xx0000x\r\nx00000000xx0000xx0000xx0000x\r\nx00000000xx0000xx0000000000x\r\nx00000000xx0000xx0000000000x\r\nxxxxx0000xx0000xx0000000000x\r\nxxxxx0000xx0000xx0000000000x\r\nxxxxx0000xx0000xxxxxxxxxxxxx\r\nxxxxx0000xx0000xxxxxxxxxxxxx\r\nx00000000xx0000000000000000x\r\nx00000000xx0000000000000000x\r\nx00000000xx0000000000000000x\r\nx00000000xx0000000000000000x\r\nx0000xxxxxxxxxxxxxxxxxx0000x\r\nx0000xxxxxxxxxxxxxxxxxx0000x\r\nx00000000000000000000000000x\r\nx00000000000000000000000000x\r\nx00000000000000000000000000x\r\nx00000000000000000000000000x\r\nxxxxxxxxxxxxxxxxxxxxxxxxxxxx', '1'),
('model_oscar', 0, 15, 1, 2, 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\nxxxxxxxxx11111111xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\nxxxxxxxxx11111111xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\nxxxxxxxxx11111111xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\nxxxxxxxxx11111111xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\nxxxxxxxxx11111111xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\nxxxxxxxxx11111111xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\nxxxxxxxxx11111111xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\nxxxxxxxxx11111111xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\nxxxxxxxxxxxx11xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\nx1111111x11111111x00000000xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\nx1111111x11111111x00000000xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\nx1111111x11111111x00000000xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\nx1111111111111111100000000xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\nx1111111111111111100000000xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\nx1111111x11111111x00000000xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\nx1111111x11111111x00000000xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\nx1111111x11111111x00000000xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\nxxxxxxxxxxxx11xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\nxxxxxxxxx00000000xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\nxxxxxxxxx00000000xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\nxxxxxxxxx00000000xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\nxxxxxxxxx00000000xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\nxxxxxxxxx00000000xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\nxxxxxxxxx00000000xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\nxxxxxxxxx00000000xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\nxxxxxxxxx00000000xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', '1'),
('model_b2g', 0, 0, 0, 2, 'xxxxxxxxxxxxxx\r\nx00000x000000x\r\nx000000000000x\r\nx00000x000000x\r\nx00000x000000x\r\nx00000x000000x\r\nx00000x000000x\r\nxxx0xxx000000x\r\nx000000000000x\r\nx000000000000x\r\nx000000000000x\r\nx000000000000x\r\nx000000000000x\r\nx000000000000x\r\nx000000000000x\r\nx000000000000x\r\nx000000000000x\r\nx00000xx00000x\r\nxxxxxxxxxxxxxx', '1'),
('model_opening', 0, 23, 2, 2, 'xxxxxxxxxxxxxxxxxxx\r\nxxxxxxx222222222222\r\nxxxxxxx222222222222\r\nxxxxxxx222222222222\r\nxxxxxxx222222222222\r\nxxxxxxx222222222222\r\nxxxxxxx222222222222\r\nxxxxxxx222222222222\r\nxxxxxxx111111111111\r\nx222221111111111111\r\nx222221111111111111\r\nx222221111111111111\r\nx222221111111111111\r\nx222221111111111111\r\nx222221111111111111\r\nx222221111111111111\r\nx222221111111111111\r\nx2222xx111111111111\r\nx2222xx000000000000\r\nx2222xx000000000000\r\nx2222xx000000000000\r\nx2222xx000000000000\r\nx2222xx000000000000\r\n22222xx000000000000\r\nx2222xx000000000000\r\nxxxxxxxxxxxxxxxxxxx', '1'),
('model_custom_a', 2, 12, 0, 2, 'xxxxxxxxxxxxxxxxxxxxxxx\r\nxxxxxx00000000000000000\r\nxxxxxx00000000000000000\r\nxxxxxx00000000000000000\r\nxxxxxx00000000000000000\r\nx0000000000000000000000\r\nx0000000000000000000000\r\nx0000000000000000000000\r\nx0000000000000000000000\r\nx0000000000000000000000\r\nxxxxxx000000000000000xx\r\nxxxxxx000000000000000xx\r\nxx0000000000000000000xx\r\nxx0000000000000000xxxxx\r\nxxxxxxx00000000000xxxxx\r\nxxxxxxxx0000000000xxxxx\r\nxxxxxxxx0000000000xxxxx\r\nxxxxxxxx0000000000xxxxx\r\nxxxxxxxx0000000000xxxxx\r\nxxxxxxxx0000000000xxxxx\r\nxxxxxxxx0000000000xxxxx\r\nxxxxxx000000000000xxxxx\r\nxxxxxx000000000000xxxxx\r\nxxxxxx000000000000xxxxx\r\nxxxxxx000000000000xxxxx\r\nxxxxxx000000000000xxxxx\r\nxxxxx0000000000000xxxxx\r\nxxxxx0000000000000xxxxx\r\nxxxxx0000000000000xxxxx\r\nxxxxxxxxxxxxxxxxxxxxxxx', '0');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `room_models`
--
ALTER TABLE `room_models`
  ADD PRIMARY KEY (`id`);
COMMIT;

-- ----------------------------------------------------------------------------------------------------------------

-- --------------------------------------------------------

--
-- Structure de la table `rooms`
--

CREATE TABLE `rooms` (
  `id` int(10) UNSIGNED NOT NULL,
  `roomtype` enum('public','private') NOT NULL DEFAULT 'private',
  `caption` varchar(100) NOT NULL DEFAULT 'Room',
  `owner` varchar(75) NOT NULL DEFAULT '',
  `description` varchar(255) NOT NULL DEFAULT '',
  `category` int(11) NOT NULL DEFAULT 0,
  `state` enum('open','locked','password') NOT NULL DEFAULT 'open',
  `users_now` int(11) NOT NULL DEFAULT 0,
  `users_max` int(11) NOT NULL DEFAULT 25,
  `model_name` varchar(50) NOT NULL,
  `public_ccts` varchar(50) NOT NULL DEFAULT '',
  `score` int(11) NOT NULL DEFAULT 0,
  `tags` varchar(100) NOT NULL DEFAULT '',
  `icon_bg` int(11) NOT NULL DEFAULT 1,
  `icon_fg` int(11) NOT NULL DEFAULT 0,
  `icon_items` varchar(50) NOT NULL DEFAULT '',
  `password` varchar(30) NOT NULL DEFAULT '',
  `wallpaper` varchar(10) NOT NULL DEFAULT '0.0',
  `floor` varchar(10) NOT NULL DEFAULT '0.0',
  `landscape` varchar(10) NOT NULL DEFAULT '0.0',
  `allow_pets` enum('0','1') NOT NULL DEFAULT '1',
  `allow_pets_eat` enum('0','1') NOT NULL DEFAULT '0',
  `allow_walkthrough` enum('0','1') NOT NULL DEFAULT '0',
  `allow_hidewall` enum('0','1') NOT NULL DEFAULT '0',
  `wallthick` int(1) NOT NULL DEFAULT 0,
  `floorthick` int(1) NOT NULL DEFAULT 0,
  `achievement` int(11) NOT NULL DEFAULT 0
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Déchargement des données de la table `rooms`
--

INSERT INTO `rooms` (`id`, `roomtype`, `caption`, `owner`, `description`, `category`, `state`, `users_now`, `users_max`, `model_name`, `public_ccts`, `score`, `tags`, `icon_bg`, `icon_fg`, `icon_items`, `password`, `wallpaper`, `floor`, `landscape`, `allow_pets`, `allow_pets_eat`, `allow_walkthrough`, `allow_hidewall`, `wallthick`, `floorthick`, `achievement`) VALUES
(1, 'public', 'Welcome Lobby', '', 'Where we give you a warm welcome to the hotel!', 0, 'open', 0, 50, 'newbie_lobby', 'hh_room_nlobby', 0, '', 1, 0, '', '', '0.0', '0.0', '0.0', '1', '0', '0', '0', 0, 0, 0),
(2, 'public', 'Theatredrome', '', 'For mass assemblies and gatherings.', 0, 'open', 0, 50, 'theater', 'hh_room_theater', 0, '', 1, 0, '', '', '0.0', '0.0', '0.0', '1', '0', '0', '0', 0, 0, 0),
(3, 'public', 'Club Orient', '', 'Come and relax, dance under the lights or chill out with a cup of tea in this oriental styled club.', 0, 'open', 0, 30, 'orient', 'hh_room_orient', 0, '', 1, 0, '', '', '0.0', '0.0', '0.0', '1', '0', '0', '0', 0, 0, 0),
(4, 'public', 'Picnic Area', '', 'Enjoy the ever-lasting summer sun with a fresh picnic, even in winter!', 0, 'open', 0, 50, 'picnic', 'hh_room_picnic', 0, '', 1, 0, '', '', '0.0', '0.0', '0.0', '1', '0', '0', '0', 0, 0, 0),
(5, 'public', 'Tea Room', '', 'Have a relaxing cup of fruit, herbal or even everyday tea in this Chinese themed tea house.', 0, 'open', 0, 30, 'tearoom', 'hh_room_tearoom', 0, '', 1, 0, '', '', '0.0', '0.0', '0.0', '1', '0', '0', '0', 0, 0, 0),
(6, 'public', 'Dusty Lounge', '', 'Origninally where the hotel air conditioning emptied its filters, this dusty, old void is now a beautifully decorated lounge!', 0, 'open', 0, 30, 'dusty_lounge', 'hh_room_dustylounge', 0, '', 1, 0, '', '', '0.0', '0.0', '0.0', '1', '0', '0', '0', 0, 0, 0),
(7, 'public', 'Cinema', '', 'Watch or perform, the choice is yours!', 0, 'open', 0, 50, 'cinema_a', 'hh_room_cinema', 0, '', 1, 0, '', '', '0.0', '0.0', '0.0', '1', '0', '0', '0', 0, 0, 0),
(8, 'private', 'test', 'Tig3r', '', 0, 'open', 1, 25, 'model_a', '', 0, '', 1, 0, '', '', '0.0', '0.0', '0.0', '1', '0', '0', '0', 0, 0, 0),
(9, 'private', 'Welcome lounge', 'Tig3r', '', 1, 'open', 1, 25, 'model_custom_a', '', 0, '', 24, 4, '', '', '0.0', '0.0', '0.0', '1', '0', '0', '0', 0, 0, 0),
(10, 'private', 'mmm', 'Tig3r', '', 0, 'open', 1, 25, 'model_a', '', 0, '', 1, 0, '', '', '0.0', '0.0', '0.0', '1', '0', '0', '0', 0, 0, 0);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `rooms`
--
ALTER TABLE `rooms`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--
