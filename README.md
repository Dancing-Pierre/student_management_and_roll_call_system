# student_management_system
基于Python Tkinter的学生管理系统，有最基本的增删改查功能，还有随机点名、顺序点名功能

## 1、研究现状综述

目前，在学生信息管理领域，各大高校面临的难题在于对学生信息管理的效率过低，传统的人工管理造成了资金和劳动力的浪费。因此，大部分学者研究的是针对高校的学生信息或成绩管理系统，而用python语言的也很少，其中大多用的是PyQt5模块。而且，针对低年级小学生的具有点名功能的学生管理系统基本没有。

## 2、可行性分析

根据市场上所具有的学生管理系统得，目前市面上的学生管理系统大多是具有增删查改等几部分内容，所面向的群体是中高校的教师群体，最主要的功能是教师方便管理学生的信息。而本设计是面向小学低年级学生的管理系统，其中最重要的功能是随机点名，顺序点名功能等，其目的是增加教师上课时的趣味性，激发学生们回答问题的兴趣。

## 3、重点/思路

- 连接数据库。使用第三方工具Navicat连接MySQL。

- 创建student表

- python连接数据库

- 主页设计。使用Tkinter.

- 点名系统时学生姓名名单的加载实现。

- 点名系统模式切换实现。通过if语句赋值判断模式。

- 点名抽取历史查看实现。先定义一个空列表，然后将取得的学生姓名加载到空列表即可。

## 4、实现

### 4.1 在MySQL中新建数据库和数据表

新建students_db数据库：

```mysql
CREATE DATABASE students_db CHARACTER SET utf8 COLLATE utf8_general_ci;
```

新建students数据表存放学生信息，有学号，姓名，年龄，性别，电话字段：

```mysql
CREATE TABLE students (
  id VARCHAR(4) NOT NULL,
  name VARCHAR(20) NOT NULL,
  age INT NOT NULL,
  gender VARCHAR(2) NOT NULL,
  phone VARCHAR(20) NOT NULL,
  PRIMARY KEY (id)
);
```

新建user用户表，存放登录用户信息，有自增id、账号、密码三个字段：

```mysql
CREATE TABLE User (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(32) NOT NULL
);
```

新建history表，存放点名记录，有自增id、点名日期、姓名三个字段：

```mysql
CREATE TABLE history (
  id INT NOT NULL AUTO_INCREMENT,
  date DATE NOT NULL,
  name VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);
```

