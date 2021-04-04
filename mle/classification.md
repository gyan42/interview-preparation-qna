# Classification

- Interview Q&A:
  - https://www.interviewquery.com/questions/bank-fraud-model
  ```
  false positive ( fraud undetected )
  false negative costs ( alarming the customer without cause )
  when a transaction’s fraud probability is high, the text is sent.
  
  Interpretbility in financial models is important, I would suggest a regression model 
  whose output can be mapped to a probability distribution ( for example logistic regression accomplishes this). 
  Developers and stakeholders can then diagnose the contributions of individual features.
  
  Metric: we want to minimize the negative log likelihood on the held-out set. This leads to a minimal divergence 
  between the predicted fraud probability distribution with the true distribution.
  ```
  
- https://www.analyticsvidhya.com/blog/2020/06/auc-roc-curve-machine-learning/
- https://medium.com/usf-msds/choosing-the-right-metric-for-evaluating-machine-learning-models-part-2-86d5649a5428