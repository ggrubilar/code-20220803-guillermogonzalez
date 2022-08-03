#This file contains the functions that we created.

# First we create a function that labels our data based on bmi categories from the table
def bmi_category(bmi):
    if bmi < 18.5:
        label_category = "Underweight"
    elif bmi >= 18.5 and bmi < 25:
        label_category = "Normal weight"
    elif bmi >= 25 and bmi < 30:
        label_category = "Overweight"
    elif bmi >= 30 and bmi < 35:
        label_category = "Moderately obese"
    elif bmi >= 35 and bmi < 40:
        label_category = "Severely obese"
    elif bmi >= 40:
        label_category = "Very severely obese"
    return label_category

# We do the same for health risk labeling
def bmi_risk(bmi):
    if bmi < 18.5:
        label_risk = "Malnutrition risk"
    elif bmi >= 18.5 and bmi < 25:
        label_risk = "Low risk"
    elif bmi >= 25 and bmi < 30:
        label_risk = "Enhanced risk"
    elif bmi >= 30 and bmi < 35:
        label_risk = "Medium risk"
    elif bmi >= 35 and bmi < 40:
        label_risk = "High risk"
    elif bmi >= 40:
        label_risk = "Very high risk"
    return label_risk


# We also create a function to calculate BMI.
# We can check that Height is not zero to avoid division by zero problems
# In reality Height or weight shouldn't be zero

def bmi(HeightCm, WeightKg):
    if HeightCm == 0:
        print("This expression is not defined. Height can't be 0")
    else: 
        bmi = WeightKg/((HeightCm/100)**2)
        bmi = round(bmi, 2)
    return bmi