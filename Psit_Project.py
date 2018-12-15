""" Psit Project """
import pandas as pd
import pygal as pg
from pygal.style import Style, DarkSolarizedStyle
def main():
    """ main function for input data """
    data = pd.read_csv("googleplaystore.csv", encoding="ISO-8859-1")
    name_data = data["App"]         # ดึงข้อมูลมาให้หมดแล้วที่จะใช้
    rating_data = data["Rating"]
    category_data = data["Category"]
    name_rating_data_dict = name_rating(name_data, rating_data)
    category_rating_data = category_rating(category_data, rating_data)
    review_data = data["Reviews"]
    size_data = data["Size"]
    size_data = [i.replace("M", "") for i in size_data] #ทำให้ data ของ Size เป็นตัวเลขทั้งหมด
    size_data = [i.replace("Varies with device", "0") for i in size_data]
    size_data = [i.replace("+", "") for i in size_data]
    size_data = [i.replace(',', '') for i in size_data]
    for i in range(len(size_data)):
        if 'k' in size_data[i]:
            size_data[i] = size_data[i].replace('k', "")
            size_data[i] = int(float(size_data[i]))
            size_data[i] /= 1024
    size_data = [float(i) for i in size_data]
    category_size_data = category_size(category_data, size_data)
    install_data = data["Installs"]
    install_data = [i.replace("+", "").replace(",", "") for i in install_data]  #ทำให้ install_data เป็มเลขกลมๆ
    install_data = [int(i) for i in install_data]
    name_install_data = name_install(name_data, install_data)
    type_data = data["Type"]
    price_data = data["Price"]
    genres_data = data["Genres"]
    price_data = [i.replace("$", "") for i in price_data]  #ทำเช่นเดียวกับ install_data
    category_review(category_data, review_data)
    # category_review_data = category_review(category_data, review_data)
    # number_min, number_max = install(install_data) #หา index ของค่า max, min
    # #หาชื่อของ app
    # min_name_data = find_name(number_min, name_data)
    # max_name_data = find_name(number_max, name_data)
    category_rating_chart = pg.HorizontalBar()
    category_rating_chart.title = "Average Rating of each Categories"
    for i in category_rating_data:
        category_rating_chart.add(i, category_rating_data[i])
    category_rating_chart.render_to_file("category_rating_chart.svg")
    category_size_chart = pg.Bar(style=DarkSolarizedStyle)
    category_size_chart.title = "Average Size of Application of each Category(MBs)"
    for i in category_size_data.keys():
        category_size_chart.add(i, category_size_data[i])
    category_size_chart.render_to_file("category_size_chart.svg")
def install(install_data):
    """" ฟังชั่นนี้ หายอดติดตั้งที่มากที่สุดและน้อยที่สุดใน google playstore """
    #นับจำนวนของ max, min install
    number_min = list()
    number_max = list()
    for i in range(len(install_data)):
        if install_data[i] == min(install_data):
            number_min.append(i)
        if install_data[i] == max(install_data):
            number_max.append(i)
    return number_min, number_max
def name_rating(name_data, rating_data):
    """  หา rating ของแต่ละแอพ แล้วมาทำ dict เพื่อให้ง่ายต่อการคนหา  """
    #เอา name-data กับ rating-data มาทำ dict
    data_dict = dict()
    index = 0
    for i in rating_data:
        data_dict.update({name_data[index]:i})
        index += 1
    return data_dict
def find_name(number, name_data):
    """ รวมแอพที่มีชื่อซ้ำ แต่คนละหมวดหมู่ ให้เป็นชื่อเดียว """
    set_name = set()
    for i in number:
        set_name.add(name_data[int(i)])
    return set_name
def count_rating(rating_data):
    """ นับค่า rating ของแต่ละแอฟ ออกมาเป็นช่วงตัวเลข """
    #นับค่า Rating ของแต่ละ แอพพลิเคชั่นออกมาเป็นช่วงของตัวเลข
    count_rating = { 5 : 0, 4.5 : 0, 4 : 0, 3.5 : 0, 3 : 0, 2.5 : 0, 2 : 0, 1.5 : 0, 1 : 0, 0 : 0}
    for i in rating_data:
        if i == 5:
            count_rating[5] += 1
        elif i >= 4.5:
            count_rating[4.5] += 1
        elif i >= 4:
            count_rating[4] += 1
        elif i >= 3.5:
            count_rating[3.5] += 1
        elif i >= 3:
            count_rating[3] += 1
        elif i >= 2.5:
            count_rating[2.5] += 1
        elif i >= 2:
            count_rating[2] += 1
        elif i >= 1.5:
            count_rating[1.5] += 1
        elif i >= 1:
            count_rating[1] += 1
        else:
            count_rating[0] += 1
    return count_rating
def category_rating(category, rating):
    """นำ rating ของ category มาหาค่าเฉลี่ย"""
    category_rating_data = {}
    category_rating_len = {}
    index = 0
    index_2 = 0
    for i in rating:
        if category[index] not in category_rating_data:
            category_rating_data[category[index]] = i
            category_rating_len[category[index]] = 1
        else:
            category_rating_len[category[index]] += 1
            category_rating_data[category[index]] += i
            index += 1
    for i in category_rating_len:
        category_rating_data[i] /= category_rating_len[i]
        index_2 += 1
    return category_rating_data
def category_review(category, review):
    """ นำ review และ category มาทำ dict """
    data_dict = dict()
    data_lst = list()
    for i in category:
        for j in review:
            data_lst.append([i, j])
    for i in data_lst:
        if i[0] not in data_dict:
            data_dict.update({i[0]:[i[1]]})
        else:
            lst1 = data_dict[i]
            lst1.append(i[1])
            data_dict.update({i:lst1})
    return data_dict
def category_size(category, size):
    """นำขนาดของแต่ละแอพพลิเคชั่นในแต่ละหมวดมาหาค่าเฉลี่ย"""
    category_size_data = {}
    category_size_len = {}
    index = 0
    index_2 = 0
    for i in size:
        if category[index] not in category_size_data:
            category_size_data[category[index]] = i
            category_size_len[category[index]] = 1
        else:
            category_size_len[category[index]] += 1
            category_size_data[category[index]] += i
        index += 1
    for i in category_size_len:
        category_size_data[i] /= category_size_len[i]
        index_2 += 1
    return category_size_data
def name_install(name, install):
    """นำยอดดาวน์โหลดของแต่ละแอพมาเชื่อมกันโดยแยกเป็นแต่ละหมวดหมู่"""
    name_install_data = {}
    index = 0
    for i in install:
        if i >= 500000000:
            name_install_data[name[index]] = i
        index += 1
    return name_install_data
def category_review(category, review):
    """ นำ review และ category มาทำ dict """
    data_dict = dict()
    data_lst = list()
    for i in range(len(category)):
            data_lst.append([category[i], review[i]])
    for i in data_lst:
        if i[0] not in data_dict:
            data_dict.update({i[0]:[i[1]]})
        else:
            lst1 = data_dict[i[0]]
            lst1.append(i[1])
            data_dict.update({i[0]:lst1})
    for i in data_dict:
        lst1 = data_dict[i]
        ava = sum(lst1)/len(lst1)
        data_dict.update({i:ava})
    print(data_dict)
main()
