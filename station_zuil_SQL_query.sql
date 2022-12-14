--Query
-------------------------------------------------------------------------------------------------------------------------------------
drop table if exists bericht cascade;
create table bericht (
    bericht_id              bigserial     primary key,
    naam        	        varchar       ,
	bericht      	        varchar       ,
	station     	        varchar       ,
    datumtijd_bericht       timestamp     ,
    goedkeuring         	integer       default 0,
    datumtijd_beoordeling   timestamp     ,
    mod_id                  integer     ,
    station_stad  	        varchar       
);


drop table if exists moderatie cascade;
create table moderatie (
    mod_id               	bigserial 	primary key,
	naam_mod     	        varchar   ,   
	email	                varchar   
);


drop table if exists station_service cascade;
create table station_service (
    station_stad  	        varchar   	primary key,
    land                	varchar   not null,
	ov_fiets                BOOLEAN   not null,
	lift         	        BOOLEAN   not null,
	wc  	                BOOLEAN   not null,
    laaden_lossen           BOOLEAN   not null
);


alter table bericht add constraint link1 
foreign key (mod_id) 
references moderatie (mod_id);

alter table bericht add constraint link2
foreign key (station_stad) 
references station_service (station_stad);

--inserts
-------------------------------------------------------------------------------------------------------------------------------------

--insert moderators(niet via python interface te doen)
insert into moderatie (naam_mod, email) values ('admin', 'marnixjahendriks@gmail.com');
insert into moderatie (naam_mod, email) values ('Marnix', 'marnix@gmail.com');
insert into moderatie (naam_mod, email) values ('NS_moderator', 'ns@gmail.com');



INSERT INTO station_service (
    station_stad, land, ov_fiets, lift, wc, laaden_lossen)
VALUES
    ('Arnhem', 'NL', true, false, true, false),
    ('Almere', 'NL', false, true, false, true),
    ('Amersfoort', 'NL', true, false, true, false),
    ('Almelo', 'NL', false, true, false, true),
    ('Alkmaar', 'NL', true, false, true, false),
    ('Apeldoorn', 'NL', false, true, false, true),
    ('Assen', 'NL', true, false, true, false),
    ('Amsterdam', 'NL', false, true, false, true),
    ('Boxtel', 'NL', true, false, true, false),
    ('Breda', 'NL', false, true, false, true),
    ('Dordrecht', 'NL', true, false, true, false),
    ('Delft', 'NL', false, true, false, true),
    ('Deventer', 'NL', true, false, true, false),
    ('Enschede', 'NL', false, true, false, true),
    ('Gouda', 'NL', true, false, true, false),
    ('Groningen', 'NL', false, true, false, true),
    ('Den Haag', 'NL', true, false, true, false),
    ('Hengelo', 'NL', false, true, false, true),
    ('Haarlem', 'NL', true, false, true, false),
    ('Helmond', 'NL', false, true, false, true),
    ('Hoorn', 'NL', true, false, true, false),
    ('Heerlen', 'NL', false, true, false, true),
    ('Den Bosch', 'NL', true, false, true, false),
    ('Hilversum', 'NL', false, true, false, true),
    ('Leiden', 'NL', true, false, true, false),
    ('Lelystad', 'NL', false, true, false, true),
    ('Leeuwarden', 'NL', true, false, true, false),
    ('Maastricht', 'NL', false, true, false, true),
    ('Nijmegen', 'NL', true, false, true, false),
    ('Oss', 'NL', false, true, false, true),
    ('Roermond', 'NL', true, false, true, false),
    ('Roosendaal', 'NL', false, true, false, true),
    ('Sittard', 'NL', true, false, true, false),
    ('Tilburg', 'NL', false, true, false, true),
    ('Utrecht', 'NL', true, false, true, false),
    ('Venlo', 'NL', false, true, false, true),
    ('Vlissingen', 'NL', true, false, true, false),
    ('Zaandam', 'NL', false, true, false, true),
    ('Zwolle', 'NL', true, false, true, false),
    ('Zutphen', 'NL', false, true, false, true);








--Om te testen
-------------------------------------------------------------------------------------------------------------------------------------

--alles:
--SELECT *
--FROM moderatie, bericht, station_service

--meest recente 5 berichten:
--SELECT naam, bericht
--FROM bericht
--ORDER BY datumtijd_bericht DESC
--LIMIT 5;
