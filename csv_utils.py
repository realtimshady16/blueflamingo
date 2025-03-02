import csv, pandas as pd

# with open("data.csv", mode="r", encoding="utf-8") as file:
#     csvFile = csv.reader(file)
#     for line in csvFile:
#         print(line)

def readCSV():
    csvFile = pd.read_csv("data.csv")
    print(csvFile)

def searchCSV(query: str):
    # qString: str = str(query) if type(query) != ""
    df = pd.read_csv("data.csv")
    results = df[df.apply(lambda row: row.astype(str).str.contains(query).any(), axis=1)]
    return results

# print(searchCSV("Matric")["Requirements"])
print(type("string") != "str")