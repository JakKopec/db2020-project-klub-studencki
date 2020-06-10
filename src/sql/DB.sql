#drop database dbprojekt;
/*
SET SQL_MODE='ALLOW_INVALID_DATES';
create database dbprojekt;
use dbprojekt;
#---------------TWORZENIE TABEL-------------------------
CREATE TABLE Sala 
(
	sala_id INT auto_increment,
    adres VARCHAR(40) not null,
    budynek VARCHAR(3) not null,
	nr_sali INT not null,
    primary key(sala_id)
);
CREATE TABLE Spotkanie
(
	spotkanie_id int auto_increment,
    sala_id INT not null,
	stowarzyszenie_id INT not null,
    data_rozpoczecia timestamp not null,
    data_zakonczenia timestamp not null,
    temat_spotkania VARCHAR(50),
    primary key(spotkanie_id)
);
CREATE TABLE Stowarzyszenie
(    
	stowarzyszenie_id INT auto_increment,
    nazwa VARCHAR(50) unique not null,
    haslo varchar(10) not null,
    przewodniczacy_id int,
    primary key(stowarzyszenie_id)
);

CREATE TABLE Czlonek
(    
	indeks INT(6) auto_increment,
    imie VARCHAR(30) not null,
    nazwisko VARCHAR(30) not null,
    wydzial VARCHAR(50) not null,
    stowarzyszenie_id INT,   
    telefon int not null unique,
    mail varchar(50) not null unique,
    primary key(indeks)
);



#------------------DODAWANIE KLUCZY OBCYCH---------------------

alter table Spotkanie
add FOREIGN KEY(sala_id) REFERENCES Sala(sala_id),
add FOREIGN KEY(stowarzyszenie_id) REFERENCES Stowarzyszenie(stowarzyszenie_id);

alter table Stowarzyszenie
add FOREIGN KEY(przewodniczacy_id) REFERENCES Czlonek(indeks);


alter table Czlonek
add FOREIGN KEY(stowarzyszenie_id) REFERENCES Stowarzyszenie(stowarzyszenie_id);

#---------------------------------------------------------------

insert into Sala(adres,budynek,nr_sali) values("Rostafinskiego 666","A-2",105);
insert into Sala(adres,budynek,nr_sali) values("Rostafinskiego 666","A-2",122);
insert into Sala(adres,budynek,nr_sali) values("Mickiewicza 44","A-4",13);
insert into Sala(adres,budynek,nr_sali) values("Słowackiego 21","A-3",4);
insert into Sala(adres,budynek,nr_sali) values("Jana Pawła II 37","A-1",90);
select * from Sala;

#NAJPIERW WPROWADZIC CZLOWIEKA DO BAZY, POTEM TWORZENIE STOWARZYSZENIA, POTEM NADANIE STOWARZYSZENIE_id
insert into Czlonek(imie,nazwisko,wydzial,telefon,mail) values("Dawid","Pasieka","WMS",105105997,"DawidPasieka@gmail.com");
insert into Stowarzyszenie(nazwa,haslo,przewodniczacy_id) values ("Miłośnicy Fizyki","fizyka",1);
update Czlonek set stowarzyszenie_id=1 where indeks=1;
insert into Czlonek(imie,nazwisko,wydzial,telefon,mail,stowarzyszenie_id) values("Jakub","Trapczak","WFiIS",112999998,"JakubTrapczak@gmail.com",1);
select * from Stowarzyszenie;

insert into Czlonek(imie,nazwisko,wydzial,telefon,mail) values("Geralt","Riv","WFiIS",11231298,"Gerwald@gmail.com");
insert into Stowarzyszenie(nazwa,haslo,przewodniczacy_id) values ("Miłośnicy RPG","rpg",3);
update Czlonek set stowarzyszenie_id=2 where indeks=3;
insert into Czlonek(imie,nazwisko,wydzial,telefon,mail,stowarzyszenie_id) values("Zenon","Bury","WIMiIP",123456789,"Bezimienny@gmail.com",2);
select * from Stowarzyszenie;
select * from Czlonek;

#LEPSZA WERSJA - DODANIE STWARZYSZENIA BEZ ID,DODANIE CZLONKOW,NADANIE STOWARZYSZENIU PRZEWODNICZACEGO
insert into Stowarzyszenie(nazwa,haslo) values ("Novigrad","novigrad");
insert into Czlonek(imie,nazwisko,wydzial,telefon,mail,stowarzyszenie_id) values("Sigismund","Djikstra","WIMiIP",000456789,"Sigi@gmail.com",3);
insert into Czlonek(imie,nazwisko,wydzial,telefon,mail,stowarzyszenie_id) values("Triss","Merigold","WIMiC",11231000,"Triss@gmail.com",3);
insert into Czlonek(imie,nazwisko,wydzial,telefon,mail,stowarzyszenie_id) values("Jaskier","Jaskier","WIMiC",11231001,"Jaskier@gmail.com",3);
insert into Czlonek(imie,nazwisko,wydzial,telefon,mail,stowarzyszenie_id) values("Ulu","Mulu","WIMiC",11231002,"Ulumulu@gmail.com",3);
insert into Czlonek(imie,nazwisko,wydzial,telefon,mail,stowarzyszenie_id) values("Randy","Lahey","WIMiC",11231004,"Randylahey@gmail.com",3);
insert into Czlonek(imie,nazwisko,wydzial,telefon,mail,stowarzyszenie_id) values("Cory","Trevor","WIMiIP",11231003,"CoryTrevor@gmail.com",3);
update Stowarzyszenie set przewodniczacy_id=5 where stowarzyszenie_id=3;
select * from Czlonek;


insert into Spotkanie(data_rozpoczecia,data_zakonczenia,temat_spotkania,sala_id,stowarzyszenie_id) values('2020-07-07 10:00:00','2020-07-07 14:00:00',"Pierwsze spotkanie",1,1);
insert into Spotkanie(data_rozpoczecia,data_zakonczenia,temat_spotkania,sala_id,stowarzyszenie_id) values('2020-07-14 10:00:00','2020-07-14 14:00:00',"Drugie spotkanie",2,1);
insert into Spotkanie(data_rozpoczecia,data_zakonczenia,temat_spotkania,sala_id,stowarzyszenie_id) values('2020-07-21 10:00:00','2020-07-21 14:00:00',"Robienie fajnych rzeczy",1,1);

insert into Spotkanie(data_rozpoczecia,data_zakonczenia,temat_spotkania,sala_id,stowarzyszenie_id) values('2020-07-07 7:00:00','2020-07-07 14:00:00',"Pierwsze spotkanie",3,2);
insert into Spotkanie(data_rozpoczecia,data_zakonczenia,temat_spotkania,sala_id,stowarzyszenie_id) values('2020-07-10 8:30:00','2020-07-10 10:00:00',"Pierwsze spotkanie",1,2);
insert into Spotkanie(data_rozpoczecia,data_zakonczenia,temat_spotkania,sala_id,stowarzyszenie_id) values('2020-07-12 8:40:00','2020-07-12 12:00:00',"Pierwsze spotkanie",1,2);
*/


select * from Stowarzyszenie;








