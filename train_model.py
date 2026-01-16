import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


BASE_PATH = r"C:\Users\kavi vala\Desktop\superstore dashbord"
df = pd.read_csv(f"{BASE_PATH}\\data\\Superstore_Management_System_Generated.csv")


X = df[["Quantity Sold","Discount"]]
y = df["Sales"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestRegressor(n_estimators=200)
model.fit(X_train, y_train)


pickle.dump(model, open(f"{BASE_PATH}\\model\\sales_model.pkl","wb"))
print("✅ ML Model Trained")