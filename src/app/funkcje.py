import pymysql;

#WORK IN PROGRESS , dodac przyjmowane argumenty funkcji
def wypisywanie_z_bazy(nazwa_tabeli):
	print("1.Czlonkowie\n");
	print("2.Stowarzyszenia\n");
	print("3.Spotkania\n");
	print("4.Sale\n");
	decyzja = int(input("Z ktorej bazy chcesz wypisac dane?:\n"));
	connection = pymysql.connect(host='localhost',
										user='root',
										password='',
										db='dbprojekt',
										charset='utf8mb4',
										cursorclass=pymysql.cursors.SSDictCursor);#kursor bez bufora, wykorzystywany ze wzgledu na slabe dzialanie serwera (sugestia z dokumentacji technicznej)
	try:
		with connection.cursor() as cursor:
			if decyzja == 1
				sql = "SELECT * FROM `Czlonek`";
			elif decyzja == 2
				sql = "SELECT * FROM `Stowarzyszenie`";
			elif decyzja == 3
				sql = "SELECT * FROM `Spotkanie`";
			elif decyzja == 4
				sql = "SELECT * FROM `Sala`";
			cursor.execute(sql);
			result=cursor.fetchall();
			print(result);
	finally:
		connection.close();

#WORK IN PROGRESS Dodac obsluge numeru telefonu
def dodawanie_do_bazy(a,b,c,e):
	connection = pymysql.connect(host='localhost',
										user='root',
										password='',
										db='dbprojekt',
										charset='utf8mb4',
										cursorclass=pymysql.cursors.SSDictCursor);
	try:
		with connection.cursor() as cursor:
			sql="INSERT INTO `Czlonek` (`imie`,`nazwisko`,`wydzial`,`telefon`,`mail`) VALUES (%s,%s,%s,12554,%s)";
			cursor.execute(sql,(a,b,c,e));
		connection.commit()			
	finally:
		connection.close();
#mozna pomyslec o dodaniu uprzednio selecta po wybraniu opcji usuniecia
#nie sprawdzalem czy to dziala -zostawiam to sobie na jutro
def usuwanie_czlonka(a):
	print("\nUSUWANIE CZLONKA\n");
	connection = pymysql.connect(host='localhost',
										user='root',
										password='',
										db='dbprojekt',
										charset='utf8mb4',
										cursorclass=pymysql.cursors.SSDictCursor);
	try:
		with connection.cursor() as cursor:
			sql="SET FOREIGN_KEY_CHECKS=0";
			cursor.execute(sql,0);
			sql="UPDATE `Stowarzyszenie` SET (`przewodziczacy_id`=0) WHERE (`przewodziczacy_id`=%d)";
			cursor.execute(sql,0);
			sql="DELETE FROM `Czlonek` WHERE (`indeks`=%d)";
			cursor.execute(sql,0);
			sql="SET FOREIGN_KEY_CHECKS=1";
			cursor.execute(sql,0);
		connection.commit()			
	finally:
		connection.close();