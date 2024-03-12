import math

def calculate_bmi(height, weight):
    return weight / ((height / 100) ** 2)

def highestAverageBMI(people):
    age_groups = {}
    
    for person in people:
        age_group = math.floor(person['age'] / 5) * 5
        if age_group not in age_groups:
            age_groups[age_group] = []
        age_groups[age_group].append(person)
    
    highest_avg_bmi = 0
    highest_avg_bmi_age_group = ""
    
    for age_group, people_in_age_group in age_groups.items():
        total_bmi = 0
        for person in people_in_age_group:
            bmi = calculate_bmi(person['height'], person['weight'])
            total_bmi += bmi
        avg_bmi = total_bmi / len(people_in_age_group)
        if avg_bmi > highest_avg_bmi:
            highest_avg_bmi = avg_bmi
            highest_avg_bmi_age_group = f"{age_group}-{age_group + 4.9}"
    
    return {'ageGroup': highest_avg_bmi_age_group, 'averageBmi': round(highest_avg_bmi, 2)}
#----------------------------------------------------------------------------------------------------------------------------------------------
# Test cases
print(highestAverageBMI([
    {'height': 175, 'weight': 50, 'age': 21},
    {'height': 170, 'weight': 77, 'age': 22},
    {'height': 175, 'weight': 70, 'age': 24},
    {'height': 175, 'weight': 75, 'age': 26},
    {'height': 175, 'weight': 50, 'age': 29},
    {'height': 170, 'weight': 77, 'age': 34}
]))  
# Output: {'ageGroup': '30-34.9', 'averageBmi': 26.64}

print(highestAverageBMI([
    {'height': 175, 'weight': 50, 'age': 24.9},
    {'height': 170, 'weight': 80, 'age': 25},
    {'height': 170, 'weight': 90, 'age': 29.9},
    {'height': 175, 'weight': 90, 'age': 32},
    {'height': 175, 'weight': 50, 'age': 39},
    {'height': 170, 'weight': 77, 'age': 44}
]))  
# Output: {'ageGroup': '25-29.9', 'averageBmi': 29.41}
