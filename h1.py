""" Classify """
def main():
    """ main function for Classify """
    dict1 = {}
    dict2 = {}
    lst = []
    lst2 = []
    id_a = ""
    id_b = ""
    check = 0
    while True:
        student_id = input()
        if student_id == "END":
            break
        else:
            lst2.append(int(student_id))
            lst2.sort()
    for i in lst2:
        student_id = str(i)
        id_a = student_id[0:2]
        if id_a == id_b:
            lst.append(student_id[2:4])
            dict1 = {student_id[0:2]:lst}
        else:
            lst = []
            lst.append(student_id[2:4])
            dict1 = {student_id[0:2]:lst}
        dict2.update(dict1)
        id_b = id_a
    for student_id in dict2:
        key = dict2.get(student_id)
        for j in key:
            check += 1
            value = key.count(j)
            id_a = j
            if id_a == id_b:
                pass
            else:
                if check == 1:
                    print("%s %i %i"%(student_id, int(j), value))
                else:
                    print("-- %i %i"%(int(j), value))
            id_b = id_a
        check = 0
main()
