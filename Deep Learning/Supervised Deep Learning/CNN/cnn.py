"""
Created on Sun Mar 25 2018

@author: Nodar Okroshiashvili
"""



# Convolutional Neural Network




# Part 1 - Building the CNN


# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense



# Each package involves each step of building CNN



# Initialising the Convolutional Neural Network
classifier = Sequential()


# Step 1 - Perform Convolution and add Convolutional Layers

# If Theano Backend "input_shape=(3,64,64)"
# In tensorflow backend "input_shape=(64,64,3)"
# In ANN activation function is used to activate neurons
# In CNN activation function is used to make sure
# we don't have negative pixel values in our feature map
# The first argument in "Conv2D" is how many feature map we want to have
# and second argument is convolution matrix which is 3 by 3
classifier.add(Conv2D(32, (3, 3), input_shape = (64, 64, 3), activation = 'relu'))



# Step 2 - Perform Max Pooling and add layers

# Pooling reduces the size of the feature map
# by applying matrix which picks only maximum element
# in the original feature map
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Adding a second convolutional layer and pooled layer
classifier.add(Conv2D(32, (3, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Step 3 - Flattening - converts pooled and convolved features into one bit vector
classifier.add(Flatten())



# Step 4 - Full connection - responsible for full connection through layers

# Fully connected layer is hidden layer same as in ANN
# Esentially this part is to construct ANN

classifier.add(Dense(units = 128, activation = 'relu'))

# Output layer
classifier.add(Dense(units = 1, activation = 'sigmoid'))
# Adding output layer completes the full connections


# Compiling the CNN
# if we had more than three outcome we use categorical cross entropy for loss function
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])




# Part 2 - Fitting the CNN to the images



# Image preprocessing
# Image augmentation process

from keras.preprocessing.image import ImageDataGenerator


train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)


test_datagen = ImageDataGenerator(rescale = 1./255)


training_set = train_datagen.flow_from_directory('data/training_set',
                                                 target_size = (64, 64),
                                                 batch_size = 32,
                                                 class_mode = 'binary')


test_set = test_datagen.flow_from_directory('data/test_set',
                                            target_size = (64, 64),
                                            batch_size = 32,
                                            class_mode = 'binary')



# Apply CNN to the dataset
classifier.fit_generator(training_set,
                         steps_per_epoch = (8000/32),
                         epochs = 25,
                         validation_data = test_set,
                         validation_steps = (2000/32))








# Part 3 - Making new predictions




# We put new pictures to predict either it is dog or cat


import numpy as np
from keras.preprocessing import image

test_image = image.load_img('data/single_prediction/cat_or_dog_1.jpg', target_size = (64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict(test_image)
training_set.class_indices

if result[0][0] == 1:
    prediction = 'dog'
else:
    prediction = 'cat'


"""
Data file for the CNN was too large to upload.
You can download it from the following links:
[ https://www.kaggle.com/c/dogs-vs-cats/data ]
or
[ https://www.microsoft.com/en-us/download/details.aspx?id=54765 ]
"""



