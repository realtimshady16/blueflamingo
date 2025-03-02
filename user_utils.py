from datetime import datetime
import re, pandas as pd, os
"""
This is the test data
"""
data = {
    "Name": ["Tim", "Tom", "Jon"],
    "Category": ["accounting", "computer-science", "science"],
    "Email" : ["S", "A", "M"]
}
df = pd.DataFrame(data)

today = datetime.today()
def getTime(curr_date: datetime, future_date: str) -> str:
    curr_date = curr_date.strftime("%d %B %Y")
    result = ""
    open_bracket = future_date.find(" (extension)")
    new_d = future_date[:open_bracket] if (open_bracket != -1) else future_date[:len(future_date)]
    date: str = datetime.strptime(new_d, "%d %B %Y")
    c_date: str = datetime.strptime(curr_date, "%d %B %Y")
    if date == c_date:
        result = "today"
    else:
        if date < c_date:
            return "Late"
        else:
            diff = date - c_date
            str_diff = str(diff)
            result = f"{str_diff[:str_diff.find(",")]}"
    return result

def obtainDate(date: str) -> str:
    newline = date.find("\n")
    real_date = date[newline+1:date.find(".")]
    return real_date
        
def getUsers(file) -> pd.DataFrame:
    if os.path.isfile(file):
        df = pd.read_csv(file)
        return df
    else:
        return "Cannot find file"

def formatLetter(filename: str, name: str, email: str, df: pd.DataFrame) -> str:
    lines = list()
    text = ""
    newline = ""
    frame = getUsers("data.csv")
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines:
        match = re.search(r"&\w+", line)
        if match:
            start, end = match.span()
            match line[start:end]:
                case "&name":
                    newline = line[:start] + name + line[end:]
                case "&category":
                    category = (df.query(f"Name == '{name}'")["Category"]).values[0]
                    newline = line[:start] + category + line[end:]
                case "&bursaries":
                    site_values = frame.loc[frame["Site"].str.contains(str(df.query(f"Name == '{name}'")["Category"].values[0])), ["Site"]] #this returns a dataframe where the category from the Users is matched with the category of the bursaries
                    newlist = [row["Site"] for index, row in site_values.iterrows()]
                    for l in newlist:
                        newline += l + "\n"
                case _:
                    newline = line
        else:
            newline = line
        text += newline
    return text

def getSitesForUser(name: str) -> pd.DataFrame:
    frame = getUsers("data.csv")
    site_values = frame.loc[frame["Site"].str.contains(str(df.query(f"Name == '{name}'")["Category"].values[0])), ["Site"]]
    merged_df = pd.merge(frame, site_values, on="Site", how="right")
    return merged_df

text = formatLetter("test.txt", "Tim", "S", df)
print(text)