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
main()

