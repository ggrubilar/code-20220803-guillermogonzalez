import pandas as pd
import json 
from utils import bmi_category, bmi_risk, bmi

#Read data from Json file
with open("data.json", "r") as rf:
    data = json.load(rf)
    print(data)
#we transform the data into a data frame
df = pd.DataFrame.from_dict(data, orient= 'columns')

#we can calculate the new columns for our data frame using the previous fucntions.
df['BMI'] = df.apply(lambda row: bmi(row['HeightCm'], row['WeightKg']), axis = 1)
df['BMI_category'] = df.apply(lambda row: bmi_category(row['BMI']), axis = 1)
df['Health_risk'] = df.apply(lambda row: bmi_risk(row['BMI']), axis = 1)
#print(df)

#count number of overweight people
n = df[df['BMI_category'] == 'Overweight'].shape[0]
print(" There are "+ str(n) + " Overweight people into the data")
