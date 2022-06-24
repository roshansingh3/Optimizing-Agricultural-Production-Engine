import pandas as pd
import pickle as pkl
data = pd.read_csv('data.csv')

from sklearn.linear_model import LogisticRegression

y = data['label']
x = data.drop(['label'], axis=1)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

model = LogisticRegression()
model.fit(x_train, y_train)


pkl.dump(model,open('model.pkl','wb'))
y_pred = model.predict(x_test)

a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:7]
l = [a]
pred = model.predict(l)
print("The suggested crop for given climatic conditions is: ",pred)

#[16, 51, 20, 30, 50, 4, 50]