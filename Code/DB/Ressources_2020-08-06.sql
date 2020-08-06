-- MySQL dump 10.13  Distrib 5.7.31, for Linux (x86_64)
--
-- Host: localhost    Database: Ressources
-- ------------------------------------------------------
-- Server version	5.7.31-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Materiaux`
--

DROP TABLE IF EXISTS `Materiaux`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Materiaux` (
  `id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `m_date` date NOT NULL,
  `m_nommodif` varchar(24) NOT NULL,
  `m_nom` varchar(62) NOT NULL,
  `m_famille` char(9) NOT NULL,
  `m_provenance` varchar(24) DEFAULT NULL,
  `m_distance` smallint(6) DEFAULT NULL,
  `m_fournisseur` varchar(32) DEFAULT NULL,
  `m_traitement` varchar(62) DEFAULT NULL,
  `m_fabrication` text,
  `m_qualitedefaut` text,
  `m_application` text,
  `m_prix` float unsigned DEFAULT NULL,
  `m_composition` varchar(32) DEFAULT NULL,
  `m_massevolumique` float(7,2) unsigned DEFAULT NULL,
  `m_young` mediumint(8) unsigned DEFAULT NULL,
  `m_poisson` float(3,3) unsigned DEFAULT NULL,
  `m_limiteelast` smallint(5) unsigned DEFAULT NULL,
  `m_resistance_traction` smallint(5) unsigned DEFAULT NULL,
  `m_resistance_compression` smallint(5) unsigned DEFAULT NULL,
  `m_vickers` smallint(5) unsigned DEFAULT NULL,
  `m_tenacite` float(7,3) unsigned DEFAULT NULL,
  `m_temp_fusion` smallint(6) DEFAULT NULL,
  `m_temp_mini` smallint(6) DEFAULT NULL,
  `m_temp_maxi` smallint(6) DEFAULT NULL,
  `m_chaleurspecifique` smallint(5) unsigned DEFAULT NULL,
  `m_coefficientdilatation` smallint(6) DEFAULT NULL,
  `m_conductivite_thermique` smallint(5) unsigned DEFAULT NULL,
  `m_resistivite_elec` float unsigned DEFAULT NULL,
  `m_optique` varchar(12) DEFAULT NULL,
  `m_durabilite_aqueux` tinyint(4) DEFAULT NULL,
  `m_durabilite_acide` tinyint(4) DEFAULT NULL,
  `m_durabilite_base` tinyint(4) DEFAULT NULL,
  `m_durabilite_huile` tinyint(4) DEFAULT NULL,
  `m_durabilite_alcool` tinyint(4) DEFAULT NULL,
  `m_durabilite_gaz` tinyint(4) DEFAULT NULL,
  `m_durabilite_construit` tinyint(4) DEFAULT NULL,
  `m_durabilite_froid` tinyint(4) DEFAULT NULL,
  `m_durabilite_temp_moyenne` tinyint(4) DEFAULT NULL,
  `m_durabilite_chaud` tinyint(4) DEFAULT NULL,
  `m_inflammabilite` tinyint(4) DEFAULT NULL,
  `m_energiegrise` int(11) DEFAULT NULL,
  `m_co2_p` float DEFAULT NULL,
  `m_eau_p` int(11) DEFAULT NULL,
  `m_recyclable` char(3) DEFAULT NULL,
  `m_reutilisable` char(3) DEFAULT NULL,
  `m_biodegradable` char(3) DEFAULT NULL,
  `m_incinerable` char(3) DEFAULT NULL,
  `m_renouvelable` char(3) DEFAULT NULL,
  `m_toxicite` varchar(128) DEFAULT 'pas d''info',
  `m_productionannuelle` int(11) DEFAULT NULL,
  `m_reserves` int(11) DEFAULT NULL,
  `m_commentaire` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Materiaux`
--

LOCK TABLES `Materiaux` WRITE;
/*!40000 ALTER TABLE `Materiaux` DISABLE KEYS */;
INSERT INTO `Materiaux` VALUES (1,'2020-07-28','xorielle','pin','organique','Lille',5,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'pas d\'info',NULL,NULL,'L\'arbre dont provient le bois est très dur. D\'ailleurs, voilà un très long commentaire.'),(2,'2020-07-28','xorielle','pin','organique',NULL,NULL,NULL,'vernissage, ponçage',NULL,'léger et facile à travailler','jardinage, extérieur, construction',NULL,NULL,450.00,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'oui','oui','RAS',NULL,NULL,'l\'arbre dont provient ce bois est géré durablement, en plus il provient de France, et n\'est pas transporté sur de longues distances.'),(3,'2020-07-28','xorielle','sapin','organique','Très très longue ville',15,NULL,NULL,NULL,NULL,'construction, vernissage, ponçage, extérieur',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'pas d\'info',NULL,NULL,'Blablabla je fais un petit commentaire un peu long quand même.'),(4,'2020-08-06','xorielle','cuivre','métal',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,8800.00,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'pas d\'info',NULL,NULL,NULL);
/*!40000 ALTER TABLE `Materiaux` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `NameMateriaux`
--

DROP TABLE IF EXISTS `NameMateriaux`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `NameMateriaux` (
  `n_m_id` varchar(32) DEFAULT NULL,
  `n_m_date` varchar(32) DEFAULT NULL,
  `n_m_nommodif` varchar(32) DEFAULT NULL,
  `n_m_nom` varchar(32) DEFAULT NULL,
  `n_m_famille` varchar(32) DEFAULT NULL,
  `n_m_provenance` varchar(32) DEFAULT NULL,
  `n_m_distance` varchar(32) DEFAULT NULL,
  `n_m_fournisseur` varchar(32) DEFAULT NULL,
  `n_m_traitement` varchar(32) DEFAULT NULL,
  `n_m_fabrication` varchar(32) DEFAULT NULL,
  `n_m_qualitedefaut` varchar(32) DEFAULT NULL,
  `n_m_application` varchar(32) DEFAULT NULL,
  `n_m_prix` varchar(32) DEFAULT NULL,
  `n_m_composition` varchar(32) DEFAULT NULL,
  `n_m_massevolumique` varchar(32) DEFAULT NULL,
  `n_m_young` varchar(32) DEFAULT NULL,
  `n_m_poisson` varchar(32) DEFAULT NULL,
  `n_m_limiteelast` varchar(32) DEFAULT NULL,
  `n_m_resistance_traction` varchar(32) DEFAULT NULL,
  `n_m_resistance_compression` varchar(32) DEFAULT NULL,
  `n_m_vickers` varchar(32) DEFAULT NULL,
  `n_m_tenacite` varchar(32) DEFAULT NULL,
  `n_m_temp_fusion` varchar(32) DEFAULT NULL,
  `n_m_temp_mini` varchar(32) DEFAULT NULL,
  `n_m_temp_maxi` varchar(32) DEFAULT NULL,
  `n_m_chaleurspecifique` varchar(32) DEFAULT NULL,
  `n_m_coefficientdilatation` varchar(32) DEFAULT NULL,
  `n_m_conductivite_thermique` varchar(32) DEFAULT NULL,
  `n_m_resistivite_elec` varchar(32) DEFAULT NULL,
  `n_m_optique` varchar(32) DEFAULT NULL,
  `n_m_durabilite_aqueux` varchar(32) DEFAULT NULL,
  `n_m_durabilite_acide` varchar(32) DEFAULT NULL,
  `n_m_durabilite_base` varchar(32) DEFAULT NULL,
  `n_m_durabilite_huile` varchar(32) DEFAULT NULL,
  `n_m_durabilite_alcool` varchar(32) DEFAULT NULL,
  `n_m_durabilite_gaz` varchar(32) DEFAULT NULL,
  `n_m_durabilite_construit` varchar(32) DEFAULT NULL,
  `n_m_durabilite_froid` varchar(32) DEFAULT NULL,
  `n_m_durabilite_temp_moyenne` varchar(32) DEFAULT NULL,
  `n_m_durabilite_chaud` varchar(32) DEFAULT NULL,
  `n_m_inflammabilite` varchar(32) DEFAULT NULL,
  `n_m_energiegrise` varchar(32) DEFAULT NULL,
  `n_m_co2_p` varchar(32) DEFAULT NULL,
  `n_m_eau_p` varchar(32) DEFAULT NULL,
  `n_m_recyclable` varchar(32) DEFAULT NULL,
  `n_m_reutilisable` varchar(32) DEFAULT NULL,
  `n_m_biodegradable` varchar(32) DEFAULT NULL,
  `n_m_incinerable` varchar(32) DEFAULT NULL,
  `n_m_renouvelable` varchar(32) DEFAULT NULL,
  `n_m_toxicite` varchar(32) DEFAULT NULL,
  `n_m_productionannuelle` varchar(32) DEFAULT NULL,
  `n_m_reserves` varchar(32) DEFAULT NULL,
  `n_m_commentaire` varchar(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `NameMateriaux`
--

LOCK TABLES `NameMateriaux` WRITE;
/*!40000 ALTER TABLE `NameMateriaux` DISABLE KEYS */;
INSERT INTO `NameMateriaux` VALUES ('ID','Date de modification','Édité par','Nom du matériau','Famille','Provenance','Distance de Roubaix','Fournisseur','Traitements adaptés','Procédés de fabrication','Qualités et défauts','Applications possibles','Prix','Composition','Masse volumique','Module de Young','Coefficient de Poisson','Limite d\'élasticité','Résistance à la traction','Résistance à la compression','Dureté Vickers','Tenacité','Température de fusion','Température minimale','Température maximale','Chaleur spécifique','Coefficient de dilatation','Conductivité thermique','Résistivité électrique','Propriétés optiques','Durabilité (milieu aqueux)','Durabilité (milieu acide)','Durabilité (milieu alcalin)','Durabilité (huile/solv./carb.)','Durabilité (alcool/R-CHO/R-CO-R)','Durabilité (milieu gazeux)','Durabilité (milieu construit)','Durabilité au froid','Durabilité à température moyenne','Durabilité au chaud','Inflammabilité','Énergie grise primaire','Empreinte CO2 primaire','Consommation d\'eau primaire','Recyclable','Réutilisable','Biodégradable','Incinérable','Renouvelable','Toxicité','Production annuelle','Réserves','Commentaires'),('False','False','False','False','True','False','False','False','True','False','False','True','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','False','True','False','False','False','False','False','False','False','False','False','False','False','False','False','False','True','True','True','True','True','False','False','False','False'),(NULL,NULL,NULL,NULL,NULL,NULL,'km',NULL,NULL,NULL,NULL,NULL,'€',NULL,'kg/m3','MPa',NULL,'MPa','MPa','MPa','HV','MPa.m^(1/2)','K','K','K','J/kg/K','10e-6 K^(-1)','W/m/K','mOhm.cm',NULL,'échelle de 0 à 5','échelle de 0 à 5','échelle de 0 à 5','échelle de 0 à 5','échelle de 0 à 5','échelle de 0 à 5','échelle de 0 à 5','échelle de 0 à 5','échelle de 0 à 5','échelle de 0 à 5','échelle de 0 à 5','kJ/kg','kg/kg','L/kg',NULL,NULL,NULL,NULL,NULL,NULL,'tonne/an','tonne',NULL),(NULL,'métadonnées','métadonnées',NULL,'propriétés physiques','procuration','procuration','procuration','usage','procuration','usage','usage','procuration','propriétés physiques','propriétés physiques','propriétés mécaniques','propriétés mécaniques','propriétés mécaniques','propriétés mécaniques','propriétés mécaniques','propriétés mécaniques','propriétés mécaniques','propriétés thermiques','propriétés thermiques','propriétés thermiques','propriétés thermiques','propriétés thermiques','propriétés thermiques','propriétés physiques','propriétés physiques','durabilités','durabilités','durabilités','durabilités','durabilités','durabilités','durabilités','durabilités','durabilités','durabilités','usage','environnement','environnement','environnement','environnement','environnement','environnement','environnement','environnement','usage','procuration','procuration','usage');
/*!40000 ALTER TABLE `NameMateriaux` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `NamePieces`
--

DROP TABLE IF EXISTS `NamePieces`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `NamePieces` (
  `n_p_id` varchar(32) DEFAULT NULL,
  `n_p_date` varchar(32) DEFAULT NULL,
  `n_p_nommodif` varchar(32) DEFAULT NULL,
  `n_p_nom` varchar(32) DEFAULT NULL,
  `n_p_materiau_principal` varchar(32) DEFAULT NULL,
  `n_p_materiau_secondaire` varchar(32) DEFAULT NULL,
  `n_p_forme` varchar(32) DEFAULT NULL,
  `n_p_longueur` varchar(32) DEFAULT NULL,
  `n_p_largeur` varchar(32) DEFAULT NULL,
  `n_p_hauteur` varchar(32) DEFAULT NULL,
  `n_p_quantite` varchar(32) DEFAULT NULL,
  `n_p_utilisation` varchar(32) DEFAULT NULL,
  `n_p_outil` varchar(32) DEFAULT NULL,
  `n_p_etat` varchar(32) DEFAULT NULL,
  `n_p_utilisation_init` varchar(32) DEFAULT NULL,
  `n_p_thermique` varchar(32) DEFAULT NULL,
  `n_p_acoustique` varchar(32) DEFAULT NULL,
  `n_p_electrique` varchar(32) DEFAULT NULL,
  `n_p_resistance` varchar(32) DEFAULT NULL,
  `n_p_flexibilite` varchar(32) DEFAULT NULL,
  `n_p_elasticite` varchar(32) DEFAULT NULL,
  `n_p_optique` varchar(32) DEFAULT NULL,
  `n_p_aimantation` varchar(32) DEFAULT NULL,
  `n_p_flottabilite` varchar(32) DEFAULT NULL,
  `n_p_impermeabilite` varchar(32) DEFAULT NULL,
  `n_p_precaution` varchar(32) DEFAULT NULL,
  `n_p_verification` varchar(32) DEFAULT NULL,
  `n_p_prealable` varchar(32) DEFAULT NULL,
  `n_p_findevie` varchar(32) DEFAULT NULL,
  `n_p_commentaire` varchar(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `NamePieces`
--

LOCK TABLES `NamePieces` WRITE;
/*!40000 ALTER TABLE `NamePieces` DISABLE KEYS */;
INSERT INTO `NamePieces` VALUES ('ID','Date de modification','Édité par','Nom de la pièce','Matériau principal','Autres matériaux','Forme','Longueur (ou diamètre)','Largeur','Hauteur','Quantité disponible','Utilisations possibles','Outils conseillés','État','Utilisation initiale','Isolation thermique','Isolation acoustique','Isolation électrique','Résistance','Flexibilité','Élasticité','Propriétés optiques','Aimantation','Flottabilité','Imperméabilité','Précaution d\'usage','Vérifications à effectuer','Préalables à l\'usage','Fin de vie','Commentaires'),('False','False','False','False','True','False','True','False','False','False','False','True','True','False','False','False','False','False','False','False','False','True','False','False','False','False','False','False','False','False'),(NULL,NULL,NULL,NULL,NULL,NULL,NULL,'cm','cm','cm','nb ou L ou kg',NULL,NULL,NULL,NULL,'échelle de 0 à 5','échelle de 0 à 5','échelle de 0 à 5','échelle de 0 à 5','échelle de 0 à 5','échelle de 0 à 5',NULL,'échelle de 0 à 5','échelle de 0 à 5','échelle de 0 à 5',NULL,NULL,NULL,NULL,NULL),(NULL,'métadonnées','métadonnées',NULL,NULL,'Divers','Dimensions','Dimensions','Dimensions','Dimensions','Divers','Usage','Usage','Divers','Usage','Propriétés','Propriétés','Propriétés','Propriétés','Propriétés','Propriétés','Propriétés','Propriétés','Propriétés','Propriétés','Usage','Usage','Usage','Usage','Divers');
/*!40000 ALTER TABLE `NamePieces` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Pieces`
--

DROP TABLE IF EXISTS `Pieces`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Pieces` (
  `id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `p_date` date NOT NULL,
  `p_nommodif` varchar(24) NOT NULL,
  `p_nom` varchar(48) DEFAULT NULL,
  `p_materiau_principal` varchar(62) DEFAULT NULL,
  `p_materiau_secondaire` varchar(62) DEFAULT NULL,
  `p_forme` varchar(48) DEFAULT NULL,
  `p_longueur` float unsigned DEFAULT NULL,
  `p_largeur` float unsigned DEFAULT NULL,
  `p_hauteur` float unsigned DEFAULT NULL,
  `p_quantite` float unsigned DEFAULT NULL,
  `p_utilisation` text,
  `p_outil` text,
  `p_etat` tinyint(3) unsigned DEFAULT NULL,
  `p_utilisation_init` varchar(48) DEFAULT NULL,
  `p_thermique` tinyint(4) DEFAULT NULL,
  `p_acoustique` tinyint(4) DEFAULT NULL,
  `p_electrique` tinyint(4) DEFAULT NULL,
  `p_resistance` tinyint(4) DEFAULT NULL,
  `p_flexibilite` tinyint(4) DEFAULT NULL,
  `p_elasticite` tinyint(4) DEFAULT NULL,
  `p_optique` varchar(12) DEFAULT NULL,
  `p_aimantation` tinyint(4) DEFAULT NULL,
  `p_flottabilite` tinyint(4) DEFAULT NULL,
  `p_impermeabilite` tinyint(4) DEFAULT NULL,
  `p_precaution` varchar(128) DEFAULT 'Pas d''info',
  `p_verification` text,
  `p_prealable` text,
  `p_findevie` text,
  `p_commentaire` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Pieces`
--

LOCK TABLES `Pieces` WRITE;
/*!40000 ALTER TABLE `Pieces` DISABLE KEYS */;
INSERT INTO `Pieces` VALUES (1,'2020-08-06','xorielle','planche','pin',NULL,'rectangulaire',120,5,2,42,'jardinage','marteau, tournevis',4,'palette',4,2,5,3,1,0,'opaque',0,5,3,'attention aux échardes','planter une pointe de couteau','vernir','compost, bois de chauffage',NULL),(2,'2020-08-06','xorielle','tuyau','cuivre',NULL,'cylindrique',150,3,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Pas d\'info',NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `Pieces` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Words`
--

DROP TABLE IF EXISTS `Words`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Words` (
  `id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `w_word` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=84 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Words`
--

LOCK TABLES `Words` WRITE;
/*!40000 ALTER TABLE `Words` DISABLE KEYS */;
INSERT INTO `Words` VALUES (1,''),(2,'alliage'),(3,'métal'),(4,'céramique'),(5,'polymère'),(6,'organique'),(7,'composite'),(8,'oui'),(9,'non'),(10,'opaque'),(11,'transparent'),(12,'translucide'),(13,'lumineux'),(14,'extérieur'),(15,'construction'),(16,'bâtiment'),(17,'jardinage'),(18,'repair café'),(19,'vitre'),(20,'serre'),(21,'combustible'),(22,'meuble'),(23,'tuyau'),(24,'câble'),(25,'isolation'),(26,'comblement'),(27,'électronique'),(28,'bricolage'),(29,'planche'),(30,'rectangulaire'),(31,'circulaire'),(32,'sphérique'),(33,'plat'),(34,'bombé'),(35,'troué'),(36,'cubique'),(37,'informe'),(38,'cylindrique'),(39,'cônique'),(40,'pyramidal'),(41,'trapèze'),(42,'creux'),(43,'plein'),(44,'long'),(45,'étroit'),(46,'large'),(47,'court'),(48,'filiforme'),(49,'scie'),(50,'marteau'),(51,'ponceuse'),(52,'tournevis'),(53,'burin'),(54,'ciseau'),(55,'ciseaux'),(56,'pince multiprise'),(57,'pince'),(58,'étau'),(59,'gants'),(60,'visseuse'),(61,'perforateuse'),(62,'scie circulaire'),(63,'scie sauteuse'),(64,'pince à sertir'),(65,'meuleuse'),(66,'couteau'),(67,'fraiseuse'),(68,'chevilleuse'),(69,'clé'),(70,'agrafeuse'),(71,'riveteuse'),(72,'pistolet à colle'),(73,'pistolet à peinture'),(74,'rabot'),(75,'décapeur thermique'),(76,'maillet'),(77,'lime'),(78,'pince coupante'),(79,'brosse'),(80,'fer à souder'),(81,'chalumeau'),(82,'vernissage'),(83,'ponçage');
/*!40000 ALTER TABLE `Words` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-08-06 16:47:05
