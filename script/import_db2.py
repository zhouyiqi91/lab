from django.contrib.auth import authenticate
from django.contrib.auth.models import User,Group

from lab.models import Project

csv_file = "data.csv"
sgr_name = "sgr_name.csv"
name_dic = {}
with open(sgr_name,"r") as namefile:
   for line in namefile:
        attr = line.split(",")
        for i in range(len(attr)):
            attr[i] = attr[i].strip()
        pinyin = attr[2]
        zhongwen = attr[0]
        name_dic[zhongwen] = pinyin


with open(csv_file,"r") as infile:
    for line in infile:
        attr = line.split(",")
        for i in range(len(attr)):
            attr[i] = attr[i].strip()
        name = attr[1]
        if attr[0][0] == "P":
            p_type = "P"
        elif attr[0][0] == ("R"):
            p_type = "RD"
        peoples = attr[2].split("、")
        p_date = attr[3]
        description = attr[4]
        p_id = attr[0]

        entry2 = Project.objects.create(name=name,project_type=p_type,project_date=p_date,description = description,p_id =p_id)
        for people in peoples:
            pinyin = name_dic[people]
            lab = User.objects.get(username=pinyin)        
            entry2.lab_people.add(lab)
        bioinfo = User.objects.get(username="hulongfei") 
        entry2.bioinfo_people.add(bioinfo)

