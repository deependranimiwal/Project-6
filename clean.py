import pandas as pd

titanic_df = pd.read_csv('titanic.csv')

bins = [0, 11, 21, 31, 41, 51, 61, 120]

#group_names = ['< 11', "11 to 20", "21 to 30", "31 to 40", "41 to 50", "51 to 60", "61 to 80"]

titanic_df = titanic_df.drop(['Name','Ticket','Cabin'], axis=1)

titanic_df = titanic_df.dropna(axis=0, how='any', subset=['Age'])

titanic_df['class'] = titanic_df['Pclass']





#After Feedbacks

titanic_df['Passenger'] = titanic_df['PassengerId']

titanic_df['Class'] = titanic_df['Pclass']
titanic_df['Class'].replace({1:'first',2:'second',3:'third'}, inplace=True)


titanic_df['Survivability'] = titanic_df['Survived']
titanic_df['Survivability'].replace({0:'Dead',1:'Alive'}, inplace=True)





group_names = ['0-11', "11-20", "21-30", "31-40", "41-50", "51-60", "61-80"]

titanic_df['age_bin'] =  pd.cut(titanic_df['Age'], bins, labels=group_names)


titanic_df.to_csv('titanic_data.csv',  index=False)