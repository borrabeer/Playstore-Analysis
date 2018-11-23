""" Psit Project """
import pandas as pd
def main():
    data = pd.read_csv("googleplaystore.csv", encoding="ISO-8859-1")
    print(data)
main()

