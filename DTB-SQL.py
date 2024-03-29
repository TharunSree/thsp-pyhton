import random as rand
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="login"
)

mycursor = mydb.cursor()


def crt():
    mycursor.execute("SELECT id FROM info")

    myresult = mycursor.fetchall()
    dtr = myresult[0]
    ids = rand.randint(1000, 9999)
    if dtr[0] == ids:
        ids = rand.randint(1000, 9999)
    name = input('Enter Full Name : ')
    dob = input('Enter DOB (ccyy-mm-dd) : ')
    gender = input('Enter Gender(M/F) : ')
    mail = input('Enter Email : ')
    print(f'\nYour information hase been successfully added\n\nYour id is {ids}\n')
    sql = 'insert into info(id,name,dob,gender,email) values (%s,%s,%s,%s,%s)'
    val = [ids, name, dob, gender, mail]
    mycursor.execute(sql, val)
    mydb.commit()
    temp = input('Hit Enter to Continue....')


def readfile():
    print(f'These are the ids present in the database\n')
    mycursor.execute("SELECT id FROM info")

    myresult = mycursor.fetchall()

    for x in myresult:
        for j in x:
            print(j, end='\n')

    temp = input('Hit Enter to Continue....')


def readinfo():
    ids = int(input('Enter Your id : '))
    a = f'SELECT * FROM info where id = {ids}'
    mycursor.execute(a)

    myresult = mycursor.fetchall()
    dtr = myresult[0]

    if dtr[0] == ids:
        print(f'''
Name : {dtr[1]}
DOB : {dtr[2]}
Gender : {dtr[3]}
Email : {dtr[4]}''')
        temp = input('\nHit Enter to Continue....')
    else:
        print('No Data Present')
        temp = input('\nHit Enter to Continue....')


def deleteinfo():
    ids = int(input('Enter the Id to be deleted : '))
    mycursor.execute("SELECT id FROM info")
    myresult = mycursor.fetchall()
    dtr = myresult[0]
    for i in dtr:
        a = f'delete from info where id = {ids}'
        mydb.commit()
        mycursor.execute(a)
        mydb.commit()
        print('Data Deleted Successfully')
        temp = input('\nHit Enter to Continue....')
        break
    else:
        print('No such id present\n')
        temp = input('\nHit Enter to Continue....')


def editinfo():
    ids = int(input('Enter Your id : '))

    t = f'select name from info where id = {ids}'
    mycursor.execute(t)
    dtr = mycursor.fetchall()
    if not dtr:
        print('Id not Present in our Database')
        temp = input('\nHit Enter to Continue....')
    else:
        print('Enter New Data')
        name = input('Enter Full Name : ')
        dob = input('Enter DOB (ccyy-mm-dd) : ')
        gender = input('Enter Gender(M/F) : ')
        mail = input('Enter Email : ')
        sql = f'update info set name="{name}",dob="{dob}",gender="{gender}",email="{mail}" where id={ids}'
        mycursor.execute(sql)
        mydb.commit()
        print('Data Edited Successfully\n')
        temp = input('Hit Enter to Continue....')


def fid():
    mycursor.execute("SELECT name FROM info")
    myresult = mycursor.fetchall()
    dtr = myresult[0]
    name = input('\nEnter Your Full Name : ')
    if name in dtr:
        sql = f'select id from info where name = "{name}"'
        mycursor.execute(sql)
        d = mycursor.fetchall()
        print(f'\nYour Id is {d[0][0]}\n')
        temp = input('Hit Enter to Continue....')
    else:
        print('No Data Present')
        temp = input('\nHit Enter to Continue....')


func = {1: crt,
        2: readfile,
        3: readinfo,
        4: editinfo,
        5: deleteinfo,
        6: fid}

while True:
    print('''1. Create Data
2. Read Entire Database
3. Read Information
4. Edit Info
5. Delete Information
6: Find Id with Name
0. Exit
''')
    ch = int(input('Enter Choice (Sno.): '))
    if ch == 0:
        break
    elif ch not in func:
        print('No such function')
        temp = input('\nHit Enter to Continue....')
    else:
        func[ch]()import random as rand
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tharun",
    database="login"
)

mycursor = mydb.cursor()


def crt():
    mycursor.execute("SELECT id FROM info")

    myresult = mycursor.fetchall()
    dtr = myresult[0]
    ids = rand.randint(1000, 9999)
    if dtr[0] == ids:
        ids = rand.randint(1000, 9999)
    name = input('Enter Full Name : ')
    dob = input('Enter DOB (ccyy-mm-dd) : ')
    gender = input('Enter Gender(M/F) : ')
    mail = input('Enter Email : ')
    print(f'\nYour information hase been successfully added\n\nYour id is {ids}\n')
    sql = 'insert into info(id,name,dob,gender,email) values (%s,%s,%s,%s,%s)'
    val = [ids, name, dob, gender, mail]
    mycursor.execute(sql, val)
    mydb.commit()
    temp = input('Hit Enter to Continue....')


def readfile():
    print(f'These are the ids present in the database\n')
    mycursor.execute("SELECT id FROM info")

    myresult = mycursor.fetchall()

    for x in myresult:
        for j in x:
            print(j, end='\n')

    temp = input('Hit Enter to Continue....')


def readinfo():
    ids = int(input('Enter Your id : '))
    a = f'SELECT * FROM info where id = {ids}'
    mycursor.execute(a)

    myresult = mycursor.fetchall()
    dtr = myresult[0]

    if dtr[0] == ids:
        print(f'''
Name : {dtr[1]}
DOB : {dtr[2]}
Gender : {dtr[3]}
Email : {dtr[4]}''')
        temp = input('\nHit Enter to Continue....')
    else:
        print('No Data Present')
        temp = input('\nHit Enter to Continue....')


def deleteinfo():
    ids = int(input('Enter the Id to be deleted : '))
    mycursor.execute("SELECT id FROM info")
    myresult = mycursor.fetchall()
    dtr = myresult[0]
    for i in dtr:
        a = f'delete from info where id = {ids}'
        mydb.commit()
        mycursor.execute(a)
        mydb.commit()
        print('Data Deleted Successfully')
        temp = input('\nHit Enter to Continue....')
        break
    else:
        print('No such id present\n')
        temp = input('\nHit Enter to Continue....')


def editinfo():
    ids = int(input('Enter Your id : '))

    t = f'select name from info where id = {ids}'
    mycursor.execute(t)
    dtr = mycursor.fetchall()
    if not dtr:
        print('Id not Present in our Database')
        temp = input('\nHit Enter to Continue....')
    else:
        print('Enter New Data')
        name = input('Enter Full Name : ')
        dob = input('Enter DOB (ccyy-mm-dd) : ')
        gender = input('Enter Gender(M/F) : ')
        mail = input('Enter Email : ')
        sql = f'update info set name="{name}",dob="{dob}",gender="{gender}",email="{mail}" where id={ids}'
        mycursor.execute(sql)
        mydb.commit()
        print('Data Edited Successfully\n')
        temp = input('Hit Enter to Continue....')


def fid():
    mycursor.execute("SELECT name FROM info")
    myresult = mycursor.fetchall()
    dtr = myresult[0]
    name = input('\nEnter Your Full Name : ')
    if name in dtr:
        sql = f'select id from info where name = "{name}"'
        mycursor.execute(sql)
        d = mycursor.fetchall()
        print(f'\nYour Id is {d[0][0]}\n')
        temp = input('Hit Enter to Continue....')
    else:
        print('No Data Present')
        temp = input('\nHit Enter to Continue....')


func = {1: crt,
        2: readfile,
        3: readinfo,
        4: editinfo,
        5: deleteinfo,
        6: fid}

while True:
    print('''1. Create Data
2. Read Entire Database
3. Read Information
4. Edit Info
5. Delete Information
6: Find Id with Name
0. Exit
''')
    ch = int(input('Enter Choice (Sno.): '))
    if ch == 0:
        break
    elif ch not in func:
        print('No such function')
        temp = input('\nHit Enter to Continue....')
    else:
        func[ch]()
