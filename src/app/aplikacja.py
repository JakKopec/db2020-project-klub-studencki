import sys;
# from nazwa_pliku import * #importowanie wszystkoch funkcji z pliku 
#--------------------------WYKORZYSTYWANE FUNKCJE-----------------------------------------#

#ZARZADZANIE CZLONKAMI
def zarz_czlonkami():
	print("\nMENU CZLONKOW");
	print("1.Dodaj czlonka do bazy");
	print("2.Usun czlonka z bazy");
	print("3.Edytuj dane istniejacego czlonka");
	print("4.Powrot do glownego menu")
	decyzja = int(input("Wybierz co chcesz zrobic\n"));

	if decyzja == 4 :
		glowne_menu();
#ZARZADZANIE STOWARZYSZENIEM
def zarz_stowarzyszenie():
	print("\nMENU STOWARZYSZEN");
	print("1.Dodaj nowe stowarzyszenie");
	print("2.Usun istniejace stowarzyszenie");
	print("3.Edytuj istniejace stowarzyszenie");
	print("4.Dodaj czlonka do stowarzyszenia");
	print("5.Usun czlonka z stowarzyszenia");
	print("6.Powrot do glownego menu\n")
	decyzja = int(input("Wybierz co chcesz zrobic\n"));

	if decyzja == 6 :
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
	else:
		print("Podaj poprawna opcje\n");
		glowne_menu();			

#--------------------GLOWNA CZESC PROGRAMU-----------------------------------
glowne_menu();
