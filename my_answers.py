import numpy as np
import math

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import keras


# TODO: fill out the function below that transforms the input series 
# and window-size into a set of input/output pairs for use with our RNN model
def window_transform_series(series, window_size):
    # containers for input/output pairs
    X = []
    y = []
    
    num_windows = len(series) - window_size
    for i in range(num_windows):
        X.append(series[i : i + window_size])
        y.append(series[i + window_size])
    

    # reshape each 
    X = np.asarray(X)
    X.shape = (np.shape(X)[0:2])
    y = np.asarray(y)
    y.shape = (len(y),1)

    return X,y

# TODO: build an RNN to perform regression on our time series input/output data
def build_part1_RNN(window_size):
    lstm_size=5
    model = Sequential()
    model.add(LSTM(lstm_size, input_shape=(window_size,1), activation='tanh'))
    model.add(Dense(1, activation='tanh'))
    
    return model
         


### TODO: return the text input with only ascii lowercase and the punctuation given below included.
def cleaned_text(text):
    # anscii word
    # A~Z  65~90
    # a~z  97~122
    punctuation = ['!', ',', '.', ':', ';', '?']
    text = ''.join([c if isLetter(c) or (c in punctuation) else ' ' for c in text])

    return text

def isLetter(c):
    if (65 <= ord(c) <= 90) or (97 <= ord(c) <= 122):
        return True
    else:
        return False

### TODO: fill out the function below that transforms the input text and window-size into a set of input/output pairs for use with our RNN model
def window_transform_text(text, window_size, step_size):
    # containers for input/output pairs
    inputs = []
    outputs = []
    
    for i in range(0, len(text) - window_size, step_size):
        inputs.append(text[i : i + window_size])
        outputs.append(text[i + window_size])

    return inputs,outputs

# TODO build the required RNN model: 
# a single LSTM hidden layer with softmax activation, categorical_crossentropy loss 
def build_part2_RNN(window_size, num_chars):
    lstm_size=200
    model = Sequential()
    model.add(LSTM(lstm_size, input_shape=(window_size, num_chars)))
    model.add(Dense(num_chars, activation='softmax'))
    
    return model