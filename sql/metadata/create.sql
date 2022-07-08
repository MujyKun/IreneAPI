INSERT INTO groupmembers.bloodtypes(name)
VALUES ('O'), ('A'), ('B'), ('AB');

INSERT INTO groupmembers.position(name)
VALUES ('Leader'), ('Vocalist'), ('Lead Vocalist'), ('Main Vocalist'), ('Dancer'), ('Main Dancer'), ('Lead Dancer'),
       ('Sub Vocalist'), ('Former'), ('Rapper'), ('Lead Rapper'), ('Main Rapper');


INSERT INTO blackjack.cardvalues(id, name, value) VALUES
  (1,'Ace of Hearts',11),
  (2,'Two of Hearts',2),
  (3,'Three of Hearts',3),
  (4,'Four of Hearts',4),
  (5,'Five of Hearts',5),
  (6,'Six of Hearts',6),
  (7,'Seven of Hearts',7),
  (8,'Eight of Hearts',8),
  (9,'Nine of Hearts',9),
  (10,'Ten of Hearts',10),
  (11,'Jack of Hearts',10),
  (12,'Queen of Hearts',10),
  (13,'King of Hearts',10),
  (14,'Ace of Diamonds',11),
  (15,'Two of Diamonds',2),
  (16,'Three of Diamonds',3),
  (17,'Four of Diamonds',4),
  (18,'Five of Diamonds',5),
  (19,'Six of Diamonds',6),
  (20,'Seven of Diamonds',7),
  (21,'Eight of Diamonds',8),
  (22,'Nine of Diamonds',9),
  (23,'Ten of Diamonds',10),
  (24,'Jack of Diamonds',10),
  (25,'Queen of Diamonds',10),
  (26,'King of Diamonds',10),
  (27,'Ace of Spades',11),
  (28,'Two of Spades',2),
  (29,'Three of Spades',3),
  (30,'Four of Spades',4),
  (31,'Five of Spades',5),
  (32,'Six of Spades',6),
  (33,'Seven of Spades',7),
  (34,'Eight of Spades',8),
  (35,'Nine of Spades',9),
  (36,'Ten of Spades',10),
  (37,'Jack of Spades',10),
  (38,'Queen of Spades',10),
  (39,'King of Spades',10),
  (40,'Ace of Clubs',11),
  (41,'Two of Clubs',2),
  (42,'Three of Clubs',3),
  (43,'Four of Clubs',4),
  (44,'Five of Clubs',5),
  (45,'Six of Clubs',6),
  (46,'Seven of Clubs',7),
  (47,'Eight of Clubs',8),
  (48,'Nine of Clubs',9),
  (49,'Ten of Clubs',10),
  (50,'Jack of Clubs',10),
  (51,'Queen of Clubs',10),
  (52,'King of Clubs',10);

INSERT INTO interactions.interactiontypes(name) VALUES ('stepon'), ('stab'), ('choke'), ('pullhair'), ('cuddle'), ('pat'), ('punch'), ('spit'), ('lick'), ('hug'), ('kiss'), ('slap');


INSERT INTO public.timezones(name, shortname) VALUES ('Europe/Andorra', 'ca'),
                                                     ('Asia/Dubai', 'ar-AE'),
                                                     ('Asia/Kabul', 'fa-AF'),
                                                     ('America/Antigua', 'en-AG'),
                                                     ('America/Anguilla', 'en-AI'),
                                                     ('Europe/Tirane', 'sq'),
                                                     ('Asia/Yerevan', 'hy'),
                                                     ('Africa/Luanda', 'pt-AO'),
                                                     ('America/Argentina/Buenos_Aires', 'es-AR'),
                                                     ('America/Argentina/Cordoba', 'es-AR'),
                                                     ('America/Argentina/Salta', 'es-AR'),
                                                     ('America/Argentina/Jujuy', 'es-AR'),
                                                     ('America/Argentina/Tucuman', 'es-AR'),
                                                     ('America/Argentina/Catamarca', 'es-AR'),
                                                     ('America/Argentina/La_Rioja', 'es-AR'),
                                                     ('America/Argentina/San_Juan', 'es-AR'),
                                                     ('America/Argentina/Mendoza', 'es-AR'),
                                                     ('America/Argentina/San_Luis', 'es-AR'),
                                                     ('America/Argentina/Rio_Gallegos', 'es-AR'),
                                                     ('America/Argentina/Ushuaia', 'es-AR'),
                                                     ('Pacific/Pago_Pago', 'en-AS'),
                                                     ('Europe/Vienna', 'de-AT'),
                                                     ('Australia/Lord_Howe', 'en-AU'),
                                                     ('Antarctica/Macquarie', 'en-AU'),
                                                     ('Australia/Hobart', 'en-AU'),
                                                     ('Australia/Currie', 'en-AU'),
                                                     ('Australia/Melbourne', 'en-AU'),
                                                     ('Australia/Sydney', 'en-AU'),
                                                     ('Australia/Broken_Hill', 'en-AU'),
                                                     ('Australia/Brisbane', 'en-AU'),
                                                     ('Australia/Lindeman', 'en-AU'),
                                                     ('Australia/Adelaide', 'en-AU'),
                                                     ('Australia/Darwin', 'en-AU'),
                                                     ('Australia/Perth', 'en-AU'),
                                                     ('Australia/Eucla', 'en-AU'),
                                                     ('America/Aruba', 'nl-AW'),
                                                     ('Europe/Mariehamn', 'sv-AX'),
                                                     ('Asia/Baku', 'az'),
                                                     ('Europe/Sarajevo', 'bs'),
                                                     ('America/Barbados', 'en-BB'),
                                                     ('Asia/Dhaka', 'bn-BD'),
                                                     ('Europe/Brussels', 'nl-BE'),
                                                     ('Africa/Ouagadougou', 'fr-BF'),
                                                     ('Europe/Sofia', 'bg'),
                                                     ('Asia/Bahrain', 'ar-BH'),
                                                     ('Africa/Bujumbura', 'fr-BI'),
                                                     ('Africa/Porto-Novo', 'fr-BJ'),
                                                     ('America/St_Barthelemy', 'fr'),
                                                     ('Atlantic/Bermuda', 'en-BM'),
                                                     ('Asia/Brunei', 'ms-BN'),
                                                     ('America/La_Paz', 'es-BO'),
                                                     ('America/Kralendijk', 'nl'),
                                                     ('America/Noronha', 'pt-BR'),
                                                     ('America/Belem', 'pt-BR'),
                                                     ('America/Fortaleza', 'pt-BR'),
                                                     ('America/Recife', 'pt-BR'),
                                                     ('America/Araguaina', 'pt-BR'),
                                                     ('America/Maceio', 'pt-BR'),
                                                     ('America/Bahia', 'pt-BR'),
                                                     ('America/Sao_Paulo', 'pt-BR'),
                                                     ('America/Campo_Grande', 'pt-BR'),
                                                     ('America/Cuiaba', 'pt-BR'),
                                                     ('America/Santarem', 'pt-BR'),
                                                     ('America/Porto_Velho', 'pt-BR'),
                                                     ('America/Boa_Vista', 'pt-BR'),
                                                     ('America/Manaus', 'pt-BR'),
                                                     ('America/Eirunepe', 'pt-BR'),
                                                     ('America/Rio_Branco', 'pt-BR'),
                                                     ('America/Nassau', 'en-BS'),
                                                     ('Asia/Thimphu', 'dz'),
                                                     ('Africa/Gaborone', 'en-BW'),
                                                     ('Europe/Minsk', 'be'),
                                                     ('America/Belize', 'en-BZ'),
                                                     ('America/St_Johns', 'en-CA'),
                                                     ('America/Halifax', 'en-CA'),
                                                     ('America/Glace_Bay', 'en-CA'),
                                                     ('America/Moncton', 'en-CA'),
                                                     ('America/Goose_Bay', 'en-CA'),
                                                     ('America/Blanc-Sablon', 'en-CA'),
                                                     ('America/Toronto', 'en-CA'),
                                                     ('America/Nipigon', 'en-CA'),
                                                     ('America/Thunder_Bay', 'en-CA'),
                                                     ('America/Iqaluit', 'en-CA'),
                                                     ('America/Pangnirtung', 'en-CA'),
                                                     ('America/Atikokan', 'en-CA'),
                                                     ('America/Winnipeg', 'en-CA'),
                                                     ('America/Rainy_River', 'en-CA'),
                                                     ('America/Resolute', 'en-CA'),
                                                     ('America/Rankin_Inlet', 'en-CA'),
                                                     ('America/Regina', 'en-CA'),
                                                     ('America/Swift_Current', 'en-CA'),
                                                     ('America/Edmonton', 'en-CA'),
                                                     ('America/Cambridge_Bay', 'en-CA'),
                                                     ('America/Yellowknife', 'en-CA'),
                                                     ('America/Inuvik', 'en-CA'),
                                                     ('America/Creston', 'en-CA'),
                                                     ('America/Dawson_Creek', 'en-CA'),
                                                     ('America/Fort_Nelson', 'en-CA'),
                                                     ('America/Vancouver', 'en-CA'),
                                                     ('America/Whitehorse', 'en-CA'),
                                                     ('America/Dawson', 'en-CA'),
                                                     ('Indian/Cocos', 'ms-CC'),
                                                     ('Africa/Kinshasa', 'fr-CD'),
                                                     ('Africa/Lubumbashi', 'fr-CD'),
                                                     ('Africa/Bangui', 'fr-CF'),
                                                     ('Africa/Brazzaville', 'fr-CG'),
                                                     ('Europe/Zurich', 'de-CH'),
                                                     ('Africa/Abidjan', 'fr-CI'),
                                                     ('Pacific/Rarotonga', 'en-CK'),
                                                     ('America/Santiago', 'es-CL'),
                                                     ('America/Punta_Arenas', 'es-CL'),
                                                     ('Pacific/Easter', 'es-CL'),
                                                     ('Africa/Douala', 'en-CM'),
                                                     ('Asia/Shanghai', 'zh-CN'),
                                                     ('Asia/Urumqi', 'zh-CN'),
                                                     ('America/Bogota', 'es-CO'),
                                                     ('America/Costa_Rica', 'es-CR'),
                                                     ('America/Havana', 'es-CU'),
                                                     ('Atlantic/Cape_Verde', 'pt-CV'),
                                                     ('America/Curacao', 'nl'),
                                                     ('Indian/Christmas', 'en'),
                                                     ('Asia/Nicosia', 'el-CY'),
                                                     ('Asia/Famagusta', 'el-CY'),
                                                     ('Europe/Prague', 'cs'),
                                                     ('Europe/Berlin', 'de'),
                                                     ('Europe/Busingen', 'de'),
                                                     ('Africa/Djibouti', 'fr-DJ'),
                                                     ('Europe/Copenhagen', 'da-DK'),
                                                     ('America/Dominica', 'en-DM'),
                                                     ('America/Santo_Domingo', 'es-DO'),
                                                     ('Africa/Algiers', 'ar-DZ'),
                                                     ('America/Guayaquil', 'es-EC'),
                                                     ('Pacific/Galapagos', 'es-EC'),
                                                     ('Europe/Tallinn', 'et'),
                                                     ('Africa/Cairo', 'ar-EG'),
                                                     ('Africa/El_Aaiun', 'ar'),
                                                     ('Africa/Asmara', 'aa-ER'),
                                                     ('Europe/Madrid', 'es-ES'),
                                                     ('Africa/Ceuta', 'es-ES'),
                                                     ('Atlantic/Canary', 'es-ES'),
                                                     ('Africa/Addis_Ababa', 'am'),
                                                     ('Europe/Helsinki', 'fi-FI'),
                                                     ('Pacific/Fiji', 'en-FJ'),
                                                     ('Atlantic/Stanley', 'en-FK'),
                                                     ('Pacific/Chuuk', 'en-FM'),
                                                     ('Pacific/Pohnpei', 'en-FM'),
                                                     ('Pacific/Kosrae', 'en-FM'),
                                                     ('Atlantic/Faroe', 'fo'),
                                                     ('Europe/Paris', 'fr-FR'),
                                                     ('Africa/Libreville', 'fr-GA'),
                                                     ('Europe/London', 'en-GB'),
                                                     ('America/Grenada', 'en-GD'),
                                                     ('Asia/Tbilisi', 'ka'),
                                                     ('America/Cayenne', 'fr-GF'),
                                                     ('Europe/Guernsey', 'en'),
                                                     ('Africa/Accra', 'en-GH'),
                                                     ('Europe/Gibraltar', 'en-GI'),
                                                     ('America/Nuuk', 'kl'),
                                                     ('America/Danmarkshavn', 'kl'),
                                                     ('America/Scoresbysund', 'kl'),
                                                     ('America/Thule', 'kl'),
                                                     ('Africa/Banjul', 'en-GM'),
                                                     ('Africa/Conakry', 'fr-GN'),
                                                     ('America/Guadeloupe', 'fr-GP'),
                                                     ('Africa/Malabo', 'es-GQ'),
                                                     ('Europe/Athens', 'el-GR'),
                                                     ('Atlantic/South_Georgia', 'en'),
                                                     ('America/Guatemala', 'es-GT'),
                                                     ('Pacific/Guam', 'en-GU'),
                                                     ('Africa/Bissau', 'pt-GW'),
                                                     ('America/Guyana', 'en-GY'),
                                                     ('Asia/Hong_Kong', 'zh-HK'),
                                                     ('America/Tegucigalpa', 'es-HN'),
                                                     ('Europe/Zagreb', 'hr-HR'),
                                                     ('America/Port-au-Prince', 'ht'),
                                                     ('Europe/Budapest', 'hu-HU'),
                                                     ('Asia/Jakarta', 'id'),
                                                     ('Asia/Pontianak', 'id'),
                                                     ('Asia/Makassar', 'id'),
                                                     ('Asia/Jayapura', 'id'),
                                                     ('Europe/Dublin', 'en-IE'),
                                                     ('Asia/Jerusalem', 'he'),
                                                     ('Europe/Isle_of_Man', 'en'),
                                                     ('Asia/Kolkata', 'en-IN'),
                                                     ('Indian/Chagos', 'en-IO'),
                                                     ('Asia/Baghdad', 'ar-IQ'),
                                                     ('Asia/Tehran', 'fa-IR'),
                                                     ('Atlantic/Reykjavik', 'is'),
                                                     ('Europe/Rome', 'it-IT'),
                                                     ('Europe/Jersey', 'en'),
                                                     ('America/Jamaica', 'en-JM'),
                                                     ('Asia/Amman', 'ar-JO'),
                                                     ('Asia/Tokyo', 'ja'),
                                                     ('Africa/Nairobi', 'en-KE'),
                                                     ('Asia/Bishkek', 'ky'),
                                                     ('Asia/Phnom_Penh', 'km'),
                                                     ('Pacific/Tarawa', 'en-KI'),
                                                     ('Pacific/Enderbury', 'en-KI'),
                                                     ('Pacific/Kiritimati', 'en-KI'),
                                                     ('Indian/Comoro', 'ar'),
                                                     ('America/St_Kitts', 'en-KN'),
                                                     ('Asia/Pyongyang', 'ko-KP'),
                                                     ('Asia/Seoul', 'ko-KR'),
                                                     ('Asia/Kuwait', 'ar-KW'),
                                                     ('America/Cayman', 'en-KY'),
                                                     ('Asia/Almaty', 'kk'),
                                                     ('Asia/Qyzylorda', 'kk'),
                                                     ('Asia/Qostanay', 'kk'),
                                                     ('Asia/Aqtobe', 'kk'),
                                                     ('Asia/Aqtau', 'kk'),
                                                     ('Asia/Atyrau', 'kk'),
                                                     ('Asia/Oral', 'kk'),
                                                     ('Asia/Vientiane', 'lo'),
                                                     ('Asia/Beirut', 'ar-LB'),
                                                     ('America/St_Lucia', 'en-LC'),
                                                     ('Europe/Vaduz', 'de-LI'),
                                                     ('Asia/Colombo', 'si'),
                                                     ('Africa/Monrovia', 'en-LR'),
                                                     ('Africa/Maseru', 'en-LS'),
                                                     ('Europe/Vilnius', 'lt'),
                                                     ('Europe/Luxembourg', 'lb'),
                                                     ('Europe/Riga', 'lv'),
                                                     ('Africa/Tripoli', 'ar-LY'),
                                                     ('Africa/Casablanca', 'ar-MA'),
                                                     ('Europe/Monaco', 'fr-MC'),
                                                     ('Europe/Chisinau', 'ro'),
                                                     ('Europe/Podgorica', 'sr'),
                                                     ('America/Marigot', 'fr'),
                                                     ('Indian/Antananarivo', 'fr-MG'),
                                                     ('Pacific/Majuro', 'mh'),
                                                     ('Pacific/Kwajalein', 'mh'),
                                                     ('Europe/Skopje', 'mk'),
                                                     ('Africa/Bamako', 'fr-ML'),
                                                     ('Asia/Yangon', 'my'),
                                                     ('Asia/Ulaanbaatar', 'mn'),
                                                     ('Asia/Hovd', 'mn'),
                                                     ('Asia/Choibalsan', 'mn'),
                                                     ('Asia/Macau', 'zh'),
                                                     ('Pacific/Saipan', 'fil'),
                                                     ('America/Martinique', 'fr-MQ'),
                                                     ('Africa/Nouakchott', 'ar-MR'),
                                                     ('America/Montserrat', 'en-MS'),
                                                     ('Europe/Malta', 'mt'),
                                                     ('Indian/Mauritius', 'en-MU'),
                                                     ('Indian/Maldives', 'dv'),
                                                     ('Africa/Blantyre', 'ny'),
                                                     ('America/Mexico_City', 'es-MX'),
                                                     ('America/Cancun', 'es-MX'),
                                                     ('America/Merida', 'es-MX'),
                                                     ('America/Monterrey', 'es-MX'),
                                                     ('America/Matamoros', 'es-MX'),
                                                     ('America/Mazatlan', 'es-MX'),
                                                     ('America/Chihuahua', 'es-MX'),
                                                     ('America/Ojinaga', 'es-MX'),
                                                     ('America/Hermosillo', 'es-MX'),
                                                     ('America/Tijuana', 'es-MX'),
                                                     ('America/Bahia_Banderas', 'es-MX'),
                                                     ('Asia/Kuala_Lumpur', 'ms-MY'),
                                                     ('Asia/Kuching', 'ms-MY'),
                                                     ('Africa/Maputo', 'pt-MZ'),
                                                     ('Africa/Windhoek', 'en-NA'),
                                                     ('Pacific/Noumea', 'fr-NC'),
                                                     ('Africa/Niamey', 'fr-NE'),
                                                     ('Pacific/Norfolk', 'en-NF'),
                                                     ('Africa/Lagos', 'en-NG'),
                                                     ('America/Managua', 'es-NI'),
                                                     ('Europe/Amsterdam', 'nl-NL'),
                                                     ('Europe/Oslo', 'no'),
                                                     ('Asia/Kathmandu', 'ne'),
                                                     ('Pacific/Nauru', 'na'),
                                                     ('Pacific/Niue', 'niu'),
                                                     ('Pacific/Auckland', 'en-NZ'),
                                                     ('Pacific/Chatham', 'en-NZ'),
                                                     ('Asia/Muscat', 'ar-OM'),
                                                     ('America/Panama', 'es-PA'),
                                                     ('America/Lima', 'es-PE'),
                                                     ('Pacific/Tahiti', 'fr-PF'),
                                                     ('Pacific/Marquesas', 'fr-PF'),
                                                     ('Pacific/Gambier', 'fr-PF'),
                                                     ('Pacific/Port_Moresby', 'en-PG'),
                                                     ('Pacific/Bougainville', 'en-PG'),
                                                     ('Asia/Manila', 'tl'),
                                                     ('Asia/Karachi', 'ur-PK'),
                                                     ('Europe/Warsaw', 'pl'),
                                                     ('America/Miquelon', 'fr-PM'),
                                                     ('Pacific/Pitcairn', 'en-PN'),
                                                     ('America/Puerto_Rico', 'en-PR'),
                                                     ('Asia/Gaza', 'ar-PS'),
                                                     ('Asia/Hebron', 'ar-PS'),
                                                     ('Europe/Lisbon', 'pt-PT'),
                                                     ('Atlantic/Madeira', 'pt-PT'),
                                                     ('Atlantic/Azores', 'pt-PT'),
                                                     ('Pacific/Palau', 'pau'),
                                                     ('America/Asuncion', 'es-PY'),
                                                     ('Asia/Qatar', 'ar-QA'),
                                                     ('Indian/Reunion', 'fr-RE'),
                                                     ('Europe/Bucharest', 'ro'),
                                                     ('Europe/Belgrade', 'sr'),
                                                     ('Europe/Kaliningrad', 'ru'),
                                                     ('Europe/Moscow', 'ru'),
                                                     ('Europe/Kirov', 'ru'),
                                                     ('Europe/Astrakhan', 'ru'),
                                                     ('Europe/Volgograd', 'ru'),
                                                     ('Europe/Saratov', 'ru'),
                                                     ('Europe/Ulyanovsk', 'ru'),
                                                     ('Europe/Samara', 'ru'),
                                                     ('Asia/Yekaterinburg', 'ru'),
                                                     ('Asia/Omsk', 'ru'),
                                                     ('Asia/Novosibirsk', 'ru'),
                                                     ('Asia/Barnaul', 'ru'),
                                                     ('Asia/Tomsk', 'ru'),
                                                     ('Asia/Novokuznetsk', 'ru'),
                                                     ('Asia/Krasnoyarsk', 'ru'),
                                                     ('Asia/Irkutsk', 'ru'),
                                                     ('Asia/Chita', 'ru'),
                                                     ('Asia/Yakutsk', 'ru'),
                                                     ('Asia/Khandyga', 'ru'),
                                                     ('Asia/Vladivostok', 'ru'),
                                                     ('Asia/Ust-Nera', 'ru'),
                                                     ('Asia/Magadan', 'ru'),
                                                     ('Asia/Sakhalin', 'ru'),
                                                     ('Asia/Srednekolymsk', 'ru'),
                                                     ('Asia/Kamchatka', 'ru'),
                                                     ('Asia/Anadyr', 'ru'),
                                                     ('Europe/Simferopol', 'uk'),
                                                     ('Europe/Kiev', 'uk'),
                                                     ('Europe/Uzhgorod', 'uk'),
                                                     ('Europe/Zaporozhye', 'uk'),
                                                     ('Africa/Kigali', 'rw'),
                                                     ('Asia/Riyadh', 'ar-SA'),
                                                     ('Pacific/Guadalcanal', 'en-SB'),
                                                     ('Indian/Mahe', 'en-SC'),
                                                     ('Africa/Khartoum', 'ar-SD'),
                                                     ('Europe/Stockholm', 'sv-SE'),
                                                     ('Asia/Singapore', 'cmn'),
                                                     ('Atlantic/St_Helena', 'en-SH'),
                                                     ('Europe/Ljubljana', 'sl'),
                                                     ('Arctic/Longyearbyen', 'no'),
                                                     ('Europe/Bratislava', 'sk'),
                                                     ('Africa/Freetown', 'en-SL'),
                                                     ('Europe/San_Marino', 'it-SM'),
                                                     ('Africa/Dakar', 'fr-SN'),
                                                     ('Africa/Mogadishu', 'so-SO'),
                                                     ('America/Paramaribo', 'nl-SR'),
                                                     ('Africa/Juba', 'en'),
                                                     ('Africa/Sao_Tome', 'pt-ST'),
                                                     ('America/El_Salvador', 'es-SV'),
                                                     ('America/Lower_Princes', 'nl'),
                                                     ('Asia/Damascus', 'ar-SY'),
                                                     ('Africa/Mbabane', 'en-SZ'),
                                                     ('America/Grand_Turk', 'en-TC'),
                                                     ('Africa/Ndjamena', 'fr-TD'),
                                                     ('Indian/Kerguelen', 'fr'),
                                                     ('Africa/Lome', 'fr-TG'),
                                                     ('Asia/Bangkok', 'th'),
                                                     ('Asia/Dushanbe', 'tg'),
                                                     ('Pacific/Fakaofo', 'tkl'),
                                                     ('Asia/Dili', 'tet'),
                                                     ('Asia/Ashgabat', 'tk'),
                                                     ('Africa/Tunis', 'ar-TN'),
                                                     ('Pacific/Tongatapu', 'to'),
                                                     ('Europe/Istanbul', 'tr-TR'),
                                                     ('America/Port_of_Spain', 'en-TT'),
                                                     ('Pacific/Funafuti', 'tvl'),
                                                     ('Asia/Taipei', 'zh-TW'),
                                                     ('Africa/Dar_es_Salaam', 'sw-TZ'),
                                                     ('Africa/Kampala', 'en-UG'),
                                                     ('Pacific/Midway', 'en-UM'),
                                                     ('Pacific/Wake', 'en-UM'),
                                                     ('America/New_York', 'en-US'),
                                                     ('America/Detroit', 'en-US'),
                                                     ('America/Kentucky/Louisville', 'en-US'),
                                                     ('America/Kentucky/Monticello', 'en-US'),
                                                     ('America/Indiana/Indianapolis', 'en-US'),
                                                     ('America/Indiana/Vincennes', 'en-US'),
                                                     ('America/Indiana/Winamac', 'en-US'),
                                                     ('America/Indiana/Marengo', 'en-US'),
                                                     ('America/Indiana/Petersburg', 'en-US'),
                                                     ('America/Indiana/Vevay', 'en-US'),
                                                     ('America/Chicago', 'en-US'),
                                                     ('America/Indiana/Tell_City', 'en-US'),
                                                     ('America/Indiana/Knox', 'en-US'),
                                                     ('America/Menominee', 'en-US'),
                                                     ('America/North_Dakota/Center', 'en-US'),
                                                     ('America/North_Dakota/New_Salem', 'en-US'),
                                                     ('America/North_Dakota/Beulah', 'en-US'),
                                                     ('America/Denver', 'en-US'),
                                                     ('America/Boise', 'en-US'),
                                                     ('America/Phoenix', 'en-US'),
                                                     ('America/Los_Angeles', 'en-US'),
                                                     ('America/Anchorage', 'en-US'),
                                                     ('America/Juneau', 'en-US'),
                                                     ('America/Sitka', 'en-US'),
                                                     ('America/Metlakatla', 'en-US'),
                                                     ('America/Yakutat', 'en-US'),
                                                     ('America/Nome', 'en-US'),
                                                     ('America/Adak', 'en-US'),
                                                     ('Pacific/Honolulu', 'en-US'),
                                                     ('America/Montevideo', 'es-UY'),
                                                     ('Asia/Samarkand', 'uz'),
                                                     ('Asia/Tashkent', 'uz'),
                                                     ('Europe/Vatican', 'la'),
                                                     ('America/St_Vincent', 'en-VC'),
                                                     ('America/Caracas', 'es-VE'),
                                                     ('America/Tortola', 'en-VG'),
                                                     ('America/St_Thomas', 'en-VI'),
                                                     ('Asia/Ho_Chi_Minh', 'vi'),
                                                     ('Pacific/Efate', 'bi'),
                                                     ('Pacific/Wallis', 'wls'),
                                                     ('Pacific/Apia', 'sm'),
                                                     ('Asia/Aden', 'ar-YE'),
                                                     ('Indian/Mayotte', 'fr-YT'),
                                                     ('Africa/Johannesburg', 'zu'),
                                                     ('Africa/Lusaka', 'en-ZM'),
                                                     ('Africa/Harare', 'en-ZW');

INSERT INTO public.languages(shortname, name) VALUES ('af', 'Afrikaans'),
                                                     ('ar', 'Arabic'),
                                                     ('ca', 'Catalan'),
                                                     ('cs', 'Czech'),
                                                     ('da', 'Danish'),
                                                     ('de', 'German'),
                                                     ('el', 'Greek'),
                                                     ('en-US', 'English'),
                                                     ('es-ES', 'Spanish'),
                                                     ('fi', 'Finnish'),
                                                     ('fr', 'French'),
                                                     ('he', 'Hebrew'),
                                                     ('hi', 'Hindi'),
                                                     ('hu', 'Hungarian'),
                                                     ('id', 'Indonesian'),
                                                     ('it', 'Italian'),
                                                     ('ja', 'Japanese'),
                                                     ('ko', 'Korean'),
                                                     ('ms', 'Malay'),
                                                     ('nl', 'Dutch'),
                                                     ('no', 'Norwegian'),
                                                     ('pl', 'Polish'),
                                                     ('pt-BR', 'Portuguese (Brazil)'),
                                                     ('pt-PT', 'Portuguese (Portugal)'),
                                                     ('ro', 'Romanian'),
                                                     ('ru', 'Russian'),
                                                     ('so', 'Somali'),
                                                     ('sr', 'Serbian'),
                                                     ('sv-SE', 'Swedish'),
                                                     ('tl', 'Tagalog'),
                                                     ('tr', 'Turkish'),
                                                     ('uk', 'Ukrainian'),
                                                     ('ur-PK', 'Urdu'),
                                                     ('vi', 'Vietnamese'),
                                                     ('zh-CN', 'Chinese');

INSERT INTO public.apiaccess(accessid, name) VALUES (-1, 'God'), (0, 'Owner'), (1, 'Developer'), (2, 'Super Patron'), (3, 'Friend'), (4, 'User');

INSERT INTO modes(modeid, name) VALUES(1, 'Normal'), (2, 'Group');