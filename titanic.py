import pandas

data = pandas.read_csv('C:\\Users\\ASUS-PC\\Downloads\\titanic.csv', index_col='PassengerId')

print data.head()
print "--------------------------"
femalde_data = data.loc[data['Sex'] == "female"]

print data.count()
print data["Sex"].value_counts()

# print data["Age"].median()
# d = data["Age"].mean()
# print round(d, 3)

d = data["Survived"].value_counts();
sum = 0.0
for i in d:
    sum += i
#print d
#print round(d[1] / sum, 4)

def parse_name(name):
    if name.find("Mrs"):
        return name.split(". ", 1)[1].split(" ")[0].replace("(", "").replace(")", "")
    if name.find("Lady") != -1:
        return name.split("(")[1].split(" ")[0]
    if name.find("Miss.") != -1:
        return name.split("Miss.", 1)[1].split(" ")[1]
    if name.find("Mrs.") != -1 & name.find("(") != -1:
        return name.split("Mrs.", 1)[1].split("(")[1].split(" ")[0]
    if name.find("Mrs.") != -1:
        return name.split("Mrs.", 1)[1]


#print femalde_data



