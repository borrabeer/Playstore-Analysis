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
    price_data = [i.replace("$", "") for i in price_data]  #ทำเช่นเดียวกับ install_data
    #print(data)
    min_install, max_install = install(install_data) #นำ install_data เข้า function install จะหายอด install สูงสุดและต่ำสุด
    print(min_install, max_install)
    print(name_rating_data_dict)
    print(max(install_data))
    rating_chart = pg.Bar()
    rating_chart.add("Rating", rating_data)
    rating_chart.render_to_file("rating_chart.svg")
    #ช่วยหาindexของ max, min install ให้หน่อย
def install(install_data):
    """" this function for max and min install """
    #นับจำนวนของ max, min install
    count_min_install = install_data.count(min(install_data))
    count_max_install = install_data.count(max(install_data))
    return count_min_install, count_max_install
def name_rating(name_data, rating_data):
    """  get dict by {name_data:rating_data} """
    #เอา name-data กับ rating-data มาทำ dict
    data_dict = dict()
    index = 0
    for i in rating_data:
        data_dict.update({name_data[index]:i})
        index += 1
    return data_dict
main()
