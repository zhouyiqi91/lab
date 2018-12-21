from django.contrib.auth.models import User,Group

from lab.models import Project,Sample

csv_file = "/SGRNJ/Database/test/1.11/data/wushuang_sample16.csv"

with open(csv_file,"r") as infile:
    index = 0 
    for line in infile:
        index +=1
        #line =line.decode("ascii")
        attr = line.split(",")
        for i in range(len(attr)):
            attr[i] = attr[i].strip()
        if index == 1:
            print "CONTINUE!!!!!!!!!"
            continue
        name = attr[1]
        project_id = attr[0]
        description = attr[3]
        library_id = attr[2]
        library_type = "scRNA_SCOPE"
        species = attr[4]

        project = Project.objects.get(p_id=project_id)
        sample_date = "2018-12-21"

        entry = Sample.objects.create(name=name,library_type=library_type,species=species,library_id=library_id,sample_date=sample_date,project=project,description=description)

        #sample_date = project.project_date    
        #entry.project.add(project)
        #entry.sample_date.add(sample_date)