-- MySQL dump 10.13  Distrib 8.2.0, for macos14.0 (arm64)
--
-- Host: localhost    Database: growth_vision
-- ------------------------------------------------------
-- Server version	8.2.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can view permission',1,'view_permission'),(5,'Can add group',2,'add_group'),(6,'Can change group',2,'change_group'),(7,'Can delete group',2,'delete_group'),(8,'Can view group',2,'view_group'),(9,'Can add user',3,'add_user'),(10,'Can change user',3,'change_user'),(11,'Can delete user',3,'delete_user'),(12,'Can view user',3,'view_user'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add user',6,'add_user'),(22,'Can change user',6,'change_user'),(23,'Can delete user',6,'delete_user'),(24,'Can view user',6,'view_user'),(25,'Can add plat form dou yin',7,'add_platformdouyin'),(26,'Can change plat form dou yin',7,'change_platformdouyin'),(27,'Can delete plat form dou yin',7,'delete_platformdouyin'),(28,'Can view plat form dou yin',7,'view_platformdouyin'),(29,'Can add data dou yin',8,'add_datadouyin'),(30,'Can change data dou yin',8,'change_datadouyin'),(31,'Can delete data dou yin',8,'delete_datadouyin'),(32,'Can view data dou yin',8,'view_datadouyin'),(33,'Can add plat form zhi hu',9,'add_platformzhihu'),(34,'Can change plat form zhi hu',9,'change_platformzhihu'),(35,'Can delete plat form zhi hu',9,'delete_platformzhihu'),(36,'Can view plat form zhi hu',9,'view_platformzhihu'),(37,'Can add data zhi hu',10,'add_datazhihu'),(38,'Can change data zhi hu',10,'change_datazhihu'),(39,'Can delete data zhi hu',10,'delete_datazhihu'),(40,'Can view data zhi hu',10,'view_datazhihu'),(41,'Can add plat form bai jia hao',11,'add_platformbaijiahao'),(42,'Can change plat form bai jia hao',11,'change_platformbaijiahao'),(43,'Can delete plat form bai jia hao',11,'delete_platformbaijiahao'),(44,'Can view plat form bai jia hao',11,'view_platformbaijiahao'),(45,'Can add plat form data',12,'add_platformdata'),(46,'Can change plat form data',12,'change_platformdata'),(47,'Can delete plat form data',12,'delete_platformdata'),(48,'Can view plat form data',12,'view_platformdata'),(49,'Can add history date',13,'add_historydate'),(50,'Can change history date',13,'change_historydate'),(51,'Can delete history date',13,'delete_historydate'),(52,'Can view history date',13,'view_historydate'),(53,'Can add plat form bilibili',14,'add_platformbilibili'),(54,'Can change plat form bilibili',14,'change_platformbilibili'),(55,'Can delete plat form bilibili',14,'delete_platformbilibili'),(56,'Can view plat form bilibili',14,'view_platformbilibili'),(57,'Can add django job',15,'add_djangojob'),(58,'Can change django job',15,'change_djangojob'),(59,'Can delete django job',15,'delete_djangojob'),(60,'Can view django job',15,'view_djangojob'),(61,'Can add django job execution',16,'add_djangojobexecution'),(62,'Can change django job execution',16,'change_djangojobexecution'),(63,'Can delete django job execution',16,'delete_djangojobexecution'),(64,'Can view django job execution',16,'view_djangojobexecution');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_apscheduler_djangojob`
--

DROP TABLE IF EXISTS `django_apscheduler_djangojob`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_apscheduler_djangojob` (
  `id` varchar(255) NOT NULL,
  `next_run_time` datetime(6) DEFAULT NULL,
  `job_state` longblob NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_apscheduler_djangojob_next_run_time_2f022619` (`next_run_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_apscheduler_djangojob`
--

LOCK TABLES `django_apscheduler_djangojob` WRITE;
/*!40000 ALTER TABLE `django_apscheduler_djangojob` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_apscheduler_djangojob` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_apscheduler_djangojobexecution`
--

DROP TABLE IF EXISTS `django_apscheduler_djangojobexecution`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_apscheduler_djangojobexecution` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `status` varchar(50) NOT NULL,
  `run_time` datetime(6) NOT NULL,
  `duration` decimal(15,2) DEFAULT NULL,
  `finished` decimal(15,2) DEFAULT NULL,
  `exception` varchar(1000) DEFAULT NULL,
  `traceback` longtext,
  `job_id` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_job_executions` (`job_id`,`run_time`),
  KEY `django_apscheduler_djangojobexecution_run_time_16edd96b` (`run_time`),
  CONSTRAINT `django_apscheduler_djangojobexecution_job_id_daf5090a_fk` FOREIGN KEY (`job_id`) REFERENCES `django_apscheduler_djangojob` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=99 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_apscheduler_djangojobexecution`
--

LOCK TABLES `django_apscheduler_djangojobexecution` WRITE;
/*!40000 ALTER TABLE `django_apscheduler_djangojobexecution` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_apscheduler_djangojobexecution` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (2,'auth','group'),(1,'auth','permission'),(3,'auth','user'),(4,'contenttypes','contenttype'),(15,'django_apscheduler','djangojob'),(16,'django_apscheduler','djangojobexecution'),(8,'mainsite','datadouyin'),(10,'mainsite','datazhihu'),(13,'mainsite','historydate'),(11,'mainsite','platformbaijiahao'),(14,'mainsite','platformbilibili'),(12,'mainsite','platformdata'),(7,'mainsite','platformdouyin'),(9,'mainsite','platformzhihu'),(6,'mainsite','user'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-11-16 10:07:11.970753'),(2,'contenttypes','0002_remove_content_type_name','2023-11-16 10:07:12.019234'),(3,'auth','0001_initial','2023-11-16 10:07:12.301916'),(4,'auth','0002_alter_permission_name_max_length','2023-11-16 10:07:12.322327'),(5,'auth','0003_alter_user_email_max_length','2023-11-16 10:07:12.337655'),(6,'auth','0004_alter_user_username_opts','2023-11-16 10:07:12.343287'),(7,'auth','0005_alter_user_last_login_null','2023-11-16 10:07:12.360649'),(8,'auth','0006_require_contenttypes_0002','2023-11-16 10:07:12.362168'),(9,'auth','0007_alter_validators_add_error_messages','2023-11-16 10:07:12.367785'),(10,'auth','0008_alter_user_username_max_length','2023-11-16 10:07:12.387160'),(11,'auth','0009_alter_user_last_name_max_length','2023-11-16 10:07:12.405048'),(12,'auth','0010_alter_group_name_max_length','2023-11-16 10:07:12.416706'),(13,'auth','0011_update_proxy_permissions','2023-11-16 10:07:12.421797'),(14,'auth','0012_alter_user_first_name_max_length','2023-11-16 10:07:12.438637'),(15,'mainsite','0001_initial','2023-11-16 10:07:12.493320'),(16,'sessions','0001_initial','2023-11-16 10:07:12.505185'),(17,'mainsite','0002_platformdouyin_auth_time','2023-11-22 11:00:36.683193'),(18,'mainsite','0003_platformzhihu','2023-11-22 11:40:30.921580'),(19,'mainsite','0004_remove_platformzhihu_id_alter_platformzhihu_zh_uid','2023-11-22 11:42:54.234440'),(20,'mainsite','0005_alter_platformzhihu_zh_uid','2023-11-22 14:01:58.742285'),(21,'mainsite','0006_alter_platformzhihu_z_c0_datazhihu','2023-11-23 10:29:44.135608'),(22,'mainsite','0007_datazhihu_create_time','2023-11-23 11:03:08.687353'),(23,'mainsite','0008_datazhihu_type','2023-11-23 11:03:08.707380'),(24,'mainsite','0009_platformbaijiahao','2023-11-27 11:31:53.806646'),(25,'mainsite','0010_platformbaijiahao_bjhstoken','2023-11-27 15:08:18.405157'),(26,'mainsite','0011_platformdata','2023-12-01 15:02:21.000327'),(27,'mainsite','0012_platformdata_nickname','2023-12-02 09:37:22.557656'),(28,'mainsite','0013_alter_platformdata_item_id','2023-12-02 10:13:06.185976'),(29,'mainsite','0014_remove_datazhihu_uid_remove_datazhihu_zh_uid_and_more','2023-12-04 09:09:11.757054'),(32,'mainsite','0015_historydate','2023-12-04 17:18:57.381390'),(33,'mainsite','0016_platformbilibili','2023-12-06 12:01:12.598411'),(34,'django_apscheduler','0001_initial','2023-12-07 09:39:07.698805'),(35,'django_apscheduler','0002_auto_20180412_0758','2023-12-07 09:39:07.719003'),(36,'django_apscheduler','0003_auto_20200716_1632','2023-12-07 09:39:07.736200'),(37,'django_apscheduler','0004_auto_20200717_1043','2023-12-07 09:39:07.801958'),(38,'django_apscheduler','0005_migrate_name_to_id','2023-12-07 09:39:07.818653'),(39,'django_apscheduler','0006_remove_djangojob_name','2023-12-07 09:39:07.831311'),(40,'django_apscheduler','0007_auto_20200717_1404','2023-12-07 09:39:07.848506'),(41,'django_apscheduler','0008_remove_djangojobexecution_started','2023-12-07 09:39:07.855959'),(42,'django_apscheduler','0009_djangojobexecution_unique_job_executions','2023-12-07 09:39:07.863017');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('03hz10fo1h4stg2435r1z16v10kneii8','eyJpbWFnZV9jb2RlIjoiOTU3NTAiLCJfc2Vzc2lvbl9leHBpcnkiOjYwfQ:1r3YAI:rfVY7gYgZWHlDMPSHl-JG4sZ_MctWapdqdrWJ-hlKbU','2023-11-16 16:56:58.979338'),('1cebdc1vnnh5gj8g1yi5465mqpaqs4ke','eyJpbWFnZV9jb2RlIjoiMDEyNTciLCJfc2Vzc2lvbl9leHBpcnkiOjYwfQ:1r4KEF:mnp4Ndh1gBV1eEGh9tZRRuiM-7xu-5KD-lgIuOTTtC4','2023-11-18 20:16:15.073211'),('1f1zv636jmbymmvdpxmpxn6qf8cajbkm','eyJpbWFnZV9jb2RlIjoiOTI3NTIiLCJfc2Vzc2lvbl9leHBpcnkiOjQzMjAwMCwiaW5mbyI6eyJ1aWQiOjIwMjMxMTE2NDUxMSwidXNlcm5hbWUiOiJhZG1pbiJ9fQ:1r6Oj0:0obKlv-LQ3e1LfBnGCSR88uw2KI_OmA_g8aljFs54G4','2023-11-29 13:27:34.004243'),('2z0sx2mr9mtzi65k5wslnnb1m9prosld','eyJpbWFnZV9jb2RlIjoiNTczNTciLCJfc2Vzc2lvbl9leHBpcnkiOjYwfQ:1r3Y7P:5rgf47NOuOJ819DAw-3qcRgdmyc9HVUmwFJJqQpjrv0','2023-11-16 16:53:59.258598'),('4lq8ytcvc2ntgywyz6hvc53jhx0gubho','.eJwVzEEKgCAQBdC7_LWLmdFaeBmRnGIWaiRBEd09egd4D6zmTdPSiyJCyAeBQxo6hvWW9NrtuBGDFyJysLZ2xAenFUQh8cw8h4nZ4Rx6tFz_JpdqDe_7AVvbHKk:1rBOaM:2LuS1CLUHDC2LV2UZGw2m6us847WK2lQv0Tp9Dhxb_w','2023-12-13 08:19:18.510236'),('axhzy15yjjlelf7pb4akcfx3cz6hyy9m','eyJpbWFnZV9jb2RlIjoiMzE4MTgiLCJfc2Vzc2lvbl9leHBpcnkiOjQzMjAwMCwiaW5mbyI6eyJ1aWQiOjIwMjMxMTIzMjc2OSwidXNlcm5hbWUiOiJ0ZW1wIn19:1rB4ww:hJWqHcJeBe4oBL6W5URYTiFS9BA0LSHvZCzjM1oYQpk','2023-12-12 11:21:18.714561'),('bd9piu92loq97rr52zf25i292o1faytm','eyJpbWFnZV9jb2RlIjoiMjI4MTkiLCJfc2Vzc2lvbl9leHBpcnkiOjYwfQ:1r49r6:yTLtCkiQg0TygHFi9Ia26kgSezGT6pBqeDyLj-7pp6E','2023-11-18 09:11:40.093166'),('hhzjg7xn9wfvr4zu5hu6fj1tqawq84mm','.eJwVzEEKgCAQBdC7_LULx0rMy4jkFLNQIxEK6e7RO8AbkBwPDltNDA_n7EpQCI1bk1oC36dcD_w8Ga21gpS9wg90SfBGm4mI7LwQKfTGV4n5b2LKUvC-H2I9HL4:1r5FrP:I2Yq5BEFxWCfqce7cDbDvPB_vxBupJBAsxE2-GCtEmg','2023-11-26 09:47:31.603400'),('iw6ckvoz6rg5wuino4gcv6ef1km2sxzv','eyJpbWFnZV9jb2RlIjoiNDk5MTkiLCJfc2Vzc2lvbl9leHBpcnkiOjYwfQ:1r4C9e:wTD40rfK_LvSVKthzb5eekyIDkKg_hHVm4q15Pt_488','2023-11-18 11:38:58.201136'),('kvx9duo7nhdahos5mfmw843n9feboxda','eyJpbWFnZV9jb2RlIjoiMTIwODEiLCJfc2Vzc2lvbl9leHBpcnkiOjYwfQ:1r4A4f:ShjKzsAGtcQqY5uoNTN1jxogznVtCvQKXDoTT0TFTqk','2023-11-18 09:25:41.403651'),('ltdkb9icdm7hgzoq36r342ddo7yhkf12','eyJpbWFnZV9jb2RlIjoiODM5NjUiLCJfc2Vzc2lvbl9leHBpcnkiOjYwfQ:1rB3SZ:RYYxIVHI5pYhEoIBmQFa_spOu-enfw_L1Ps1Qk9gTXE','2023-12-07 09:46:51.043410'),('nmo69yq8rkle68h08lgzioa2tl10r85t','eyJpbWFnZV9jb2RlIjoiNTUzNzAiLCJfc2Vzc2lvbl9leHBpcnkiOjYwLCJpbmZvIjp7InVpZCI6MjAyMzExMTY0NTExLCJ1c2VybmFtZSI6ImFkbWluIn19:1r6Oeb:C_rUW_ZoFkMIWp6O4RqUX1R6QeuIgbLGJhoOoCu3sbk','2023-11-24 13:24:01.256688'),('r6zul75a23nh1u8jkyeorq928tm86fyl','eyJpbWFnZV9jb2RlIjoiODc1NTMiLCJfc2Vzc2lvbl9leHBpcnkiOjYwfQ:1r49xs:PxL9UrsNfXU_hKcvabvLVz0Gj7dr7rHkFaEfnDTgSjE','2023-11-18 09:18:40.275946'),('ujoq335utgjwaangtrul5do8inv0d8ky','.eJwVzEEKgCAQBdC7_LULx0zCy4jkFLNQQwkK8e7RO8AbkBxPDntNDI_NGUtQCJ17l1oCP5e0F94uRmutIOWo8AO3JHijzUJEzq5ECnfnVmL-m5iyFMz5AV7xHLM:1rB4xh:Ne3iDkHQi54PcfRYz0KxbguEgseo3ZgSSpTnEleniCY','2023-12-12 11:22:05.230164'),('w4din8qxz0nkdjp45h5c5dcvq2ufc9gi','eyJpbWFnZV9jb2RlIjoiNzk4ODMiLCJfc2Vzc2lvbl9leHBpcnkiOjYwfQ:1r3c5P:-cN4SzjJvglAHfMcm266koYAhxO5U-ugmCBWKiDhlFA','2023-11-16 21:08:11.344390'),('w95lf7mswsqzbralxczt254wsphxekcq','eyJpbWFnZV9jb2RlIjoiNDE1NjgiLCJfc2Vzc2lvbl9leHBpcnkiOjYwfQ:1r4A78:uvcQeujd6rJoQ9204agcfku5LxgQ6v3Tx9GEwq5b95o','2023-11-18 09:28:14.249761');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mainsite_historydate`
--

DROP TABLE IF EXISTS `mainsite_historydate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mainsite_historydate` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `nickname` varchar(64) NOT NULL,
  `platform_uid` varchar(500) NOT NULL,
  `uid` varchar(64) NOT NULL,
  `platform` varchar(64) NOT NULL,
  `like_sum` int NOT NULL,
  `comment_sum` int NOT NULL,
  `play_sum` int NOT NULL,
  `download_rec_sum` int NOT NULL,
  `share_vote_sum` int NOT NULL,
  `forward_collect_sum` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=60 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mainsite_historydate`
--

LOCK TABLES `mainsite_historydate` WRITE;
/*!40000 ALTER TABLE `mainsite_historydate` DISABLE KEYS */;
INSERT INTO `mainsite_historydate` VALUES (1,'2023-11-30','四叶天代理IP001','_0004KdgRfrPtVLR8nN2WKq_hQp5sQT6orgn','202311164511','抖音',236,97,60578,5,46,0),(2,'2023-11-30','短效IP百里','1734231139480701','202311164511','百家号',232,277,140114,216621,90,535),(3,'2023-11-30','四叶天','1fdef83551b8a7f4190a7fc9c5f9aa6e','202311164511','知乎',1,0,2434,0,0,5),(4,'2023-11-30','四叶天代理','_000k75I4Y4kVLb9WJdcliUhUr7nJHFtTugR','202311164511','抖音',27,1,7507,3,3,0),(5,'2023-12-01','四叶天代理IP001','_0004KdgRfrPtVLR8nN2WKq_hQp5sQT6orgn','202311164511','抖音',248,100,60777,10,60,10),(6,'2023-12-01','短效IP百里','1734231139480701','202311164511','百家号',244,300,147777,236621,100,600),(7,'2023-12-01','四叶天','1fdef83551b8a7f4190a7fc9c5f9aa6e','202311164511','知乎',13,2,2777,10,10,10),(8,'2023-12-01','四叶天代理','_000k75I4Y4kVLb9WJdcliUhUr7nJHFtTugR','202311164511','抖音',35,6,7777,20,9,6),(29,'2023-12-02','四叶天代理','_000k75I4Y4kVLb9WJdcliUhUr7nJHFtTugR','202311164511','抖音',77,51,7607,203,33,15),(30,'2023-12-02','短效IP百里','1734231139480701','202311164511','百家号',282,327,140214,216821,120,550),(31,'2023-12-02','四叶天代理IP001','_0004KdgRfrPtVLR8nN2WKq_hQp5sQT6orgn','202311164511','抖音',286,147,60678,205,76,15),(32,'2023-12-02','四叶天','1fdef83551b8a7f4190a7fc9c5f9aa6e','202311164511','知乎',51,50,2534,200,30,20),(33,'2023-12-03','四叶天代理','_000k75I4Y4kVLb9WJdcliUhUr7nJHFtTugR','202311164511','抖音',127,101,7657,253,63,30),(34,'2023-12-03','四叶天代理IP001','_0004KdgRfrPtVLR8nN2WKq_hQp5sQT6orgn','202311164511','抖音',336,197,60728,255,106,30),(35,'2023-12-03','四叶天','1fdef83551b8a7f4190a7fc9c5f9aa6e','202311164511','知乎',101,100,2584,250,60,35),(36,'2023-12-03','短效IP百里','1734231139480701','202311164511','百家号',332,377,140264,216871,150,565),(37,'2023-12-04','四叶天','1fdef83551b8a7f4190a7fc9c5f9aa6e','202311164511','知乎',151,150,2684,350,100,65),(38,'2023-12-04','四叶天代理IP001','_0004KdgRfrPtVLR8nN2WKq_hQp5sQT6orgn','202311164511','抖音',386,247,60828,355,146,60),(39,'2023-12-04','四叶天代理','_000k75I4Y4kVLb9WJdcliUhUr7nJHFtTugR','202311164511','抖音',177,151,7757,353,103,60),(40,'2023-12-04','短效IP百里','1734231139480701','202311164511','百家号',382,427,140364,216971,190,595),(41,'2023-12-05','四叶天','1fdef83551b8a7f4190a7fc9c5f9aa6e','202311164511','知乎',1,0,2439,0,0,5),(42,'2023-12-05','短效IP百里','1734231139480701','202311164511','百家号',232,277,140129,216622,90,535),(43,'2023-12-05','四叶天代理','_000k75I4Y4kVLb9WJdcliUhUr7nJHFtTugR','202311164511','抖音',27,1,7592,3,3,0),(44,'2023-12-05','四叶天代理IP001','_0004KdgRfrPtVLR8nN2WKq_hQp5sQT6orgn','202311164511','抖音',237,97,60889,6,47,0),(50,'2023-12-06','四叶天代理','_000k75I4Y4kVLb9WJdcliUhUr7nJHFtTugR','202311164511','抖音',27,1,7687,3,3,0),(51,'2023-12-06','四叶天','1fdef83551b8a7f4190a7fc9c5f9aa6e','202311164511','知乎',1,0,2451,0,0,5),(52,'2023-12-06','四叶天ip代理','9aa6e1e9fc0f47f6b2999d0e333e9291','202311164511','哔哩哔哩',19,4,1775,0,6,3),(53,'2023-12-06','四叶天代理','ebdf5476069f420daafb77d7ffdbc62d','202311164511','哔哩哔哩',27,2,4963,0,0,12),(54,'2023-12-06','四叶天代理IP001','_0004KdgRfrPtVLR8nN2WKq_hQp5sQT6orgn','202311164511','抖音',239,97,61323,6,47,0),(55,'2023-12-07','四叶天代理IP001','_0004KdgRfrPtVLR8nN2WKq_hQp5sQT6orgn','202311164511','抖音',239,97,61545,6,47,0),(56,'2023-12-07','四叶天代理','_000k75I4Y4kVLb9WJdcliUhUr7nJHFtTugR','202311164511','抖音',27,1,7747,3,3,0),(57,'2023-12-07','四叶天代理','ebdf5476069f420daafb77d7ffdbc62d','202311164511','哔哩哔哩',27,2,4993,0,0,12),(58,'2023-12-07','四叶天ip代理','9aa6e1e9fc0f47f6b2999d0e333e9291','202311164511','哔哩哔哩',19,4,1783,0,6,3),(59,'2023-12-07','四叶天','1fdef83551b8a7f4190a7fc9c5f9aa6e','202311164511','知乎',1,0,2452,0,0,5);
/*!40000 ALTER TABLE `mainsite_historydate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mainsite_platformbaijiahao`
--

DROP TABLE IF EXISTS `mainsite_platformbaijiahao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mainsite_platformbaijiahao` (
  `nickname` varchar(26) NOT NULL,
  `avatar` varchar(255) NOT NULL,
  `expires_time` datetime(6) NOT NULL,
  `auth_time` datetime(6) DEFAULT NULL,
  `app_id` varchar(255) NOT NULL,
  `bduss` varchar(500) NOT NULL,
  `token` varchar(500) NOT NULL,
  `uid_id` bigint NOT NULL,
  `bjhstoken` varchar(500) NOT NULL,
  PRIMARY KEY (`app_id`),
  KEY `mainsite_platformbaijiahao_uid_id_d933106b_fk_mainsite_user_uid` (`uid_id`),
  CONSTRAINT `mainsite_platformbaijiahao_uid_id_d933106b_fk_mainsite_user_uid` FOREIGN KEY (`uid_id`) REFERENCES `mainsite_user` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mainsite_platformbaijiahao`
--

LOCK TABLES `mainsite_platformbaijiahao` WRITE;
/*!40000 ALTER TABLE `mainsite_platformbaijiahao` DISABLE KEYS */;
INSERT INTO `mainsite_platformbaijiahao` VALUES ('四叶天代理','https://pic.rmb.bdstatic.com/bjh/user/65473f8faba23b3b4ed61dc415bb51e5.jpeg','2024-02-05 16:14:02.000000','2023-12-07 16:14:02.000000','1699159270507497','0xpdTRUcVplNTBTTUx6QmJCOXpGa1NTMkdJSGZic2JmR1VLazRnZnd6Z1pDWmxsRUFBQUFBJCQAAAAAAAAAAAEAAAD6H8k22K1BY2NvbXBhbnkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABl8cWUZfHFlc','eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9iYWlqaWFoYW8uYmFpZHUuY29tIiwiYXVkIjoiaHR0cDpcL1wvYmFpamlhaGFvLmJhaWR1LmNvbSIsImlhdCI6MTcwMTkzNjM1MSwibmJmIjoxNzAxODkzMTU2LCJleHAiOjE3MDE5Nzk1NTZ9.Gld_-3TeH3yVY219zJ3ziDkCYx-FnFRM84pUpZjp88s',202311164511,'359172b222d17663cd1928c6efb2645e5925b3bad45de5623549d6c016c9efde');
/*!40000 ALTER TABLE `mainsite_platformbaijiahao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mainsite_platformbilibili`
--

DROP TABLE IF EXISTS `mainsite_platformbilibili`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mainsite_platformbilibili` (
  `openid` varchar(255) NOT NULL,
  `access_token` varchar(255) NOT NULL,
  `refresh_token` varchar(255) NOT NULL,
  `nickname` varchar(64) NOT NULL,
  `avatar` varchar(255) NOT NULL,
  `expires_in` datetime(6) NOT NULL,
  `auth_time` datetime(6) DEFAULT NULL,
  `uid_id` bigint NOT NULL,
  PRIMARY KEY (`openid`),
  KEY `mainsite_platformbilibili_uid_id_07f12353_fk_mainsite_user_uid` (`uid_id`),
  CONSTRAINT `mainsite_platformbilibili_uid_id_07f12353_fk_mainsite_user_uid` FOREIGN KEY (`uid_id`) REFERENCES `mainsite_user` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mainsite_platformbilibili`
--

LOCK TABLES `mainsite_platformbilibili` WRITE;
/*!40000 ALTER TABLE `mainsite_platformbilibili` DISABLE KEYS */;
INSERT INTO `mainsite_platformbilibili` VALUES ('ebdf5476069f420daafb77d7ffdbc62d','380bf3cf10bd8e9625090b47f77ea5c1','aaf5a25c53ce78dc0f42a77e71d045c1','四叶天代理','https://i0.hdslb.com/bfs/face/6a094769ccd963782e44af35af7795a494680653.jpg','2024-06-04 08:42:36.000000','2023-12-07 16:27:12.000000',202311164511);
/*!40000 ALTER TABLE `mainsite_platformbilibili` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mainsite_platformdata`
--

DROP TABLE IF EXISTS `mainsite_platformdata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mainsite_platformdata` (
  `platform` smallint NOT NULL,
  `item_id` varchar(500) NOT NULL,
  `title` varchar(255) NOT NULL,
  `type` varchar(64) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `platform_uid` varchar(500) NOT NULL,
  `share_url` varchar(500) NOT NULL,
  `like_count` int NOT NULL,
  `comment_count` int NOT NULL,
  `play_count` int NOT NULL,
  `download_rec_count` int NOT NULL,
  `share_vote_count` int NOT NULL,
  `forward_collect_count` int NOT NULL,
  `uid_id` bigint NOT NULL,
  `nickname` varchar(64) NOT NULL,
  PRIMARY KEY (`item_id`),
  KEY `mainsite_platformdata_uid_id_4279d784_fk_mainsite_user_uid` (`uid_id`),
  CONSTRAINT `mainsite_platformdata_uid_id_4279d784_fk_mainsite_user_uid` FOREIGN KEY (`uid_id`) REFERENCES `mainsite_user` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mainsite_platformdata`
--

LOCK TABLES `mainsite_platformdata` WRITE;
/*!40000 ALTER TABLE `mainsite_platformdata` DISABLE KEYS */;
INSERT INTO `mainsite_platformdata` VALUES (1,'@9VwUxeSUWJ9lMiXzco1kRc79123hO/iEM5Z5qg6mLVMVbfD560zdRmYqig357zEB03jU+xSjgM2NaVPhHFOuow==','网络连接中的动态IP每次连接自动切换 #四叶天代理 #ip #dhcp #地址 #切换 #动态','视频','2023-10-11 15:57:08.000000','2023-12-07 17:45:07.000000','_000k75I4Y4kVLb9WJdcliUhUr7nJHFtTugR','https://www.iesdouyin.com/share/video/7288606838340226315/?region=CN&mid=7288606897238379320&u_code=250cbek8656c&did=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&with_sec_did=1&titleType=title&share_sign=OClf6BUJu0aJrLoyEIc9o.CfkcqH.4tcrxwVR_YsvQQ-&share_version=230200&ts=1701942307&from_aid=1128&from_ssr=1',1,0,1021,1,1,0,202311164511,'四叶天代理'),(1,'@9VwUxeSUWJ9lMiXzco1kRc79123hOPqHPZd1qQ+kJlMUafn860zdRmYqig357zEBgdNule0wLIjJioUaQAF+5w==','网络管理员可设置动态IP租约时间 #四叶天代理 #ip #dhcp #地址 #切换 #动态','视频','2023-10-11 10:42:19.000000','2023-12-07 17:45:08.000000','_000k75I4Y4kVLb9WJdcliUhUr7nJHFtTugR','https://www.iesdouyin.com/share/video/7288525624052927780/?region=CN&mid=7288525759017274167&u_code=250cbek8656c&did=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&with_sec_did=1&titleType=title&share_sign=pPQPpipr0TkXzMOTkOWYheSyRs95nn1EBn7hwGdpp9A-&share_version=230200&ts=1701942308&from_aid=1128&from_ssr=1',2,0,1280,0,0,0,202311164511,'四叶天代理'),(1,'@9VwUxeSUWJ9lMiXzco1kRc79123hP/iAOJJxrw6nKVYUa/n860zdRmYqig357zEBnqPoGcIXA840Y4sidGxzuw==','#四叶天代理','视频','2023-10-10 13:48:00.000000','2023-12-07 17:45:08.000000','_000k75I4Y4kVLb9WJdcliUhUr7nJHFtTugR','https://www.iesdouyin.com/share/video/7288202370641677580/?region=CN&mid=7288202525247851323&u_code=250cbek8656c&did=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&with_sec_did=1&titleType=title&share_sign=XSJMXeIopa6275TK7oS8TMQaTxhnMNNLch8IetI0WjM-&share_version=230200&ts=1701942308&from_aid=1128&from_ssr=1',1,0,331,0,0,0,202311164511,'四叶天代理'),(1,'@9VwUxeSUWJ9lMiXzco1kRc79123hP/mEO5B4oQmiJlARbvD160zdRmYqig357zEBmghItbKdbwJtI3HpB8wevQ==','#四叶天代理','视频','2023-10-10 14:41:02.000000','2023-12-07 17:45:08.000000','_000k75I4Y4kVLb9WJdcliUhUr7nJHFtTugR','https://www.iesdouyin.com/share/video/7288216059834912019/?region=CN&mid=7288216183659252535&u_code=250cbek8656c&did=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&with_sec_did=1&titleType=title&share_sign=Ng6Xl9uRj_EDSKD_nvJdyNQxCr26IBdqpkuWbmb.54Q-&share_version=230200&ts=1701942308&from_aid=1128&from_ssr=1',0,0,372,0,0,0,202311164511,'四叶天代理'),(1,'@9VwUxeSUWJ9lMiXzco1kRc79123uOf2BOJVyrQqnKFARZ/T860zdRmYqig357zEBJXstSeiW9aA0c/zi81ARKg==','网络IP冲突原因揭秘手动设置和网络分配两方面！ #四叶天代理 #ip #冲突 #地址 #网络 #动态','视频','2023-10-08 13:21:13.000000','2023-12-07 17:45:08.000000','_000k75I4Y4kVLb9WJdcliUhUr7nJHFtTugR','https://www.iesdouyin.com/share/video/7287453303401712950/?region=CN&mid=7287453465956404023&u_code=250cbek8656c&did=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&with_sec_did=1&titleType=title&share_sign=j2xkyZP34RSvTKzQcn9suqY5P37xVjSCjN.UVOtdqD0-&share_version=230200&ts=1701942308&from_aid=1128&from_ssr=1',2,0,691,0,0,0,202311164511,'四叶天代理'),(1,'@9VwUxeSUWJ9lMiXzco1kRc79123uOPmHPZ1wrQ+nKlMUavb060zdRmYqig357zEBKTQCE7aB6BP+VQa5xGJ5rw==','#四叶天代理','视频','2023-10-08 17:23:07.000000','2023-12-07 17:45:08.000000','_000k75I4Y4kVLb9WJdcliUhUr7nJHFtTugR','https://www.iesdouyin.com/share/video/7287515681451527478/?region=CN&mid=7287515795324324669&u_code=250cbek8656c&did=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&with_sec_did=1&titleType=title&share_sign=eWqmP78zApXiUyMcUD4G_00C2GnmWdI94WtufcqgmQw-&share_version=230200&ts=1701942308&from_aid=1128&from_ssr=1',4,0,548,1,0,0,202311164511,'四叶天代理'),(1,'@9VwUxeSUWJ9lMiXzco1kRc7912LsPPuHPJNzrgKmLlcQbfX860zdRmYqig357zEBosInDiRY/LfUqzoHhpNxHw==','动态IP与拨号你需要了解的网络连接方式 #四叶天代理 #ip #拨号 #地址 #动态 #连接','视频','2023-09-05 08:43:12.000000','2023-12-07 17:45:08.000000','_000k75I4Y4kVLb9WJdcliUhUr7nJHFtTugR','https://www.iesdouyin.com/share/video/7275135762780163340/?region=CN&mid=7275136002463976253&u_code=250cbek8656c&did=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&with_sec_did=1&titleType=title&share_sign=IBX7hnwkGUNQM6M.3UNKdQNqotqOfWI5mkBrU53b6sY-&share_version=230200&ts=1701942308&from_aid=1128&from_ssr=1',3,0,389,0,0,0,202311164511,'四叶天代理'),(1,'@9VwUxeSUWJ9lMiXzco1kRc7912LsPPyDOpJ3qQOjKFYSZ/X860zdRmYqig357zEBmuWbxgRAEqDQNyasH3DfKw==','四叶天代理IP站点保护用户隐私 #四叶天代理 #ip #地址 #设备 #动态 #定位','视频','2023-09-05 09:03:51.000000','2023-12-07 17:45:08.000000','_000k75I4Y4kVLb9WJdcliUhUr7nJHFtTugR','https://www.iesdouyin.com/share/video/7275141176095771940/?region=CN&mid=7275141316277750565&u_code=250cbek8656c&did=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&with_sec_did=1&titleType=title&share_sign=bA4rCLVBmKeQ8f54SM2hVMGGI7qR..i1JQR_AHSMbyk-&share_version=230200&ts=1701942308&from_aid=1128&from_ssr=1',2,0,343,0,0,0,202311164511,'四叶天代理'),(1,'@9VwUxeSUWJ9lMiXzco1kRc7912LsPPyKOJd4qAukLlcSa/j160zdRmYqig357zEBiprVWQemJU1tVjGhvw5fiQ==','企业网络实现IP地址动态分配提高灵活性与可扩展性 #四叶天代理 #ip #地址 #dhcp #动态分配 #配置','视频','2023-09-05 09:31:37.000000','2023-12-07 17:45:08.000000','_000k75I4Y4kVLb9WJdcliUhUr7nJHFtTugR','https://www.iesdouyin.com/share/video/7275148329112161599/?region=CN&mid=7275148485496769341&u_code=250cbek8656c&did=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&with_sec_did=1&titleType=title&share_sign=VkcpmddwYn8mT641wvAO8fLhUYzqJz.d4hUP9kZaegQ-&share_version=230200&ts=1701942308&from_aid=1128&from_ssr=1',2,0,186,0,0,0,202311164511,'四叶天代理'),(1,'@9VwUxeSUWJ9lMiXzco1kRc7912LtNPiAP5xwrwOlKVcWa/b760zdRmYqig357zEBx4QWJK50tYGxXKJVZ4hv7g==','如何设置动态IP上网？轻松享受灵活便捷的上网体验！ #四叶天代理 #ip #用户 #动态 #设置 #路由器','视频','2023-09-04 17:37:22.000000','2023-12-07 17:45:08.000000','_000k75I4Y4kVLb9WJdcliUhUr7nJHFtTugR','https://www.iesdouyin.com/share/video/7274902491693665577/?region=CN&mid=7274902566654528312&u_code=250cbek8656c&did=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&with_sec_did=1&titleType=title&share_sign=b0MRO0pAxgD70._JLCbn2nY8mLE72Gq4D_T8yPhhdaI-&share_version=230200&ts=1701942308&from_aid=1128&from_ssr=1',1,0,183,0,0,0,202311164511,'四叶天代理'),(1,'@9VwUxeSUWJ9lMiXzco1kRc7912zoNf6DMpFyrwqiKFYVbPL/60zdRmYqig357zEBqN23B3WY4yCRVRGj82rGbA==','动态DNS服务在局域网共享中的作用 #四叶天代理 #ip #局域网 #动态 #共享 #设备','视频','2023-10-20 10:28:48.000000','2023-12-07 17:45:07.000000','_000k75I4Y4kVLb9WJdcliUhUr7nJHFtTugR','https://www.iesdouyin.com/share/video/7291861943604776233/?region=CN&mid=7291862054368414491&u_code=250cbek8656c&did=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&with_sec_did=1&titleType=title&share_sign=sLF9OoEq2rqAxdUDH2wqn6dhXpQdCp7M3WEX3rxYsuo-&share_version=230200&ts=1701942307&from_aid=1128&from_ssr=1',3,0,341,0,0,0,202311164511,'四叶天代理'),(1,'@9VwUxeSUWJ9lMiXzco1kRc7912zoNP2KPpV3qwyuLVUabff/60zdRmYqig357zEBKjalT2RhiIOqk5k6EYZj9w==','动态IP设置路由器配置的重要环节 #四叶天代理 #ip #地址 #网络 #设置 #动态','视频','2023-10-20 16:43:38.000000','2023-12-07 17:45:07.000000','_000k75I4Y4kVLb9WJdcliUhUr7nJHFtTugR','https://www.iesdouyin.com/share/video/7291958506268249363/?region=CN&mid=7291958632453770034&u_code=250cbek8656c&did=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&with_sec_did=1&titleType=title&share_sign=I3.ZqW379IQK75NWveFHNVY9HYYYWntrmQ7GKWKGEFM-&share_version=230200&ts=1701942307&from_aid=1128&from_ssr=1',1,0,323,0,0,0,202311164511,'四叶天代理'),(1,'@9VwUxeSUWJ9lMiXzco1kRc7912zoNP6HOJBxrQqhKVQXaPf760zdRmYqig357zEBJMo5GnV5qjQq8qjLA8VOQw==','路由器设置动态IP的作用 #四叶天代理 #ip #地址 #网络 #设置 #动态','视频','2023-10-20 17:10:07.000000','2023-12-07 17:45:07.000000','_000k75I4Y4kVLb9WJdcliUhUr7nJHFtTugR','https://www.iesdouyin.com/share/video/7291965350407654667/?region=CN&mid=7291965457678633765&u_code=250cbek8656c&did=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&with_sec_did=1&titleType=title&share_sign=h4IKwhvzyvOUqkPtc_j3fRPnK3whh7nwZcQ0lITzoBI-&share_version=230200&ts=1701942307&from_aid=1128&from_ssr=1',2,0,328,0,0,0,202311164511,'四叶天代理'),(1,'@9VwUxeSUWJ9lMiXzco1kRc7912zoO/iEPZJ5qAygJ1gaZ/n860zdRmYqig357zEBrF7U+wmB9b9ezCa4Wku+tw==','动态IP与静态IP的区别是什么？ #四叶天代理 #ip #地址 #动态 #网络 #用户','视频','2023-10-19 17:58:04.000000','2023-12-07 17:45:07.000000','_000k75I4Y4kVLb9WJdcliUhUr7nJHFtTugR','https://www.iesdouyin.com/share/video/7291606678166899980/?region=CN&mid=7291606732160207667&u_code=250cbek8656c&did=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&with_sec_did=1&titleType=title&share_sign=uCivCs.6BVzdlyf9uKA4NFjcxltCTJf7SsvbO7Ef3dE-&share_version=230200&ts=1701942307&from_aid=1128&from_ssr=1',0,0,258,0,0,0,202311164511,'四叶天代理'),(1,'@9VwUxeSUWJ9lMiXzco1kRc7912zoOP+AO51xoQquKFEaavD560zdRmYqig357zEBL3fC5XQSa00atIakA2/rNQ==','解开束缚, 追求梦想 梦梦的冒险之旅 #四叶天代理 #梦梦 #海海 #翅膀 #蔚蓝 #飞翔','视频','2023-10-19 15:43:51.000000','2023-12-07 17:45:07.000000','_000k75I4Y4kVLb9WJdcliUhUr7nJHFtTugR','https://www.iesdouyin.com/share/video/7291572080808709415/?region=CN&mid=7291572132104899386&u_code=250cbek8656c&did=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&with_sec_did=1&titleType=title&share_sign=yt34q3_AhFZWDHxeuYYSZlJ2P6GHhPcpDKrmNM9TgE4-&share_version=230200&ts=1701942307&from_aid=1128&from_ssr=1',0,0,14,0,0,0,202311164511,'四叶天代理'),(1,'@9VwUxeSUWJ9lMiXzco1kRc7912zoOP+LPZZ2rQmiKlIWb/n760zdRmYqig357zEB/nR1rNbN8WUF9YHYoE2OQQ==','网络加速利器:动态IP全国跳 #四叶天代理 #ip #动态 #网络 #全国 #用户','视频','2023-10-19 16:13:11.000000','2023-12-07 17:45:07.000000','_000k75I4Y4kVLb9WJdcliUhUr7nJHFtTugR','https://www.iesdouyin.com/share/video/7291579637434535187/?region=CN&mid=7291579699864177467&u_code=250cbek8656c&did=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&with_sec_did=1&titleType=title&share_sign=utIdyuvzW047eq_9oCLX2d6OhUQYBGqKZLEjJ.nbuGE-&share_version=230200&ts=1701942307&from_aid=1128&from_ssr=1',2,1,653,1,2,0,202311164511,'四叶天代理'),(1,'@9VwUxeSUWJ9lMiXzco1kRc7912zoOP6FOJB1oAumLlAUb/f960zdRmYqig357zEBQn5zEikol513Vy68xrewTg==','#四叶天代理 #ip #动态 #网络 #全国 #跳转','视频','2023-10-19 15:25:32.000000','2023-12-07 17:45:07.000000','_000k75I4Y4kVLb9WJdcliUhUr7nJHFtTugR','https://www.iesdouyin.com/share/video/7291567354910117161/?region=CN&mid=7291567411118197565&u_code=250cbek8656c&did=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&with_sec_did=1&titleType=title&share_sign=NeuKGa_uRu17ZELHdwwVjOTMiK2_tfZHtHGT6ayZnL4-&share_version=230200&ts=1701942307&from_aid=1128&from_ssr=1',0,0,60,0,0,0,202311164511,'四叶天代理'),(1,'@9VwUxeSUWJ9lMiXzco1kRc7912zoOPGDM5Bwrw+mK1MTbvH160zdRmYqig357zEBtbKjFKfbSLHvq5BmR3OyYQ==','#四叶天代理','视频','2023-10-19 17:00:31.000000','2023-12-07 17:45:07.000000','_000k75I4Y4kVLb9WJdcliUhUr7nJHFtTugR','https://www.iesdouyin.com/share/video/7291591851650420009/?region=CN&mid=7291591908613196605&u_code=250cbek8656c&did=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&with_sec_did=1&titleType=title&share_sign=NbN63lUuxCfCgKwX3ONSn5rIphhaiuUTp0Xof9fcTiI-&share_version=230200&ts=1701942307&from_aid=1128&from_ssr=1',2,0,350,0,0,0,202311164511,'四叶天代理'),(1,'@9VwUxeSUWJ9lMiXzco1kRc7912zpOv6GPZJzrQ6iLlUTZvD160zdRmYqig357zEBW18UstFFVN1HV7/jdYNz3Q==','#四叶天代理','视频','2023-10-17 11:30:42.000000','2023-12-07 17:45:07.000000','_000k75I4Y4kVLb9WJdcliUhUr7nJHFtTugR','https://www.iesdouyin.com/share/video/7290764672444140819/?region=CN&mid=7290764741956373305&u_code=250cbek8656c&did=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&with_sec_did=1&titleType=title&share_sign=2DG7VdAT1L_syFy4Rs_AC9zOlPFHQpEbC4h_MoYIOIw-&share_version=230200&ts=1701942307&from_aid=1128&from_ssr=1',0,0,122,0,0,0,202311164511,'四叶天代理'),(2,'1680988722135588864','WIN系统教程如何将静态IP改为动态IP','视频','2023-09-01 17:02:29.000000','2023-12-07 17:45:13.000000','1fdef83551b8a7f4190a7fc9c5f9aa6e','https://zhuanlan.zhihu.com/p/1680988722135588864',0,0,25,0,0,0,202311164511,'四叶天'),(2,'1681246894301478912','静态IP和动态IP互联网中的两种IP地址类型','视频','2023-09-02 10:08:22.000000','2023-12-07 17:45:13.000000','1fdef83551b8a7f4190a7fc9c5f9aa6e','https://zhuanlan.zhihu.com/p/1681246894301478912',0,0,127,0,0,0,202311164511,'四叶天'),(2,'1682084775182196737','如何设置动态IP上网？轻松享受灵活便捷的上网体验！','视频','2023-09-04 17:37:51.000000','2023-12-07 17:45:13.000000','1fdef83551b8a7f4190a7fc9c5f9aa6e','https://zhuanlan.zhihu.com/p/1682084775182196737',0,0,120,0,0,0,202311164511,'四叶天'),(2,'1682086420389359616','网络安全需求高路由器动态IP设置教程','视频','2023-09-04 17:44:22.000000','2023-12-07 17:45:13.000000','1fdef83551b8a7f4190a7fc9c5f9aa6e','https://zhuanlan.zhihu.com/p/1682086420389359616',0,0,128,0,0,0,202311164511,'四叶天'),(2,'1682312867410518016','动态IP与拨号你需要了解的网络连接方式','视频','2023-09-05 08:44:10.000000','2023-12-07 17:45:13.000000','1fdef83551b8a7f4190a7fc9c5f9aa6e','https://zhuanlan.zhihu.com/p/1682312867410518016',0,0,128,0,0,0,202311164511,'四叶天'),(2,'1682317962705661952','四叶天代理IP站点保护用户隐私','视频','2023-09-05 09:04:26.000000','2023-12-07 17:45:13.000000','1fdef83551b8a7f4190a7fc9c5f9aa6e','https://zhuanlan.zhihu.com/p/1682317962705661952',0,0,53,0,0,0,202311164511,'四叶天'),(2,'1682325021425590272','企业网络实现IP地址动态分配提高灵活性与可扩展性','视频','2023-09-05 09:32:22.000000','2023-12-07 17:45:13.000000','1fdef83551b8a7f4190a7fc9c5f9aa6e','https://zhuanlan.zhihu.com/p/1682325021425590272',0,0,75,0,0,0,202311164511,'四叶天'),(2,'1683078701942734848','教你设置静态IP，网络畅通无阻','视频','2023-09-07 11:27:19.000000','2023-12-07 17:45:13.000000','1fdef83551b8a7f4190a7fc9c5f9aa6e','https://zhuanlan.zhihu.com/p/1683078701942734848',0,0,199,0,0,0,202311164511,'四叶天'),(2,'1683081449224417280','WI-FI静态IP与动态IP哪种更安全？','视频','2023-09-07 11:38:14.000000','2023-12-07 17:45:13.000000','1fdef83551b8a7f4190a7fc9c5f9aa6e','https://zhuanlan.zhihu.com/p/1683081449224417280',0,0,111,0,0,0,202311164511,'四叶天'),(2,'1683092312505307137','网络大变革！动态分配IP地址成主流','视频','2023-09-07 12:21:24.000000','2023-12-07 17:45:13.000000','1fdef83551b8a7f4190a7fc9c5f9aa6e','https://zhuanlan.zhihu.com/p/1683092312505307137',0,0,152,0,0,3,202311164511,'四叶天'),(2,'1683118276073381888','动态IP保障上网安全','视频','2023-09-07 14:04:38.000000','2023-12-07 17:45:13.000000','1fdef83551b8a7f4190a7fc9c5f9aa6e','https://zhuanlan.zhihu.com/p/1683118276073381888',0,0,16,0,0,0,202311164511,'四叶天'),(2,'1683120844967112704','动态IP地址的优缺点你了解吗？','视频','2023-09-07 14:14:50.000000','2023-12-07 17:45:13.000000','1fdef83551b8a7f4190a7fc9c5f9aa6e','https://zhuanlan.zhihu.com/p/1683120844967112704',0,0,98,0,0,1,202311164511,'四叶天'),(2,'1683136502740180992','轻松设置动态IP畅享上网乐趣！','视频','2023-09-07 15:17:02.000000','2023-12-07 17:45:13.000000','1fdef83551b8a7f4190a7fc9c5f9aa6e','https://zhuanlan.zhihu.com/p/1683136502740180992',0,0,6,0,0,0,202311164511,'四叶天'),(2,'1683433232257998849','互联网时代动态IP地址正式解密！','视频','2023-09-08 10:56:09.000000','2023-12-07 17:45:13.000000','1fdef83551b8a7f4190a7fc9c5f9aa6e','https://zhuanlan.zhihu.com/p/1683433232257998849',0,0,32,0,0,0,202311164511,'四叶天'),(2,'1684487226636029952','路由器动态IP获取问题解决方法','视频','2023-09-11 08:44:20.000000','2023-12-07 17:45:13.000000','1fdef83551b8a7f4190a7fc9c5f9aa6e','https://zhuanlan.zhihu.com/p/1684487226636029952',0,0,202,0,0,0,202311164511,'四叶天'),(2,'1684603253965451264','动态和静态IP地址的区别','视频','2023-09-11 16:25:24.000000','2023-12-07 17:45:13.000000','1fdef83551b8a7f4190a7fc9c5f9aa6e','https://zhuanlan.zhihu.com/p/1684603253965451264',0,0,77,0,0,0,202311164511,'四叶天'),(2,'1684856491952254976','路由器启用DHCP功能电脑IP地址变动态','视频','2023-09-12 09:11:36.000000','2023-12-07 17:45:13.000000','1fdef83551b8a7f4190a7fc9c5f9aa6e','https://zhuanlan.zhihu.com/p/1684856491952254976',0,0,140,0,0,0,202311164511,'四叶天'),(2,'1684858759749521409','路由器静态IP与动态IP的区别你了解吗？','视频','2023-09-12 09:20:40.000000','2023-12-07 17:45:13.000000','1fdef83551b8a7f4190a7fc9c5f9aa6e','https://zhuanlan.zhihu.com/p/1684858759749521409',0,0,126,0,0,1,202311164511,'四叶天'),(2,'1695071629179281408','#四叶天代理','视频','2023-10-10 13:42:51.000000','2023-12-07 17:45:13.000000','1fdef83551b8a7f4190a7fc9c5f9aa6e','https://zhuanlan.zhihu.com/p/1695071629179281408',0,0,2,0,0,0,202311164511,'四叶天'),(2,'1695073124905893888','#四叶天代理','视频','2023-10-10 13:48:52.000000','2023-12-07 17:45:13.000000','1fdef83551b8a7f4190a7fc9c5f9aa6e','https://zhuanlan.zhihu.com/p/1695073124905893888',0,0,86,0,0,0,202311164511,'四叶天'),(2,'1695086277605646336','#四叶天代理','视频','2023-10-10 14:41:04.000000','2023-12-07 17:45:13.000000','1fdef83551b8a7f4190a7fc9c5f9aa6e','https://zhuanlan.zhihu.com/p/1695086277605646336',0,0,85,0,0,0,202311164511,'四叶天'),(2,'1695088110503833600','网络管理员可调整动态IP刷新频率 #四叶天代理','视频','2023-10-10 14:48:26.000000','2023-12-07 17:45:13.000000','1fdef83551b8a7f4190a7fc9c5f9aa6e','https://zhuanlan.zhihu.com/p/1695088110503833600',0,0,14,0,0,0,202311164511,'四叶天'),(2,'1698363918869827585','解开束缚, 追求梦想 梦梦的冒险之旅','视频','2023-10-19 15:45:18.000000','2023-12-07 17:45:13.000000','1fdef83551b8a7f4190a7fc9c5f9aa6e','https://zhuanlan.zhihu.com/p/1698363918869827585',0,0,35,0,0,0,202311164511,'四叶天'),(2,'1698371185895694336','网络加速利器:动态IP全国跳','视频','2023-10-19 16:14:09.000000','2023-12-07 17:45:13.000000','1fdef83551b8a7f4190a7fc9c5f9aa6e','https://zhuanlan.zhihu.com/p/1698371185895694336',0,0,98,0,0,0,202311164511,'四叶天'),(2,'1698388740572155904','动态IP和静态IP的区别四叶天代理IP站点优势解析','视频','2023-10-19 17:23:53.000000','2023-12-07 17:45:13.000000','1fdef83551b8a7f4190a7fc9c5f9aa6e','https://zhuanlan.zhihu.com/p/1698388740572155904',0,0,75,0,0,0,202311164511,'四叶天'),(2,'1698397881420169217','动态IP与静态IP的区别是什么？','视频','2023-10-19 18:00:30.000000','2023-12-07 17:45:13.000000','1fdef83551b8a7f4190a7fc9c5f9aa6e','https://zhuanlan.zhihu.com/p/1698397881420169217',0,0,99,0,0,0,202311164511,'四叶天'),(2,'1698646910481764352','动态DNS服务在局域网共享中的作用','视频','2023-10-20 10:29:59.000000','2023-12-07 17:45:13.000000','1fdef83551b8a7f4190a7fc9c5f9aa6e','https://zhuanlan.zhihu.com/p/1698646910481764352',0,0,95,0,0,0,202311164511,'四叶天'),(3,'1775714513650036643','教你设置手机代理ip，轻松实现特定网络访问目的','video','2023-08-31 11:45:16.000000','2023-12-07 17:45:15.000000','1699159270507497','http://baijiahao.baidu.com/builder/preview/s?id=1775714513650036643',2,3,1895,742,0,2,202311164511,'四叶天代理'),(3,'1783403692966888789','青岛今天下雪了啦','news','2023-11-24 08:38:35.000000','2023-12-07 17:45:15.000000','1699159270507497','http://baijiahao.baidu.com/builder/preview/s?id=1783403692966888789',0,0,91,3358,0,0,202311164511,'四叶天代理'),(2,'668546183','青岛今天下雪了啦','文章','2023-11-24 11:01:28.000000','2023-12-07 17:45:13.000000','1fdef83551b8a7f4190a7fc9c5f9aa6e','https://zhuanlan.zhihu.com/p/668546183',1,0,49,0,0,0,202311164511,'四叶天'),(4,'BV14h4y1m7oS','四叶天代理IP站点','视频','2023-09-04 07:26:45.000000','2023-12-07 17:45:10.000000','ebdf5476069f420daafb77d7ffdbc62d','https://www.bilibili.com/video/BV14h4y1m7oS?share_source=open_plat',0,0,279,0,0,1,202311164511,'四叶天代理'),(4,'BV18m4y1T73N','手机代理ip怎么设置','视频','2023-08-31 00:21:17.000000','2023-12-07 17:45:12.000000','ebdf5476069f420daafb77d7ffdbc62d','https://www.bilibili.com/video/BV18m4y1T73N?share_source=open_plat',3,0,714,0,0,2,202311164511,'四叶天代理'),(4,'BV19G41197Ek','网络连接故障？动态IP获取不到IP地址？重启设备解决问题！','视频','2023-09-05 03:11:33.000000','2023-12-07 17:45:09.000000','ebdf5476069f420daafb77d7ffdbc62d','https://www.bilibili.com/video/BV19G41197Ek?share_source=open_plat',2,0,132,0,0,0,202311164511,'四叶天代理'),(4,'BV1aG411R7eL','动态IP与静态IP：区别与联系','视频','2023-09-07 07:25:58.000000','2023-12-07 17:45:09.000000','ebdf5476069f420daafb77d7ffdbc62d','https://www.bilibili.com/video/BV1aG411R7eL?share_source=open_plat',0,0,23,0,0,0,202311164511,'四叶天代理'),(4,'BV1c94y1t7zc','路由器动态IP地址的灵活性','视频','2023-09-05 02:37:08.000000','2023-12-07 17:45:09.000000','ebdf5476069f420daafb77d7ffdbc62d','https://www.bilibili.com/video/BV1c94y1t7zc?share_source=open_plat',0,0,4,0,0,0,202311164511,'四叶天代理'),(4,'BV1du4y1D7of','家庭ip不适合作代理ip','视频','2023-09-01 03:46:08.000000','2023-12-07 17:45:11.000000','ebdf5476069f420daafb77d7ffdbc62d','https://www.bilibili.com/video/BV1du4y1D7of?share_source=open_plat',0,0,17,0,0,0,202311164511,'四叶天代理'),(4,'BV1FH4y1X7v7','动态IP的定义、特点、应用','视频','2023-09-05 01:50:17.000000','2023-12-07 17:45:09.000000','ebdf5476069f420daafb77d7ffdbc62d','https://www.bilibili.com/video/BV1FH4y1X7v7?share_source=open_plat',0,0,1,0,0,0,202311164511,'四叶天代理'),(4,'BV1iP41187y7','动态IP地址提高网络安全','视频','2023-09-11 01:07:04.000000','2023-12-07 17:45:08.000000','ebdf5476069f420daafb77d7ffdbc62d','https://www.bilibili.com/video/BV1iP41187y7?share_source=open_plat',0,0,79,0,0,0,202311164511,'四叶天代理'),(4,'BV1JH4y1D7D4','轻松实现静态IP切换动态IP','视频','2023-09-11 00:58:51.000000','2023-12-07 17:45:08.000000','ebdf5476069f420daafb77d7ffdbc62d','https://www.bilibili.com/video/BV1JH4y1D7D4?share_source=open_plat',1,0,140,0,0,0,202311164511,'四叶天代理'),(4,'BV1ju411K7RX','静态IP VS 动态IP哪个更适合你？','视频','2023-09-01 07:03:19.000000','2023-12-07 17:45:11.000000','ebdf5476069f420daafb77d7ffdbc62d','https://www.bilibili.com/video/BV1ju411K7RX?share_source=open_plat',0,0,34,0,0,0,202311164511,'四叶天代理'),(4,'BV1K841167Kg','如何查看自己的IP是否为动态IP','视频','2023-09-04 07:23:21.000000','2023-12-07 17:45:10.000000','ebdf5476069f420daafb77d7ffdbc62d','https://www.bilibili.com/video/BV1K841167Kg?share_source=open_plat',0,0,9,0,0,0,202311164511,'四叶天代理'),(4,'BV1K94y1t7S3','轻松设置动态IP保障网络稳定安全','视频','2023-09-02 02:50:33.000000','2023-12-07 17:45:10.000000','ebdf5476069f420daafb77d7ffdbc62d','https://www.bilibili.com/video/BV1K94y1t7S3?share_source=open_plat',0,0,33,0,0,0,202311164511,'四叶天代理'),(4,'BV1ku411P7rd','动态IP：保障隐私提升网络安全','视频','2023-09-07 04:29:11.000000','2023-12-07 17:45:09.000000','ebdf5476069f420daafb77d7ffdbc62d','https://www.bilibili.com/video/BV1ku411P7rd?share_source=open_plat',0,0,11,0,0,0,202311164511,'四叶天代理'),(4,'BV1P34y1T7KM','四叶天代理ip站点免费提供服务','视频','2023-08-31 07:49:16.000000','2023-12-07 17:45:12.000000','ebdf5476069f420daafb77d7ffdbc62d','https://www.bilibili.com/video/BV1P34y1T7KM?share_source=open_plat',0,0,57,0,0,0,202311164511,'四叶天代理'),(4,'BV1Pm4y1K7j9','动态IP服务器随时切换IP地址保护个人隐私','视频','2023-09-08 03:11:10.000000','2023-12-07 17:45:09.000000','ebdf5476069f420daafb77d7ffdbc62d','https://www.bilibili.com/video/BV1Pm4y1K7j9?share_source=open_plat',0,0,43,0,0,0,202311164511,'四叶天代理'),(4,'BV1pp4y1N7HK','教你苹果设备设置代理ip','视频','2023-08-30 07:32:12.000000','2023-12-07 17:45:12.000000','ebdf5476069f420daafb77d7ffdbc62d','https://www.bilibili.com/video/BV1pp4y1N7HK?share_source=open_plat',0,0,112,0,0,0,202311164511,'四叶天代理'),(4,'BV1qh4y1m7kg','教你轻松实现动态IP到静态IP转换','视频','2023-09-02 03:22:18.000000','2023-12-07 17:45:10.000000','ebdf5476069f420daafb77d7ffdbc62d','https://www.bilibili.com/video/BV1qh4y1m7kg?share_source=open_plat',7,0,779,0,0,1,202311164511,'四叶天代理'),(4,'BV1qh4y1w7zZ','四叶天代理IP站点','视频','2023-09-12 01:46:56.000000','2023-12-07 17:45:08.000000','ebdf5476069f420daafb77d7ffdbc62d','https://www.bilibili.com/video/BV1qh4y1w7zZ?share_source=open_plat',1,0,101,0,0,0,202311164511,'四叶天代理'),(4,'BV1Tj411m7kM','教你设置无线路由器代理ip','视频','2023-09-01 03:41:44.000000','2023-12-07 17:45:11.000000','ebdf5476069f420daafb77d7ffdbc62d','https://www.bilibili.com/video/BV1Tj411m7kM?share_source=open_plat',2,0,516,0,0,1,202311164511,'四叶天代理'),(4,'BV1TP411a71N','如何轻松改变电脑IP地址重点介绍动态IP地址','视频','2023-09-04 00:25:26.000000','2023-12-07 17:45:10.000000','ebdf5476069f420daafb77d7ffdbc62d','https://www.bilibili.com/video/BV1TP411a71N?share_source=open_plat',0,0,127,0,0,0,202311164511,'四叶天代理'),(4,'BV1TP411a7zH','轻松查看自己的IP是否为动态IP，了解保护隐私的实用方法！','视频','2023-09-04 00:36:26.000000','2023-12-07 17:45:10.000000','ebdf5476069f420daafb77d7ffdbc62d','https://www.bilibili.com/video/BV1TP411a7zH?share_source=open_plat',1,0,21,0,0,0,202311164511,'四叶天代理'),(4,'BV1uF411k7MN','如何设置网吧代理ip让你的网络畅通无阻','视频','2023-08-30 09:42:06.000000','2023-12-07 17:45:12.000000','ebdf5476069f420daafb77d7ffdbc62d','https://www.bilibili.com/video/BV1uF411k7MN?share_source=open_plat',2,1,550,0,0,1,202311164511,'四叶天代理'),(4,'BV1V14y1y7W9','教你如何设置路由器的动态IP','视频','2023-09-01 06:54:42.000000','2023-12-07 17:45:11.000000','ebdf5476069f420daafb77d7ffdbc62d','https://www.bilibili.com/video/BV1V14y1y7W9?share_source=open_plat',0,0,115,0,0,1,202311164511,'四叶天代理'),(4,'BV1vH4y1X7fb','路由器动态IP提高网络安全','视频','2023-09-11 08:34:08.000000','2023-12-07 17:45:08.000000','ebdf5476069f420daafb77d7ffdbc62d','https://www.bilibili.com/video/BV1vH4y1X7fb?share_source=open_plat',0,0,94,0,0,0,202311164511,'四叶天代理'),(4,'BV1W14y1y7UB','路由器代理ip功能保障你的网络隐私安全！','视频','2023-08-31 08:49:09.000000','2023-12-07 17:45:12.000000','ebdf5476069f420daafb77d7ffdbc62d','https://www.bilibili.com/video/BV1W14y1y7UB?share_source=open_plat',0,0,59,0,0,0,202311164511,'四叶天代理'),(4,'BV1WH4y1Q7y1','轻松改变电脑IP地址让你畅游互联网！','视频','2023-09-02 03:57:49.000000','2023-12-07 17:45:10.000000','ebdf5476069f420daafb77d7ffdbc62d','https://www.bilibili.com/video/BV1WH4y1Q7y1?share_source=open_plat',3,0,397,0,0,2,202311164511,'四叶天代理'),(4,'BV1Wk4y1w7hq','如何判断电脑是动态IP','视频','2023-09-12 01:38:29.000000','2023-12-07 17:45:08.000000','ebdf5476069f420daafb77d7ffdbc62d','https://www.bilibili.com/video/BV1Wk4y1w7hq?share_source=open_plat',2,0,46,0,0,0,202311164511,'四叶天代理'),(4,'BV1Ww411S7BP','网络安全新手必备如何设置代理ip服务器','视频','2023-08-31 07:56:06.000000','2023-12-07 17:45:12.000000','ebdf5476069f420daafb77d7ffdbc62d','https://www.bilibili.com/video/BV1Ww411S7BP?share_source=open_plat',1,0,260,0,0,2,202311164511,'四叶天代理'),(4,'BV1Y14y1k7hv','动态IP保护隐私S10提供额外安全屏障','视频','2023-09-02 02:03:23.000000','2023-12-07 17:45:11.000000','ebdf5476069f420daafb77d7ffdbc62d','https://www.bilibili.com/video/BV1Y14y1k7hv?share_source=open_plat',0,0,4,0,0,0,202311164511,'四叶天代理'),(4,'BV1yk4y1A7fU','动态IP地址轻松修改3种方法告诉你','视频','2023-09-08 03:04:56.000000','2023-12-07 17:45:09.000000','ebdf5476069f420daafb77d7ffdbc62d','https://www.bilibili.com/video/BV1yk4y1A7fU?share_source=open_plat',1,1,231,0,0,1,202311164511,'四叶天代理'),(4,'BV1Zw411S7GX','动态IP和静态IP的优劣势比较，了解一下？','视频','2023-09-04 09:52:29.000000','2023-12-07 17:45:10.000000','ebdf5476069f420daafb77d7ffdbc62d','https://www.bilibili.com/video/BV1Zw411S7GX?share_source=open_plat',1,0,22,0,0,0,202311164511,'四叶天代理');
/*!40000 ALTER TABLE `mainsite_platformdata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mainsite_platformdouyin`
--

DROP TABLE IF EXISTS `mainsite_platformdouyin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mainsite_platformdouyin` (
  `access_token` varchar(255) NOT NULL,
  `refresh_token` varchar(64) NOT NULL,
  `open_id` varchar(255) NOT NULL,
  `expires_in` datetime(6) NOT NULL,
  `e_account_role` varchar(255) DEFAULT NULL,
  `nickname` varchar(64) NOT NULL,
  `avatar` varchar(255) NOT NULL,
  `uid_id` bigint NOT NULL,
  `auth_time` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`open_id`),
  KEY `mainsite_platformdouyin_uid_id_694d41ee_fk_mainsite_user_uid` (`uid_id`),
  CONSTRAINT `mainsite_platformdouyin_uid_id_694d41ee_fk_mainsite_user_uid` FOREIGN KEY (`uid_id`) REFERENCES `mainsite_user` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mainsite_platformdouyin`
--

LOCK TABLES `mainsite_platformdouyin` WRITE;
/*!40000 ALTER TABLE `mainsite_platformdouyin` DISABLE KEYS */;
INSERT INTO `mainsite_platformdouyin` VALUES ('act.3.wZrTjU4yaBkU4yX9upWnOV_UfDaiSXBvs0BlGnJ4ieCTnh4Gz_yuQM1P9RrbkVzgJLqSN176jz_XgQ7lNRtR5T8WgVB4rOm4cx1bm57Zvw0fNUI0Am1dhJD7oN29sDjHoZ6S9RmOa3s71efpq4VDUxoIHhu07ljclh0DR2fWjx7odSh-X-d_VeZNHhc=','rft.31fa8d905333cfc58e39552e2e602c4b89sidqKJL5Gl4yv1HbHnPlUtMl8x','_000k75I4Y4kVLb9WJdcliUhUr7nJHFtTugR','2023-12-22 16:41:06.000000','None','四叶天代理','https://p6.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-i-0813c001_o0Ex9MJUkENAAAAKhCefBDIhIXzARYAE7gNqH3.jpeg?from=4010531038',202311164511,'2023-12-07 15:36:06.000000');
/*!40000 ALTER TABLE `mainsite_platformdouyin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mainsite_platformzhihu`
--

DROP TABLE IF EXISTS `mainsite_platformzhihu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mainsite_platformzhihu` (
  `nickname` varchar(26) NOT NULL,
  `avatar` varchar(255) NOT NULL,
  `expires_time` datetime(6) NOT NULL,
  `auth_time` datetime(6) DEFAULT NULL,
  `zh_uid` varchar(255) NOT NULL,
  `z_c0` varchar(500) NOT NULL,
  `uid_id` bigint NOT NULL,
  PRIMARY KEY (`zh_uid`),
  KEY `mainsite_platformzhihu_uid_id_4b569f38_fk_mainsite_user_uid` (`uid_id`),
  CONSTRAINT `mainsite_platformzhihu_uid_id_4b569f38_fk_mainsite_user_uid` FOREIGN KEY (`uid_id`) REFERENCES `mainsite_user` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mainsite_platformzhihu`
--

LOCK TABLES `mainsite_platformzhihu` WRITE;
/*!40000 ALTER TABLE `mainsite_platformzhihu` DISABLE KEYS */;
INSERT INTO `mainsite_platformzhihu` VALUES ('四叶天','https://pic1.zhimg.com/v2-49ba7f8fbbfeed644835ccdcaacee01d_l.jpg?source=32738c0c','2024-06-04 15:47:14.000000','2023-12-07 15:47:14.000000','1fdef83551b8a7f4190a7fc9c5f9aa6e','2|1:0|10:1701934997|4:z_c0|92:Mi4xZV9oV1NnQUFBQUFBd05WQVgtTFFGeVlBQUFCZ0FsVk5rOFZlWmdEWGNPTHplSzVBYnBDYU8wX3dxcUxYbEdQcHF3|4c3de0d572a1a67c718c1120fc605eb21bdec689596d5d064ef1571799baea0b',202311164511);
/*!40000 ALTER TABLE `mainsite_platformzhihu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mainsite_user`
--

DROP TABLE IF EXISTS `mainsite_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mainsite_user` (
  `uid` bigint NOT NULL,
  `username` varchar(32) NOT NULL,
  `password` varchar(64) NOT NULL,
  `status` smallint NOT NULL,
  `register_time` datetime(6) NOT NULL,
  `last_login_time` datetime(6) NOT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mainsite_user`
--

LOCK TABLES `mainsite_user` WRITE;
/*!40000 ALTER TABLE `mainsite_user` DISABLE KEYS */;
INSERT INTO `mainsite_user` VALUES (202311164511,'admin','ef92bec6a280e67f0c14bbfa19dddb97',1,'2023-11-16 21:13:01.264719','2023-12-08 08:19:18.506836'),(202311172240,'test','2b2f4bfa180dc614be122335bbb295cc',1,'2023-11-17 12:01:21.287305','2023-11-23 13:46:46.907249'),(202311232769,'temp','335b9d6506d151627db42cce8a64d49e',1,'2023-11-23 13:49:17.561786','2023-12-07 11:21:18.713090');
/*!40000 ALTER TABLE `mainsite_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-08  8:31:56
