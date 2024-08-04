SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 数据库： `my_django`
--

-- --------------------------------------------------------

--
-- 表的结构 `account_user`
--

CREATE TABLE `account_user` (
  `uid` int NOT NULL,
  `account` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  `nickname` varchar(50) NOT NULL,
  `group` smallint NOT NULL,
  `status` smallint NOT NULL,
  `create_datetime` datetime(6) NOT NULL,
  `last_login_datetime` datetime(6) DEFAULT NULL,
  `access_token` varchar(50) DEFAULT NULL,
  `access_token_expire` datetime(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- 转存表中的数据 `account_user`
--

INSERT INTO `account_user` (`uid`, `account`, `password`, `nickname`, `group`, `status`, `create_datetime`, `last_login_datetime`, `access_token`, `access_token_expire`) VALUES
(1, 'test_user', 'e10adc3949ba59abbe56e057f20f883e', '测试用户', 1, 1, '2024-07-30 08:19:58.000000', '2024-07-30 08:33:01.000000', NULL, NULL);

-- --------------------------------------------------------

--
-- 表的结构 `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- 表的结构 `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- 表的结构 `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- 转存表中的数据 `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add article', 7, 'add_article'),
(26, 'Can change article', 7, 'change_article'),
(27, 'Can delete article', 7, 'delete_article'),
(28, 'Can view article', 7, 'view_article'),
(29, 'Can add user', 8, 'add_user'),
(30, 'Can change user', 8, 'change_user'),
(31, 'Can delete user', 8, 'delete_user'),
(32, 'Can view user', 8, 'view_user');

-- --------------------------------------------------------

--
-- 表的结构 `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- 转存表中的数据 `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$720000$ztZ31BHb8IukkbBmJ57NsH$lySEyVdjxpk3dRWTjzl672Bt96VC7Z17DV2+HoCdFsE=', '2024-07-30 08:39:58.913000', 1, 'admin', '', '', '', 1, 1, '2024-07-29 21:57:29.888000');

-- --------------------------------------------------------

--
-- 表的结构 `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- 表的结构 `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- 表的结构 `demo_article`
--

CREATE TABLE `demo_article` (
  `id` bigint NOT NULL,
  `title` varchar(50) NOT NULL,
  `content` longtext NOT NULL,
  `author_uid` int NOT NULL,
  `pub_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- 转存表中的数据 `demo_article`
--

INSERT INTO `demo_article` (`id`, `title`, `content`, `author_uid`, `pub_date`) VALUES
(1, '文章一', '内容1', 1000, '2024-07-29 20:48:51.677000'),
(2, '文章二', '内容2', 1000, '2024-07-29 20:50:48.969000'),
(3, '文章三', '内容3', 1000, '2024-07-29 20:50:55.062000'),
(4, '文章四', '内容4', 1000, '2024-07-29 20:51:00.549000'),
(5, '文章五', '内容5', 1000, '2024-07-29 20:51:07.817000'),
(6, '文章六', '内容6', 1000, '2024-07-29 20:51:16.984000'),
(7, '文章七', '内容7', 1001, '2024-07-29 20:51:25.429000'),
(8, '文章八', '内容8', 1001, '2024-07-29 20:51:34.899000'),
(9, '文章九', '内容9', 1001, '2024-07-29 20:51:42.014000'),
(10, '文章十', '内容10', 1001, '2024-07-29 20:51:51.351000');

-- --------------------------------------------------------

--
-- 表的结构 `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL
) ;

--
-- 转存表中的数据 `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2024-07-30 08:23:37.468000', '1', 'User object (1)', 1, '[{\"added\": {}}]', 8, 1),
(2, '2024-07-30 08:40:08.214000', '1', 'User object (1)', 2, '[{\"changed\": {\"fields\": [\"\\u767b\\u5f55\\u9a8c\\u8bc1Token\"]}}]', 8, 1),
(3, '2024-07-30 09:03:43.472000', '1', 'User object (1)', 2, '[{\"changed\": {\"fields\": [\"\\u767b\\u5f55\\u9a8c\\u8bc1Token\"]}}]', 8, 1);

-- --------------------------------------------------------

--
-- 表的结构 `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- 转存表中的数据 `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(8, 'account', 'user'),
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'demo', 'article'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- 表的结构 `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- 转存表中的数据 `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'account', '0001_initial', '2024-07-30 21:15:58.833153'),
(2, 'contenttypes', '0001_initial', '2024-07-30 21:15:58.849247'),
(3, 'auth', '0001_initial', '2024-07-30 21:15:58.920021'),
(4, 'admin', '0001_initial', '2024-07-30 21:15:58.943399'),
(5, 'admin', '0002_logentry_remove_auto_add', '2024-07-30 21:15:58.945950'),
(6, 'admin', '0003_logentry_add_action_flag_choices', '2024-07-30 21:15:58.948102'),
(7, 'contenttypes', '0002_remove_content_type_name', '2024-07-30 21:15:58.962085'),
(8, 'auth', '0002_alter_permission_name_max_length', '2024-07-30 21:15:58.971432'),
(9, 'auth', '0003_alter_user_email_max_length', '2024-07-30 21:15:58.981543'),
(10, 'auth', '0004_alter_user_username_opts', '2024-07-30 21:15:58.984177'),
(11, 'auth', '0005_alter_user_last_login_null', '2024-07-30 21:15:58.992823'),
(12, 'auth', '0006_require_contenttypes_0002', '2024-07-30 21:15:58.993129'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2024-07-30 21:15:58.996685'),
(14, 'auth', '0008_alter_user_username_max_length', '2024-07-30 21:15:59.007066'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2024-07-30 21:15:59.017168'),
(16, 'auth', '0010_alter_group_name_max_length', '2024-07-30 21:15:59.025767'),
(17, 'auth', '0011_update_proxy_permissions', '2024-07-30 21:15:59.028757'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2024-07-30 21:15:59.046339'),
(19, 'demo', '0001_initial', '2024-07-30 21:15:59.048765'),
(20, 'sessions', '0001_initial', '2024-07-30 21:15:59.052994');

-- --------------------------------------------------------

--
-- 表的结构 `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- 转存表中的数据 `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('apjsyn1coqvx5rc0dja5exc68hlzmbnh', '.eJxVjEEOwiAQRe_C2pCWgWl16d4zkIEZpGogKe3KeHfbpAvdvvf-fytP65L92mT2E6uL6tXplwWKTym74AeVe9WxlmWegt4Tfdimb5XldT3av4NMLW9rIwHAiqNzSGRFegLsOrQJybExkpwDhwYwiWxoiKMlax3gOBiODOrzBevQN9A:1sYauE:Ec72kh15KZXx-zSfrFBRZ7OEifLipSuou7NWDm0LxWM', '2024-08-13 08:39:58.952000'),
('b8lbaujjpbvqy112i4j3sw32u3pfyku9', '.eJxVjEEOwiAQRe_C2pCWgWl16d4zkIEZpGogKe3KeHfbpAvdvvf-fytP65L92mT2E6uL6tXplwWKTym74AeVe9WxlmWegt4Tfdimb5XldT3av4NMLW9rIwHAiqNzSGRFegLsOrQJybExkpwDhwYwiWxoiKMlax3gOBiODOrzBevQN9A:1sYQt8:HxeV6yeQbPS8A9-k1a5x1OCaJM9nCvG3i014c6PaHCA', '2024-08-12 21:58:10.803000'),
('s86unk6cw64fi7e271bokgfpm7nnz4y6', '.eJxVjEEOwiAQRe_C2pCWgWl16d4zkIEZpGogKe3KeHfbpAvdvvf-fytP65L92mT2E6uL6tXplwWKTym74AeVe9WxlmWegt4Tfdimb5XldT3av4NMLW9rIwHAiqNzSGRFegLsOrQJybExkpwDhwYwiWxoiKMlax3gOBiODOrzBevQN9A:1sYaYr:AD10O_b9GeVHJkzdB06ABzq8PIp2QDDzW53z7sB2KUQ', '2024-08-13 08:17:53.463000');

--
-- 转储表的索引
--

--
-- 表的索引 `account_user`
--
ALTER TABLE `account_user`
  ADD PRIMARY KEY (`uid`),
  ADD UNIQUE KEY `account` (`account`);

--
-- 表的索引 `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- 表的索引 `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- 表的索引 `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- 表的索引 `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- 表的索引 `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- 表的索引 `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- 表的索引 `demo_article`
--
ALTER TABLE `demo_article`
  ADD PRIMARY KEY (`id`);

--
-- 表的索引 `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- 表的索引 `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- 表的索引 `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- 表的索引 `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `account_user`
--
ALTER TABLE `account_user`
  MODIFY `uid` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- 使用表AUTO_INCREMENT `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- 使用表AUTO_INCREMENT `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- 使用表AUTO_INCREMENT `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `demo_article`
--
ALTER TABLE `demo_article`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- 使用表AUTO_INCREMENT `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- 使用表AUTO_INCREMENT `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- 限制导出的表
--

--
-- 限制表 `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- 限制表 `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- 限制表 `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- 限制表 `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- 限制表 `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
