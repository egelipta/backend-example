/*
 Navicat Premium Data Transfer

 Source Server         : pjvms22
 Source Server Type    : MariaDB
 Source Server Version : 100237
 Source Host           : 192.180.0.61:3306
 Source Schema         : base

 Target Server Type    : MariaDB
 Target Server Version : 100237
 File Encoding         : 65001

 Date: 16/07/2022 22:08:57
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for access
-- ----------------------------
DROP TABLE IF EXISTS `access`;
CREATE TABLE `access` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL DEFAULT current_timestamp(6) COMMENT 'Creation time',
  `update_time` datetime(6) NOT NULL DEFAULT current_timestamp(6) ON UPDATE current_timestamp(6) COMMENT 'Update time',
  `access_name` varchar(25) NOT NULL COMMENT 'Permission name',
  `parent_id` int(11) NOT NULL DEFAULT 0 COMMENT 'Parent ID',
  `scopes` varchar(255) NOT NULL COMMENT 'Permanent scope identification',
  `access_desc` varchar(255) DEFAULT NULL COMMENT 'Permissions description',
  `menu_icon` varchar(255) DEFAULT NULL COMMENT 'Menu icon',
  `is_check` tinyint(1) NOT NULL DEFAULT 0 COMMENT 'Whether to verify the permissions TRUE to verify that FALSE does not verify',
  `is_menu` tinyint(1) NOT NULL DEFAULT 0 COMMENT 'Whether it is the menu TRUE menu FALSE is not the menu',
  PRIMARY KEY (`id`),
  UNIQUE KEY `scopes` (`scopes`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COMMENT='Permissions table';

-- ----------------------------
-- Records of access
-- ----------------------------
BEGIN;
INSERT INTO `access` VALUES (1, '2022-05-18 18:28:15.699736', '2022-05-18 18:28:15.699771', 'All Access', 0, 'all', NULL, NULL, 1, 0);
INSERT INTO `access` VALUES (2, '2022-05-18 18:28:55.162023', '2022-05-18 18:28:55.162070', 'User Management', 0, 'user_m', NULL, NULL, 0, 1);
INSERT INTO `access` VALUES (3, '2022-05-18 18:32:45.768538', '2022-05-19 07:27:43.328990', 'User query', 2, 'user_query', NULL, NULL, 1, 0);
INSERT INTO `access` VALUES (4, '2022-05-18 18:33:05.634450', '2022-05-18 18:33:05.634498', 'User add', 2, 'user_add', NULL, NULL, 1, 0);
INSERT INTO `access` VALUES (5, '2022-05-18 18:33:35.677990', '2022-05-18 18:33:35.678038', 'User editor', 2, 'user_update', NULL, NULL, 1, 0);
INSERT INTO `access` VALUES (6, '2022-05-18 18:33:53.455916', '2022-05-18 18:33:53.455964', 'User delete', 2, 'user_delete', NULL, NULL, 1, 0);

INSERT INTO `access` VALUES (7, '2022-05-18 18:31:48.630306', '2022-05-18 18:31:48.630354', 'Role Management', 0, 'role_m', NULL, NULL, 0, 1);
INSERT INTO `access` VALUES (8, '2022-05-18 18:34:55.614617', '2022-05-19 11:32:14.861397', 'Role Assignments', 7, 'user_role', NULL, NULL, 1, 0);
INSERT INTO `access` VALUES (9, '2022-05-18 18:35:16.093767', '2022-05-19 09:15:13.190683', 'Role Query', 8, 'role_query', NULL, NULL, 1, 0);
INSERT INTO `access` VALUES (10, '2022-05-18 18:35:35.856673', '2022-05-19 09:14:55.453576', 'Role Add', 8, 'role_add', NULL, NULL, 1, 0);
INSERT INTO `access` VALUES (11, '2022-05-18 18:35:53.266453', '2022-05-19 09:14:41.721341', 'Role Edit', 8, 'role_update', NULL, NULL, 1, 0);
INSERT INTO `access` VALUES (12, '2022-05-18 18:36:27.876248', '2022-05-19 09:14:23.501602', 'Role Delete', 8, 'role_delete', NULL, NULL, 1, 0);
INSERT INTO `access` VALUES (13, '2022-05-19 09:13:06.535110', '2022-05-19 09:13:56.906714', 'Permission allocation', 7, 'role_access', NULL, NULL, 1, 0);

-- INSERT INTO `access` VALUES (14, '2022-05-19 09:13:06.535110', '2022-05-19 09:13:56.906714', 'Dashboard Management', 0, 'dashboard_m', NULL, NULL, 0, 1);
-- INSERT INTO `access` VALUES (15, '2022-05-19 09:13:06.535110', '2022-05-19 09:13:56.906714', 'Dashboard Query', 14, 'dashboard_query', NULL, NULL, 1, 0);

-- INSERT INTO `access` VALUES (16, '2022-05-19 09:13:06.535110', '2022-05-19 09:13:56.906714', 'Person Management', 0, 'person_m', NULL, NULL, 0, 1);
-- INSERT INTO `access` VALUES (17, '2022-05-19 09:13:06.535110', '2022-05-19 09:13:56.906714', 'Employee Management', 16, 'employee_m', NULL, NULL, 0, 1);
-- INSERT INTO `access` VALUES (18, '2022-05-19 09:13:06.535110', '2022-05-19 09:13:56.906714', 'Visitor Management', 16, 'visitor_m', NULL, NULL, 0, 1);

-- INSERT INTO `access` VALUES (19, '2022-05-19 09:13:06.535110', '2022-05-19 09:13:56.906714', 'Employee Query', 17, 'employee_query', NULL, NULL, 1, 0);
-- INSERT INTO `access` VALUES (20, '2022-05-19 09:13:06.535110', '2022-05-19 09:13:56.906714', 'Employee Update', 17, 'employee_update', NULL, NULL, 1, 0);
-- INSERT INTO `access` VALUES (21, '2022-05-19 09:13:06.535110', '2022-05-19 09:13:56.906714', 'Employee Add', 17, 'employee_add', NULL, NULL, 1, 0);
-- INSERT INTO `access` VALUES (22, '2022-05-19 09:13:06.535110', '2022-05-19 09:13:56.906714', 'Employee Delete', 17, 'employee_delete', NULL, NULL, 1, 0);
-- INSERT INTO `access` VALUES (23, '2022-05-19 09:13:06.535110', '2022-05-19 09:13:56.906714', 'Visitor Query', 18, 'visitor_query', NULL, NULL, 1, 0);
-- INSERT INTO `access` VALUES (24, '2022-05-19 09:13:06.535110', '2022-05-19 09:13:56.906714', 'Visitor Update', 18, 'visitor_update', NULL, NULL, 1, 0);
-- INSERT INTO `access` VALUES (25, '2022-05-19 09:13:06.535110', '2022-05-19 09:13:56.906714', 'Visitor Add', 18, 'visitor_add', NULL, NULL, 1, 0);
-- INSERT INTO `access` VALUES (26, '2022-05-19 09:13:06.535110', '2022-05-19 09:13:56.906714', 'Visitor Delete', 18, 'visitor_delete', NULL, NULL, 1, 0);


-- INSERT INTO `access` VALUES (27, '2022-05-19 09:13:06.535110', '2022-05-19 09:13:56.906714', 'Device Management', 0, 'device_m', NULL, NULL, 0, 1);
-- INSERT INTO `access` VALUES (28, '2022-05-19 09:13:06.535110', '2022-05-19 09:13:56.906714', 'Device query', 27, 'device_query', NULL, NULL, 1, 0);
-- INSERT INTO `access` VALUES (29, '2022-05-19 09:13:06.535110', '2022-05-19 09:13:56.906714', 'Device update', 27, 'device_update', NULL, NULL, 1, 0);
-- INSERT INTO `access` VALUES (30, '2022-05-19 09:13:06.535110', '2022-05-19 09:13:56.906714', 'Device add', 27, 'device_add', NULL, NULL, 1, 0);
-- INSERT INTO `access` VALUES (31, '2022-05-19 09:13:06.535110', '2022-05-19 09:13:56.906714', 'Device delete', 27, 'device_delete', NULL, NULL, 1, 0);
-- INSERT INTO `access` VALUES (39, '2022-05-19 09:13:06.535110', '2022-05-19 09:13:56.906714', 'Device unlock', 27, 'device_unlock', NULL, NULL, 1, 0);


-- INSERT INTO `access` VALUES (32, '2022-05-19 09:13:06.535110', '2022-05-19 09:13:56.906714', 'Attendance', 0, 'attendance_m', NULL, NULL, 0, 1);
-- INSERT INTO `access` VALUES (33, '2022-05-19 09:13:06.535110', '2022-05-19 09:13:56.906714', 'Attendance Query', 32, 'attendance_query', NULL, NULL, 1, 0);

-- INSERT INTO `access` VALUES (34, '2022-05-19 09:13:06.535110', '2022-05-19 09:13:56.906714', 'Passrecord', 0, 'passrecord_m', NULL, NULL, 0, 1);
-- INSERT INTO `access` VALUES (35, '2022-05-19 09:13:06.535110', '2022-05-19 09:13:56.906714', 'Passrecord Query', 34, 'passrecord_query', NULL, NULL, 1, 0);


-- INSERT INTO `access` VALUES (36, '2022-05-19 09:13:06.535110', '2022-05-19 09:13:56.906714', 'System Management', 0, 'systemss_m', NULL, NULL, 1, 0);
-- INSERT INTO `access` VALUES (40, '2022-05-19 09:13:06.535110', '2022-05-19 09:13:56.906714', 'Logs Management', 36, 'logs_m', NULL, NULL, 1, 0);
-- INSERT INTO `access` VALUES (41, '2022-05-19 09:13:06.535110', '2022-05-19 09:13:56.906714', 'About Management', 36, 'about_m', NULL, NULL, 1, 0);
-- INSERT INTO `access` VALUES (37, '2022-05-19 09:13:06.535110', '2022-05-19 09:13:56.906714', 'Logs', 40, 'log_query', NULL, NULL, 0, 1);
-- INSERT INTO `access` VALUES (38, '2022-05-19 09:13:06.535110', '2022-05-19 09:13:56.906714', 'About', 41, 'about_query', NULL, NULL, 0, 1);
COMMIT;

-- ----------------------------
-- Table structure for access_log
-- ----------------------------
DROP TABLE IF EXISTS `access_log`;
CREATE TABLE `access_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL DEFAULT current_timestamp(6) COMMENT 'Creation time',
  `update_time` datetime(6) NOT NULL DEFAULT current_timestamp(6) ON UPDATE current_timestamp(6) COMMENT 'Update time',
  `user_id` int(11) NOT NULL COMMENT 'User ID',
  `target_url` varchar(255) DEFAULT NULL COMMENT 'Access URL',
  `user_agent` varchar(255) DEFAULT NULL COMMENT 'Visit UA',
  `request_params` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL COMMENT 'Request parameter get|post',
  `ip` varchar(32) DEFAULT NULL COMMENT 'Access IP',
  `note` varchar(255) DEFAULT NULL COMMENT 'Remark',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='User operation record table';

-- ----------------------------
-- Records of access_log
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for role
-- ----------------------------
DROP TABLE IF EXISTS `role`;
CREATE TABLE `role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL DEFAULT current_timestamp(6) COMMENT 'Creation time',
  `update_time` datetime(6) NOT NULL DEFAULT current_timestamp(6) ON UPDATE current_timestamp(6) COMMENT 'Update time',
  `role_name` varchar(25) NOT NULL COMMENT 'Role Name',
  `role_status` tinyint(1) NOT NULL DEFAULT 0 COMMENT 'True: Enable False: Disable',
  `role_desc` varchar(255) DEFAULT NULL COMMENT 'Character description',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Character table';

-- ----------------------------
-- Records of role
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for role_access
-- ----------------------------
DROP TABLE IF EXISTS `role_access`;
CREATE TABLE `role_access` (
  `role_id` int(11) NOT NULL,
  `access_id` int(11) NOT NULL,
  KEY `role_id` (`role_id`),
  KEY `access_id` (`access_id`),
  CONSTRAINT `role_access_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`) ON DELETE CASCADE,
  CONSTRAINT `role_access_ibfk_2` FOREIGN KEY (`access_id`) REFERENCES `access` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of role_access
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for system_params
-- ----------------------------
DROP TABLE IF EXISTS `system_params`;
CREATE TABLE `system_params` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL DEFAULT current_timestamp(6) COMMENT 'Creation time',
  `update_time` datetime(6) NOT NULL DEFAULT current_timestamp(6) ON UPDATE current_timestamp(6) COMMENT 'Update time',
  `params_name` varchar(255) NOT NULL COMMENT 'parameter name',
  `params` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT 'parameter',
  PRIMARY KEY (`id`),
  UNIQUE KEY `params_name` (`params_name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COMMENT='System parameter table';

-- ----------------------------
-- Records of system_params
-- ----------------------------
BEGIN;
INSERT INTO `system_params` VALUES (1, '2022-06-04 18:03:00.648479', '2022-07-16 14:07:37.491553', 'wechat_auth', '{\"appid\":\"1\",\"secret\":\"1\",\"redirect_uri\":\"http://fastapi.binkuolo.com/api/v1/wechat/auth/call\",\"expire\":1}');
INSERT INTO `system_params` VALUES (2, '2022-06-07 21:42:48.946171', '2022-07-16 14:07:45.691333', 'tencent_sms', '{\"secret_id\":\"1\",\"secret_key\":\"1\",\"region\":\"ap-guangzhou\",\"app_id\":\"1400440642\",\"sign\":\"贵州红帽网络\",\"template_id\":\"757896\",\"expire\":10}');
INSERT INTO `system_params` VALUES (3, '2022-07-08 17:56:05.098642', '2022-07-16 14:07:54.795525', 'tencent_cos', '{\"duration_seconds\":1800,\"secret_id\":\"1\",\"secret_key\":\"1\",\"region\":\"ap-chongqing\"}');
COMMIT;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL DEFAULT current_timestamp(6) COMMENT 'Created at',
  `update_time` datetime(6) NOT NULL DEFAULT current_timestamp(6) ON UPDATE current_timestamp(6) COMMENT 'Updated at',
  `username` varchar(25) DEFAULT NULL ,
  `user_type` tinyint(1) NOT NULL DEFAULT 0 COMMENT 'True:SuperAdmin False:Admin',
  `password` varchar(255) DEFAULT NULL,
  `nickname` varchar(255) NOT NULL DEFAULT 'dgos',
  `user_phone` varchar(15) DEFAULT NULL COMMENT 'phone number',
  `user_email` varchar(255) DEFAULT NULL COMMENT 'Mail',
  `full_name` varchar(255) DEFAULT NULL COMMENT 'Name',
  `user_status` int(11) NOT NULL DEFAULT 2 COMMENT '0 No activation 1 Normal 2 Disable',
  `header_img` varchar(255) DEFAULT NULL COMMENT 'avatar',
  `sex` int(11) DEFAULT 0 COMMENT '0 Unknown 1 Men and 2 Women',
  `remarks` varchar(30) DEFAULT NULL COMMENT 'Remark',
  `client_host` varchar(19) DEFAULT NULL COMMENT 'Access IP',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COMMENT='user table';

-- ----------------------------
-- Records of user
-- ----------------------------
BEGIN;
INSERT INTO `user` VALUES (1, '2022-05-18 18:25:56.776176', '2022-07-16 09:36:46.742337', 'root', 1, '$pbkdf2-sha256$29000$f88ZgzDGeC8lJGSM0RpjzA$ZEKDz34TzG0b5Qhd1o1IS6rc63xj1rQV2/T1kohGw/0', 'dgosroot', '19391008993', 'dev@dgos.id', NULL, 1, '', 0, 'string', NULL);
COMMIT;

-- ----------------------------
-- Table structure for user_role
-- ----------------------------
DROP TABLE IF EXISTS `user_role`;
CREATE TABLE `user_role` (
  `user_id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL,
  KEY `user_id` (`user_id`),
  KEY `role_id` (`role_id`),
  CONSTRAINT `user_role_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE,
  CONSTRAINT `user_role_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of user_role
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for user_wechat
-- ----------------------------
DROP TABLE IF EXISTS `user_wechat`;
CREATE TABLE `user_wechat` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL DEFAULT current_timestamp(6) COMMENT 'Creation time',
  `update_time` datetime(6) NOT NULL DEFAULT current_timestamp(6) ON UPDATE current_timestamp(6) COMMENT 'Update time',
  `city` varchar(255) DEFAULT NULL COMMENT 'city',
  `country` varchar(255) DEFAULT NULL COMMENT 'nation',
  `headimgurl` varchar(255) DEFAULT NULL COMMENT 'WeChat avatar',
  `nickname` varchar(255) DEFAULT NULL COMMENT 'WeChat nickname',
  `openid` varchar(255) NOT NULL COMMENT 'openid',
  `unionid` varchar(255) DEFAULT NULL COMMENT 'unionid',
  `province` varchar(255) DEFAULT NULL COMMENT 'province',
  `sex` int(11) DEFAULT NULL COMMENT 'gender',
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `openid` (`openid`),
  UNIQUE KEY `user_id` (`user_id`),
  UNIQUE KEY `unionid` (`unionid`),
  CONSTRAINT `fk_user_wec_user_a1775abb` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='User WeChat';

-- ----------------------------
-- Records of user_wechat
-- ----------------------------
BEGIN;
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;


-- -- ----------------------------
-- -- Table structure for systemInfo
-- -- ----------------------------
-- DROP TABLE IF EXISTS `systemInfo`;
-- CREATE TABLE `systemInfo` (
--   `software_name` varchar(255) NOT NULL,
--   `version` varchar(255) DEFAULT NULL,
--   `system` varchar(255) DEFAULT NULL,
--   `jdk_version` varchar(255) DEFAULT NULL,
--   `database_type` varchar(20) DEFAULT NULL,
--   `database_port` varchar(255) DEFAULT NULL,
--   PRIMARY KEY (`software_name`)
-- ) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COMMENT='SystemInfo Table';

-- --
-- -- Dumping data for table `systemInfo`
-- --

-- INSERT INTO `systemInfo` (`software_name`, `version`, `system`, `jdk_version`, `database_type`, `database_port`) VALUES
-- ('Diskominfotik, PEMPROV DKI', '2.0.0', 'Unix', '1.8.0_162', 'MySQL', '*');


-- ----------------------------
-- Table of aset
-- ----------------------------

DROP TABLE IF EXISTS `aset`;
CREATE TABLE `aset` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
 `create_time` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) COMMENT 'Created at',
  `update_time` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6) COMMENT 'Updated at',
  `merek` varchar(255) DEFAULT NULL,
  `tipe` varchar(255) DEFAULT NULL,
  `fungsi_perangkat` varchar(255) DEFAULT NULL,
  `foto_perangkat` varchar(255) DEFAULT NULL,
  `nomor_seri` varchar(255) DEFAULT NULL,
  `jenis_infra` varchar(255) DEFAULT NULL,
  `instansi_pemilik` varchar(255) DEFAULT NULL,
  `penanggung_jawab` varchar(255) DEFAULT NULL,
  `lokasi` varchar(255) DEFAULT NULL,
  `nama_ruangan` varchar(255) DEFAULT NULL,
  `posisi_rak` varchar(255) DEFAULT NULL,
  `psu` varchar(255) DEFAULT NULL,
  `posisi_u` varchar(255) DEFAULT NULL,
  `power` varchar(255) DEFAULT NULL,
  `kapasitas_cpu` varchar(255) DEFAULT NULL,
  `kapasitas_hdd` varchar(255) DEFAULT NULL,
  `kapasitas_ram` varchar(255) DEFAULT NULL,
  `daya` varchar(255) DEFAULT NULL,
  `tanggal_pemasangan` datetime(6) NOT NULL,
  `tanggal_penarikan` datetime(6) DEFAULT NULL,
  `keterangan` varchar(255) DEFAULT NULL,
  `status_aset` tinyint(1) DEFAULT NULL,
  `user` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COMMENT='aset table';



-- ----------------------------
-- Table of layanan
-- ----------------------------

DROP TABLE IF EXISTS `layanan`;
CREATE TABLE `layanan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) COMMENT 'Created at',
  `update_time` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6) COMMENT 'Updated at',
  `nomor_tiket` varchar(255) DEFAULT NULL,
  `jenis_layanan` varchar(255) DEFAULT NULL,
  `co_location` varchar(255) DEFAULT NULL,
  `jenis_infra` varchar(255) DEFAULT NULL,
  `perangkat` varchar(255) DEFAULT NULL,
  `mulai_kunjungan` datetime(6) DEFAULT NULL,
  `akhir_kunjungan` datetime(6) DEFAULT NULL,
  `pemandu` varchar(255) DEFAULT NULL,
  `status` int(11) NOT NULL DEFAULT '0',
  `detail_tolak` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COMMENT='layanan table';


-- ----------------------------
-- Table of daftar_pengunjung
-- ----------------------------

DROP TABLE IF EXISTS `daftar_pengunjung`;
CREATE TABLE `daftar_pengunjung` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL DEFAULT current_timestamp(6) COMMENT 'Created at',
  `update_time` datetime(6) NOT NULL DEFAULT current_timestamp(6) ON UPDATE current_timestamp(6) COMMENT 'Updated at',
  `nama` varchar(25) DEFAULT NULL ,
  `nik` varchar(25) DEFAULT NULL ,
  `status` varchar(25) DEFAULT NULL ,
  `instansi` varchar(255) DEFAULT NULL ,
  `foto` varchar(255) DEFAULT NULL ,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COMMENT='daftar_pengunjung table';

-- ----------------------------
-- Records of daftar_pengunjung
-- ----------------------------
BEGIN;
INSERT INTO `daftar_pengunjung` (`id`, `create_time`, `update_time`, `nik`, `nama`, `status`, `instansi`, `foto`) 
VALUES (1, '2023-01-19 11:51:28.250339', '2023-01-20 11:35:52.184249', '1234567890123456', 'Elwin Gelipta', 'ASN', 'DKI', 'gambar.jpg');
COMMIT;


-- ----------------------------
-- Table of buku_tamu
-- ----------------------------

DROP TABLE IF EXISTS `buku_tamu`;
CREATE TABLE `buku_tamu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL DEFAULT current_timestamp(6) COMMENT 'Created at',
  `update_time` datetime(6) NOT NULL DEFAULT current_timestamp(6) ON UPDATE current_timestamp(6) COMMENT 'Updated at',
  `no_tiket` varchar(25) DEFAULT NULL ,
  `jam_masuk` datetime(6) NOT NULL DEFAULT current_timestamp(6) ,
  `jam_keluar` datetime(6) NOT NULL DEFAULT current_timestamp(6) ,
  `laporan_pekerjaan` varchar(255) DEFAULT NULL ,
  `daftar_pengunjung` varchar(255) DEFAULT NULL ,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COMMENT='buku_tamu table';

-- ----------------------------
-- Records of buku_tamu
-- ----------------------------
BEGIN;
INSERT INTO `buku_tamu` (`id`, `create_time`, `update_time`, `no_tiket`,`jam_masuk`,  `jam_keluar`, `laporan_pekerjaan`, `daftar_pengunjung`) 
VALUES (1, '2023-01-19 11:51:28.250339', '2023-01-20 11:35:52.184249', '1234567890123456', '2023-01-19 11:51:28.250339', '2023-01-19 11:51:28.250339', 'Maintenance', 'Ilham, Reza, Waldo');
COMMIT;



-- ----------------------------
-- Table of merek_tipe
-- ----------------------------

DROP TABLE IF EXISTS `merek_tipe`;
CREATE TABLE `merek_tipe` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL DEFAULT current_timestamp(6) COMMENT 'Created at',
  `update_time` datetime(6) NOT NULL DEFAULT current_timestamp(6) ON UPDATE current_timestamp(6) COMMENT 'Updated at',
  `merek` varchar(255) DEFAULT NULL ,
  `tipe` varchar(255) DEFAULT NULL ,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COMMENT='merek_tipe table';

-- ----------------------------
-- Records of merek_tipe
-- ----------------------------
BEGIN;
INSERT INTO `merek_tipe` (`id`, `create_time`, `update_time`, `merek`,`tipe`) 
VALUES (1, '2023-01-19 11:51:28.250339', '2023-01-20 11:35:52.184249', 'Fujitsu', 'Primergy X270');
COMMIT;


-- ----------------------------
-- Table of pemandu
-- ----------------------------

DROP TABLE IF EXISTS `pemandu`;
CREATE TABLE `pemandu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL DEFAULT current_timestamp(6) COMMENT 'Created at',
  `update_time` datetime(6) NOT NULL DEFAULT current_timestamp(6) ON UPDATE current_timestamp(6) COMMENT 'Updated at',
  `nama` varchar(25) DEFAULT NULL ,
  `no_hp` varchar(255) DEFAULT NULL ,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COMMENT='pemandu table';

DROP TABLE IF EXISTS `lokasi`;
CREATE TABLE `lokasi` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lokasi` varchar(255) NOT NULL,
  `nama_ruangan` varchar(255) NOT NULL,
  `posisi_rak` varchar(255) NOT NULL,
  `posisi_u` varchar(255) NOT NULL,
  `sn_aset` varchar(255) NOT NULL DEFAULT 'kosong',
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
   PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='lokasi table';

BEGIN;
INSERT INTO `lokasi` (`id`, `lokasi`, `nama_ruangan`, `posisi_rak`, `posisi_u`, `sn_aset`, `create_time`, `update_time`) VALUES
(1, 'Kominfo', 'Server', '1', '1', '', '2023-09-11 09:00:24', '2023-09-11 09:00:24'),
(2, 'Kominfo', 'Server', '1', '2', '', '2023-09-11 09:00:52', '2023-09-11 09:00:52'),
(3, 'Kominfo', 'Server', '1', '3', '', '2023-09-11 09:01:07', '2023-09-11 09:01:07'),
(4, 'Kominfo', 'Server', '2', '3', '', '2023-09-11 09:01:18', '2023-09-11 09:01:18'),
(5, 'Kominfo', 'Server', '2', '2', '', '2023-09-11 09:01:34', '2023-09-11 09:01:34'),
(6, 'Kominfo', 'Server', '2', '1', '', '2023-09-11 09:01:42', '2023-09-11 09:01:42');
COMMIT;

DROP TABLE IF EXISTS 'power';
CREATE TABLE `power` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nama` varchar(255) NOT NULL,
  `lokasi` varchar(255) NOT NULL,
  `nama_ruangan` varchar(255) NOT NULL,
  `posisi_rak` varchar(255) NOT NULL,
  `source` char(1) NOT NULL,
  `power` varchar(255) NOT NULL,
  `tipe` varchar(255) NOT NULL,
  `sn_aset` varchar(255) NOT NULL DEFAULT 'kosong',
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='power table';

BEGIN;
INSERT INTO `power` (`id`, `nama`, `lokasi`, `nama_ruangan`, `posisi_rak`, `source`, `power`, `tipe`, `sn_aset`, `create_time`, `update_time`) VALUES
(1, 'PDU_1A', 'Kominfo', 'Server', '1', 'A', '1', 'CH14', '', '2023-09-11 09:00:24', '2023-09-11 09:00:24'),
(2, 'PDU_1A', 'Kominfo', 'Server', '1', 'A', '2', 'CH14', '', '2023-09-11 09:00:52', '2023-09-11 09:00:52'),
(3, 'PDU_1B', 'Kominfo', 'Server', '1', 'B', '1', 'CH14', '', '2023-09-11 09:01:07', '2023-09-11 09:01:07'),
(4, 'PDU_2B', 'Kominfo', 'Server', '2', 'B', '1', 'CH14', '', '2023-09-11 09:01:18', '2023-09-11 09:01:18'),
(5, 'PDU_2B', 'Kominfo', 'Server', '2', 'B', '2', 'CH14', '', '2023-09-11 09:01:34', '2023-09-11 09:01:34'),
(6, 'PDU_1B', 'Kominfo', 'Server', '2', 'A', '1', 'CH14', '', '2023-09-11 09:01:42', '2023-09-11 09:01:42'),
(7, 'PDU_2A', 'Kominfo', 'Server', '1', 'A', '1', 'CH20', '', '2023-09-14 06:28:05', '2023-09-14 06:28:05'),
(8, 'PDU_2A', 'Kominfo', 'Server', '1', 'A', '2', 'CH21', '', '2023-09-14 06:28:05', '2023-09-14 06:28:05')
COMMIT;

DROP TABLE IF EXISTS 'pakai_aset';
CREATE TABLE `pakai_aset` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nomor_seri` varchar(255) NOT NULL,
  `nomor_tiket` varchar(255) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
   PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='pakai_aset table';

DROP TABLE IF EXISTS 'pengunjung_hadir';
CREATE TABLE `pengunjung_hadir` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nomor_tiket` varchar(255) NOT NULL,
  `nik` varchar(20) NOT NULL,
  `hadir` varchar(20) DEFAULT '-',
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
   PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='pengunjung_hadir table';

DROP TABLE IF EXISTS 'rack';
CREATE TABLE `rack` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `posx` int(11) NOT NULL,
  `posy` int(11) NOT NULL,
  `posz` int(11) NOT NULL,
  `width` int(11) NOT NULL,
  `height` int(11) NOT NULL,
  `depth` int(11) NOT NULL,
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
   PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='rack table';
