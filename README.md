 
 Handwritten-Digit-Recognition
 
 This project focuses on the implementation and development of handwritten digit recognition algorithm (back-propagation) using
 Artificial Neural Networks. It is a classification problem solved using aforementioned algorithm. A total of 400 input layers are used,
 corresponding to each pixel of the image and 10 output layers, corresponding to each digit from 0-9. The number of nodes in each hidden
 layer have been set to 25. The implementation of the same is done on Matlab, using Octave-GUI 4.2.1. ANN model was trained with 5000
 images of various digits. The algorithm predicted English numerical digits with a maximum accuracy of 99.98%.

 Approach
 The proposed Neural Network Architecture consists of 3 layers i.e. input layer, hidden layer and the output layer. The input and the
 hidden layer is connected by weights theta1 and the hidden and the output layer is connected by weights theta2. The weighted sum from
 the hidden as well as the output layer can take any value ranging from 0 to infinity and hence in order to limit the value of the sum
 it’s passed through an activation function. In this scenario we use sigmoid function as the activation function where the value of
 sigmoid function always lies between 0 and 1.


 A. Input Layer The input from the outside world/user is given to the input layer. Input is given in the form of a matrix X where the
 number of training examples is same as the number of rows in the matrix and the 400 pixels extracted from the image is arranged as one
 single row in the input matrix X. Hence the dimensions of matrix is given as X (Number of Training Examples x 400).

 B. Hidden Layer There is no valid formula to calculate the number of units/nodes in the hidden layer. To minimize computational costs
 here the number of hidden nodes have been taken as 25.


 C. Output Layer The output layer in this algorithm consists of 10 units with each unit representing various digits from 0-9. Randomly
 initialize the weights


 The weights connecting the input and the hidden layer as well as the hidden and the output layer are randomly initialized. The range of
 the weights are as given in Table


 Forward Propagation
 
 Step-1: The inputs given to the input layer is multiplied with the weights connecting the input and the hidden layer and then passed
 through sigmoid function. i.e. - Output one = SIGMOID(XTheta_layer_one) Step-2: The Output_one is then multiplied with the weights
 connecting the hidden and the output layer and then passed through the sigmoid function. i.e.Output_two = SIGMOID
 (Output_oneTheta_layer_two) Hence this way we clearly obtain the final output of our network.

 Cost Function
 Initial value of the cost function is calculated using the randomly initialized values of weights connecting the input and the hidden
 layer and weights connecting the hidden and the output layer. Error regularization is taken into account while calculating the value of
 cost function and adjustments are made for the same.

 Back Propagation
 Back-propagation gives us a way to determine the error in the output of a previous layer given the output of a current layer. The
 process starts at the last layer and calculates the change in the weights for the last layer. Then we can calculate the error in the
 output of the previous layer. Using the error in each layer partial derivatives can be calculated for weights connecting the input and
 the hidden layer as well as weights connecting the hidden and the output layer.

 1. The Main file in HandWriting.m
 Run Handwriting.m in either octave/MATLAB to execute the program.
 
 2. The file convert_png_image_to_matlab_dataset.py contains a function imageprepare which converts a png image to matlab data. 
 
 3. The file 'randweight.m' randomly initializes the weights.
 
 4. The file 'displayData.m' is used to display the digits. 
 
 5. The file 'sigmoid.m' defines the sigmoid function. 
 
 6. The file 'sigmoidGradient.m' is used to apply sigmoid function.
 
 7. The file 'predictdigit.m' is used to predict the digit. 
