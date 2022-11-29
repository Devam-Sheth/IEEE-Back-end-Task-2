CREATE TABLE `books` (
  `Id` int DEFAULT NULL,
  `Barcode` varchar(20) DEFAULT NULL,
  `Title` varchar(20) DEFAULT NULL,
  `Author` varchar(20) DEFAULT NULL,
  `Category` varchar(20) DEFAULT NULL,
  `Pyear` int DEFAULT NULL,
  `Rack` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

insert into books(Id,Barcode,Title,Author,Category,Pyear,Rack) values(101, 'A1', 'BBB01' , 'Devam Sheth' ,'CS', 2017,1),(102, 'A2', 'BBB02' , 'E BALA' ,'CS', 2018,1),(103, 'A3', 'BBB03' , 'Devam Sheth' ,'CS', 2019,1),(104, 'B1', 'BBB04' , 'AA' ,'Adventure', 2005,2),(105, 'P1', 'BBB05' , 'AA' ,'Adventure', 2006,2),(106, 'A6', 'BBB06' , 'AB' ,'Politics', 1980,3),(107, 'A7', 'BBB07' , 'AC' ,'War', 1943,4),(108, 'A8', 'BBB08' , 'AD' ,'War', 1946,4),(109, 'Tintin in Tibet', 'BBB09' , 'AE' ,'Comic', 1912,5),(110, 'Tintin in America', 'BBB10' , 'AE' ,'Comic', 1913,5),(111, 'A1', 'BBB11' , 'Devam Sheth' ,'CS', 2017,1)