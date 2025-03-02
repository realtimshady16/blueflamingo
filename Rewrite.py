file = open("sites.txt", "r")
myList = file.readlines()

def makeCategories():
    categories = []
    category_set =set()
    for i in range(7, 23):
        line = myList[i]
        za = line.find(".za/")
        category = line[za+4:]
        categories.append(category[:(category.find("south-africa") if "south-africa" in category else category.find("/"))] + ("details" if "south-africa" in category else "-details"))
    for category in categories:
        category_set.add(category)
    return category_set

def main():
    categories = list(makeCategories())
    myList = list()
    # print(categories)
    for category in categories:
        with open((str(category) + ".txt"), "r", encoding='utf-8', errors="ignore") as f:
            content = f.read() + "\n"
            myList.append(content)
    with open("test.txt", "w", encoding="utf-8") as f:
        f.writelines(line for line in myList)

if __name__ == "__main__":
    main()