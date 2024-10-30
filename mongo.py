import pandas as pd
from pymongo import MongoClient


url = 'https://raw.githubusercontent.com/hantswilliams/HHA-504-2024/refs/heads/main/other/module8/module8_nosql_hw.csv'
df = pd.read_csv(url)


data = df.to_dict(orient='records')


client = MongoClient("mongodb+srv://ferminacy:Kimheechul1@cluster1029.khukt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1029")
db = client.patient_data  
collection = db.patient_records 


try:
    collection.insert_many(data)
    print("Data successfully uploaded to MongoDB!")
except Exception as e:
    print("Error uploading data:", e)




