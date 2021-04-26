# Statistics

- [Joint Probability vs Conditional Probability](https://medium.com/@mlengineer/joint-probability-vs-conditional-probability-fa2d47d95c4a)
    - Join porbability of independent events: `P(A and B) = P(A) * P(B)`
    - Conditional probability: The joint probability of two dependent events becomes `P(A and B) = P(A)P(B|A)`
    - Bayes Theorem
      ```
      P(A and B) = P(A)P(B|A) and P(B and A) = P(B)P(A|B)
      P(A)P(B|A) = P(B)P(A|B)
      P(A|B) = P(A) P(B|A) / P(B)
      ```
    - In Machine Learning terms, Change A as Hypothesis and B as Evidence, then
      `P(H|E) = P(H) P(E|H) / P(E)` : “The posterior probability equals the prior probability times the likelihood ratio”
- Bayes Theorem
    - https://betterexplained.com/articles/an-intuitive-and-short-explanation-of-bayes-theorem/
    
- Conditional random field
    - https://towardsdatascience.com/conditional-random-fields-explained-e5b8256da776
    - https://medium.com/ml2vec/overview-of-conditional-random-fields-68a2a20fa541
    - Uses contextual nformation from previous labels
    - Graphical model which implements dependencies between the predictions
    - Discriminative model `P(Y|X)`
    - Graph of dependencies for all Y conditioned on their respective input X

