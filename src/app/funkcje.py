import pymysql;

#WORK IN PROGRESS , dodac przyjmowane argumenty funkcji
def wypisywanie_z_bazy(nazwa_tabeli): 
	connection = pymysql.connect(host='localhost',
										user='root',
										password='',
										db='dbprojekt',
										charset='utf8mb4',
										cursorclass=pymysql.cursors.SSDictCursor);#kursor bez bufora, wykorzystywany ze wzgledu na slabe dzialanie serwera (sugestia z dokumentacji technicznej)
	try:
		with connection.cursor() as cursor:
			sql = "SELECT * FROM `Czlonek`";
			cursor.execute(sql);
			result=cursor.fetchall();
			print(result);
	finally:
		connection.close();

#WORK IN PROGRESS Dodać obsluge numeru telefonu
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