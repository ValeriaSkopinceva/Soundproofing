import psycopg2
from psycopg2 import Error


def get_Data_soundproofing(freq):
    try:
        # Подключиться к существующей базе данных
        connection = psycopg2.connect(user="postgres",
                                      password="1111",
                                      host="127.0.0.1",
                                      database="postgres")
        cursor = connection.cursor()
        # postgreSQL_select_all = "SELECT * FROM public.Materials"
        # cursor.execute(postgreSQL_select_all)
        # data = cursor.fetchall()
        postgreSQL_select_Query = "select soundproofing  from materials where frequency = %s"
        cursor.execute(postgreSQL_select_Query, (freq,))
        data_select_Query = cursor.fetchall()
        # print("Вывод каждой строки и ее столбцов")
        # for row in data:
        #     print(
        #         "Материал " + row[1] + ", коэффициент шумоподавления: " + str(float(row[2])) + ", октавная частота " + str(float(
        #             row[3])))
        # print("Вывод данных")
        arr_sound = []
        for row in data_select_Query:
            arr_sound.append(row[0])
        return arr_sound

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            # print("Соединение с PostgreSQL закрыто")


def get_Data_materials(freq):
    try:
        # Подключиться к существующей базе данных
        connection = psycopg2.connect(user="postgres",
                                      password="1111",
                                      host="127.0.0.1",
                                      database="postgres")

        cursor = connection.cursor()
        postgreSQL_select_Query = "select material from materials where frequency = %s"
        cursor.execute(postgreSQL_select_Query, (freq,))

        data_select_Query = cursor.fetchall()
        # print("Вывод данных")
        arr_mat = []
        for row in data_select_Query:
            arr_mat.append(row[0])
        return arr_mat

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            # print("Соединение с PostgreSQL закрыто")


def get_Data_material(mat, fr):
    try:
        # Подключиться к существующей базе данных
        connection = psycopg2.connect(user="postgres",
                                      password="1111",
                                      host="127.0.0.1",
                                      database="postgres")

        cursor = connection.cursor()
        postgreSQL_select_Query = "select soundproofing  from materials where material = %s and frequency = %s"
        cursor.execute(postgreSQL_select_Query, (mat, fr))
        data_select_Query = cursor.fetchall()
        arr_sound = []
        for row in data_select_Query:
            arr_sound.append(row[0])
            # print("soundproofing ",row[0])
        return arr_sound

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()


def get_Data_additional_measures(freq):
    try:
        # Подключиться к существующей базе данных
        connection = psycopg2.connect(user="postgres",
                                      password="1111",
                                      host="127.0.0.1",
                                      database="postgres")

        cursor = connection.cursor()
        postgreSQL_select_Query = "select soundproofing  from additional_measures where frequency = %s"
        cursor.execute(postgreSQL_select_Query, (freq,))

        data_select_measures = cursor.fetchall()
        # print("Вывод данных по селекту")
        arr_sound = []
        for row in data_select_measures:
            arr_sound.append(row[0])
        return arr_sound

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            # print("Соединение с PostgreSQL закрыто")


def get_Data_measure(fr):
    try:
        # Подключиться к существующей базе данных
        connection = psycopg2.connect(user="postgres",
                                      password="1111",
                                      host="127.0.0.1",
                                      database="postgres")

        cursor = connection.cursor()
        postgreSQL_select_Query = "select measure from additional_measures where frequency = %s"
        cursor.execute(postgreSQL_select_Query, (fr,))
        data_select_measure = cursor.fetchall()
        arr_sound = []
        for row in data_select_measure:
            arr_sound.append(row[0])
            # print("soundproofing ",row[0])
        return arr_sound

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()


def insert_to_repository(name_material, soundproofing):
    try:
        # Подключиться к существующей базе данных
        connection = psycopg2.connect(user="postgres",
                                      password="1111",
                                      host="127.0.0.1",
                                      database="postgres")

        cursor = connection.cursor()
        # Выполнение SQL-запроса для вставки данных в таблицу
        insert_query = " INSERT INTO repository (name_material, soundproofing) VALUES (%s,%s) "
        cursor.execute(insert_query, (name_material, soundproofing))
        connection.commit()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
