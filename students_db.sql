/*
 Navicat Premium Data Transfer

 Source Server         : MySQL
 Source Server Type    : MySQL
 Source Server Version : 50741
 Source Host           : localhost:3306
 Source Schema         : students_db

 Target Server Type    : MySQL
 Target Server Version : 50741
 File Encoding         : 65001

 Date: 22/05/2023 14:51:04
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for history
-- ----------------------------
DROP TABLE IF EXISTS `history`;
CREATE TABLE `history`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `chuqing` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 33 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of history
-- ----------------------------
INSERT INTO `history` VALUES (1, '2023-05-17', '张三', '出勤');
INSERT INTO `history` VALUES (2, '2023-05-17', '李四', '未出勤');
INSERT INTO `history` VALUES (3, '2023-05-17', '张三', '出勤');
INSERT INTO `history` VALUES (4, '2023-05-17', '李四', '出勤');
INSERT INTO `history` VALUES (5, '2023-05-17', '王五', '未出勤');
INSERT INTO `history` VALUES (6, '2023-05-17', '李四', '出勤');
INSERT INTO `history` VALUES (7, '2023-05-17', '张三', '出勤');
INSERT INTO `history` VALUES (8, '2023-05-17', '王五', '未出勤');
INSERT INTO `history` VALUES (9, '2023-05-17', '张三', '出勤');
INSERT INTO `history` VALUES (10, '2023-05-22', '张三', '未出勤');
INSERT INTO `history` VALUES (11, '2023-05-22', '李四', '出勤');
INSERT INTO `history` VALUES (12, '2023-05-22', '张三', '未出勤');
INSERT INTO `history` VALUES (13, '2023-05-22', '李四', '出勤');
INSERT INTO `history` VALUES (14, '2023-05-22', '王五', '出勤');
INSERT INTO `history` VALUES (15, '2023-05-22', '李四', '未出勤');
INSERT INTO `history` VALUES (16, '2023-05-22', '张三', '出勤');
INSERT INTO `history` VALUES (17, '2023-05-22', '李四', '未出勤');
INSERT INTO `history` VALUES (18, '2023-05-22', '张三', '出勤');
INSERT INTO `history` VALUES (19, '2023-05-22', '李四', '未出勤');
INSERT INTO `history` VALUES (20, '2023-05-22', '王五', '出勤');
INSERT INTO `history` VALUES (21, '2023-05-22', '李四', '出勤');
INSERT INTO `history` VALUES (22, '2023-05-22', '张三', '未出勤');
INSERT INTO `history` VALUES (23, '2023-05-22', '王五', '出勤');
INSERT INTO `history` VALUES (24, '2023-05-22', '张三', '未出勤');
INSERT INTO `history` VALUES (25, '2023-05-22', '张三', '出勤');
INSERT INTO `history` VALUES (26, '2023-05-22', '王五', '出勤');
INSERT INTO `history` VALUES (27, '2023-05-22', '王五', '出勤');
INSERT INTO `history` VALUES (28, '2023-05-22', '李四', '出勤');
INSERT INTO `history` VALUES (29, '2023-05-22', '王五', '出勤');
INSERT INTO `history` VALUES (30, '2023-05-22', '李四', '出勤');
INSERT INTO `history` VALUES (31, '2023-05-22', '张三', '出勤');
INSERT INTO `history` VALUES (32, '2023-05-22', '李四', '出勤');

-- ----------------------------
-- Table structure for score
-- ----------------------------
DROP TABLE IF EXISTS `score`;
CREATE TABLE `score`  (
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `class` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `subject` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `score` int(255) NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of score
-- ----------------------------
INSERT INTO `score` VALUES ('张三', '1班', '语文', 98);
INSERT INTO `score` VALUES ('王五', '1班', '语文', 80);
INSERT INTO `score` VALUES ('李四', '2班', '语文', 100);
INSERT INTO `score` VALUES ('张三', '1班', '数学', 100);
INSERT INTO `score` VALUES ('4', '2班', '语文', 90);

-- ----------------------------
-- Table structure for students
-- ----------------------------
DROP TABLE IF EXISTS `students`;
CREATE TABLE `students`  (
  `id` varchar(4) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `age` int(11) NOT NULL,
  `gender` varchar(2) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `phone` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `parents_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `address` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of students
-- ----------------------------
INSERT INTO `students` VALUES ('1', '张三', 13, '女', '123123', '张三_1', '江苏');
INSERT INTO `students` VALUES ('2', '李四', 12, '女', '2424245', '王五', '杭州');
INSERT INTO `students` VALUES ('3', '王五', 12, '男', '3253535', '张三', '北京');
INSERT INTO `students` VALUES ('4', '4', 4, '4', '4', '4', '上海');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password_hash` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 10000 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (2, '123', '202cb962ac59075b964b07152d234b70');
INSERT INTO `user` VALUES (7, '333', '310dcbbf4cce62f762a2aaa148d556bd');
INSERT INTO `user` VALUES (8, '222', 'bcbe3365e6ac95ea2c0343a2395834dd');
INSERT INTO `user` VALUES (9, '444', '550a141f12de6341fba65b0ad0433500');
INSERT INTO `user` VALUES (9999, 'admin', '21232f297a57a5a743894a0e4a801fc3');

SET FOREIGN_KEY_CHECKS = 1;
