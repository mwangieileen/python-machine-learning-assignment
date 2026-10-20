#Importing Libraries
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#Preparing Data while separating input feautures(x) and target values(y): features=x(hours studied),labels=y(exam score)
x=[[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
y=[30,40,45,55,65,70,80,85,90,95]

#Creating Linear Regression Model
model=LinearRegression()

#Prediction
model.fit(x,y)

#Allow user to enter number of hours studied
hours=float(input("Enter hours studied:"))
prediction=model.predict([[hours]])
print("Predicted exam score:",round(prediction[0],2))

#Visualization on matplot
#creating scatter plot
plt.scatter(x,y,label="Training Data")

#adding regression line
plt.plot(x,model.predict(x),color="red",label="Line of best fit")

#add prediction on graph with separate colour
plt.scatter(hours,prediction,color="yellow",label="Prediction")

#labelling
plt.xlabel("Study Hours")
plt.ylabel("Examination Scores")
plt.title("Relationship between study hours and examination scores")
plt.legend()

#display
plt.show()
