

import json
path="cleaned_related_skills.json"
with open(path) as f:
    json_skills = json.load(f)
    print(json_skills)
skills={}
for i in json_skills:
    skills[i["name"]]=[]
    for s in i:
        if s!="name":
            skills[i["name"]].append(i[s])
skills_list=[]
for key,value in skills.items():
    skills_list.append([key,value])




