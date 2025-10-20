import sys
import numpy as np                       #for numerical operations
import pandas as pd                      #for data manipulation
import matplotlib.pyplot as plt          #for data visualization
import scipy.stats as stats              #for linear regression
from sklearn import linear_model, metrics          
# form sklearn.metrics import r2_score        #for R squared calculation   this is the error for the future will be solved[ fix it later
from sklearn.preprocessing import StandardScaler  #for scale standardization

from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

def mean_median():
    student_grade=np.array([np.random.randint(50, 101) for _ in range(100)])
    # print("Student Grades Array:" + str(student_grade))
    mean_grade = np.mean(student_grade)
    print("Mean Student Grade: " + str(mean_grade))
    meadian_grade = np.median(student_grade)
    print("Median Student Grade: " + str(meadian_grade))
# mean_median()

#*********************standard deviation and variance***********************
def std_variance(): 
    data = pd.DataFrame({
        'A': np.random.randint(1, 10, 50),
        'B': np.random.randint(1, 100, 50)
    })
    std_dev_A = np.std(data['A'])
    std_dev_B = np.std(data['B'])
    print("Standard Deviation of column A: " + str(std_dev_A))
    print("Standard Deviation of column B: " + str(std_dev_B))
# std_variance()

#*********************percentile*****************************
def percentile():
    data = pd.DataFrame({
        # 'name_student': ['student_' + str(i) for i in range(10)],
        'Scores': np.random.randint(30, 100, 10),
        # "grade_level": np.random.choice(['A', 'B', 'C', 'D'], 10)
    })
    # print(np.percentile(data['Scores'], 25))
    # print(np.percentile(data['Scores'],40))
# percentile()
#*********************data distrinution*****************************

def data_distrinution():
    # mydata=np.random.uniform(0.0, 5.0, 100000)
    # print("Data Distrinution: " + str(mydata))
    # plt.hist(mydata, bins=30, color='green')
    # plt.title('Data Distribution Histogram')
    # plt.xlabel('Value')
    # plt.ylabel('Frequency') 
    #******************Normal data distribution********************88
    # Normal_Data_dist=np.random.normal(5.0, 1.0, 100000)
    # plt.hist(Normal_Data_dist, 100)

    #********************Scatter Plot******************************* 
    # x=np.random.normal(0,1,1000)
    # y=np.random.normal(0,1,1000)
    # plt.scatter(x,y)
    # plt.title('Scatter Plot of Normally Distributed Data')
    #************************Linear Regression*****************************
    x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
    y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
    slope, intercept, r, p, std_err = stats.linregress(x, y)

    def myfunc(x):
        return slope * x + intercept
    mymodel = list(map(myfunc, x))

    print("relationship between x and y: " + str(r))   #correlation coefficient
    # print(f" My new pridiction from  my Model is : {myfunc(10)}")  #pridiction
    plt.scatter(x, y)
    plt.plot(x, mymodel)
    plt.show()
# data_distrinution()


    #************************Polynomial Regression*******************
def polynomial_regression():
     x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
     y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

     my_model=np.poly1d(np.polyfit(x, y, 3))  #3 is degree of polynomial   Just like trained the model(object of y axis)
     myline=np.linspace(1,22,100)             #100 points between 1 and 22 for x axis it is important for smooth curve  (object of x axis)
    #  plt.plot(myline, my_model(myline))
    #  plt.scatter(x, y)   

     print(" My Pridiction from Polynomial Regression is : " + str(my_model(17)))  #pridiction
     print("relationship between x and y: " + str(np.corrcoef(y, my_model(x))[0,1]))   #correlation coefficient (square R)
    #  plt.show()

# polynomial_regression()

def multiple_regression():
    my_dataframe_CSV=pd.read_csv('C:/Users/Nigatie/Downloads/data.csv')
    # print(my_dataframe_CSV.head())
    x_valus=my_dataframe_CSV[["Weight","Volume"]]
    y_valus=my_dataframe_CSV["CO2"]
    # my_regression=linear_model.LinearRegression().fit(x_valus,y_valus)
    # print("Multiple Regression Coefficient: " + str(my_regression.coef_))       #coefficients for Weight and Volume
    # print("Multiple Regression Intercept: " + str(my_regression.intercept_))     #intercept
    # predicted_CO2=my_regression.predict([[2300,1300]])
    # predicted_CO2_2=my_regression.predict([[1500,800]])
    # print("Predicted CO2 Emission for Weight 2300 and Volume 1300: " + str(predicted_CO2))
    # print("Predicted CO2 Emission for Weight 1500 and Volume 800: " + str(predicted_CO2_2))
    #********************** Scale Standardization***********************
    scaledX=StandardScaler().fit_transform(x_valus)
    my_regression=linear_model.LinearRegression().fit(scaledX,y_valus)

    scaled=StandardScaler().fit_transform([[2300,1300],[1500,800]])
    predicted_CO2=my_regression.predict([scaled[0]])


    # print("Scaled X Values: " + str(scaledX))
    print("Predicted CO2 Emission for Weight 2300 and Volume 1300 after Scaling: " + str(predicted_CO2))
   
# multiple_regression()

def train_test():            
    # My ilustratio is 100 customers in shop and thier buying habites
    np.random.seed(2)    #for reproducibility
    x=np.random.normal(3,1,100)   #independant variable
    y=np.random.normal(150, 40, 100)/x   #dependant variable

    #train and test split
    train_x=x[:80]
    train_y=y[:80]

    #test split
    test_x=x[80:]
    test_y=y[80:]

    Poly_model=np.poly1d(np.polyfit(train_x, train_y, 4))  #4 is degree of polynomial
    my_train_linespace=np.linspace(0,6,100)             #100 points between 0 and 6 for x axis it is important for smooth curve
    # plt.plot(my_train_linespace, Poly_model(my_train_linespace))
    # plt.scatter(train_x, train_y, color='b')

    # plt.scatter(test_x, test_y, color='r')
    #Now pridicting the future value
    test_y_pridicted=Poly_model(10)       #The given value is for x = 10 and the output is the pridiction of y
    print("Test Y Pridicted: " + str(test_y_pridicted))
    # plt.show()
# train_test()

def decision_tree():
    read_CSV=pd.read_csv(r"C:\Users\Nigatie\Documents\Files (2)\Files\Practice\pythone\Dataset_Files/note.txt")
    # print(read_CSV.head())
    #Mapping non numerical value to numerical value by map method
    map_nationality={"UK":0, "USA": 1, "N":2}
    map_Go={"YES":1, "NO": 0}
    read_CSV["Nationality"]=read_CSV["Nationality"].map(map_nationality)
    read_CSV['Go']=read_CSV["Go"].map(map_Go)
    # print(read_CSV.head())

    features=["Age", "Experience", "Rank", "Nationality"]
    x=read_CSV[features]
    y=read_CSV["Go"]
    print(x)
    # print(y)

    # my_data_tree=DecisionTreeClassifier().fit(x, y)
    # tree.plot_tree(my_data_tree, feature_names=features)

# decision_tree()

#*****************Confusion Matrix******************
def confusion_matrix():
    actual_value=np.random.binomial(1, 0.9, 100)
    predict_value=np.random.binomial(1, 0.9, 100)

    confusion_matrix=metrics.confusion_matrix(actual_value, predict_value)
    confusion_matrix_display=metrics.ConfusionMatrixDisplay(confusion_matrix=confusion_matrix, display_labels=[0, 1])
    confusion_matrix_display.plot()
    plt.show()
# confusion_matrix()

