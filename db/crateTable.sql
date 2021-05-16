CREATE DATABASE `person_manage`;
USE `person_manage`;

CREATE TABLE `user_info` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `username` varchar(32) NOT NULL COMMENT '登录用户名',
    `password` varchar(32) NOT NULL NULL COMMENT '登录密码',
    `type` tinyint(4) NOT NULL DEFAULT 1 COMMENT '账号类型: 1-普通用户, 2-普通管理员, 3-超级管理员',
    `status` tinyint(4) NOT NULL DEFAULT 0 COMMENT '账号状态: 0-存续, 1-废除',
    `createtime` datetime NOT NULL COMMENT '创建时间',
    `lastupdate` datetime NOT NULL COMMENT '更新时间',
    PRIMARY KEY (`id`),
    UNIQUE KEY (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COMMENT='用户账号信息表';
INSERT INTO `user_info` (id, username, password, type, status, createtime, lastupdate) VALUES (1, 'root', '123456', 3, 0, now(), now());
INSERT INTO `user_info` (id, username, password, type, status, createtime, lastupdate) VALUES (2, 'admin', '123456', 2, 0, now(), now());


CREATE TABLE `register_map` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `register_id` int(11) NOT NULL COMMENT '注册者id',
    `registered_id` int(11) NOT NULL NULL COMMENT '被注册者id',
    `createtime` datetime NOT NULL COMMENT '创建时间',
    PRIMARY KEY (`id`),
    UNIQUE KEY (`registered_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COMMENT='管理员注册账号关系表';


CREATE TABLE `family_info` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `user_id` int(11) NOT NULL COMMENT '录入者用户id',
    `community` varchar(32) NOT NULL COMMENT '社区名称',
    `building` varchar(32) NOT NULL COMMENT '楼(幢)号',
    `dormitory` varchar(32) NOT NULL COMMENT '户(室)号',
    `master_name` varchar(32) DEFAULT NULL COMMENT '户主姓名',
    `json_data` text DEFAULT NULL COMMENT '房屋信息json字符串',
    `createtime` datetime NOT NULL COMMENT '创建时间',
    PRIMARY KEY (`id`),
    UNIQUE KEY (`community`, `building`, `dormitory`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COMMENT='房屋信息表';


CREATE TABLE `personnel_info` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `user_id` int(11) NOT NULL COMMENT '归属账号id',
    `family_id` int(11) NOT NULL COMMENT '家庭id',
    `type` tinyint(4) NOT NULL DEFAULT 0 COMMENT '0-常驻人口, 1-流动人口, 2-新生人口, 3-死亡人口',
    `domicile` varchar(32) NOT NULL COMMENT '户籍所在地',
    `json_data` text DEFAULT NULL COMMENT '房屋信息json字符串',
    `createtime` datetime NOT NULL COMMENT '创建时间',
    PRIMARY KEY (`id`),
    UNIQUE KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COMMENT='居民信息表';