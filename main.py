import math
import random
from scipy import integrate
from sympy import *
import ConnectDB


intercept_location = {"смежные помещения, не оборудованные системами звукоусиления": 46,
                      "смежные помещения, оборудованные системами звукоусиления": 60,
                      "уличное пространство без транспорта, не оборудованные системами звукоусиления": 36,
                      "уличное пространство без транспорта, оборудованные системами звукоусиления": 50,
                      "уличное пространство с транспортом, не оборудованные системами звукоусиления": 26,
                      "уличное пространство с транспортом, оборудованные системами звукоусиления": 40,
                      }

L_n = random.uniform(0, 20)  # генерация шума


def output_of_room():
    print("смежные помещения, не оборудованные системами звукоусиления - 1")
    print("смежные помещения, оборудованные системами звукоусиления - 2")
    print("уличное пространство без транспорта, не оборудованные системами звукоусиления - 3")
    print("уличное пространство без транспорта, оборудованные системами звукоусиления - 4")
    print("уличное пространство с транспортом, не оборудованные системами звукоусиления - 5")
    print("уличное пространство с транспортом, оборудованные системами звукоусиления - 6")


def room(val_v):
    val = int(float(val_v))
    if val == 1:
        return 46
    elif val == 2:
        return 60
    elif val == 3:
        return 36
    elif val == 4:
        return 50
    elif val == 5:
        return 26
    elif val == 6:
        return 40


def output_of_materials():
    print("Минеральный войлок - 1")
    print("Строительный войлок - 2")
    print("Фанера - 3")
    print("Перфорированные панели с асбестовой ватой - 4")
    print("Плиты Акмигран - 5")
    print("Плиты типа ПА/О ТУ 21-24-60-77 - 6")
    print("Стеклянная вата - 7")
    print("Перфорированные металлические листы просадочно-вытяжные с рыхлым поглотителем - 8")
    print("Асбетоцементная плита с поглотителем из стекломатов - 9")


def material_selection(val):
    if 1 <= val <= 9:
        if val == 1:
            return "Минеральный войлок"
        elif val == 2:
            return "Строительный войлок"
        elif val == 3:
            return "Фанера"
        elif val == 4:
            return "Перфорированные панели с асбестовой ватой"
        elif val == 5:
            return "Плиты Акмигран"
        elif val == 6:
            return "Плиты типа ПА/О ТУ 21-24-60-77"
        elif val == 7:
            return "Стеклянная вата"
        elif val == 8:
            return "Перфорированные металлические листы просадочно-вытяжные с рыхлым поглотителем"
        elif val == 9:
            return "Асбетоцементная плита с поглотителем из стекломатов"
    else:
        print("Введено неверное значение при выборе материала")
        return 0


def output_of_frequency():
    print("Частота 500 Гц - 1")
    print("Частота 1000 Гц - 2")
    print("Частота 2000 Гц - 3")
    print("Частота 4000 Гц - 4")


def frequency_selection(val):
    if 1 <= val <= 4:
        if val == 1:
            return 500
        elif val == 2:
            return 1000
        elif val == 3:
            return 2000
        elif val == 4:
            return 4000
    else:
        print("Введено неверное значение при выборе частоты")
        return 0


def Delta(L_sum_v, L_n_v):
    L_sum = float(L_sum_v)
    L_n = float(L_n_v)
    if difference(L_sum, L_n) > 10:
        return 0
    elif 10 >= difference(L_sum, L_n) > 6:
        return 1
    elif 6 >= difference(L_sum, L_n) >= 4:
        return 2
    elif 4 > difference(L_sum, L_n) > 2:
        return 3
    elif 2 >= difference(L_sum, L_n) > 1:
        return 4
    elif 1 >= difference(L_sum, L_n) > 0.5:
        return 7
    elif difference(L_sum, L_n) < 0.5:
        return 10


def acoustic_signal(L_sum, L_n):  
    # L_n - уровень акуст шума (noize)
    # D - delta, поправка к расчетному значению уровня тестового акустического сигнала в контрольной точке
    # L_sum - уровень суммарного акуст. сигнала и шума
    if difference(L_sum, L_n) >= 10:
        L_a = L_sum
    elif difference(L_sum, L_n) <= 10:
        L_a = L_sum - Delta(L_sum, L_n)
    return L_a


def difference(L_sum, L_n):
    return L_sum - L_n


def soundproofing(L_test, L_sum):  # Q - коэффициент звукоизоляции
    L_n = random.uniform(0, 30)
    return L_test - acoustic_signal(L_sum, L_n)


# величина ослабления акустического сигнала
def soundproofing_mat(val_mat, val_fr):  # q-коэффициент шумоподавления
    q = ConnectDB.get_Data_material(val_mat, frequency_selection(val_fr))
    R = -10 * math.log10(q[0])
    return R


def display_of_protective_equipment():  # выбор средств по минимальному значению звукоизоляции
    arr_return = []
    arr_name_mat = []
    arr_meas = []
    arr_sound_mat = []
    print("Введите цифру, соответствующую описанию помещения, смежному с защищаемым: ")
    output_of_room()
    val = input()
    print("Введите значение тестового сигнала: ")
    test = float(input())
    print("Введите значение принятого сигнала : ")
    test_1 = float(input())
    if room(val) > soundproofing(test, test_1):
        print("Значение звукоизоляции соответствует норме, дополнительные средства звукоизолияции не требуются")
        arr_return.append(
            "Значение звукоизоляции соответствует норме, дополнительные средства звукоизолияции не требуются")
    elif room(val) < soundproofing(test, test_1):
        print("Пожалуйста, введите цифру, соответствующую выбранной Вами частоте (в диапазоне от 1 до 4)")
        output_of_frequency()
        val_fr = int(input())
        print("Величина ослабления акустического сигнала:")
        for i in range(len(ConnectDB.get_Data_materials(frequency_selection(val_fr)))):
            arr_name_mat.append(ConnectDB.get_Data_materials(frequency_selection(val_fr))[i])
            arr_sound_mat.append(
                soundproofing_mat(ConnectDB.get_Data_materials(frequency_selection(val_fr))[i], val_fr))
        for i in range(len(arr_sound_mat)):
            if abs(room(val) - soundproofing(test, test_1)) > arr_sound_mat[i]:
                for i in range(len(ConnectDB.get_Data_measure(frequency_selection(val_fr)))):
                    arr_meas.append(str(ConnectDB.get_Data_measure(frequency_selection(val_fr))[i]) + " - " + str(
                        ConnectDB.get_Data_additional_measures(frequency_selection(val_fr))[i]))
    if len(arr_meas) == 0:
        for i in range(len(arr_name_mat)):
            arr_return.append(arr_name_mat[i] + " - " + str(arr_sound_mat[i]))
    else:
        arr_return.append("Величина ослабления акустического сигнала:")
        for i in range(len(arr_sound_mat)):
            arr_return.append(arr_name_mat[i] + " - " + str(arr_sound_mat[i]))
        arr_return.append("\n")
        arr_return.append("В дополнение к звукопоглощающим материалам используйте следующие дополнительные средства: ")
        for i in range(len(arr_name_mat)):
            arr_return.append(arr_meas[i])
    for i in range(len(arr_return)):
        print(arr_return[i])
    return arr_return
    # метод считывания данных из файла и записи данных в файл


def get_data(arr):
    with open('testout.txt', 'w') as f_out:
        for i in range(len(arr)):
            f_out.write(arr[i] + "\n")  # пишем результат в файл в строковом типе


get_data(display_of_protective_equipment())
