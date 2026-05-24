# multi layer perceptron
# what is a perceptron? -- linear
# very good for non-linear problems that's why we use multi layer perceptron

# activation functions
# sigmoid
# tanh
# ReLU 

# we can have many hidden layers and then there is types of layers which is input layer
# each represents a feature and on the right hand side we have output layer abd we can have 
# have here each node represenrs a class and 

# we use softmax activation function in the output layer for multi class classification problems
# evrynode connects to each other node in the next layer and each connection has a weight associated with it

# in forward direction we lern about the input data and in backward direction we update the weights
#  based on the error/loss between predicted output and actual output

# epoch is a one complete pass through the entire training dataset and we can have multiple 
# epochs to train the model better. 
# we can use small batches in our dataset forward and backward for larger dataset and then we finalize 
# the weights after each batch. we do this multiple times 

# cnn - convolutional neural network is good for image classification and is more efficient
# cnn uses relu activation function and if the value is posrive it will return the same value 
# and if it is negative it will return 0

# rnn - recurrent neural network is good for sequential data like time series and natural language processing

# loss funciion is a measure of how well the model is performing
# learning rate specifies how much we update the weights in the backward pass
 
# the difference between larger and smaller learning rate is that with larger learning rate 
# we can converge faster but we might overshoot the optimal weights and with 
# smaller learning rate we can converge slower but we are less likely to overshoot the optimal weights

# in the validation dataset we can evaluate the model performance and tune the hyperparameters 
# like learning rate, number of hidden layers, number of neurons in each layer, number of epochs,
# batch size, activation function, etc.

# to reduce overfitting we can use regularization techniques like dropout, L1 and L2 regularization (uses
# drop out rate), early stopping, loss function, etc.