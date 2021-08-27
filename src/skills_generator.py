

from skills_list_generator import skills_list



import random
def binary_search(arr, low, high, x):
    
    """Search through the skills_list to find relatable skills

    Args:
        arr: a list of skills in format [["skill",[relatable skills]],...]
        low: A beginning of the array
        high: An end of an array
        x: a skill to find
      

    Returns:
      A list of relatable skill
      If nothing is found returns a string


    """
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid][0] == x:
            
            return arr[mid]
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid][0] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        print("Nothing found for ",x)
        return -1
 


def skills_generator(number_lower=3,number_upper=15,skill=random.choice(["Sales",
    "Marketing",
    "Operations",
    "Software engineering",
    "Engineering",
    "Procurement",
    "Analytics",
    "Finance",
    "HR",
    "Legal",
    "Innovation",
    "Teaching",
    "Art",
    "Medicine",
    "culinary skills",
    "Civil engineering",
    "Fashion",
    "Design",
    "Construction",
    "Aviation"])):
    """Generates a random size skillset 

    Args:
        number_lower: a minimum number of skills to find 
        number_upper: a maximum number of skills to find 

      

    Returns:
        A skillset list

    
    """
    skill=random.choice(random_skills)
    list_skills=[skill.lower()]
    number=random.randint(number_lower,number_upper)


    for i in range(number):
        random_n=random.randint(1,9)

        relatable=binary_search(skills_list,0, len(skills_list)-1,skill.lower())
        skill=relatable[1][random_n]
        if skill in list_skills:
            random_n=random.randint(1,9)
            try:
                skill=relatable[1][random_n]
            except:
                continue



        list_skills.append(skill)
    return list_skills
    
    



