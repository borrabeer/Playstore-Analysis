""" Playstore-Analysis Project """
import pandas as pd
import pygal as pg
from pygal.style import Style, DarkSolarizedStyle
def main():
    """ main function for data and making charts """
    """

    Pulling Data from CSV file

    """
    data = pd.read_csv("googleplaystore.csv", encoding="ISO-8859-1") #อ่านไฟล์ csv
    name_data = data["App"] #data ชื่อแอพพลิเคชั่น
    rating_data = data["Rating"] #data rating ของแต่ละแอพพลิเคชั่น
    category_data = data["Category"] #data หมวดหมู่ของแต่ละแอพพลิเคชั่น
    review_data = data["Reviews"] #data reviews ของแต่ละแอพพลิเคชั่น
    size_data = data["Size"] #data ขนาดของแต่ละแอพพลิเคชั่น
    install_data = data["Installs"] #data ยอดดาวน์โหลดของแต่ละแอพพลิเคชั่น
    """

    Editing data into readable data

    """
    size_data = [i.replace("M", "").replace("Varies with device", "0").replace("+", "").replace(',', '') for i in size_data] #ทำให้ data ของ Size เป็นตัวเลขทั้งหมด
    for i in range(len(size_data)): #ทำให้ขนาดของ data เป็นหน่วยเดียวกัน
        if 'k' in size_data[i]:
            size_data[i] = size_data[i].replace('k', "")
            size_data[i] = int(float(size_data[i]))
            size_data[i] /= 1024
    size_data = [float(i) for i in size_data]
    install_data = [i.replace("+", "") for i in install_data]  #ทำให้ data ของยอดดาวน์โหลดเป็นตัวเลขทั้งหมด
    """

    Using function and returning data in to variables

    """
    category_review_data = category_review(category_data, review_data)
    category_rating_data = category_rating(category_data, rating_data)
    name_install_data = name_install(name_data, install_data)
    category_size_data = category_size(category_data, size_data)
    """
    
    Making an Average reviews of each Categories chart

    """
    category_review_chart = pg.Bar()
    category_review_chart.title = "Average Reviews of each Categories"
    for i in category_review_data:
        category_review_chart.add(i, category_review_data[i])
    category_review_chart.render_to_file("category_review_chart.svg")
    """

    Making an Average ratings of each Categories chart

    """
    category_rating_chart = pg.HorizontalBar()
    category_rating_chart.title = "Average Ratings of each Categories"
    for i in category_rating_data:
        category_rating_chart.add(i, category_rating_data[i])
    category_rating_chart.render_to_file("category_rating_chart.svg")
    """

    Making an Average sizes of each Categories chart

    """
    category_size_chart = pg.Bar(style=DarkSolarizedStyle)
    category_size_chart.title = "Average Sizes of Application of each Categories(MBs)"
    for i in category_size_data.keys():
        category_size_chart.add(i, category_size_data[i])
    category_size_chart.render_to_file("category_size_chart.svg")
    """

    Making a Most install application chart
    
    """
    name_install_chart = pg.Bar(fill=True)
    name_install_chart.title = "The Most Installs Applications on Google Playstore"
    for i in name_install_data:
        name_install_chart.add(i, name_install_data[i])
    name_install_chart.render_to_file("name_install_chart.svg", key=len)
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
        if len(i) > 11:
            name_install_data[name[index]] = i
        index += 1
    return name_install_data
main()
