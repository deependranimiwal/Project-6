# DataVisualization

## Summary 
This dataset contains demographics and passenger information from 891 of the 2224 passengers and crew on board the Titanic. Our purpose is to analyze this data to get interesting answers of some pertinent questions. We conclude the following points from the visualizations.

1. We notice that upper class was given priority while saving lives, Our visualizations clearly depicts that despite class 3 people were higher in number, they survived less. 

2. Women were also given priority while saving lives. We see huge difference in the mean of survivability of male and female.

3. We do not notice any clear trend in survivability by age group, But we can say that children with age group 0-9 were given priority over elderly people with age group 60-79. 


## Design 

### Dataset information
This dataset is taken from [Kaggle]( https://www.kaggle.com/c/titanic/data?train.csv#) website.  I cleaned the data by removing categories I was uninterested in (passenger name, cabin number, fare). I created new category age_bin for divding the passengers in age groups. Some changes were also made in dataset after taking feedbacks.

### Version 1
Three basic questions arise into my mind while checking the data. In the first set of graph, I plot Gender, Class and Age Group so that our audiance get an overview of the variables. Next each varible is visualized with simple bar graph to check the relation of each variable with survivability. We plot percent bar graph to get a clear picture of their relation.   

### Version 2 (based on feedbacks )
I got many interesting and useful feedbacks. Friend 1 noticed while hovering over the graph you see PassengerId:453, Which is indeed the count of total passengers. For people not to get confused i changed the variable name in data set to 'Passengers' instead of 'PassengersId'. He also suggested i should change "1,2,3" as class name to "first, second, third" . Similarly i also changed "0/1" to "Dead/Alive" by using simple replace function in python. Friend 2 suggested i should try differnt colors. I did research and found new colors can be easily applied with simple myChart.defaultColors function. Friend 3 suggested i should remove background lines, I removed the lines with "y.showGridlines = false" . After all the changes i believe visulizations look much refined and easy to understand.    

## Feedback 
### Feedback #1:

> What do you notice in the visualization?

I can see difference in data overview clearly. I notice how males are in larger number than female. I also see 3 in class has maximum number of passengers. Also maximum number of people are of age group 21-30. 

> What questions do you have about the data?

What is PassengerId?
So 1,2,3 represent class ticket? 

> Is there anyway i can imporve this graphic?

Yes, you should add more discription to this data.

### Feedback #2:
> What do you notice in the visualization?

Is this real? I notice how female survivability is around 70% while male survivability is only around 20%. This won't happen today. Gender equality you see.  
 
> What questions do you have about the data?

This '1' is for alive and '0' is for dead, Why don't you write dead/alive instead of this.

> Is there anyway i can imporve this graphic?

Naa, I got nothing. Can you change colors? I like Purple.

### Feedback #3

> What do you notice in the visualization?

I notice gender differnce in both number and rate of survival. It is quite evident that females were given priority while saving lives. Question second shows us the real face of the world. First class survived more, because rich people were given life boats first right? I really hoped there was a decreasing graph with increasing age.  
 
> What questions do you have about the data?

No, i don't have any questions. Graphs follow a easy to understand pattern for the mentioned questions.
 
> Is there anyway i can imporve this graphic?

You can smooth the graph by removing background lines. 

## Resources 

https://en.wikipedia.org/wiki/RMS_Titanic
http://www.w3schools.com/css/
https://github.com/deependranimiwal/Project-2
