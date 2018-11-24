""" Psit Project """
import pandas as pd
import pygal as pg
def main():
    """ main function for input data """
    data = pd.read_csv("googleplaystore.csv", encoding="ISO-8859-1")
    name_data = data["App"]         # ดึงข้อมูลมาใหเหมดแล้วที่จะใช้
    rating_data = data["Rating"]
    name_rating_data_dict = name_rating(name_data, rating_data)
    review_data = data["Reviews"]
    size_data = data["Size"]
    install_data = data["Installs"]
    type_data = data["Type"]
    price_data = data["Price"]
    genres_data = data["Genres"]
    install_data = [i.replace("+", "").replace(",", "") for i in install_data]  #ทำให้ install_data เป็มเลขกลมๆ
    install_data = [int(i) for i in install_data]
    price_data = [i.replace("$", "") for i in price_data]  #ทำเช่นเดียวกับ install_data
    #print(data)
    number_min, number_max = install(install_data) #หา index ของค่า max, min
    #หาชื่อของ app
    min_name_data = find_name(number_min, name_data)
    max_name_data = find_name(number_max, name_data)
    print(max(install_data))
    print(number_min)
    print(number_max)
    print(min_name_data)
    print(max_name_data)
    count_rating_data = count_rating(rating_data)
    rating_chart = pg.Bar()
    rating_chart.title = "Rating in Google Playstore"
    rating_chart.x_labels = count_rating_data.keys()
    rating_chart.add("Rating", count_rating_data.values())
    rating_chart.render_to_file("rating_chart.svg")
    print(count_rating_data)
    #print(name_rating_data_dict)
def install(install_data):
    """" this function for max and min install """
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
    """  get dict by {name_data:rating_data} """
    #เอา name-data กับ rating-data มาทำ dict
    data_dict = dict()
    index = 0
    for i in rating_data:
        data_dict.update({name_data[index]:i})
        index += 1
    return data_dict
def find_name(number, name_data):
    """ find name in name_data """
    set_name = set()
    for i in number:
        set_name.add(name_data[int(i)])
    return set_name
def count_rating(rating_data):
    """count rating in to set of int"""
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
main()
