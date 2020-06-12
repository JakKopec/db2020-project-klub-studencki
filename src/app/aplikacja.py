import sys;
import funkcje;
import sys;
import smtplib;
from smtplib import SMTP;

global server;
# from nazwa_pliku import * #importowanie wszystkoch funkcji z pliku 
#--------------------------WYKORZYSTYWANE FUNKCJE-----------------------------------------#

#ZARZADZANIE CZLONKAMI
def zarz_czlonkami():
	print("\nMENU CZLONKOW");
	print("1.Dodaj czlonka do bazy");
	print("2.Usun czlonka z bazy");
	print("3.Edytuj dane istniejacego czlonka");
	print("4.Wypisz wszystkich czlonkow z bazy");
	print("5.Powrot do glownego menu");
	decyzja = int(input("Wybierz co chcesz zrobic\n"));

	if decyzja ==1:
		imie = raw_input("Wprowadz imie:\n");
		nazwisko = raw_input("Wprowadz nazwisko:\n");
		wydzial = raw_input("Wprowadz wydzial:\n");
		email = raw_input("Wprowadz email:\n");
		funkcje.dodawanie_do_bazy(imie,nazwisko,wydzial,email);
		#funkcje.dodawanie_do_bazy('Adam','Malysz','EAIIB','Suhar@mail.com');
	elif decyzja ==2:
		czlonek_id = raw_input("Podaj id czlonka ktorego chcesz usunac\n");
		funkcje.usuwanie_czlonka(czlonek_id);
	elif decyzja == 4:
		funkcje.wypisywanie_z_bazy("Yep");
	elif decyzja == 5 :
		glowne_menu();
#ZARZADZANIE STOWARZYSZENIEM
def zarz_stowarzyszenie():
	print("\nMENU STOWARZYSZEN");
	print("1.Dodaj nowe stowarzyszenie");
	print("2.Usun istniejace stowarzyszenie");
	print("3.Edytuj istniejace stowarzyszenie");
	print("4.Dodaj czlonka do stowarzyszenia");
	print("5.Usun czlonka z stowarzyszenia");
	print("6.Wypisz wsystkich czlonkow wybranego stowarzyszenia");
	print("7.Wypisz wszystkie spotkania wybranego stowarzyszenia");
	print("8.Powrot do glownego menu\n")
	decyzja = int(input("Wybierz co chcesz zrobic\n"));

	if decyzja == 8 :
		glowne_menu();


#ZARZADZANIE SPOTKANIEM
def zarz_spotkanie():
	print("\nMENU SPOTKAN");
	print("1.Stworz spotkanie");
	print("2.Edytuj istniejace spotkanie");
	print("3.Usun spotkanie");
	print("4.Powrot do glownego menu")
	decyzja = int(input("Wybierz co chcesz zrobic\n"));

	if decyzja == 4 :
		glowne_menu();

#WYSWIETLENIE GLOWNEGO MENU
def glowne_menu():
	print("\nMENU GLOWNE");
	print("1.Zarzadzanie czlonkami");
	print("2.Zarzadzanie stowarzyszeniami");
	print("3.Zarzadzanie spotkaniami");
	print("4.Zamknij program");
	decyzja = int(input("Wybierz co chcesz zrobic\n"));

	if decyzja == 1:
		zarz_czlonkami();
	elif decyzja == 2:
		zarz_stowarzyszenie();
	elif decyzja == 3:
		zarz_spotkanie();
	elif decyzja == 4:
		sys.exit();
	elif decyzja == 5:
		mail();
	else:
		print("Podaj poprawna opcje\n");
		glowne_menu();			

"""
def mail():
	print("\n\nMAIL\n\n");
	#fromaddr = "BD2020JkBk@gmail.com"
	#toaddr = "Lasiuk883@gmail.com"
    #msg['from']= fromaddr
    #msg['to']=toadrr
    #msg['subject']= "Python email"


    #from email.MIMEMultipart import MIMEMultipart;
    #from email.MIMEText import MIMEText;
    server = smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo();
	server.starttls();
	server.ehlo();
	server.login("BD2020JkBk@gmail.com","gXPID9HNwdhgnX6t");
"""


#--------------------GLOWNA CZESC PROGRAMU-----------------------------------
#funkcje.wypisywanie_z_bazy();
glowne_menu();

