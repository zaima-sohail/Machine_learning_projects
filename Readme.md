

````markdown
# AIwithPython

A collection of Python and machine-learning projects covering data analysis, visualization, classification, regression, and ensemble learning.

## Requirements

Install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter mlxtend
```

## Projects

### 1. Placement Prediction

**Notebook:** `placement.ipynb`

Predicts whether a student will be placed using:

- CGPA
- Resume score

**Techniques used:**

- Pandas data loading
- Seaborn visualization
- Perceptron classification
- Decision-region visualization
- Accuracy evaluation

**Dataset:** `placement.csv`

---

### 2. House Price Prediction

**Notebook:** `house.ipynb`

Predicts house prices using property-related features.

**Techniques used:**

- Data preprocessing
- Exploratory data analysis
- Feature selection
- Regression modeling
- Model evaluation

---

### 3. Iris Flower Classification

**Notebook:** `iris.ipynb`

Classifies iris flowers into different species using flower measurements.

**Features:**

- Sepal length
- Sepal width
- Petal length
- Petal width

**Techniques used:**

- Classification
- Train-test splitting
- Model prediction
- Accuracy evaluation
- Confusion matrix

---

### 4. Telecom Customer Churn Prediction

**Notebook:** `telecom_customer.ipynb`

Predicts whether a telecom customer is likely to leave the service.

**Techniques used:**

- Customer-data analysis
- Data cleaning
- Classification
- Confusion matrix
- Classification report
- Accuracy evaluation

---

### 5. Wine Classification

**Notebook:** `load_wine.ipynb`

Classifies wine samples into different categories using chemical properties.

**Techniques used:**

- Scikit-learn wine dataset
- Random Forest classification
- Feature analysis
- Train-test splitting
- Accuracy evaluation

---

### 6. Digits Recognition

**Notebook:** `load_digits.ipynb`

Recognizes handwritten digits using image-based numerical features.

**Techniques used:**

- Scikit-learn digits dataset
- Classification
- Random Forest modeling
- Prediction and evaluation
- Confusion matrix

---

### 7. Diabetes Prediction

**Notebook:** `load_breast.ipynb`

This notebook currently loads the scikit-learn diabetes dataset and applies a Random Forest model.

**Techniques used:**

- Scikit-learn diabetes dataset
- Random Forest model
- Out-of-bag score
- Test accuracy
- Prediction error calculation

> Note: The notebook is named `load_breast.ipynb`, but the code uses `load_diabetes()`. Rename the notebook or change the dataset to avoid confusion.

---

## Common Machine-Learning Workflow

Most projects follow these steps:

1. Import Python libraries.
2. Load or create a dataset.
3. Explore the data.
4. Separate features and target values.
5. Split data into training and testing sets.
6. Train a machine-learning model.
7. Make predictions.
8. Evaluate model performance.
9. Visualize the results.

## Project Structure

```text
AIwithPython/
├── placement.ipynb
├── placement.csv
├── house.ipynb
├── iris.ipynb
├── telecom_customer.ipynb
├── load_wine.ipynb
├── load_digits.ipynb
├── load_breast.ipynb
└── Readme.md
```

## How to Run

Open a terminal in the project folder and run:

```bash
jupyter notebook
```

Alternatively, open any `.ipynb` file directly in Visual Studio Code and run the cells in order.
````