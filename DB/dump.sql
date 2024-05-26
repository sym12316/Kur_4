-- MySQL dump 10.13  Distrib 8.0.37, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: asormo
-- ------------------------------------------------------
-- Server version	8.0.37

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
-- Table structure for table `appointment`
--

DROP TABLE IF EXISTS `appointment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `appointment` (
  `ID_appointment` int NOT NULL AUTO_INCREMENT,
  `Day_appointment` text,
  `Time_appointment` text,
  `ID_Pat` int DEFAULT (0),
  `ID_Doc` int DEFAULT NULL,
  `appointment_status` int DEFAULT (0),
  PRIMARY KEY (`ID_appointment`),
  KEY `ID_Pat` (`ID_Pat`),
  KEY `ID_Doc` (`ID_Doc`),
  CONSTRAINT `appointment_ibfk_1` FOREIGN KEY (`ID_Pat`) REFERENCES `patient_card` (`ID_Pat`),
  CONSTRAINT `appointment_ibfk_2` FOREIGN KEY (`ID_Doc`) REFERENCES `doc` (`ID_Doc`)
) ENGINE=InnoDB AUTO_INCREMENT=170 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `appointment`
--

LOCK TABLES `appointment` WRITE;
/*!40000 ALTER TABLE `appointment` DISABLE KEYS */;
INSERT INTO `appointment` VALUES (107,'15.02.2024','13:40',1,12,0),(108,'15.02.2024','13:50',1,13,0),(109,'15.02.2024','12:40',1,4,0),(110,'15.02.2024','12:30',1,3,0),(111,'15.02.2024','14:00',1,1,0),(112,'15.02.2024','14:10',1,2,0),(113,'15.02.2024','14:20',1,3,0),(114,'15.02.2024','12:20',1,2,0),(115,'15.02.2024','12:00',1,1,0),(116,'15.02.2024','14:30',1,4,0),(117,'15.02.2024','12:00',1,5,0),(118,'15.02.2024','12:20',1,6,0),(119,'15.02.2024','12:30',1,7,0),(120,'15.02.2024','12:50',1,5,0),(121,'15.02.2024','12:00',1,7,0),(122,'15.02.2024','09:00',1,12,0),(123,'15.02.2024','11:00',2,13,2),(124,'15.02.2024','12:20',1,1,0),(125,'15.02.2024','13:30',1,2,0),(126,'15.02.2024','13:40',1,3,0),(127,'15.02.2024','13:50',1,4,0),(128,'15.02.2024','14:00',1,5,0),(129,'15.02.2024','14:10',1,6,0),(130,'15.02.2024','14:20',1,7,0),(131,'15.02.2024','12:00',1,12,0),(132,'15.02.2024','09:00',1,13,0),(133,'15.02.2024','11:00',1,1,0),(134,'15.02.2024','12:30',1,2,0),(135,'15.02.2024','13:30',1,3,0),(136,'15.02.2024','13:40',1,4,0),(137,'15.02.2024','13:50',1,5,0),(138,'15.02.2024','14:00',1,6,0),(139,'15.02.2024','14:10',1,7,0),(140,'16.02.2024','12:00',1,13,0),(141,'16.02.2024','12:30',1,13,0),(142,'16.02.2024','13:00',1,12,0),(143,'16.02.2024','13:30',1,12,0),(144,'16.02.2024','14:00',1,12,0),(145,'16.02.2024','14:30',1,12,0),(146,'15.02.2024','13:40',1,8,0),(147,'15.02.2024','13:50',1,10,0),(148,'15.02.2024','14:00',1,8,0),(149,'15.02.2024','14:10',1,10,0),(150,'16.02.2024','12:00',1,9,0),(151,'16.02.2024','12:30',1,11,0),(152,'16.02.2024','13:00',1,9,0),(153,'16.02.2024','13:30',22,11,1),(154,'16.02.2024','14:00',21,10,1),(155,'16.02.2024','14:30',1,11,0),(156,'15.02.2024','15:40',2,10,1),(157,'15.02.2024','15:50',5,10,2),(158,'15.02.2024','16:00',3,10,2),(159,'15.02.2024','16:10',4,10,2),(160,'15.02.2024','15:40',2,9,2),(161,'15.02.2024','15:50',5,9,1),(162,'15.02.2024','16:00',3,9,2),(163,'15.02.2024','16:10',4,9,1),(164,'17.02.2024','16:00',1,9,0),(167,'16.05.2024','12:30',23,5,1),(168,'16.05.2024','13:00',24,5,1);
/*!40000 ALTER TABLE `appointment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doc`
--

DROP TABLE IF EXISTS `doc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doc` (
  `ID_Doc` int NOT NULL AUTO_INCREMENT,
  `Doc_FIO` text,
  `Spec` text,
  PRIMARY KEY (`ID_Doc`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doc`
--

LOCK TABLES `doc` WRITE;
/*!40000 ALTER TABLE `doc` DISABLE KEYS */;
INSERT INTO `doc` VALUES (1,'Покровская Л. Р.','Окулист'),(2,'Ермолаева З. К.','ЛОР'),(3,'Платонов И. П.','Педиатр'),(4,'Сорокин Т. С.','ЛОР'),(5,'Сафонова О. М.','Окулист'),(6,'Баранова Д. Я.','ЛОР'),(7,'Антипов В. Ф.','Педиатр'),(8,'Гусев Л. Д.','Педиатр'),(9,'Федоров П. Н.','Педиатр'),(10,'Шубина Л. Т.','ЛОР'),(11,'Ушаков Л. С.','ЛОР'),(12,'Мальцева В. С.','ЛОР'),(13,'Рыбакова Е. П.','Травматолог'),(14,'Орехов Т.Р.','Травматолог'),(15,'Лопатов А.П.','Кардиолог');
/*!40000 ALTER TABLE `doc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patient_card`
--

DROP TABLE IF EXISTS `patient_card`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patient_card` (
  `ID_Pat` int NOT NULL AUTO_INCREMENT,
  `Pat_FIO` text,
  `Phone_num` text,
  `Pat_Card` decimal(1,0) DEFAULT (0),
  PRIMARY KEY (`ID_Pat`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient_card`
--

LOCK TABLES `patient_card` WRITE;
/*!40000 ALTER TABLE `patient_card` DISABLE KEYS */;
INSERT INTO `patient_card` VALUES (1,'Свободно','-',0),(2,'Емельянов Владимир Петрович','+71079724449',1),(3,'Панфилова Елена Алексеевна','+77770644904',0),(4,'Ефимов Султан Филиппович','+77341329002',0),(5,'Трифонов Роберт Антонович','+70621500671',0),(6,'Третьяков Владимир Андреевич','+79871326360',1),(7,'Балашова Динара Платоновна','+77862961894',0),(8,'Фирсова Арина Матвеевна','+78397394333',0),(9,'Демин Алексей Маркович','+71745010585',0),(10,'Леонтьев Мансур Георгиевич','+77802768488',0),(11,'Митрофанова Регина Ярославовна','+79965187548',0),(12,'Свиридов Фёдор Денисович','+77232656162',0),(13,'Гуляев Ярослав Григорьевич','+79354043535',0),(14,'Суханова Веста Тимуровна','+75801513920',1),(15,'Мартынова Софья Прохоровна','+71159437391',0),(18,'Зинаида Климова','+78529631212',1),(19,'1','2',0),(20,'2','2',0),(21,'Иванов Андрей','+9639639632',0),(22,'Лалаев Андрей Иванович','+78521234565',0),(23,'Уткина Вероника Петровна','+78522581232',1),(24,'Казакова Ирина Петровна','+77417411191',1);
/*!40000 ALTER TABLE `patient_card` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-27  0:30:06
