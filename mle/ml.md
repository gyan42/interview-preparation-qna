# Machine Learning

- Problem: Dive in with the interviewer and explore what the problem is. Look for edge cases or simple and high-impact parts of the problem that you might be able to close out quickly.
- Metrics: Once you have determined the scope and parameters of the problem you’re trying to solve, figure out how you will measure success. Focus on what is important to the business and not just what is easy to measure.
- Data: Figure out what data is available to solve the problem. The interviewer might give you a couple of examples, but ask about additional information sources. If you know of some public data that might be useful, bring it up here too.
- Labels and Features: Using the data sources you discussed, what features would you build? If you are attacking a supervised classification problem, how would you generate labels? How would you see if they were useful?
- Model: Now that you have a metric, data, features, and labels, what model is a good fit? Why? How would you train it? What do you need to watch out for?
- Validation: How would you make sure your model works offline? What data would you hold out to test your model works as expected? What metrics would you measure?
- Deployment and Monitoring: Having developed a model you are comfortable with, how would you deploy it? Does it need to be real-time or is it sufficient to batch inputs and periodically run the model? How would you check performance in production? How would you monitor for model drift where its performance changes over time?



- https://medium.com/analytics-vidhya/preparing-for-interview-on-machine-learning-3145caeea06b

- Classification Evaluation Metric
    - https://www.kaggle.com/ishivinal/machine-learning-model-evaluation-metrics
    - Accuracy
    - Precision
    - Recall
    - F1 Score
    - AUC - ROC Curve
    - Logistic Loss
- Regression Evaluation Metric
    - MSE
    - RMSE
    - MSLogError
    - RMSLogError
- Cross Validation
    - KFold
    - StritifiedKFold
    - LOOCV
 ![img.png](../images/metrics.png)

 One important distinction between MAE & RMSE that I forgot to mention earlier is that minimizing 
 the squared error over a set of numbers results in finding its mean, and minimizing the absolute 
 error results in finding its median. This is the reason why MAE is robust to outliers whereas 
 RMSE is not. This answer explains this concept in detail.
- https://www.quora.com/How-would-a-model-change-if-we-minimized-absolute-error-instead-of-squared-error-What-about-the-other-way-around
- https://medium.com/usf-msds/choosing-the-right-metric-for-evaluating-machine-learning-models-part-2-86d5649a5428
  

- https://elvissaravia.substack.com/p/10-must-read-ml-blog-posts

