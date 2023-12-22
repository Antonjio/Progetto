-- Drop tables if they exist
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS game;
DROP TABLE IF EXISTS funko_pop;
DROP TABLE IF EXISTS fumetto;
DROP TABLE IF EXISTS cart;
DROP TABLE IF EXISTS orders;  -- Use a different name for the "order" table

-- Create tables
CREATE TABLE users (
    name         VARCHAR(50),
    lastname      VARCHAR(50),
    number       CHAR(10),
    country        VARCHAR(50),
    address    VARCHAR(100),
    password     VARCHAR(256) NOT NULL,
    birthdate DATE         NOT NULL,
    email        VARCHAR(255) PRIMARY KEY,
    username     VARCHAR(50)  UNIQUE
);

CREATE TABLE game (
    ean_game       VARCHAR(13) PRIMARY KEY,
    game_name        VARCHAR(50)  NOT NULL,
    game_price      NUMBER(5,2) NOT NULL,
    game_release DATE         NOT NULL,
    genre          VARCHAR(20)  NOT NULL,
    pegi         NUMBER(2)    NOT NULL,
    sh_name         VARCHAR(100) NOT NULL,
    image        VARCHAR(255) NOT NULL
);

CREATE TABLE funko_pop (
    funko_ean       VARCHAR(13) PRIMARY KEY,
    fun_name        VARCHAR(50)  NOT NULL,
    fun_price      NUMBER(5,2) NOT NULL,
    fun_release DATE         NOT NULL,
    height         NUMBER(5,2) NOT NULL,
    deptha      NUMBER(5,2) NOT NULL,
    width       NUMBER(5,2) NOT NULL,
    image        VARCHAR(255) NOT NULL,
    category       VARCHAR(30)  NOT NULL
);

CREATE TABLE fumetto (
    ean_comics             VARCHAR(13) PRIMARY KEY,
    comics_name        VARCHAR(50)                 NOT NULL,
    comics_price      NUMBER(5,2) NOT NULL,
    comics_release DATE                        NOT NULL,
    comics_type        VARCHAR(10)
        CHECK (comics_type IN ('manga', 'comics')) NOT NULL,
    pages              NUMBER(4) NOT NULL,
    author              CHAR(30)                    NOT NULL,
    image            VARCHAR(255)                NOT NULL,
    editor_name            VARCHAR(30)                 NOT NULL
);

CREATE TABLE cart (
    cart_id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_id VARCHAR(13),
    time    DATETIME DEFAULT CURRENT_TIMESTAMP,
    user    VARCHAR(255) NOT NULL,
    FOREIGN KEY (item_id) REFERENCES game (ean_game) ON DELETE CASCADE,
    FOREIGN KEY (item_id) REFERENCES funko_pop (funko_ean) ON DELETE CASCADE,
    FOREIGN KEY (user) REFERENCES users (email) ON DELETE CASCADE,
    FOREIGN KEY (item_id) REFERENCES fumetto (ean_comics) ON DELETE CASCADE
);
insert into fumetto values('9788828709619','Captain Marvel vol.1',14.99,'2016-04-09','comics',128,'Kelly Thompson','captainmarvel1.jpg','Panini');
insert into fumetto values('9781846533372','America Chavez vol.1',15.99,'2022-02-01','comics',120,'Kalinda Vazquez','americachavez1.jpg','Panini');
insert into fumetto values('9788891215659','Torcia Umana vol.1',20.99,'2015-12-11','comics',272,'Stan Lee','torciaumana1.jpg','Panini');
insert into fumetto VALUES('9788828704232','Black Widow vol.1',9.99,'2021-05-13','comics',128,'Kelly Thompson','Blackwidow1.jpg','Panini');
insert into fumetto values('9788828708223','Smascherato. Spider-Man vol.1',12.99,'2012-02-01','comics',160,'Stan Lee','spiderman1.jpg','Panini');
insert into fumetto values('9788891224835','Il mitico Thor vol.1',12.99,'2018-08-20','comics',368,'Stan Lee','thor1.jpg','Panini');
insert into fumetto values('9788891241535','Fantastici quattro vol.1',10.99,'2009-02-25','comics',232,'Stan Lee','fantastici1.jpg','Panini');
insert into fumetto values('9788828713661','She-Hulk vol.1',10.99,'2021-06-15','comics',120,'Stan Lee','she-hulk1.jpg','Panini');
insert into fumetto values('9788891236807','Hulk vol.1',13.99,'2017-10-01','comics',220,'Stan Lee','hulk1.jpg','Panini');
insert into fumetto values('9781302945404','Captain America vol.1',13.99,'2015-05-12','comics',176,'Stan Lee','capitan america1.jpg','Panini');
insert into fumetto values('9788891276575','Iron man vol.1',12.59,'2022-04-10','comics',128,'Stan Lee','ironman1.jpg','Panini');
insert into fumetto values('9788891296535','Hunter x Hunter vol1',4.99,'2013-08-20','manga',202,'Yoshihiro Togashi','HxH1.jpg','Mondadori');
insert into fumetto values('9788891293206','Attack on Titan vol.1',5.99,'2020-03-20','manga',200,'Hajime Isayama','AoT1.jpg','Feltrinelli');
insert into fumetto values('9788864201795','One Piece  vol.1',5.49,'2001-07-01','manga',208,'Eiichiro Oda','OP1.jpg','Panini');
insert into fumetto values('9788828742470','Naruto vol.1',6.32,'2022-02-20','manga',172,'Masashi Kishimoto','Naruto1.jpg','Mondadori');
insert into fumetto values('9788828722762','Berserk Deluxe vol.1',57.99,'2022-11-17','manga',700,'Kentaro Miura','Berserk1.jpg','Mondadori');
insert into fumetto values('9788891299390','Blue lock vol.1',7.99,'2021-09-17','manga',208,'Muneyuki Kaneshiro','BL1.jpg','Mondadori');
insert into fumetto values('9788822613158','Demon slayer vol.1',6.90,'2019-04-17','manga',700,'Koyoharu Gotouge','DS1.jpg','Mondadori');
insert into fumetto values('9788834904404','Zombie 100 vol.1',5.90,'2021-04-21','manga',160,'Haro Aso','zombie1001.jpg','Mondadori');
insert into fumetto values('9781974709939','Chainsaw Man vol.1',9.90,'2020-10-11','manga',192,'Tatsuki Fujimoto','chainsawman1.jpg','Feltrinelli');
insert into fumetto values('9788828763260','Spy x Family vol.1',4.90,'2021-10-21','manga',216,'Tatsuya Endo','spyxfamily1.jpg','Mondadori');
insert into fumetto values('9788828754220','Jujutsu Kaisen vol.1',5.20,'2023-06-29','manga',208,'Gege Akutami','jjk1.jpg','Mondadori');


insert into funko_pop values ('889698592888','Batman',9.99,'2020-02-01',9.5,6.4,6.4,'B.jpg','film');
insert into funko_pop values ('889698627818','Iron Man - Mystic Armor',9.99,'2016-05-01',9.5,6.4,6.4,'IM - Mystic Armor.jpg','film');
insert into funko_pop values ('889698656528','Harry Potter',9.99,'2018-03-31',9.5,6.4,6.4,'HP.jpg','film');
insert into funko_pop values ('889698675345','Star Wars - Darth Vader',9.29,'2011-04-15',9.5,6.4,6.4,'SW - Darth.jpg','film');
insert into funko_pop values ('889698676083','Spider-Man - Integrated Suit',9.39,'2018-02-28',9.5,6.4,6.4,'SM - Integrated.jpg','film');
insert into funko_pop values ('889698623919','Stranger Things - Eleven',9.49,'2021-07-16',9.5,6.4,6.4,'ST - Eleven.jpg','serietv');
insert into funko_pop values ('889698122153','Game of Thrones - Jon Snow',9.49,'2022-01-11',9.5,6.4,6.4,'GOT - Jon.jpg','serietv');
insert into funko_pop values ('889698349062','The Office - Dwight Schrute',9.49,'2017-07-26',9.5,6.4,6.4,'TO - Dwight.jpg','serietv');
insert into funko_pop values ('830395030890','Game of Thrones - Arya Stark',9.49,'2018-11-18',9.5,6.4,6.4,'GOT - Arya.jpg','serietv');
insert into funko_pop values ('889698110709','Walking Dead - Negan',9.49,'2021-10-15',9.5,6.4,6.4,'WD - Negan.jpg','game');
insert into funko_pop values ('889698564496','Diablo II - Dark Wanderer',22.49,'2022-05-05',9.5,6.4,6.4,'D2 - Dark.jpg','game');
insert into funko_pop values ('889698504027','Pokemon - Squirtle',24.99,'2022-12-03',9.5,6.4,6.4,'P - Squirtle.jpg','game');
insert into funko_pop values ('889698615495','Overwatch 2 - Junker Queen',17.90,'2023-05-21',9.5,6.4,6.4,'O - Junker.jpg','game');
insert into funko_pop values ('889698724982','Diablo IV - Lilith',29.90,'2023-10-07',9.5,6.4,6.4,'D4 - Lilith.jpg','game');
insert into funko_pop values ('889698433433','Crash Bandicoot',16.90,'2020-10-07',9.5,6.4,6.4,'CB - Crash.jpg','game');
insert into funko_pop values ('889698537865','Mortal Kombat - Mileena',31.50,'2021-05-07',9.5,6.4,6.4,'MK - Mileena.jpg','game');
insert into funko_pop values ('889698639989','Apex Legends - Crypto',17.90,'2021-11-27',9.5,6.4,6.4,'AL - Crypto.jpg','game');
insert into funko_pop values ('889698114127','Dishonored 2 - Outsider',15.90,'2016-06-12',9.5,6.4,6.4,'D2 - Outsider.jpg','game');
insert into funko_pop values ('830395033747','World of Warcraft - Illidan',20.90,'2014-01-22',9.5,6.4,6.4,'WOW - Illidan.jpg','game');


insert into game values('5030945124276','Fifa 23',39.99,'2022-09-30','sport',3,'Electronic Arts','Fifa 23.jpeg');
insert into game values('5030941123778','Fifa 22',19.99,'2021-09-30','sport',3,'Electronic Arts','Fifa 22.jpeg');
insert into game values('5056208822284','F1 Manager 2023',39.99,'2023-09-10','sport',3,'Electronic Arts','f1manager.jpeg');
insert into game values('0811949035486','Cuphead',29.99,'2022-06-10','azione',3,'Studio MDHR','cuphead.jpeg');
insert into game values('5030935121933','Fifa 19',9.99,'2018-09-30','sport',3,'Electronic Arts','Fifa 19.jpeg');
insert into game values('5030949124944','F1 22',15.99,'2022-06-16','sport',3,'Electronic Arts','F1 22.jpg');
insert into game values('5030940125162','F1 23',39.99,'2023-06-16','sport',3,'Electronic Arts','F1 23.jpg');
insert into game values('5026555432641','Nba 2k23',30.99,'2022-09-09','sport',3,'Electronic Arts','Nba 2k23.jpg');
insert into game values('711719765790','Gran Turismo 7',30.99,'2022-03-04','sport',3,'Sony Interactive Entertainment','Gran Turismo 7.jpg');
insert into game values('3391892017267','Elden Ring',49.99,'2022-02-25','azione',16,'FromSoftware','Elden Ring.jpg');
insert into game values('5026555430838','Grand Theft Auto the trilogy',29.99,'2021-11-11','azione',16,'Rockstar Games','Grand Theft Auto the trilogy.jpg');
insert into game values('711719436775','Bloodborne',44.99,'2018-07-18','azione',16,'FromSoftware','Bloodborne.jpg');
insert into game values('711719995791','God of War III: Remastered',19.99,'2019-06-28','azione',16,'Sony Int. Ent.','God of War III Remastered.jpg');
insert into game values('5026555416986','Grand Theft Auto V',19.99,'2013-09-17','azione',18,'Rockstar Games','Gta V.jpg');
insert into game values('5026555423083','Red Dead Redemption II',59.99,'2018-10-26','azione',18,'Rockstar Games','Red Dead Redemption II.jpg');
insert into game values('5051891160569','Hitman 2',19.99,'2018-11-13','azione',18,'Warner Bros. Entertainment','Hitman 2.jpg');
insert into game values('5021290095083','Final Fantasy VII - Reunion',29.99,'2022-12-13','avventura',16,'Square Enix','Final Fantasy VII - Reunion.jpg');
insert into game values('3307216170808','Far Cry 6',49.99,'2021-10-07','avventura',16,'Ubisoft','Far Cry 6.jpg');
insert into game values('0711719405597','The Last of Us I remastered',59.99,'2022-09-02','avventura',16,'Naughty Dog','The Last of Us Remastered.jpg');
insert into game values('711719330301','The Last of Us II',34.99,'2020-06-19','avventura',16,'Naughty Dog','The Last of Us II.jpg');
insert into game values('3307215977415','Assassin s Creed The Ezio Collection',14.99,'2016-11-17','avventura',16,'Ubisoft','Assassin s Creed The Ezio Collection.jpg');
insert into game values('3307216257646','Assassin''s Creed Mirage',50.99,'2023-10-05','avventura',16,'Ubisoft','Assassin s Creed Mirage.jpg');
insert into game values('811949035608','Stray',30.99,'2022-11-08','avventura',12,'Annapurna','Stray.jpg');