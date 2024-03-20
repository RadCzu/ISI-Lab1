import sqlite3

con = sqlite3.connect("uczelnia.db")

cur = con.cursor()

# cur.execute("CREATE TABLE uczelnia(id_uczelni INT NOT NULL, nazwa_uczelni VARCHAR(50) NOT NULL, PRIMARY KEY (id_uczelni));")
# cur.execute("CREATE TABLE wydzial(id_wydzialu INT NOT NULL, nazwa VARCHAR(40) NOT NULL, id_uczelni INT NOT NULL, PRIMARY KEY (id_wydzialu), FOREIGN KEY (id_uczelni) REFERENCES uczelnia(id_uczelni));")
# cur.execute("CREATE TABLE grupa_studencka(id_grupy INT NOT NULL,nazwa VARCHAR(40) NOT NULL,id_wydzialu INT NOT NULL,PRIMARY KEY (id_grupy),FOREIGN KEY (id_wydzialu) REFERENCES wydzial(id_wydzialu));")
# cur.execute("CREATE TABLE przedmiot (id_przediotu INT NOT NULL, nazwa VARCHAR(40) NOT NULL, PRIMARY KEY (id_przediotu));")
# cur.execute("CREATE TABLE student (id_studenta INT NOT NULL, imie VARCHAR(40) NOT NULL, nazwisko VARCHAR(40) NOT NULL, id_grupy INT NOT NULL, PRIMARY KEY (id_studenta), FOREIGN KEY (id_grupy) REFERENCES grupa_studencka(id_grupy));")
# cur.execute("CREATE TABLE ocena (wartosc FLOAT NOT NULL, id_oceny INT NOT NULL, id_przediotu INT NOT NULL, id_studenta INT NOT NULL, PRIMARY KEY (id_oceny, id_przediotu), FOREIGN KEY (id_przediotu) REFERENCES przedmiot(id_przediotu), FOREIGN KEY (id_studenta) REFERENCES student(id_studenta));")
# cur.execute("CREATE TABLE przedmioty_grupy (id_przediotu INT NOT NULL, id_grupy INT NOT NULL, PRIMARY KEY (id_przediotu, id_grupy), FOREIGN KEY (id_przediotu) REFERENCES przedmiot(id_przediotu), FOREIGN KEY (id_grupy) REFERENCES grupa_studencka(id_grupy));")
# cur.execute("CREATE TABLE wykladowca (id_wykladowcy INT NOT NULL, imie VARCHAR(40) NOT NULL, nazwisko VARCHAR(40) NOT NULL, id_przediotu INT NOT NULL, id_wydzialu INT NOT NULL, PRIMARY KEY (id_wykladowcy), FOREIGN KEY (id_przediotu) REFERENCES przedmiot(id_przediotu), FOREIGN KEY (id_wydzialu) REFERENCES wydzial(id_wydzialu));")

# cur.execute("INSERT INTO UCZELNIA VALUES ('1', 'AMW')")

# cur.execute("INSERT INTO WYDZIAL VALUES ('1', 'WME', '1')")
# cur.execute("INSERT INTO WYDZIAL VALUES ('2', 'WDiOM', '1')")

res = cur.execute("SELECT * FROM student")
students = res.fetchall()


def display_student(student):
    print(f"ID: {student[0]}")
    print(f"Imie: {student[1]}")
    print(f"Nazwisko: {student[2]}")
    print(f"ID_Grupy: {student[3]}")
    print(f"\n")


print("Studenci:")
for student in students:
    display_student(student)

res = cur.execute("SELECT * FROM student WHERE id_grupy=1")
students = res.fetchall()

print("Studenci grupy 1:")
for student in students:
    display_student(student)

    res = cur.execute("SELECT DISTINCT * FROM student AS S LEFT JOIN ocena AS O ON O.id_studenta=S.id_studenta WHERE O.wartosc > 3.5" )
    students = res.fetchall()

    print("Studenci z ocenami 4 lub większymi:")
    for student in students:
        display_student(student)