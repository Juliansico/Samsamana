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
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add categoria',6,'add_categoria'),(22,'Can change categoria',6,'change_categoria'),(23,'Can delete categoria',6,'delete_categoria'),(24,'Can view categoria',6,'view_categoria'),(25,'Can add compra',7,'add_compra'),(26,'Can change compra',7,'change_compra'),(27,'Can delete compra',7,'delete_compra'),(28,'Can view compra',7,'view_compra'),(29,'Can add detalle compra',8,'add_detallecompra'),(30,'Can change detalle compra',8,'change_detallecompra'),(31,'Can delete detalle compra',8,'delete_detallecompra'),(32,'Can view detalle compra',8,'view_detallecompra'),(33,'Can add marca',9,'add_marca'),(34,'Can change marca',9,'change_marca'),(35,'Can delete marca',9,'delete_marca'),(36,'Can view marca',9,'view_marca'),(37,'Can add presentacion',10,'add_presentacion'),(38,'Can change presentacion',10,'change_presentacion'),(39,'Can delete presentacion',10,'delete_presentacion'),(40,'Can view presentacion',10,'view_presentacion'),(41,'Can add producto',11,'add_producto'),(42,'Can change producto',11,'change_producto'),(43,'Can delete producto',11,'delete_producto'),(44,'Can view producto',11,'view_producto'),(45,'Can add venta',12,'add_venta'),(46,'Can change venta',12,'change_venta'),(47,'Can delete venta',12,'delete_venta'),(48,'Can view venta',12,'view_venta'),(49,'Can add detalle venta',13,'add_detalleventa'),(50,'Can change detalle venta',13,'change_detalleventa'),(51,'Can delete detalle venta',13,'delete_detalleventa'),(52,'Can view detalle venta',13,'view_detalleventa'),(53,'Can add user',14,'add_usuario'),(54,'Can change user',14,'change_usuario'),(55,'Can delete user',14,'delete_usuario'),(56,'Can view user',14,'view_usuario'),(57,'Can add proveedor',15,'add_proveedor'),(58,'Can change proveedor',15,'change_proveedor'),(59,'Can delete proveedor',15,'delete_proveedor'),(60,'Can view proveedor',15,'view_proveedor'),(61,'Can add respaldo',16,'add_respaldo'),(62,'Can change respaldo',16,'change_respaldo'),(63,'Can delete respaldo',16,'delete_respaldo'),(64,'Can view respaldo',16,'view_respaldo');
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
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(6,'gestionar_categoria','categoria'),(7,'gestionar_compra','compra'),(8,'gestionar_compra','detallecompra'),(9,'gestionar_marca','marca'),(10,'gestionar_presentacion','presentacion'),(11,'gestionar_productos','producto'),(15,'gestionar_proveedor','proveedor'),(16,'gestionar_respaldo','respaldo'),(14,'gestionar_usuarios','usuario'),(13,'gestionar_ventas','detalleventa'),(12,'gestionar_ventas','venta'),(5,'sessions','session');
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
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-10-10 14:26:05.476576'),(2,'contenttypes','0002_remove_content_type_name','2024-10-10 14:26:05.579058'),(3,'auth','0001_initial','2024-10-10 14:26:05.919679'),(4,'auth','0002_alter_permission_name_max_length','2024-10-10 14:26:06.051605'),(5,'auth','0003_alter_user_email_max_length','2024-10-10 14:26:06.061876'),(6,'auth','0004_alter_user_username_opts','2024-10-10 14:26:06.074824'),(7,'auth','0005_alter_user_last_login_null','2024-10-10 14:26:06.089860'),(8,'auth','0006_require_contenttypes_0002','2024-10-10 14:26:06.100876'),(9,'auth','0007_alter_validators_add_error_messages','2024-10-10 14:26:06.121858'),(10,'auth','0008_alter_user_username_max_length','2024-10-10 14:26:06.143464'),(11,'auth','0009_alter_user_last_name_max_length','2024-10-10 14:26:06.168509'),(12,'auth','0010_alter_group_name_max_length','2024-10-10 14:26:06.222538'),(13,'auth','0011_update_proxy_permissions','2024-10-10 14:26:06.248738'),(14,'auth','0012_alter_user_first_name_max_length','2024-10-10 14:26:06.272808'),(15,'gestionar_usuarios','0001_initial','2024-10-10 14:26:07.009623'),(16,'admin','0001_initial','2024-10-10 14:26:07.195548'),(17,'admin','0002_logentry_remove_auto_add','2024-10-10 14:26:07.209550'),(18,'admin','0003_logentry_add_action_flag_choices','2024-10-10 14:26:07.224546'),(19,'gestionar_categoria','0001_initial','2024-10-10 14:26:07.255108'),(20,'gestionar_proveedor','0001_initial','2024-10-10 14:26:07.287094'),(21,'gestionar_proveedor','0002_remove_proveedor_producto','2024-10-10 14:26:07.315107'),(22,'gestionar_presentacion','0001_initial','2024-10-10 14:26:07.346721'),(23,'gestionar_marca','0001_initial','2024-10-10 14:26:07.377708'),(24,'gestionar_productos','0001_initial','2024-10-10 14:26:07.650273'),(25,'gestionar_productos','0002_alter_producto_precio','2024-10-10 14:26:07.753808'),(26,'gestionar_productos','0003_alter_producto_precio','2024-10-10 14:26:07.853134'),(27,'gestionar_productos','0004_alter_producto_precio','2024-10-10 14:26:07.863135'),(28,'gestionar_productos','0005_producto_proveedor','2024-10-10 14:26:07.985106'),(29,'gestionar_productos','0006_alter_producto_proveedor','2024-10-10 14:26:08.159311'),(30,'gestionar_compra','0001_initial','2024-10-10 14:26:08.443522'),(31,'gestionar_compra','0002_alter_compra_productos','2024-10-10 14:26:08.454051'),(32,'gestionar_compra','0003_detallecompra_remove_compra_cantidad_producto_and_more','2024-10-10 14:26:09.230312'),(33,'gestionar_compra','0004_remove_detallecompra_proveedor','2024-10-10 14:26:09.359578'),(34,'gestionar_presentacion','0002_remove_presentacion_cantidad_stock_and_more','2024-10-10 14:26:09.465517'),(35,'gestionar_presentacion','0003_alter_presentacion_nombre','2024-10-10 14:26:09.501661'),(36,'gestionar_productos','0007_producto_stock','2024-10-10 14:26:09.596008'),(37,'gestionar_respaldo','0001_initial','2024-10-10 14:26:09.623616'),(38,'gestionar_usuarios','0002_alter_usuario_groups_alter_usuario_user_permissions','2024-10-10 14:26:09.652217'),(39,'gestionar_usuarios','0003_alter_usuario_tipo_documento','2024-10-10 14:26:09.665545'),(40,'gestionar_usuarios','0004_remove_usuario_nombre_remove_usuario_rol_de_usuario_and_more','2024-10-10 14:26:09.865414'),(41,'gestionar_usuarios','0005_remove_usuario_correo_alter_usuario_email','2024-10-10 14:26:09.988184'),(42,'gestionar_usuarios','0006_alter_usuario_documento_alter_usuario_telefono','2024-10-10 14:26:10.200462'),(43,'gestionar_ventas','0001_initial','2024-10-10 14:26:10.530769'),(44,'gestionar_ventas','0002_alter_venta_productos','2024-10-10 14:26:10.578937'),(45,'gestionar_ventas','0003_remove_venta_fecha_cierre_remove_venta_saldo_actual_and_more','2024-10-10 14:26:10.680393'),(46,'gestionar_ventas','0004_rename_fecha_apertura_venta_fecha','2024-10-10 14:26:10.716912'),(47,'gestionar_ventas','0005_remove_venta_total_venta_realizada_venta_total_venta','2024-10-10 14:26:10.814272'),(48,'gestionar_ventas','0006_remove_venta_nombre_producto_and_more','2024-10-10 14:26:11.074743'),(49,'gestionar_ventas','0007_detalleventa_remove_venta_cantidad_venta_and_more','2024-10-10 14:26:11.785781'),(50,'gestionar_ventas','0008_rename_producto_detalleventa_producto_and_more','2024-10-10 14:26:12.061452'),(51,'gestionar_ventas','0009_alter_venta_usuario','2024-10-10 14:26:12.264508'),(52,'sessions','0001_initial','2024-10-10 14:26:12.332456'),(53,'gestionar_usuarios','0007_remove_usuario_is_active','2024-10-17 22:48:15.144164');
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
INSERT INTO `django_session` VALUES ('a0favi21gxxmkvtckywh6py1nw5si96o','.eJxVjMsOwiAQRf-FtSHA8HTpvt9AYBilaiAp7cr479qkC93ec859sZi2tcZt0BLnws5MstPvlhM-qO2g3FO7dY69rcuc-a7wgw4-9ULPy-H-HdQ06rdWMlAAaTUZKOiNS2AwOPBSJJNVcAWk0MpnDdYAXrPLAA4tEaABodj7A7HmNrA:1t1aVh:5jL-aoaVrVpREXfvpajZp3dEoCCaKqXCqvHCRolVs0g','2024-11-01 00:06:29.276621'),('a226uzzi8l9eu2mksisxwq9ihj0ry2dr','.eJxVjMsOwiAQRf-FtSHA8HTpvt9AYBilaiAp7cr479qkC93ec859sZi2tcZt0BLnws5MstPvlhM-qO2g3FO7dY69rcuc-a7wgw4-9ULPy-H-HdQ06rdWMlAAaTUZKOiNS2AwOPBSJJNVcAWk0MpnDdYAXrPLAA4tEaABodj7A7HmNrA:1t0U8B:rPMEcfPw1QZVK2ycLYCaAGGNs2C-cHiw1q2DFvyuIYM','2024-10-28 23:05:39.686557'),('n2cif8zbvcb70ai9u2q8qcno4hs9dmha','.eJxVjMsOwiAQRf-FtSHA8HTpvt9AYBilaiAp7cr479qkC93ec859sZi2tcZt0BLnws5MstPvlhM-qO2g3FO7dY69rcuc-a7wgw4-9ULPy-H-HdQ06rdWMlAAaTUZKOiNS2AwOPBSJJNVcAWk0MpnDdYAXrPLAA4tEaABodj7A7HmNrA:1t1CuE:o9j6C2oio4kC-WZ2aXrC15LHmgBknn3GIrOKouDkmmo','2024-10-30 22:54:14.316180'),('qgpbdcmzrjo33zflho6mb7x84hv70sgv','.eJxVjMsOwiAQRf-FtSHA8HTpvt9AYBilaiAp7cr479qkC93ec859sZi2tcZt0BLnws5MstPvlhM-qO2g3FO7dY69rcuc-a7wgw4-9ULPy-H-HdQ06rdWMlAAaTUZKOiNS2AwOPBSJJNVcAWk0MpnDdYAXrPLAA4tEaABodj7A7HmNrA:1t0UC5:ficmjJI5kM1sAm1xwz-Dw5BOXiW9F5E4mj30pylDqPo','2024-10-28 23:09:41.719752'),('rpes7vdx0svp7caf6oer6gsajvbv2oh1','.eJxVjMsOwiAQRf-FtSHA8HTpvt9AYBilaiAp7cr479qkC93ec859sZi2tcZt0BLnws5MstPvlhM-qO2g3FO7dY69rcuc-a7wgw4-9ULPy-H-HdQ06rdWMlAAaTUZKOiNS2AwOPBSJJNVcAWk0MpnDdYAXrPLAA4tEaABodj7A7HmNrA:1t0sLP:LCZFhyEDjalAivXyUzC5GOx97uFumwIQr4nis9AodXA','2024-10-30 00:56:55.340236');
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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gestionar_categoria_categoria`
--

LOCK TABLES `gestionar_categoria_categoria` WRITE;
/*!40000 ALTER TABLE `gestionar_categoria_categoria` DISABLE KEYS */;
INSERT INTO `gestionar_categoria_categoria` VALUES (1,'Lacteos',1),(2,'Alchool',1),(3,'Chocolates',1),(4,'Dulces',1),(5,'Refrescos',1);
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
  `estado` tinyint(1) NOT NULL,
  `cantidad_productos` int NOT NULL,
  `fecha` datetime(6) NOT NULL,
  `usuario_id` bigint NOT NULL,
  `total_compra` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `gestionar_compra_com_usuario_id_6b9d9dea_fk_gestionar` (`usuario_id`),
  CONSTRAINT `gestionar_compra_com_usuario_id_6b9d9dea_fk_gestionar` FOREIGN KEY (`usuario_id`) REFERENCES `gestionar_usuarios_usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gestionar_compra_compra`
--

LOCK TABLES `gestionar_compra_compra` WRITE;
/*!40000 ALTER TABLE `gestionar_compra_compra` DISABLE KEYS */;
INSERT INTO `gestionar_compra_compra` VALUES (1,1,0,'2024-10-10 14:37:27.825066',1,45000.00),(2,1,0,'2024-10-10 14:37:43.911136',1,25000.00),(3,1,0,'2024-10-10 14:38:09.584292',1,25000.00),(4,1,0,'2024-10-10 14:38:19.257042',1,0.04),(5,1,0,'2024-10-10 15:00:03.075572',1,55000.00),(7,1,0,'2024-10-14 22:38:14.974665',1,6000.00),(9,1,0,'2024-10-16 22:49:43.911302',1,15000.00),(10,1,0,'2024-10-16 22:51:09.512958',1,15000.00),(11,1,0,'2024-10-16 22:51:41.437607',1,12500.00);
/*!40000 ALTER TABLE `gestionar_compra_compra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gestionar_compra_detallecompra`
--

DROP TABLE IF EXISTS `gestionar_compra_detallecompra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gestionar_compra_detallecompra` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `cantidad` int unsigned NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `compra_id` bigint NOT NULL,
  `producto_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `gestionar_compra_det_compra_id_73aa3b95_fk_gestionar` (`compra_id`),
  KEY `gestionar_compra_det_producto_id_458a498f_fk_gestionar` (`producto_id`),
  CONSTRAINT `gestionar_compra_det_compra_id_73aa3b95_fk_gestionar` FOREIGN KEY (`compra_id`) REFERENCES `gestionar_compra_compra` (`id`),
  CONSTRAINT `gestionar_compra_det_producto_id_458a498f_fk_gestionar` FOREIGN KEY (`producto_id`) REFERENCES `gestionar_productos_producto` (`id`),
  CONSTRAINT `gestionar_compra_detallecompra_chk_1` CHECK ((`cantidad` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gestionar_compra_detallecompra`
--

LOCK TABLES `gestionar_compra_detallecompra` WRITE;
/*!40000 ALTER TABLE `gestionar_compra_detallecompra` DISABLE KEYS */;
INSERT INTO `gestionar_compra_detallecompra` VALUES (1,30,45000.00,1,1),(2,12,25000.00,2,2),(3,30,25000.00,3,3),(4,55,0.04,4,4),(5,30,55000.00,5,2),(6,15,6000.00,7,2),(7,6,15000.00,9,1),(8,12,15000.00,10,1),(9,12,12500.00,11,5);
/*!40000 ALTER TABLE `gestionar_compra_detallecompra` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gestionar_marca_marca`
--

LOCK TABLES `gestionar_marca_marca` WRITE;
/*!40000 ALTER TABLE `gestionar_marca_marca` DISABLE KEYS */;
INSERT INTO `gestionar_marca_marca` VALUES (1,'COCACOLA','logoTipo/Coca-Cola_logo.svg_RiFgdj5.png',1),(2,'Aguila Light','logoTipo/AGUILALIGH_mje7Wl3.png',1),(3,'Costeña bacana','logoTipo/Costena-Bacana-Lata.png',1),(4,'Pony-Malta','logoTipo/Pony-Malta_8Pv9sMd.png',1),(5,'Chocorramo','logoTipo/Chocorramo.jpg',1),(6,'Pepsi','logoTipo/Pepsi_logo.png',1),(7,'Bimbo','logoTipo/Bimbo_logo_2Sq9ez9.webp',1),(8,'Costeña bacana','logoTipo/Costena_bacana_botella_69Xr0tO.png',0);
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
  `estado` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `gestionar_presentacion_presentacion_nombre_2ca765f3_uniq` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gestionar_presentacion_presentacion`
--

LOCK TABLES `gestionar_presentacion_presentacion` WRITE;
/*!40000 ALTER TABLE `gestionar_presentacion_presentacion` DISABLE KEYS */;
INSERT INTO `gestionar_presentacion_presentacion` VALUES (1,'Botella',1),(2,'Lata',1),(3,'Paquete pequeño',1),(4,'Paquete mediano',1),(5,'Paquete papas grande',1),(6,'Paquete papas familiar',1),(7,'Bombombum Rojo',1),(8,'Chocorramo pequeño',1);
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
  `precio` decimal(50,2) NOT NULL,
  `unidad_de_medida` varchar(50) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `categoria_id` bigint NOT NULL,
  `marca_id` bigint NOT NULL,
  `presentacion_id` bigint NOT NULL,
  `proveedor_id` bigint NOT NULL,
  `stock` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `gestionar_productos__categoria_id_5ef4955d_fk_gestionar` (`categoria_id`),
  KEY `gestionar_productos__marca_id_3d5a9cbd_fk_gestionar` (`marca_id`),
  KEY `gestionar_productos__presentacion_id_2b5ecb2a_fk_gestionar` (`presentacion_id`),
  KEY `gestionar_productos__proveedor_id_780be8db_fk_gestionar` (`proveedor_id`),
  CONSTRAINT `gestionar_productos__categoria_id_5ef4955d_fk_gestionar` FOREIGN KEY (`categoria_id`) REFERENCES `gestionar_categoria_categoria` (`id`),
  CONSTRAINT `gestionar_productos__marca_id_3d5a9cbd_fk_gestionar` FOREIGN KEY (`marca_id`) REFERENCES `gestionar_marca_marca` (`id`),
  CONSTRAINT `gestionar_productos__presentacion_id_2b5ecb2a_fk_gestionar` FOREIGN KEY (`presentacion_id`) REFERENCES `gestionar_presentacion_presentacion` (`id`),
  CONSTRAINT `gestionar_productos__proveedor_id_780be8db_fk_gestionar` FOREIGN KEY (`proveedor_id`) REFERENCES `gestionar_proveedor_proveedor` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gestionar_productos_producto`
--

LOCK TABLES `gestionar_productos_producto` WRITE;
/*!40000 ALTER TABLE `gestionar_productos_producto` DISABLE KEYS */;
INSERT INTO `gestionar_productos_producto` VALUES (1,'Cocacola',4500.00,'ML',1,5,1,1,1,18),(2,'Bombombum',2500.00,'DAG',1,3,5,7,3,3),(3,'Cerveza',4500.00,'ML',1,2,2,1,4,-4),(4,'Pastel',4600.00,'DAG',1,3,7,3,3,-9),(5,'papas',2000.00,'DL',1,3,7,4,3,8),(6,'Cocacola',12500.00,'DL',1,1,1,2,1,0),(7,'cocacola',5000.00,'DL',1,2,1,2,1,0);
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
  `estado` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gestionar_proveedor_proveedor`
--

LOCK TABLES `gestionar_proveedor_proveedor` WRITE;
/*!40000 ALTER TABLE `gestionar_proveedor_proveedor` DISABLE KEYS */;
INSERT INTO `gestionar_proveedor_proveedor` VALUES (1,'Cocacola','k 12 #2-33','325485698','cocacola@gmail.com',1),(2,'Pepsi','calle 4 # 33-33','325458596','pepsi@gmail.com',1),(3,'Bombombum','carrera 16 # 3 -22','325451458','bombombum@gmail.com',1),(4,'aguila light','k 12 #22-33','3254875486','aguila@gmail.com',1);
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
  `date_joined` datetime(6) NOT NULL,
  `reset_token` varchar(255) DEFAULT NULL,
  `apellido` varchar(150) NOT NULL,
  `tipo_documento` varchar(2) NOT NULL,
  `documento` varchar(10) NOT NULL,
  `telefono` varchar(10) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `gestionar_usuarios_usuario_documento_1977ec72_uniq` (`documento`),
  UNIQUE KEY `gestionar_usuarios_usuario_email_5b069e1b_uniq` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gestionar_usuarios_usuario`
--

LOCK TABLES `gestionar_usuarios_usuario` WRITE;
/*!40000 ALTER TABLE `gestionar_usuarios_usuario` DISABLE KEYS */;
INSERT INTO `gestionar_usuarios_usuario` VALUES (1,'pbkdf2_sha256$320000$ecMMNUZCugZsr4QvVqGyvI$BI45a+YTCTVn/16nhFFeIVQYmib+OERVkQyDfnwLDZM=','2024-10-18 00:06:29.270932',1,'Juliansico','','','rodriguezdiazjulianfelipe@gmail.com',1,'2024-10-10 14:26:32.192997',NULL,'','','','',1),(2,'pbkdf2_sha256$320000$76j1fwbAv8hIh8VYTcc5Gi$yEpI5Bm/DqXfIC0Zu36rX5hLjpVON+FAt2wTr70vIE0=','2024-10-10 14:51:54.838236',0,'stiven','','','brayan@gmail.com',0,'2024-10-10 14:51:50.701713',NULL,'Fernandez','TI','12547964','3254145876',1);
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
-- Table structure for table `gestionar_ventas_detalleventa`
--

DROP TABLE IF EXISTS `gestionar_ventas_detalleventa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gestionar_ventas_detalleventa` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `cantidad` int unsigned NOT NULL,
  `producto_id` bigint NOT NULL,
  `venta_id` bigint NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `gestionar_ventas_det_venta_id_3f5e12d5_fk_gestionar` (`venta_id`),
  KEY `gestionar_ventas_det_producto_id_bf0876bc_fk_gestionar` (`producto_id`),
  CONSTRAINT `gestionar_ventas_det_producto_id_bf0876bc_fk_gestionar` FOREIGN KEY (`producto_id`) REFERENCES `gestionar_productos_producto` (`id`),
  CONSTRAINT `gestionar_ventas_det_venta_id_3f5e12d5_fk_gestionar` FOREIGN KEY (`venta_id`) REFERENCES `gestionar_ventas_venta` (`id`),
  CONSTRAINT `gestionar_ventas_detalleventa_chk_1` CHECK ((`cantidad` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gestionar_ventas_detalleventa`
--

LOCK TABLES `gestionar_ventas_detalleventa` WRITE;
/*!40000 ALTER TABLE `gestionar_ventas_detalleventa` DISABLE KEYS */;
INSERT INTO `gestionar_ventas_detalleventa` VALUES (3,12,3,2,4500.00),(4,5,3,3,4500.00),(5,10,1,4,4500.00),(6,21,2,5,2500.00),(7,20,4,5,4600.00),(8,12,4,6,4600.00),(9,1,2,7,2500.00),(10,2,5,7,2000.00);
/*!40000 ALTER TABLE `gestionar_ventas_detalleventa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gestionar_ventas_venta`
--

DROP TABLE IF EXISTS `gestionar_ventas_venta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gestionar_ventas_venta` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fecha` datetime(6) NOT NULL,
  `usuario_id` bigint NOT NULL,
  `valor_total` decimal(10,2) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `gestionar_ventas_ven_usuario_id_2a7de5d6_fk_gestionar` (`usuario_id`),
  CONSTRAINT `gestionar_ventas_ven_usuario_id_2a7de5d6_fk_gestionar` FOREIGN KEY (`usuario_id`) REFERENCES `gestionar_usuarios_usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gestionar_ventas_venta`
--

LOCK TABLES `gestionar_ventas_venta` WRITE;
/*!40000 ALTER TABLE `gestionar_ventas_venta` DISABLE KEYS */;
INSERT INTO `gestionar_ventas_venta` VALUES (2,'2024-10-10 14:38:59.186678',1,54000.00,1),(3,'2024-10-10 14:39:17.265477',1,22500.00,1),(4,'2024-10-10 14:39:30.750540',1,45000.00,1),(5,'2024-10-10 15:02:23.392740',1,144500.00,1),(6,'2024-10-15 19:41:31.028755',1,55200.00,1),(7,'2024-10-17 23:59:37.889908',1,6500.00,1);
/*!40000 ALTER TABLE `gestionar_ventas_venta` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-17 19:06:35
