### Transaction Prediction and Cost Reduction Model

This repository contains a comprehensive project for building and optimizing a machine learning model aimed at predicting transaction outcomes to minimize transaction costs. The primary goal is to create a predictive model that can accurately forecast successful transactions and reduce associated fees based on predefined fee structures.

#### Project Overview

- **Data Preparation**: Loading, cleaning, and preprocessing transaction data.
- **Exploratory Data Analysis (EDA)**: Visualizing distributions of transaction amounts, success status, 3D secured status, country, payment service providers (PSP), and card providers.
- **Feature Engineering**: Creating new features from timestamps and other relevant data.
- **Modeling**:
  - Baseline Model: Logistic Regression
  - Advanced Models: Support Vector Machine (SVM), Random Forest, Gradient Boosting, XGBoost, LightGBM
- **Hyperparameter Tuning**: Using GridSearchCV to optimize model parameters for Random Forest and LightGBM.
- **Cost Calculation**: Calculating actual and predicted transaction fees based on model predictions.
- **Sweet Spot Analysis**: Identifying the optimal threshold for transaction success prediction to minimize costs.

#### Key Metrics

- **Accuracy**
- **Precision**
- **Recall**
- **F1-Score**
- **Total Transaction Fees**

#### Results

- LightGBM with tuned hyperparameters showed the best performance in terms of balancing accuracy, precision, recall, and F1-score while aiming to minimize transaction fees.

#### Tools and Libraries

- Python
- Pandas
- NumPy
- Scikit-learn
- LightGBM
- Seaborn
- Matplotlib
- SMOTE for handling class imbalance

#### How to Use

1. Clone the repository.
2. Install the required libraries.
3. Run the Jupyter notebooks or Python scripts to reproduce the analysis and model training.
4. Evaluate the results and use the optimized model for predicting transaction outcomes to minimize fees.

---

Feel free to customize this description further based on your specific needs and any additional details you'd like to include.
