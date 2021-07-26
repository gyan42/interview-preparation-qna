# DL
- https://github.com/alirezadir/Production-Level-Deep-Learning
- https://github.com/haltakov/natural-language-image-search
- https://github.com/haltakov/prisoners-dilemma-bot
- https://github.com/google/jax
- [A Recipe for Training Neural Networks](https://karpathy.github.io/2019/04/25/recipe/)

- What Is the Difference Between Epoch, Batch, and Iteration in Deep Learning?
- What Is Data Normalization, and Why Do We Need It?
    - Text normalization : abbreviations, remove duplicates
    - DF[age, income] where age <<< income, but equally important
        ```
        from sklearn import preprocessing
        std_scale = preprocessing.StandardScaler().fit(train_norm)
        x_train_norm = std_scale.transform(train_norm)
        ```
    - Gradient oscillations
    - Min-Max Scaling: `x normalized = (x – x minimum) / (x maximum – x minimum)`
    - Standard score: `(X - mean) / std deviation`
- What Is the Role of Activation Functions in a Neural Network?
    - Without AF(`Y = AF(Z)`),  `Y = Z = WX + bias` is equal to linear equaation
    - Decide neuron fire value range `AF(WX)`
    - Continuous
        - Sigmoid (0,1)
        - Tanh (-1,1)
        - Softmax [0,1) probabilities sums to 1
    - Discreet
        - Step
        - Relu and family [0, inf)
          - Less computation
          - Dying cells, leaky relu is used to overcome this  
          - No vanishing gradient but can blow up gradient
- What Is the Cost/Loss/Error Function?
    - Measure teh diff between predicted and actual value
-  What Do You Understand by Backpropagation?
    - Uses partial derivative to find the error portion for each neuron in the network and adjust its weights
- FFN vs RNN
    - RNN : has internal memory for past data, due to the feedback loop
    - FNNNN : Signla travels in only one direction
- What Will Happen If the Learning Rate Is Set Too Low or Too High?
    - Low LR : small weight updates
    - High LR: divergent behaviour 
- What Is Dropout?
    - Randomly dropping units to prevent ovrefitting and have generalization
    - Default drop 20%
    - Increses the iterations by factor of 2
- What is covariate shift?
    - An internal covariate shift occurs when there is a change in the input distribution to
      our network. When the input  distribution changes, hidden layers try to learn to adapt to 
      the new distribution. This slows down the training process.
- What is Batch Normalization?
    - `BN(x) = scale factor gamma * Std(X) + scale offset beta`
    - Standardizing the activations of each input variable per mini-batch, 
      such as the activations of a node from the previous layer.
    _ Standardization refers to rescaling data to have a mean of zero and a 
      standard deviation of one, e.g. a standard Gaussian.
    - Reduces number of epochs needed
    - It can have regularize effect also
- Weights intialization?
    - Xavier Initialization keeps zero mean and unit variance by considering sqrt(2/(n_in_neurons + n_out_neirons))
- Optimizers
    - https://ruder.io/optimizing-gradient-descent/
- Why Adam optimizer?
    - https://www.geeksforgeeks.org/intuition-of-adam-optimizer/
    - Gradient Descent + RMSP
    - Adam learns the learning rates itself, on a per-parameter basis. 
    


### RNN / LSTM
- https://d2l.ai/chapter_recurrent-modern/lstm.html
- https://colah.github.io/posts/2015-08-Understanding-LSTMs/
- https://www.analyticsvidhya.com/blog/2017/12/fundamentals-of-deep-learning-introduction-to-lstm/?utm_source=blog&utm_medium=comprehensive-popular-deep-learning-interview-questions-answers
- LSTM
    - Forget gate : f_t -> Sigmoid + point wise multiplication
    - Input gate layer: C_t -> sigmoid * tanh + point wise sum
    - Hidden state : sigmoid * tanh(c_t)
    
- What is Overfitting and Underfitting, and How to Combat Them?
    - Complex network, less data
    - Complex data, simpler network
- How Does an LSTM Network Work?
    - Step 1: The network decides what to forget and what to remember.
    - Step 2: It selectively updates cell state values.
    - Step 3: The network decides what part of the current state makes it to the output
- What Are Vanishing and Exploding Gradients?
    - Vanisheing when gradient are too small
    - Exploding: When the gradient are high
- Why is GRU faster as compared to LSTM?
- Backpropagation Through Time in Detail?
    - https://en.wikipedia.org/wiki/Backpropagation_through_time
  
## CNN
- What’s the difference between valid and same padding in a CNN?
    - Valid paddings: Output image will have less dimensions `(n – f + 1) X (n – f + 1)`
    - Same padding: Adds pixels to corners to get same put  dimensions
    
- What is GANS?
    - Generator
    - Discriminator


## Transformers
  - Keys, Query, VAlues @ https://d2l.ai/chapter_attention-mechanisms/attention-cues.html
  - Illustration