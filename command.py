CREATE TABLE Words (
    id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    w_word VARCHAR(32) NOT NULL,
    PRIMARY KEY (id)
)
ENGINE=INNODB;



CREATE TABLE Materiaux (
    id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    m_date DATE NOT NULL,
    m_nommodif VARCHAR(24) NOT NULL,
    m_nom VARCHAR(62) NOT NULL,
    m_famille CHAR(9) NOT NULL,
    m_provenance VARCHAR(24),
    m_distance SMALLINT,
    m_fournisseur VARCHAR(32),
    m_traitement VARCHAR(62),
    m_fabrication TEXT,
    m_qualitedefaut TEXT,
    m_application TEXT,
    m_prix FLOAT UNSIGNED,
    m_composition VARCHAR(32),
    m_massevolumique FLOAT(7,2) UNSIGNED,
    m_young MEDIUMINT UNSIGNED,
    m_poisson FLOAT(3,3) UNSIGNED,
    m_limiteelast SMALLINT UNSIGNED,
    m_resistance_traction SMALLINT UNSIGNED,
    m_resistance_compression SMALLINT UNSIGNED,
    m_vickers SMALLINT UNSIGNED,
    m_tenacite FLOAT(7,3) UNSIGNED,
    m_temp_fusion SMALLINT,
    m_temp_mini SMALLINT,
    m_temp_maxi SMALLINT,
    m_chaleurspecifique SMALLINT UNSIGNED,
    m_coefficientdilatation SMALLINT,
    m_conductivite_thermique SMALLINT UNSIGNED,
    m_resistivite_elec FLOAT UNSIGNED,
    m_optique VARCHAR(12),
    m_durabilite_aqueux TINYINT,
    m_durabilite_acide TINYINT,
    m_durabilite_base TINYINT,
    m_durabilite_huile TINYINT,
    m_durabilite_alcool TINYINT,
    m_durabilite_gaz TINYINT,
    m_durabilite_construit TINYINT,
    m_durabilite_froid TINYINT,
    m_durabilite_temp_moyenne TINYINT,
    m_durabilite_chaud TINYINT,
    m_inflammabilite TINYINT,
    m_energiegrise INT,
    m_co2_p FLOAT,
    m_eau_p INT,
    m_recyclable CHAR(3),
    m_reutilisable CHAR(3),
    m_biodegradable CHAR(3),
    m_incinerable CHAR(3),
    m_renouvelable CHAR(3),
    m_toxicite VARCHAR(128) DEFAULT 'pas d\'info',
    m_productionannuelle INT,
    m_reserves INT,
    m_commentaire TEXT,
    PRIMARY KEY (m_id)
)
ENGINE=INNODB;



CREATE TABLE Pieces (
    id SMALLINT UNSIGNED AUTO_INCREMENT,
    p_date DATE NOT NULL,
    p_nommodif VARCHAR(24) NOT NULL,
    p_nom VARCHAR(48),
    p_materiau_principal VARCHAR(62),
    p_materiau_secondaire VARCHAR(62),
    p_forme VARCHAR(48),
    p_longueur FLOAT UNSIGNED,
    p_largeur FLOAT UNSIGNED,
    p_hauteur FLOAT UNSIGNED,
    p_quantite FLOAT UNSIGNED,
    p_utilisation TEXT,
    p_outil TEXT,
    p_etat TINYINT UNSIGNED,
    p_utilisation_init VARCHAR(48),
    p_thermique TINYINT,
    p_acoustique TINYINT,
    p_electrique TINYINT,
    p_resistance TINYINT,
    p_flexibilite TINYINT,
    p_elasticite TINYINT,
    p_optique VARCHAR(12),
    p_aimantation TINYINT,
    p_flottabilite TINYINT,
    p_impermeabilite TINYINT,
    p_precaution VARCHAR(128) DEFAULT 'Pas d\'info',
    p_verification TEXT,
    p_prealable TEXT,
    p_findevie TEXT,
    p_commentaire TEXT,
    PRIMARY KEY (id)
)
ENGINE=INNODB;



CREATE TABLE NameMateriaux (
    n_m_id VARCHAR(32),
    n_m_date VARCHAR(32),
    n_m_nommodif VARCHAR(32),
    n_m_nom VARCHAR(32),
    n_m_famille VARCHAR(32),
    n_m_provenance VARCHAR(32),
    n_m_distance VARCHAR(32),
    n_m_fournisseur VARCHAR(32),
    n_m_traitement VARCHAR(32),
    n_m_fabrication VARCHAR(32),
    n_m_qualitedefaut VARCHAR(32),
    n_m_application VARCHAR(32),
    n_m_prix VARCHAR(32),
    n_m_composition VARCHAR(32),
    n_m_massevolumique VARCHAR(32),
    n_m_young VARCHAR(32),
    n_m_poisson VARCHAR(32),
    n_m_limiteelast VARCHAR(32),
    n_m_resistance_traction VARCHAR(32),
    n_m_resistance_compression VARCHAR(32),
    n_m_vickers VARCHAR(32),
    n_m_tenacite VARCHAR(32),
    n_m_temp_fusion VARCHAR(32),
    n_m_temp_mini VARCHAR(32),
    n_m_temp_maxi VARCHAR(32),
    n_m_chaleurspecifique VARCHAR(32),
    n_m_coefficientdilatation VARCHAR(32),
    n_m_conductivite_thermique VARCHAR(32),
    n_m_resistivite_elec VARCHAR(32),
    n_m_optique VARCHAR(32),
    n_m_durabilite_aqueux VARCHAR(32),
    n_m_durabilite_acide VARCHAR(32),
    n_m_durabilite_base VARCHAR(32),
    n_m_durabilite_huile VARCHAR(32),
    n_m_durabilite_alcool VARCHAR(32),
    n_m_durabilite_gaz VARCHAR(32),
    n_m_durabilite_construit VARCHAR(32),
    n_m_durabilite_froid VARCHAR(32),
    n_m_durabilite_temp_moyenne VARCHAR(32),
    n_m_durabilite_chaud VARCHAR(32),
    n_m_inflammabilite VARCHAR(32),
    n_m_energiegrise VARCHAR(32),
    n_m_co2_p VARCHAR(32),
    n_m_eau_p VARCHAR(32),
    n_m_recyclable VARCHAR(32),
    n_m_reutilisable VARCHAR(32),
    n_m_biodegradable VARCHAR(32),
    n_m_incinerable VARCHAR(32),
    n_m_renouvelable VARCHAR(32),
    n_m_toxicite VARCHAR(32),
    n_m_productionannuelle VARCHAR(32),
    n_m_reserves VARCHAR(32),
    n_m_commentaire VARCHAR(32)
)
ENGINE=INNODB;



CREATE TABLE NamePieces (
    n_p_id VARCHAR(32),
    n_p_date VARCHAR(32),
    n_p_nommodif VARCHAR(32),
    n_p_nom VARCHAR(32),
    n_p_materiau_principal VARCHAR(32),
    n_p_materiau_secondaire VARCHAR(32),
    n_p_forme VARCHAR(32),
    n_p_longueur VARCHAR(32),
    n_p_largeur VARCHAR(32),
    n_p_hauteur VARCHAR(32),
    n_p_quantite VARCHAR(32),
    n_p_utilisation VARCHAR(32),
    n_p_outil VARCHAR(32),
    n_p_etat VARCHAR(32),
    n_p_utilisation_init VARCHAR(32),
    n_p_thermique VARCHAR(32),
    n_p_acoustique VARCHAR(32),
    n_p_electrique VARCHAR(32),
    n_p_resistance VARCHAR(32),
    n_p_flexibilite VARCHAR(32),
    n_p_elasticite VARCHAR(32),
    n_p_optique VARCHAR(32),
    n_p_aimantation VARCHAR(32),
    n_p_flottabilite VARCHAR(32),
    n_p_impermeabilite VARCHAR(32),
    n_p_precaution VARCHAR(32),
    n_p_verification VARCHAR(32),
    n_p_prealable VARCHAR(32),
    n_p_findevie VARCHAR(32),
    n_p_commentaire VARCHAR(32)
)
ENGINE=INNODB;



INSERT INTO NameMateriaux VALUES
    ('ID',
    'Date de modification', 
    'Édité par', 
    'Nom du matériau', 
    'Famille', 
    'Provenance', 
    'Distance de Roubaix', 
    'Fournisseur', 
    'Traitements adaptés', 
    'Procédés de fabrication',
    'Qualités et défauts',
    'Applications possibles', 
    'Prix', 
    'Composition', 
    'Masse volumique', 
    'Module de Young', 
    'Coefficient de Poisson', 
    'Limite d\'élasticité', 
    'Résistance à la traction', 
    'Résistance à la compression', 
    'Dureté Vickers', 
    'Tenacité', 
    'Température de fusion', 
    'Température minimale', 
    'Température maximale', 
    'Chaleur spécifique', 
    'Coefficient de dilatation', 
    'Conductivité thermique', 
    'Résistivité électrique', 
    'Propriétés optiques', 
    'Durabilité (milieu aqueux)', 
    'Durabilité (milieu acide)', 
    'Durabilité (milieu alcalin)', 
    'Durabilité (huile/solv./carb.)', 
    'Durabilité (alcool/R-CHO/R-CO-R)', 
    'Durabilité (milieu gazeux)', 
    'Durabilité (milieu construit)', 
    'Durabilité au froid', 
    'Durabilité à température moyenne', 
    'Durabilité au chaud', 
    'Inflammabilité', 
    'Énergie grise primaire', 
    'Empreinte CO2 primaire', 
    'Consommation d\'eau primaire', 
    'Recyclable', 
    'Réutilisable', 
    'Biodégradable', 
    'Incinérable', 
    'Renouvelable', 
    'Toxicité', 
    'Production annuelle', 
    'Réserves', 
    'Commentaires'),
    ('False', 'False', 'False', 'False', 'True', 'False', 'False', 'False', 'True', 'False', 'False', 'True', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'True', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'True', 'True', 'True', 'True', 'True', 'False', 'False', 'False', 'False'),
    (NULL, NULL, NULL, NULL, NULL, NULL, 'km', NULL, NULL, NULL, NULL, NULL, '€', NULL, 'kg/m3', 'MPa', NULL, 'MPa', 'MPa', 'MPa', 'HV', 'MPa.m^(1/2)', 'K', 'K', 'K', 'J/kg/K', '10e-6 K^(-1)', 'W/m/K', 'mOhm.cm', NULL, 'échelle de 0 à 5', 'échelle de 0 à 5', 'échelle de 0 à 5', 'échelle de 0 à 5', 'échelle de 0 à 5', 'échelle de 0 à 5', 'échelle de 0 à 5', 'échelle de 0 à 5', 'échelle de 0 à 5', 'échelle de 0 à 5', 'échelle de 0 à 5', 'kJ/kg', 'kg/kg', 'L/kg', NULL, NULL, NULL, NULL, NULL, NULL, 'tonne/an', 'tonne', NULL);


    INSERT INTO NamePieces VALUES 
    ('ID',
    'Date de modification',
    'Édité par',
    'Nom de la pièce',
    'Matériau principal',
    'Autres matériaux',
    'Forme',
    'Longueur (ou diamètre)',
    'Largeur',
    'Hauteur',
    'Quantité disponible',
    'Utilisations possibles',
    'Outils conseillés',
    'État',
    'Utilisation initiale',
    'Isolation thermique',
    'Isolation acoustique',
    'Isolation électrique',
    'Résistance',
    'Flexibilité',
    'Élasticité',
    'Propriétés optiques',
    'Aimantation',
    'Flottabilité',
    'Imperméabilité',
    'Précaution d\'usage',
    'Vérifications à effectuer',
    'Préalables à l\'usage',
    'Fin de vie',
    'Commentaires'
    ),
    ('False', 'False', 'False', 'False', 'True', 'False', 'True', 'False', 'False', 'False', 'False', 'True', 'True', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'True', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False'),
    (NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'cm', 'cm', 'cm', 'nb ou L ou kg', NULL, NULL, NULL, NULL, 'échelle de 0 à 5', 'échelle de 0 à 5', 'échelle de 0 à 5', 'échelle de 0 à 5', 'échelle de 0 à 5', 'échelle de 0 à 5', NULL, 'échelle de 0 à 5', 'échelle de 0 à 5', 'échelle de 0 à 5', NULL, NULL, NULL, NULL, NULL);



INSERT INTO Words (w_word) VALUES
    (''),
    ('alliage'),
    ('métal'),
    ('céramique'),
    ('polymère'),
    ('organique'),
    ('composite'),
    ('oui'),
    ('non'),
    ('opaque'),
    ('transparent'),
    ('translucide'),
    ('lumineux'),
    ('extérieur'),
    ('construction'),
    ('bâtiment'),
    ('jardinage'),
    ('repair café'),
    ('vitre'),
    ('serre'),
    ('combustible'),
    ('meuble'),
    ('tuyau'),
    ('câble'),
    ('isolation'),
    ('comblement'),
    ('électronique'),
    ('bricolage'),
    ('planche'),
    ('rectangulaire'),
    ('circulaire'),
    ('sphérique'),
    ('plat'),
    ('bombé'),
    ('troué'),
    ('cubique'),
    ('informe'),
    ('cylindrique'),
    ('cônique'),
    ('pyramidal'),
    ('trapèze'),
    ('creux'),
    ('plein'),
    ('long'),
    ('étroit'),
    ('large'),
    ('court'),
    ('filiforme'),
    ('scie'),
    ('marteau'),
    ('ponceuse'),
    ('tournevis'),
    ('burin'),
    ('ciseau'),
    ('ciseaux'),
    ('pince multiprise'),
    ('pince'),
    ('étau'),
    ('gants'),
    ('visseuse'),
    ('perforateuse'),
    ('scie circulaire'),
    ('scie sauteuse'),
    ('pince à sertir'),
    ('meuleuse'),
    ('couteau'),
    ('fraiseuse'),
    ('chevilleuse'),
    ('clé'),
    ('agrafeuse'),
    ('riveteuse'),
    ('pistolet à colle'),
    ('pistolet à peinture'),
    ('rabot'),
    ('décapeur thermique'),
    ('maillet'),
    ('lime'),
    ('pince coupante'),
    ('brosse'),
    ('fer à souder'),
    ('chalumeau');

# TODO compléter avec les traitements et applications possibles pour les matériaux




