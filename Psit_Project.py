""" Psit Project """
import pandas as pd
def main():
    data = pd.read_csv("googleplaystore.csv", encoding="ISO-8859-1")
    name_data = data["App"]
    rating_data = data["Rating"]
    review_data = data["Reviews"]
    size_data = data["Size"]
    install_data = data["Installs"]
    type_data = data["Type"]
    price_data = data["Price"]
    genres_data = data["Genres"]
    install_data = [i.replace("+", "").replace(",", "") for i in install_data]
    install_data = list(map(int, install_data))
    review_data = list(map(int, review_data))
    price_data = list(map(int, price_data))
    print(install_data)
    print(min(install_data))
    #print(data)
main()

