""" Psit Project """
import pandas as pd
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
    number_min, number_max = install(install_data) #หา index ของค่า max, min
    print(number_min)
    print(number_max)
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
main()
