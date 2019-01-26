"""
Created on Sun Mar 11 18:07:18 2018

@author: Nodar.Okroshiashvili
"""
#%%

"""

Natural Language Processing

"""
#%%

# Import the libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Open the dataset

dataset = pd.read_csv('data/Restaurant_Reviews.tsv', delimiter = '\t', quoting = 3)

# "quoting=3" ignores double quotes in the dataset as it can create some problems
# For NLP generally, it's better to use tab delimited file as comma separated values
# CSV may arise some problems while reading file
 

#%%

"""

Our mission is to create model that will predict new review is positive or negative

"""


# Cleaning the texts


# import libraries to clean the text

import re

# Firstly, we clean first observation and then by using for loop we'll do it 
# for all observation


# In the first step we'll remove all the numbers and punctuations
# We keep only latter from A to Z

review = re.sub('[^a-zA-Z]',' ', dataset['Review'][0])
# First parameters means we don't want to remove letters
# Second parameter puts space, so we don't have two words stuck together
# Third parameter is where we want to remove all but not letters

#%%

# Second step of the cleaning process is to set all the letters as lower case

review = review.lower()


#%%

# At third step we remove non-significant words
# We need to import nltk library to remove unuseful words

import nltk
nltk.download('stopwords')

# We need to split review into different words
review = review.split() # It is now list

# List comprehension to remove unnecessary words
from nltk.corpus import stopwords

"""
Here, also we incorporate fourth step which is stemming.
This means we take the root of the words, or we convert words into original form

"""

from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()



review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
# We add set function as python sets are much faster than lists

#%%

# We have to join everything back and have one string containing three words

review = ' '.join(review)

#%%

# Now let apply all these steps to the whole dataset

# import libraries
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()



corpus = []
for i in range(0, 1000):
    review = re.sub('[^a-zA-Z]',' ', dataset['Review'][i])
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)


#%%
    
# Create Bag of Words Model
    
"""
Tokenization is the process of taking all the different words of the review and creating one column for each word.

Matrix with lots of zeros is sparse matrix and this fact is sparsity.
We try to minimize sparsity.

We'll create The Bag of Words Model through the tokenization

"""


# We have to import count vectorization class

from sklearn.feature_extraction.text import CountVectorizer

# Create class object
cv = CountVectorizer(max_features = 1500)

# Apply the model to our corpus
# We'll create now sparse matrix, putting all the different words in different columns 
X = cv.fit_transform(corpus).toarray()  

"""
Our sparse matrix has 1000 line and 1565 words in it.
By using max_features parameter we can even filter our corpus to remove irelevant words.

Passing max_feature parameter and setting it to 1500 we get new matrix consisting of 1500 columns.

"""

# We don't have dependent variable, so we need to add it
y = dataset.iloc[:, 1].values

#%%

"""
Here we create classification model to predict the out of review
whether it is positive or negative



In sparse matrix each line corresponds to one specific review and each column
corresponds to one word for those specific reviews.

"""


# Let apply Naive Bayes model to the bag of words



from sklearn.cross_validation import train_test_split


# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)


#%%

# Fitting Naive Bayes to the Training set
from sklearn.naive_bayes import GaussianNB

# Define classifier object
classifier = GaussianNB()

# Fit the model
classifier.fit(X_train, y_train)


#%%

# Predicting the Test set results
y_pred = classifier.predict(X_test)

#%%

# Make the Confusion Matrix

from sklearn.metrics import confusion_matrix

# Create confusion matrix
cm = confusion_matrix(y_test, y_pred)

#%%
