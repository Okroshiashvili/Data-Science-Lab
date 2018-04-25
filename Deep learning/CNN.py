"""
Created on Sun Mar 25 14:40:03 2018

@author: Nodar.Okroshiashvili
"""

"""
Convolutional Neural Network

"""

#%%

# Part I

# Building Convolutional Neural Network



# Importing Keras libraries
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

# Each package involves each step of building CNN


#%%

# Initialize the CNN
classifier = Sequential()


#%%


# Step - 1
# Adding the layers
# First layers is convolutional layer

classifier.add(Conv2D(32, (3, 3), input_shape = (64, 64, 3), activation = "relu"))


#%%

# Step - 2
# Pooling


# applying max-pooling each of feature map
classifier.add(MaxPooling2D(pool_size = (2,2)))

#%%

"""
This is to improve performance on test set

"""
# We apply this layer to the pooled feature maps

# Improve the performance on test set by adding one more convolutional layer
classifier.add(Conv2D(32, (3, 3), activation = "relu"))
classifier.add(MaxPooling2D(pool_size = (2,2)))



#%%

# Step - 3
# Flattening


# We take all feature maps and put them into vector
classifier.add(Flatten())


#%%

# Step - 4
# Full connection


# Make classic ANN composed with some fully connected layers
# Add fully connected layer
classifier.add(Dense(units = 128, activation = "relu"))

# Layer for output
classifier.add(Dense(units = 1, activation = "sigmoid"))

#%%


# Compile the CNN


classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics=['accuracy'])
# if we had more than three outcome we use categorical cross entropy for loss function

#%%


# Image pre-processing


# image augmentation process


from keras.preprocessing.image import ImageDataGenerator


train_datagen = ImageDataGenerator(
                                    rescale=1./255,
                                    shear_range=0.2,
                                    zoom_range=0.2,
                                    horizontal_flip=True)


test_datagen = ImageDataGenerator(rescale=1./255)


training_set = train_datagen.flow_from_directory(
                                                'dataset/training_set',
                                                target_size=(64, 64),
                                                batch_size=32,
                                                class_mode='binary')

test_set = test_datagen.flow_from_directory(
                                            'dataset/test_set',
                                             target_size=(64, 64),
                                             batch_size=32,
                                             class_mode='binary')



# Apply CNN to the dataset
classifier.fit_generator(training_set,
                    steps_per_epoch=8000,
                    epochs=25,
                    validation_data=test_set,
                    validation_steps=2000)

#%%

# Improve the performance on test set

# We can improve the results on test set by using two ways.
# one is to add one more convolutional layer
# second is to add one more fully connected layer
# If we want even better accuracy we have to increase target_size parameter

