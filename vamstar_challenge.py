import pandas as pd

data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]
#we transform the data into a data frame
df = pd.DataFrame.from_dict(data, orient= 'columns')

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


#Then we can calculate the new columns for our data frame using the previous fucntions.
df['BMI'] = df.apply(lambda row: bmi(row['HeightCm'], row['WeightKg']), axis = 1)
df['BMI_category'] = df.apply(lambda row: bmi_category(row['BMI']), axis = 1)
df['Health_risk'] = df.apply(lambda row: bmi_risk(row['BMI']), axis = 1)
#print(df)

#count number of overweight people
n = df[df['BMI_category'] == 'Overweight'].shape[0]
print(" There are "+ str(n) + " Overweight people into the data")




