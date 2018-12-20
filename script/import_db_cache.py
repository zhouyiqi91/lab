from django.contrib.auth import authenticate
from django.contrib.auth.models import User,Group

#from lab.models import Employee

import sys

#User = get_user_model()

csv_file = "sgr_name.csv"
lab_group = Group.objects.get(name='lab')
bioinfo_group = Group.objects.get(name='bioinfo')
xingzheng_group = Group.objects.get(name='admin')
manage_group = Group.objects.get(name='manage')

with open(csv_file,"r") as infile:
    for line in infile:
        attr = line.split(",")
        for i in range(len(attr)):
            attr[i] = attr[i].strip()
        entry1 = User(username=attr[2],last_name=attr[0],is_staff=True,is_active=True)
        entry1.set_password("sgr123456")
        entry1.save()
        #entry2 = Employee(user=entry1,department=attr[1])
        #entry2.save()
        if attr[1] == "lab":
            lab_group.user_set.add(entry1)
        elif attr[1] == "xingzheng":
            xingzheng_group.user_set.add(entry1)
        elif attr[1] == "manage":
            manage_group.user_set.add(entry1)
        elif attr[1] == "bioinfo":
            bioinfo_group.user_set.add(entry1)





