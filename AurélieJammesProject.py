''' Toulouse Business School MSc AIBA

Course: Python for Data Science -- PROJECT
Author: YOUR NAME HERE
Version: v1.0
'''

"""
PROJECT INSTRUCTIONS
---
Your project shoud :
- import at least one of the following packages:
    - matplotlib
    - pandas
- load the dataset into a pandas DataFrame
- have at least one variable defined and printed
- print a filtered dataframe with a comparison operator
- print a filtered dataframe with a boolean operator
- have a for-loop to create a new column to the DataFrame
- display a plot:
    - either a line-plot, a scatter-plot, or a histogram-plot
    - with x-axis and y-axis labels
    - with a title
- have some comments
"""

def main():
    print("Starting the project...")
    
    # WRITE YOUR CODE HERE
    
    #import packages
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd
    
    #load the dataset into a pandas DataFrame
    HR_employee = pd.read_csv("/Users/aureliejammes/Desktop/AIBA/Programming/Python for data science/Project Python/HR-Employee-Attrition.csv",index_col=0)
    print(HR_employee) # I use print() to check the database
    
    # have at least one variable defined and printed
    variable_1 = 1999
    print(variable_1)
    
    
    # print a filtered dataframe with a comparison operator
    # we want to select from the database only those employees who were last promoted less than two years ago. 
    YearsSinceLastPromotion=HR_employee["YearsSinceLastPromotion"]
    print(YearsSinceLastPromotion)
    recent_promotion=YearsSinceLastPromotion<2
    print(recent_promotion)
    print(HR_employee[recent_promotion])
    
    
    # print a filtered dataframe with a boolean operator
    # we want to select from the database only those employees who whose motivation is between 2 and 4.
    JobInvolvement=HR_employee["JobInvolvement"]
    print(HR_employee[np.logical_and(JobInvolvement > 2, JobInvolvement < 4)])
    
    
    # have a for-loop to create a new column to the DataFrame
    # we will add a new column with the number of letter in the the column "EducationField".
    HR_employee["EducationField_length"]= HR_employee["EducationField"].apply(len)
    print(HR_employee)
    
    
    # display a plot 
    # We are going to display a plot to answer the question "are employees far from their job ?"; 
    # the best plot to represent it is an histogram
    plt.hist(HR_employee["DistanceFromHome"], bins=10)
    # we are going to add the titles of the axes, and the title of the plot
    plt.xlabel("Distance from home")
    plt.ylabel("Number of employee")
    plt.title("Distribution of distance from employees' home")
    #Now we can display the plot
    plt.show()
    
    
    print("... project ended.")

if __name__ == '__main__':
    main()
