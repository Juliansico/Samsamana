-- MySQL dump 10.13  Distrib 9.0.1, for Win64 (x86_64)
--
-- Host: localhost    Database: inventario
-- ------------------------------------------------------
-- Server version	9.0.1

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
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add categoria',6,'add_categoria'),(22,'Can change categoria',6,'change_categoria'),(23,'Can delete categoria',6,'delete_categoria'),(24,'Can view categoria',6,'view_categoria'),(25,'Can add compra',7,'add_compra'),(26,'Can change compra',7,'change_compra'),(27,'Can delete compra',7,'delete_compra'),(28,'Can view compra',7,'view_compra'),(29,'Can add compra_has_producto',8,'add_compra_has_producto'),(30,'Can change compra_has_producto',8,'change_compra_has_producto'),(31,'Can delete compra_has_producto',8,'delete_compra_has_producto'),(32,'Can view compra_has_producto',8,'view_compra_has_producto'),(33,'Can add marca',9,'add_marca'),(34,'Can change marca',9,'change_marca'),(35,'Can delete marca',9,'delete_marca'),(36,'Can view marca',9,'view_marca'),(37,'Can add presentacion',10,'add_presentacion'),(38,'Can change presentacion',10,'change_presentacion'),(39,'Can delete presentacion',10,'delete_presentacion'),(40,'Can view presentacion',10,'view_presentacion'),(41,'Can add producto',11,'add_producto'),(42,'Can change producto',11,'change_producto'),(43,'Can delete producto',11,'delete_producto'),(44,'Can view producto',11,'view_producto'),(45,'Can add venta',12,'add_venta'),(46,'Can change venta',12,'change_venta'),(47,'Can delete venta',12,'delete_venta'),(48,'Can view venta',12,'view_venta'),(49,'Can add ventas_has_producto',13,'add_ventas_has_producto'),(50,'Can change ventas_has_producto',13,'change_ventas_has_producto'),(51,'Can delete ventas_has_producto',13,'delete_ventas_has_producto'),(52,'Can view ventas_has_producto',13,'view_ventas_has_producto'),(53,'Can add user',14,'add_usuario'),(54,'Can change user',14,'change_usuario'),(55,'Can delete user',14,'delete_usuario'),(56,'Can view user',14,'view_usuario'),(57,'Can add proveedor',15,'add_proveedor'),(58,'Can change proveedor',15,'change_proveedor'),(59,'Can delete proveedor',15,'delete_proveedor'),(60,'Can view proveedor',15,'view_proveedor'),(61,'Can add respaldo',16,'add_respaldo'),(62,'Can change respaldo',16,'change_respaldo'),(63,'Can delete respaldo',16,'delete_respaldo'),(64,'Can view respaldo',16,'view_respaldo');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_gestionar` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_gestionar` FOREIGN KEY (`user_id`) REFERENCES `gestionar_usuarios_usuario` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
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
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(6,'gestionar_categoria','categoria'),(7,'gestionar_compra','compra'),(8,'gestionar_compra','compra_has_producto'),(9,'gestionar_marca','marca'),(10,'gestionar_presentacion','presentacion'),(11,'gestionar_productos','producto'),(15,'gestionar_proveedor','proveedor'),(16,'gestionar_respaldo','respaldo'),(14,'gestionar_usuarios','usuario'),(12,'gestionar_ventas','venta'),(13,'gestionar_ventas','ventas_has_producto'),(5,'sessions','session');
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
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-08-27 21:51:27.199217'),(2,'contenttypes','0002_remove_content_type_name','2024-08-27 21:51:27.281894'),(3,'auth','0001_initial','2024-08-27 21:51:27.770523'),(4,'auth','0002_alter_permission_name_max_length','2024-08-27 21:51:27.839525'),(5,'auth','0003_alter_user_email_max_length','2024-08-27 21:51:27.850514'),(6,'auth','0004_alter_user_username_opts','2024-08-27 21:51:27.859560'),(7,'auth','0005_alter_user_last_login_null','2024-08-27 21:51:27.868514'),(8,'auth','0006_require_contenttypes_0002','2024-08-27 21:51:27.874572'),(9,'auth','0007_alter_validators_add_error_messages','2024-08-27 21:51:27.885514'),(10,'auth','0008_alter_user_username_max_length','2024-08-27 21:51:27.893513'),(11,'auth','0009_alter_user_last_name_max_length','2024-08-27 21:51:27.903526'),(12,'auth','0010_alter_group_name_max_length','2024-08-27 21:51:27.925523'),(13,'auth','0011_update_proxy_permissions','2024-08-27 21:51:27.935517'),(14,'auth','0012_alter_user_first_name_max_length','2024-08-27 21:51:27.945515'),(15,'gestionar_usuarios','0001_initial','2024-08-27 21:51:28.572664'),(16,'admin','0001_initial','2024-08-27 21:51:28.852194'),(17,'admin','0002_logentry_remove_auto_add','2024-08-27 21:51:28.862204'),(18,'admin','0003_logentry_add_action_flag_choices','2024-08-27 21:51:28.872194'),(19,'gestionar_categoria','0001_initial','2024-08-27 21:51:28.894194'),(20,'gestionar_presentacion','0001_initial','2024-08-27 21:51:28.920237'),(21,'gestionar_marca','0001_initial','2024-08-27 21:51:28.945206'),(22,'gestionar_productos','0001_initial','2024-08-27 21:51:29.246157'),(23,'gestionar_proveedor','0001_initial','2024-08-27 21:51:29.290295'),(24,'gestionar_compra','0001_initial','2024-08-27 21:51:29.749344'),(25,'gestionar_compra','0002_alter_compra_productos','2024-08-27 21:51:29.771345'),(26,'gestionar_respaldo','0001_initial','2024-08-27 21:51:29.816343'),(27,'gestionar_usuarios','0002_alter_usuario_groups_alter_usuario_user_permissions','2024-08-27 21:51:29.857341'),(28,'gestionar_ventas','0001_initial','2024-08-27 21:51:30.147337'),(29,'gestionar_ventas','0002_alter_venta_productos','2024-08-27 21:51:30.161359'),(30,'sessions','0001_initial','2024-08-27 21:51:30.205337');
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
INSERT INTO `django_session` VALUES ('9dy3t3gwcqmsi0itc1lmaiv45ik0uuqw','.eJxVjDsOwjAQRO_iGlnZtYkTSnrOEI3XGxxAjpRPhbg7iZQCutG8N_M2HdYld-usUzckczFkTr9dhDy17CA9UO6jlbEs0xDtrtiDzvY2Jn1dD_fvIGPO25qp0eYMRiWscOJ94BgSmJR6dlv0jqQGUKNqAzmhPvk2iEZHrGo-X-WhODo:1sj476:rKE5joUguLW5fZUPsxLXZbQfVf9q4SsZL__1neFB3EA','2024-09-10 21:52:32.040329'),('rqp2pqdm17bmzg236qxz8po4jussxb8h','.eJxVjEEOwiAQRe_C2hBgaKAu3XsGMjNMpWogKe3KeHdt0oVu_3vvv1TCbS1p67KkOauzsur0uxHyQ-oO8h3rrWludV1m0ruiD9r1tWV5Xg7376BgL9-a42RdzuAjGiCyPkY3MjEAZzACLC54mNgPIQxiENCTtSI-yogWRb0_60c4Sw:1sjAMU:fx1KY2qAQVDr2J87UDPOoCHHrMTw0dmIO9vJ6YWLEi8','2024-09-11 04:32:50.408874');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gestionar_categoria_categoria`
--

DROP TABLE IF EXISTS `gestionar_categoria_categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gestionar_categoria_categoria` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gestionar_categoria_categoria`
--

LOCK TABLES `gestionar_categoria_categoria` WRITE;
/*!40000 ALTER TABLE `gestionar_categoria_categoria` DISABLE KEYS */;
/*!40000 ALTER TABLE `gestionar_categoria_categoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gestionar_compra_compra`
--

DROP TABLE IF EXISTS `gestionar_compra_compra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gestionar_compra_compra` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fecha_Compra` datetime(6) NOT NULL,
  `total_Compra` double NOT NULL,
  `cantidad_Producto` int NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `proveedor_Id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `gestionar_compra_com_proveedor_Id_id_813bb986_fk_gestionar` (`proveedor_Id_id`),
  CONSTRAINT `gestionar_compra_com_proveedor_Id_id_813bb986_fk_gestionar` FOREIGN KEY (`proveedor_Id_id`) REFERENCES `gestionar_proveedor_proveedor` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gestionar_compra_compra`
--

LOCK TABLES `gestionar_compra_compra` WRITE;
/*!40000 ALTER TABLE `gestionar_compra_compra` DISABLE KEYS */;
/*!40000 ALTER TABLE `gestionar_compra_compra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gestionar_compra_compra_has_producto`
--

DROP TABLE IF EXISTS `gestionar_compra_compra_has_producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gestionar_compra_compra_has_producto` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `compra_id` bigint NOT NULL,
  `producto_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `gestionar_compra_com_compra_id_42ee1348_fk_gestionar` (`compra_id`),
  KEY `gestionar_compra_com_producto_id_8cfc0752_fk_gestionar` (`producto_id`),
  CONSTRAINT `gestionar_compra_com_compra_id_42ee1348_fk_gestionar` FOREIGN KEY (`compra_id`) REFERENCES `gestionar_compra_compra` (`id`),
  CONSTRAINT `gestionar_compra_com_producto_id_8cfc0752_fk_gestionar` FOREIGN KEY (`producto_id`) REFERENCES `gestionar_productos_producto` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gestionar_compra_compra_has_producto`
--

LOCK TABLES `gestionar_compra_compra_has_producto` WRITE;
/*!40000 ALTER TABLE `gestionar_compra_compra_has_producto` DISABLE KEYS */;
/*!40000 ALTER TABLE `gestionar_compra_compra_has_producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gestionar_marca_marca`
--

DROP TABLE IF EXISTS `gestionar_marca_marca`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gestionar_marca_marca` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `logoTipo` varchar(100) DEFAULT NULL,
  `estado` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gestionar_marca_marca`
--

LOCK TABLES `gestionar_marca_marca` WRITE;
/*!40000 ALTER TABLE `gestionar_marca_marca` DISABLE KEYS */;
/*!40000 ALTER TABLE `gestionar_marca_marca` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gestionar_presentacion_presentacion`
--

DROP TABLE IF EXISTS `gestionar_presentacion_presentacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gestionar_presentacion_presentacion` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `precio_venta` double NOT NULL,
  `precio_compra` double NOT NULL,
  `cantidad_Stock` int NOT NULL,
  `unidades_Paquete` int NOT NULL,
  `estado` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gestionar_presentacion_presentacion`
--

LOCK TABLES `gestionar_presentacion_presentacion` WRITE;
/*!40000 ALTER TABLE `gestionar_presentacion_presentacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `gestionar_presentacion_presentacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gestionar_productos_producto`
--

DROP TABLE IF EXISTS `gestionar_productos_producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gestionar_productos_producto` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `precio` double NOT NULL,
  `unidad_de_medida` varchar(50) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `categoria_id` bigint NOT NULL,
  `marca_id` bigint NOT NULL,
  `presentacion_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `gestionar_productos__categoria_id_5ef4955d_fk_gestionar` (`categoria_id`),
  KEY `gestionar_productos__marca_id_3d5a9cbd_fk_gestionar` (`marca_id`),
  KEY `gestionar_productos__presentacion_id_2b5ecb2a_fk_gestionar` (`presentacion_id`),
  CONSTRAINT `gestionar_productos__categoria_id_5ef4955d_fk_gestionar` FOREIGN KEY (`categoria_id`) REFERENCES `gestionar_categoria_categoria` (`id`),
  CONSTRAINT `gestionar_productos__marca_id_3d5a9cbd_fk_gestionar` FOREIGN KEY (`marca_id`) REFERENCES `gestionar_marca_marca` (`id`),
  CONSTRAINT `gestionar_productos__presentacion_id_2b5ecb2a_fk_gestionar` FOREIGN KEY (`presentacion_id`) REFERENCES `gestionar_presentacion_presentacion` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gestionar_productos_producto`
--

LOCK TABLES `gestionar_productos_producto` WRITE;
/*!40000 ALTER TABLE `gestionar_productos_producto` DISABLE KEYS */;
/*!40000 ALTER TABLE `gestionar_productos_producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gestionar_proveedor_proveedor`
--

DROP TABLE IF EXISTS `gestionar_proveedor_proveedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gestionar_proveedor_proveedor` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `direccion` varchar(255) NOT NULL,
  `telefono` varchar(20) NOT NULL,
  `email` varchar(254) NOT NULL,
  `producto` varchar(255) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gestionar_proveedor_proveedor`
--

LOCK TABLES `gestionar_proveedor_proveedor` WRITE;
/*!40000 ALTER TABLE `gestionar_proveedor_proveedor` DISABLE KEYS */;
/*!40000 ALTER TABLE `gestionar_proveedor_proveedor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gestionar_respaldo_respaldo`
--

DROP TABLE IF EXISTS `gestionar_respaldo_respaldo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gestionar_respaldo_respaldo` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre_archivo` varchar(255) NOT NULL,
  `fecha_creacion` datetime(6) NOT NULL,
  `tamano` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gestionar_respaldo_respaldo`
--

LOCK TABLES `gestionar_respaldo_respaldo` WRITE;
/*!40000 ALTER TABLE `gestionar_respaldo_respaldo` DISABLE KEYS */;
/*!40000 ALTER TABLE `gestionar_respaldo_respaldo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gestionar_usuarios_usuario`
--

DROP TABLE IF EXISTS `gestionar_usuarios_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gestionar_usuarios_usuario` (
  `id` bigint NOT NULL AUTO_INCREMENT,
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
  `reset_token` varchar(255) DEFAULT NULL,
  `usuario` varchar(150) NOT NULL,
  `apellido` varchar(150) NOT NULL,
  `nombre` varchar(150) NOT NULL,
  `tipo_documento` varchar(2) NOT NULL,
  `documento` varchar(20) NOT NULL,
  `telefono` varchar(20) NOT NULL,
  `rol_de_usuario` varchar(50) NOT NULL,
  `correo` varchar(254) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `correo` (`correo`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gestionar_usuarios_usuario`
--

LOCK TABLES `gestionar_usuarios_usuario` WRITE;
/*!40000 ALTER TABLE `gestionar_usuarios_usuario` DISABLE KEYS */;
INSERT INTO `gestionar_usuarios_usuario` VALUES (1,'pbkdf2_sha256$870000$xETT8mG239u5VoNfik0LwN$onx8Cd3RbbZChYtYQD/YFwKhbNsqkwlSSbgINEDaZyc=','2024-08-28 04:32:50.404091',1,'juli','','','rodriguezdiazjulianfelipe@gmail.com',1,1,'2024-08-27 21:51:55.110196',NULL,'','','','','','','','',1);
/*!40000 ALTER TABLE `gestionar_usuarios_usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gestionar_usuarios_usuario_groups`
--

DROP TABLE IF EXISTS `gestionar_usuarios_usuario_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gestionar_usuarios_usuario_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `usuario_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `gestionar_usuarios_usuar_usuario_id_group_id_a0a3588e_uniq` (`usuario_id`,`group_id`),
  KEY `gestionar_usuarios_u_group_id_b8184d2e_fk_auth_grou` (`group_id`),
  CONSTRAINT `gestionar_usuarios_u_group_id_b8184d2e_fk_auth_grou` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `gestionar_usuarios_u_usuario_id_8cb01a4c_fk_gestionar` FOREIGN KEY (`usuario_id`) REFERENCES `gestionar_usuarios_usuario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gestionar_usuarios_usuario_groups`
--

LOCK TABLES `gestionar_usuarios_usuario_groups` WRITE;
/*!40000 ALTER TABLE `gestionar_usuarios_usuario_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `gestionar_usuarios_usuario_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gestionar_usuarios_usuario_user_permissions`
--

DROP TABLE IF EXISTS `gestionar_usuarios_usuario_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gestionar_usuarios_usuario_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `usuario_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `gestionar_usuarios_usuar_usuario_id_permission_id_0c12431a_uniq` (`usuario_id`,`permission_id`),
  KEY `gestionar_usuarios_u_permission_id_3a5b6fb4_fk_auth_perm` (`permission_id`),
  CONSTRAINT `gestionar_usuarios_u_permission_id_3a5b6fb4_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `gestionar_usuarios_u_usuario_id_0c20325d_fk_gestionar` FOREIGN KEY (`usuario_id`) REFERENCES `gestionar_usuarios_usuario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gestionar_usuarios_usuario_user_permissions`
--

LOCK TABLES `gestionar_usuarios_usuario_user_permissions` WRITE;
/*!40000 ALTER TABLE `gestionar_usuarios_usuario_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `gestionar_usuarios_usuario_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gestionar_ventas_venta`
--

DROP TABLE IF EXISTS `gestionar_ventas_venta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gestionar_ventas_venta` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre_Producto` varchar(255) NOT NULL,
  `precio_Producto` double NOT NULL,
  `cantidad_Venta` double NOT NULL,
  `total_Venta_Realizada` double NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `saldo_Inicial` double DEFAULT NULL,
  `saldo_Actual` double DEFAULT NULL,
  `fecha_Apertura` datetime(6) NOT NULL,
  `fecha_Cierre` datetime(6) DEFAULT NULL,
  `id_Usuario_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `gestionar_ventas_ven_id_Usuario_id_87e3fb76_fk_gestionar` (`id_Usuario_id`),
  CONSTRAINT `gestionar_ventas_ven_id_Usuario_id_87e3fb76_fk_gestionar` FOREIGN KEY (`id_Usuario_id`) REFERENCES `gestionar_usuarios_usuario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gestionar_ventas_venta`
--

LOCK TABLES `gestionar_ventas_venta` WRITE;
/*!40000 ALTER TABLE `gestionar_ventas_venta` DISABLE KEYS */;
/*!40000 ALTER TABLE `gestionar_ventas_venta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gestionar_ventas_ventas_has_producto`
--

DROP TABLE IF EXISTS `gestionar_ventas_ventas_has_producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gestionar_ventas_ventas_has_producto` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `producto_id` bigint NOT NULL,
  `venta_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `gestionar_ventas_ven_producto_id_86df36c1_fk_gestionar` (`producto_id`),
  KEY `gestionar_ventas_ven_venta_id_202cf550_fk_gestionar` (`venta_id`),
  CONSTRAINT `gestionar_ventas_ven_producto_id_86df36c1_fk_gestionar` FOREIGN KEY (`producto_id`) REFERENCES `gestionar_productos_producto` (`id`),
  CONSTRAINT `gestionar_ventas_ven_venta_id_202cf550_fk_gestionar` FOREIGN KEY (`venta_id`) REFERENCES `gestionar_ventas_venta` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gestionar_ventas_ventas_has_producto`
--

LOCK TABLES `gestionar_ventas_ventas_has_producto` WRITE;
/*!40000 ALTER TABLE `gestionar_ventas_ventas_has_producto` DISABLE KEYS */;
/*!40000 ALTER TABLE `gestionar_ventas_ventas_has_producto` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-27 23:32:56
