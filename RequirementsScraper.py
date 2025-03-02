import os
import pandas as pd
import re

text = ""
current_dir = os.getcwd()
for filename in os.listdir(current_dir):
    if os.path.isfile(os.path.join(current_dir, filename)) and "south-africa.txt" in filename:
        # print(filename)
        file = f"{filename}"
        with open(file, "r", encoding="utf-8") as f:
            text += filename
            text += f.read()
mylist = text.split("*******")
# print(len(mylist))
req_list = list()
fields_list = list()
date_list = list()
apply_list = list()
contact_list = list()
about_list = list()
sites_list = list()


for text in mylist: #I need to find the different parts of a bursary and put them into a dataframe
    http_String = "https://www.zabursaries.co.za/"
    about_String = "ABOUT THE BURSARY PROVIDER"
    req_String = "ELIGIBILITY REQUIREMENTS"
    date_String = "CLOSING DATE"
    apply_String = "HOW TO APPLY"
    fields_String = "FIELDS COVERED"
    contact_String = "CONTACT THE BURSARY PROVIDER"

    apply_i = text.find(apply_String) if text.find(apply_String) is not None else 0.0
    http_i = text.find(http_String) if text.find(http_String) is not None else 0.0
    about_i = text.find(about_String) if text.find(about_String) is not None else 0.0
    fields_i = text.find(fields_String) if text.find(fields_String) is not None else 0.0
    contact_i = text.find(contact_String) if text.find(contact_String) is not None else 0.0
    req_i = text.find(req_String) if text.find(req_String) is not None else 0.0
    date_i = text.find(date_String) if text.find(date_String) is not None else 0.0
    
    requirements = text[req_i:apply_i] if req_i != 0.0 and apply_i != 0.0 else ""
    applying = text[apply_i:date_i] if apply_i != 0.0 and date_i != 0.0 else ""
    date = text[date_i:contact_i] if date_i != 0.0 and contact_i != 0.0 else ""
    contact = text[contact_i:] if contact_i != 0.0 else ""
    about = text[about_i:req_i] if about_i != 0.0 and req_i != 0.0 else ""
    link = text[http_i:about_i]
    site = "https://www.zabursaries.co.za/"
    south_africa = "-south-africa/"
    pattern = fr"^{site}.+{south_africa}.*/$"
    match = re.search(pattern, link, re.MULTILINE)
    if match:
        start, end = match.span()
        site = link[start:end]
    
    req_list.append(requirements)
    apply_list.append(applying)
    date_list.append(date)
    contact_list.append(contact)
    about_list.append(about)
    sites_list.append(site)

data = {
    "Site" : sites_list,
    "Requirements" : req_list,
    "How to Apply" : apply_list,
    "Date" : date_list,
    "Contact" : contact_list,
    "About" : about_list
}

df = pd.DataFrame(data)

df.to_csv("data.csv", index=False)

