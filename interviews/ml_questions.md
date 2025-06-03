## 🧠 Machine Learning Warm-Up & Practice Questions

Asked in a TestGorilla interview.

### 1. K-nearest neighbors average prediction

**Question:**  
You are applying the K-nearest neighbors regressor and want the value of the new observation to be equal to the average value of all data points.  
**What should be the number of neighbors for the K-nearest neighbor regressor?**

- Number of current data points minus one  
- One  
- Number of current data points  
- Number of current data points plus one  

<details>
<summary>✅ Show answer</summary>

**Answer:** Number of current data points  
**Explanation:** Using all data points as neighbors ensures the prediction is the average of the entire dataset (the number of neighbors K includes all current data points).
</details>

---

### 2. Classification metric for correctly classified observations

**Question:**  
You are applying gender classification and want to estimate the portion of correctly classified observations.  
**Which metric should you use?**

- Accuracy  
- Duality  
- Recall  
- Precision  

<details>
<summary>✅ Show answer</summary>

**Answer:** Accuracy  
**Explanation:** Accuracy measures the proportion of correctly classified instances over the total number of instances.
* *Accuracy:* Number of Correct Predictions / Total Number of Predictions. `(TP+TN)/(TP+TN+FP+FN)`
* *Duality:* Not a standard metric in classification.
* *Recall:* Measures how many actual positives were correctly identified. `TP/(TP+FN)`
* *Precision:* Measures how many predicted positives were correct. `TP/(TP+FP)`
</details>

---

### 3. Residual Sum of Squares (RSS) Evaluation

**Question:**  
You are applying a decision-tree regressor on house prices and have got 12,345 as the value of the residual sum of squares (RSS).  
**How should you find an acceptable value for RSS?**

- Find the lowest price and set it as the minimal threshold for RSS  
- Calculate the average house price and compute the difference  
- Find the highest price and set it as the maximal threshold for RSS  
- Calculate the median house price and compute the difference  

<details>
<summary>✅ Show answer</summary>

**Answer:** Calculate the average house price and compute the difference  
**Explanation:** Comparing RSS to the variance from the mean provides context for the model's error.

The RSS in any regressor measures the total squared difference between predicted and actual values:

$$
RSS = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
$$

Therefore, Lower RSS = better model (less error), but RSS by itself means nothing unless you compare it to a baseline.

None of the options are technically correct for determining an acceptable RSS. However, the most reasonable approach in practice is to compare the RSS to a baseline model, such as a model that always predicts the mean house price.
This lets you judge whether your decision tree regressor is improving prediction accuracy.
</details>

---

### 4. SVM distance metric for geospatial clustering

**Question:**  
You are applying k-means clustering on geospatial data of cities in the USA to determine cities falling in the same climate region. The available data contains latitudes and longitudes of cities.  
**Which distance metric should you use?**

- Manhattan distance using latitude and longitude  
- Correlation coefficient using latitude and longitude  
- Actual distance between the cities using existing roads  
- Euclidean distance using latitude and longitude

<details>
<summary>✅ Show answer</summary>

**Answer:** Euclidean distance using latitude and longitude
**Explanation:** Euclidean distance is commonly used in k-means clustering for continuous variables like coordinates. In this case, we are trying to predict climate, which will correlate to distance between 2 points, not road distance (2 near points will have the same weather even if not connected by roads), manhattan distance (we want to use the actual distance, and not the sum of the components, this is not a grid), correlation coeficient (not for measuring distance, for measuring relationships).
</details>

---

### 5. Linear regression intercept interpretation

**Question:**  
You are applying linear regression on an advertising dataset where you try to predict sales of a product (in units) based on advertising expenditure (in dollars) on TV, radio, and newspaper media. You get a value of 12.34 for β₀.  
**What is the projected sales amount if you don’t spend any money on advertising?**

- 0 units  
- 1.234 units  
- 12.34 units  
- 1,234 units  

<details>
<summary>✅ Show answer</summary>

**Answer:** 12.34 units  
**Explanation:** The intercept β₀ represents the expected value of the dependent variable when all predictors are zero.
$$
\hat{y} = \beta_0 + \beta_1 \cdot 0 + \beta_2 \cdot 0 + \beta_3 \cdot 0 = \beta_0
$$
* ŷ = predicted sales
* β₀ = intercept
* x₁, x₂, x₃ = TV, radio, and newspaper advertising spend
* β₁, β₂, β₃ = corresponding coefficients

If we spend 0 in advertising, all x's will be 0, so the projected sales amount ŷ will be β₀.
</details>

---

### 6. Leave-one-out cross-validation

**Question:**  
You are applying regression analysis on a house price dataset containing information about 121 houses. You want to separately test the model on each house and save the accuracy measure as a single row in a dataframe. You apply leave-one-out cross-validation.  
**What should be the size of the training data in each iteration?**

- 1  
- 12  
- 120  
- 121  

<details>
<summary>✅ Show answer</summary>

**Answer:** 120  
**Explanation:** In leave-one-out cross-validation, one observation is used for testing, and the remaining n-1 for training.
</details>

---

### 7. Number of coefficients in linear regression

**Question:**  
You are applying linear regression on an advertising expenditures dataset where you try to predict sales based on advertising via TV, radio, and newspaper media.  
**How many coefficients will you need to estimate for the linear regression model (including the intercept)?**

- 1  
- 2  
- 3  
- 4  

<details>
<summary>✅ Show answer</summary>

**Answer:** 4  
**Explanation:** One coefficient for each predictor (3) plus one intercept term equals 4 coefficients.
$$
\hat{y} = \beta_0 + \beta_1 \cdot 0 + \beta_2 \cdot 0 + \beta_3 \cdot 0 = \beta_0
$$
* ŷ = predicted sales
* β₀ = intercept
* x₁, x₂, x₃ = TV, radio, and newspaper advertising spend
* β₁, β₂, β₃ = corresponding coefficients
</details>

---

### 8. Regularization for zeroing out coefficients

**Question:**  
You are applying linear regression where you have 15 predictors. You want to identify the predictors that are not important for the model and assign a coefficient of 0 to them.  
**Which regularization approach should you use to achieve this?**

- Ridge regression  
- Ordinary least squares regression  
- Lasso regression  
- Elastic net regression  

<details>
<summary>✅ Show answer</summary>

**Answer:** Lasso regression  
**Explanation:** Lasso regression uses L1 regularization, which can shrink some coefficients to exactly zero, effectively performing feature selection.

$$
\text{Loss} = \text{RSS} + \lambda \sum_{j=1}^{p} |\beta_j|
$$

Every time we need to do variable selection, we use L1/Lasso. The L1 penalty encourages sparsity — meaning some coefficients become exactly zero, effectively performing feature selection.

* Ridge regression: Uses L2 regularization, which shrinks coefficients but does not make them exactly zero.
* Ordinary least squares (OLS): No regularization — it fits all predictors without penalizing complexity, so it uses all variables. May overfit.
* Elastic net regression: Combines L1 and L2 penalties. It can set coefficients to zero like Lasso, but it’s more complex and often used when predictors are highly correlated.
</details>

---

### 9. Parameter estimation method for logistic regression

**Question:**  
You are applying classification with logistic regression on a dataset of two classes and you want to estimate the values of parameters to use in the model.  
**Which mathematical method should you use?**

- Maximum odds  
- Maximum likelihood  
- Method of moments  
- Naive Bayes  

<details>
<summary>✅ Show answer</summary>

**Answer:** Maximum likelihood  
**Explanation:** Logistic regression parameters are estimated using maximum likelihood estimation to find the best-fitting model.

When applying logistic regression for classification, the goal is to estimate the parameters (coefficients) that make the observed data most probable under the model. This is done using MLE. 

Logistic regression models the probability of a class (e.g., class 1 vs class 0):
$$
P(y=1 \mid \mathbf{x}) = \frac{1}{1 + e^{-(\beta_0 + \beta_1 x_1 + \dots + \beta_n x_n)}}
$$

We want to find the parameters β that maximize the likelihood of the observed data.

Logistic regression parameters are estimated by maximizing the likelihood function:

$$
L(\beta) = \prod_{i=1}^{n} P(y_i \mid \mathbf{x}_i; \beta)
$$

Or, more commonly, maximizing the log-likelihood:

$$
\log L(\beta) = \sum_{i=1}^{n} \left[ y_i \log(p_i) + (1 - y_i) \log(1 - p_i) \right]
$$

Where:

$$
p_i = \frac{1}{1 + e^{-\mathbf{x}_i^T \beta}}
$$

* Maximum odds: Not a real statistical estimation method. The odds are used in logistic regression, but we don’t maximize them.
* Method of moments: Used in some statistical models, but not standard for estimating logistic regression parameters.
* Naive Bayes: A different classification algorithm that uses Bayes’ theorem with the assumption of conditional independence. It’s not a parameter estimation method for logistic regression.
</details>

---

### 10. Selecting SVM model based on margin

**Question:**  
You are applying classification with the help of support vector machines. The data is not linearly separable; thus, you fit four different models that provide solutions. They have the same amount of slack variables but with different values of margins. The results are shown below.
| Model   | Value of Margin |
|---------|-----------------|
| 1       | 1.2             |
| 2       | 2.3             |
| 3       | 3.3             |
| 4       | 4.0             |


**Which of the models should you choose for the final analysis?**

- 1  
- 2  
- 3  
- 4  

<details>
<summary>✅ Show answer</summary>

**Answer:** 4  
**Explanation:** A larger margin in SVM generally leads to better generalization, assuming equal slack variables.

In Support Vector Machines (SVM), the objective is to maximize the margin between classes while allowing some misclassification (controlled by slack variables).

Since all models have the same number of slack variables, meaning they misclassify the same number of training points, the only remaining factor to compare is the margin size.

A larger margin means better generalization to unseen data. Thus, Model 4, with the largest margin of 4.0, is the best choice.

SVM optimization goal: Minimize $ \quad \frac{1}{2} \| \mathbf{w} \|^2 + C \sum \xi_i $
* ∥w∥ relates inversely to the margin size
* ξi are slack variables (misclassification penalties)
* 𝐶 balances margin width vs misclassification
</details>

---

### 11. False negatives in a confusion matrix

**Question:**
You are applying classification on a dataset with two classes that has 1,000 observations, 700 of which belong to class 1 (“positive” class) and 300 of which belong to class 0 (“negative” class). The model you created correctly classified 800 observations. Among the wrongly classified ones, the model assigned 120 to class 1 and 80 to class 0.
**What is the value of false negatives in the confusion matrix of your model?**

- 40  
- 80  
- 120  
- 220  

<details>
<summary>✅ Show answer</summary>

**Answer:** 80  
**Explanation:** False negatives are instances where actual class 1 is predicted as class 0, totaling 80 in this case.
</details>

---

### 12. Best SVM kernel for circular decision boundary

**Question:**  
You are applying classification with the help of support vector machines (SVM). The data is not linearly separable, and, after plotting it, you notice that the decision boundary will be a geometric shape very close to a circle.
**Which SVM kernel should you use?**

- Hyperbolic tangent  
- Polynomial with degree 3  
- Polynomial with degree 2  
- Radial basis function  

<details>
<summary>✅ Show answer</summary>

**Answer:** Radial basis function  
**Explanation:** The RBF kernel is effective for non-linear problems with circular decision boundaries.
</details>

---

### 13. Decision tree majority vote

**Question:**  
You are applying decision tree classification and after running the algorithm the current observation you are looking at appears in a region with five other observations having the following labels: 1, 3, 2, 1, and 5.
**What label should you give to the current observation?**

- 1  
- 2  
- 3  
- 5  

<details>
<summary>✅ Show answer</summary>

**Answer:** 1  
**Explanation:** Label 1 appears most frequently (twice) among the five, so it's assigned by majority vote.

In decision tree classification, when a new observation reaches a leaf node, it is classified based on the majority class of the training observations in that region.
</details>

---

### 14. Tree time complexity and leaf size

**Question:**  
True or false: A larger value for the minimum number of samples required to be at a leaf node will decrease the time complexity of the tree generation process.

- True  
- False  

<details>
<summary>✅ Show answer</summary>

**Answer:** True  
**Explanation:** Increasing the minimum samples per leaf reduces the tree's depth, thus decreasing training time.

A decision tree is built by splitting the data into regions (nodes) that are increasingly "pure" (i.e., where most data points have the same label). When a node cannot be split further, it becomes a leaf node and gets a label (classification) or value (regression).

The minimum number of samples required to be at a leaf node controls how deep the decision tree can grow.

If you increase this value:

* The tree's smallest possible leaf will have more samples
* The tree will be shallower
* It will stop splitting sooner
* There will be fewer nodes

Hence, the time complexity of tree generation will decrease.
</details>

---

### 15. Bagging regression prediction

**Question:**  
You are applying regression with decision trees, and you want to test the results with bagging. You bootstrap four samples and, after running the algorithm on them, you get the following predictions for the current observation: 32, 34, 24, and 30.
**What value will you predict for the current observation?**

- 24  
- 30  
- 32  
- 34  

<details>
<summary>✅ Show answer</summary>

**Answer:** 30  
**Explanation:** Bagging for regression averages the predictions: (32 + 34 + 24 + 30) / 4 = 30.

Bagging (Bootstrap Aggregating) is an ensemble learning technique used to reduce variance and improve model stability, especially with high-variance models like decision trees.

The core idea is to train multiple models on different random subsets of the training data, then combine their predictions.

Steps:
* Bootstrap sampling: Randomly sample the training data with replacement to create multiple datasets of the same size as the original.
* Train a model on each sample: Usually the same type of model — e.g., a decision tree — is trained on each bootstrapped dataset.
* Aggregate predictions: For regression, average the predictions. For classification, majority vote.
</details>

---

### 16. AdaBoost initial weights

**Question:**  
You are applying boosting in a classification task and want to use the AdaBoost algorithm. There are 40 training observations in the dataset.
**What weight should you apply on training observations in the initial state?**

- 1/40  
- 40/100  
- 140/100  
- 40/10  

<details>
<summary>✅ Show answer</summary>

**Answer:** 1/40  
**Explanation:** AdaBoost initializes all sample weights equally, summing to 1; thus, each weight is 1/40.

Boosting is an ensemble technique that builds a strong learner by combining many weak learners, trained sequentially, each trying to fix the errors of the previous one.

Steps:
* Train the first weak learner (e.g. a small decision tree).
* Measure its errors.
* Give more weight to the misclassified examples.
* Train the next learner focusing on the harder cases.
* Repeat for many rounds.
* Combine all the weak learners’ predictions using a weighted vote or sum.

</details>

---

### 17. Hierarchical clustering complete linkage

**Question:**  
You are applying hierarchical clustering and want to find the dissimilarity value between two clusters using **complete** linkage. You get the following values for pairwise dissimilarities between the points of the cluster: 1, 4, 5, and 2.
**What is the dissimilarity value?**

- 1  
- 2  
- 3  
- 4  
- 5  
- 6  

<details>
<summary>✅ Show answer</summary>

**Answer:** 5  
**Explanation:** Complete linkage uses the maximum dissimilarity between any two points in the two clusters — which here is 5.

Hierarchical clustering is an unsupervised machine learning algorithm used to group data into clusters by building a tree-like structure (dendrogram).

Two approaches:
* Agglomerative (Bottom-Up)
  * Start with each data point as its own cluster
  * Iteratively merge the two closest clusters
  * Continue until all points are in a single cluster (or a desired number is reached)

* Divisive (Top-Down)
  * Start with one large cluster containing all points
  * Recursively split it into smaller clusters

The most common method is agglomerative.

The "closeness" between clusters is defined by a linkage method — i.e., how to compute dissimilarity between clusters.

| Linkage Type     | Description                                               | Formula                                | Tends to Produce               |
|------------------|-----------------------------------------------------------|----------------------------------------|--------------------------------|
| **Single**       | Min distance between any two points across clusters       | \( \min(d(a, b)) \)                    | Long, chain-like clusters      |
| **Complete**     | Max distance between any two points across clusters       | \( \max(d(a, b)) \)                    | Compact, spherical clusters    |
| **Average**      | Average pairwise distance between all points in clusters  | \( \frac{1}{|A||B|} \sum d(a, b) \)    | Balanced clusters              |
| **Centroid**     | Distance between cluster centroids                        | \( d(\mu_A, \mu_B) \)                  | Can sometimes cause inversions |

In hierarchical clustering, complete linkage (also called maximum linkage) defines the dissimilarity between two clusters as: The maximum distance (or dissimilarity) between any pair of points, one from each cluster.
</details>

---

### 18. K-means centroid update

**Question:**  
You are applying K-means clustering and want to adjust the coordinates of each of the centroids using the coordinates of the data points belonging to its cluster. For the currently observed centroid, there are three data points belonging to its cluster with the following coordinates: (5.5, 3), (2, 1), and (0, 2).
**What coordinates should you assign to the centroid?**

- (2.5, 2)  
- (0, 1)  
- (5, 6)  
- (3, 4)  

<details>
<summary>✅ Show answer</summary>

**Answer:** (2.5, 2)  
**Explanation:** The centroid is the mean of the coordinates:  
X = (5.5 + 2 + 0)/3 = 2.5, Y = (3 + 1 + 2)/3 = 2.
</details>

---