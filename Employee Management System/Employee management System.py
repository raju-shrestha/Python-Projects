'''

Write a simple employee management program. It should have common features like getting input about details of employees
and storing those details to database. Implement a loop to get the input till the user wants. Your program should be able
to search/insert/update/delete employees on the basis of any one parameter(that you can decide) and print the details of
that employee. Try to use the data structures(list,dictionary), functions, exception handling and custom functions.
 Use OOP for Employee modelling. ​ ​There ​ ​should ​ ​be ​ ​an ​ ​option ​ ​to ​ ​provide ​ ​a ​ ​csv​ ​file ​ ​of ​ ​database.

'''

import pymysql.cursors

# For connection
conn = pymysql.connect(host='localhost', user='root', password='', db='assignment')

# Insert Operation

TABLE = 'Employee'
insert_queries = []


def createTable():
    return "create table if not exists {0}" \
           "(id int(10) NOT NULL AUTO_INCREMENT PRIMARY KEY, name varchar(20) NOT NULL, " \
           "department VARCHAR (20), dob DATE, join_date DATE, salary float(10));".format(TABLE)


def create_table():
    #print(createTable())

    with conn.cursor() as cursor:
        cursor.execute(createTable())


def prepare_insert_query(TABLE=None, name=None, department=None, dob=None, join_date=None, salary=None):
    return "insert into {0} (name, department, dob, join_date, salary) values ('{1}','{2}','{3}',{4}, {5})".format(
        TABLE, name, department, dob, join_date, salary)


def insert_records():
    choice = 'Y'

    while choice.lower() == 'y':
        name = input("Enter name: ")
        department = input("Enter department: ")
        dob = input("Enter dob: ")
        join_date = input("Enter join date: ")
        salary = int(input("Enter salary: "))

        insert_queries.append(prepare_insert_query(TABLE, name, department, dob, join_date, salary))

        choice = input("Want to insert another(Y/N)")

    try:
        with conn.cursor() as cursor:
            for insert in insert_queries:
                print("query = " + insert)
                cursor.execute(insert)

        conn.commit()
    except Exception as error:
        print(error)
        conn.rollback()


def see_records():
    print("{0:<20}{1:20}{2:<20}{3:<20}{4:<10}".format("name", "department", "dob", "join_date", "salary"))
    print("---------------------------------------------------------------------------")
    with conn.cursor() as cursor:
        cursor.execute("select * from {}".format(TABLE))
        allRecords = cursor.fetchall()
        for i in allRecords:
            print("{0:<20}{1:<20}{2:<20}{3:<10}{4:<10}".format(i[1], i[2], i[3], i[4], i[5]))


def delete_record():
    del_name = input("Enter name to be deleted")

    query = "delete from {0} where name='{1}'".format(TABLE, del_name)

    result = None

    try:
        with conn.cursor() as cursor:
            result = cursor.execute(query)

        conn.commit()
    except Exception as error:
        print(error)
        conn.rollback()

    if (result != 1):
        print("Cannot delete. Make sure your query is correct")


def update_name():
    old_name = input("Enter the name to be replaced :")
    new_name = input("Enter the name to be replaced with :")

    result = None

    query = "update {} set name='{}' where name = '{}'".format(TABLE, new_name, old_name)

    try:
        with conn.cursor() as cursor:
            result = cursor.execute(query)
    except Exception as error:
        print(error)
        conn.rollback()

    conn.commit()

    if result != 1:
        print("Cannot update. Make sure your query is correct")


def main():
    create_table()

    print("Select Option\n1.Insert Records\n2.See all Records\n3.Delete Records\n4.Update Name")
    user_choice = input("Enter your choice: ")
    if user_choice == '1':
        insert_records()
    elif user_choice == '2':
        see_records()
    elif user_choice == '3':
        delete_record()
    elif user_choice == '4':
        update_name()
    else:
        print("Wrong choice")

    conn.close()


if __name__ == '__main__':
    main()
