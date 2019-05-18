# Model Explainability



### Generally, we can  extract the following insights from sophisticated machine learning models:
* What features in the data did the model think are most important?
* For any single prediction from a model, how did each feature in the data affect that particular prediction?
* How does each feature affect the model's predictions in a big-picture sense (what is its typical effect when considered over a large number of possible predictions)?


### Why are those insights valuable? They can help to:
* Debugging
* Informing feature engineering
* Directing future data collection
* Informing human decision-making
* Building Trust


#### Let explain each of them in detail

##### Debuging
In the real world, data is dirty. While preprocessing this dirty data we add some errors and these errors are **target leakage**

##### Informing Feature Engineering
Proper feature engineering is usually the most effective way to increase model accuracy. Sometimes we do feature engineering only based on our intuition but what if we have hundreds of features and the field is unknown for us? In this case, we need some direction to go.

##### Directing Future Data Collection.
Many businesses and organizations using data science have opportunities to expand what types of data they collect. Collecting new types of data can be expensive or inconvenient, so they only want to do this if they know it will be worthwhile. Model-based insights give you a good understanding of the value of features you currently have, which will help you reason about what new values may be most helpful.

##### Informing Human Decision-Making
In business many important decisions are made by humans. For these decisions, insights can be more valuable than predictions.

##### Building Trust
Many people won't assume they can trust your model for important decisions without verifying some basic facts. This is a smart precaution given the frequency of data errors. In practice, showing insights that fit their general understanding of the problem will help build trust, even among people with little deep knowledge of data science.



