### 📊 Supervised ML Methods for Regression Problems

| **Method**                            | **Pros**                                                                 | **Cons**                                                   |
| ------------------------------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------- |
| **Linear Regression**                 | - Simple and easy to interpret- Fast to train- Good for linear trends    | - Assumes linear relationship- Poor on complex patterns    |
| **Ridge/Lasso Regression**            | - Handles multicollinearity- Adds regularization to reduce overfitting   | - Can still underperform on non-linear data                |
| **Decision Tree Regression**          | - Easy to visualize- Captures non-linear relationships                   | - Prone to overfitting- Unstable to small data changes     |
| **Random Forest Regression**          | - Handles non-linearity well- Less overfitting- Good accuracy            | - Slower to train- Harder to interpret                     |
| **Gradient Boosting (e.g., XGBoost)** | - High predictive power- Works well with messy data                      | - Longer training time- Sensitive to parameter tuning      |
| **Support Vector Regression (SVR)**   | - Effective in high-dimensional spaces- Flexible with kernels            | - Computationally heavy- Hard to tune for large datasets   |
| **k-Nearest Neighbors (kNN)**         | - Simple and intuitive- No training phase                                | - Slow during prediction- Sensitive to irrelevant features |
| **Neural Networks**                   | - Powerful for complex, large-scale problems- Can model any function     | - Requires a lot of data- Less interpretable- Needs tuning |
| **ElasticNet Regression**             | - Combines Ridge & Lasso advantages- Works well with correlated features | - Needs careful tuning of alpha & lambda parameters        |

---

### ✅ **Popular Supervised ML Methods for Classification**

| **Algorithm**                         | **Pros**                                                                                               | **Cons**                                                                                |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------- |
| **Logistic Regression**               | - Easy to implement and interpret- Fast training- Works well for linearly separable classes            | - Struggles with non-linear relationships- Assumes linearity between input and log-odds |
| **Decision Tree**                     | - Easy to visualize and explain- Handles both numerical and categorical data- No need for data scaling | - Prone to overfitting- Small changes in data can change tree structure                 |
| **Random Forest**                     | - Reduces overfitting compared to a single tree- Good accuracy- Handles missing data well              | - Slower for real-time prediction- Less interpretable than a single tree                |
| **Support Vector Machine (SVM)**      | - Performs well with high-dimensional data- Effective for margin-based classification                  | - Hard to interpret- Requires feature scaling- Not suitable for large datasets          |
| **K-Nearest Neighbors (KNN)**         | - Simple to understand and implement- No training time (lazy learner)                                  | - Slow at prediction time for large datasets- Sensitive to irrelevant features          |
| **Naive Bayes**                       | - Fast and scalable- Works well with text (e.g., spam filtering)- Handles noisy data well              | - Assumes feature independence (rarely true)- Struggles with correlated features        |
| **Gradient Boosting (e.g., XGBoost)** | - High performance in competitions- Handles missing data and interactions well- Robust to outliers     | - Training time can be long- Harder to tune and interpret- Sensitive to overfitting     |
| **Neural Networks (Shallow)**         | - Can model complex non-linear patterns- Works well with enough data                                   | - Requires more data and tuning- Often seen as a black box- Risk of overfitting         |

### ✅ **Popular Unsupervised ML Methods **

| **Algorithm**                                           | **Pros**                                                                                         | **Cons**                                                                                |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------- |
| **K-Means Clustering**                                  | - Simple and fast- Scales well to large data- Easy to interpret                                  | - Needs to predefine number of clusters (K)- Struggles with irregular shapes and noise  |
| **Hierarchical Clustering**                             | - No need to define K- Provides a tree-like structure (dendrogram)- Useful for small datasets    | - Not scalable to large datasets- Sensitive to noise and outliers                       |
| **DBSCAN (Density-Based)**                              | - Identifies clusters of arbitrary shape- Robust to noise- No need to specify number of clusters | - Poor performance in varying densities- Hard to tune `eps` and `minPts`                |
| **PCA (Principal Component Analysis)**                  | - Great for reducing dimensionality- Enhances visualization- Improves model performance          | - Components are hard to interpret- Assumes linear relationships                        |
| **t-SNE (t-distributed Stochastic Neighbor Embedding)** | - Excellent for visualizing high-dimensional data- Captures non-linear structure                 | - Computationally expensive- Only useful for visualization, not for downstream modeling |
| **Autoencoders**                                        | - Powerful for complex dimensionality reduction- Learns non-linear patterns- Can denoise data    | - Requires large data- Acts like a black box- Needs tuning and GPU power                |

---

### 
