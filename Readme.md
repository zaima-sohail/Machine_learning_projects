

````markdown
# AIwithPython
# 30 Days of Machine Learning with Python

A structured, notebook-by-notebook journey through Python fundamentals, data analysis, and machine learning — from basic syntax to deep learning and a deployed web app. This repository is a personal learning log built while working through a 30-day ML/Python course, with every exercise saved as its own notebook or script for reference.

---

## 📁 Repository Structure

```
.
├── .venv/                                  # Python virtual environment
├── .vscode/                                # Editor settings
├── templates/                              # Flask HTML templates + clustering/classification notebooks
│   ├── home.html
│   ├── input.html
│   ├── agg.ipynb
│   ├── agglomerative.ipynb
│   ├── kmeans.ipynb
│   ├── kmeans12.ipynb
│   ├── knn.ipynb
│   ├── knntest.ipynb
│   ├── load_digits.ipynb
│   ├── naviebayes.ipynb
│   ├── naviebayes12.ipynb
│   ├── pca.ipynb
│   ├── wine.ipynb
│   └── wine12.ipynb
├── blank_plot.png
├── breast.ipynb
├── cal.py
├── circle.ipynb
├── datastructures.ipynb
├── datatypes.ipynb
├── decision.ipynb
├── deep learning.ipynb
├── demo.txt
├── ecommerce.ipynb
├── ecommerce_sales_analytics_5000.csv
├── excep.py
├── exception.ipynb
├── file.ipynb
├── hello.py
├── iris.ipynb
├── iris1.ipynb
├── linear.ipynb
├── lists.ipynb
├── load_breast.ipynb
├── loan.csv
├── loan.ipynb
├── Mall_Customers.csv
├── matplot.ipynb
├── mini.ipynb
├── module.py
├── modules.ipynb
├── numpy.ipynb
├── OPPS.ipynb
├── pandas.ipynb
├── placement.csv
└── placement.ipynb
```

---

## 🗓️ 30-Day Curriculum Map

### Week 1 — Python Foundations (Days 1–7)
| Day | Topic | File |
|-----|-------|------|
| 1 | Hello World & environment setup | `hello.py` |
| 2 | Data types | `datatypes.ipynb` |
| 3 | Lists & sequences | `lists.ipynb` |
| 4 | Data structures (tuples, sets, dicts) | `datastructures.ipynb` |
| 5 | Functions & modules | `module.py`, `modules.ipynb` |
| 6 | Exception handling | `excep.py`, `exception.ipynb` |
| 7 | File handling | `file.ipynb`, `demo.txt` |

### Week 2 — OOP & Core Libraries (Days 8–14)
| Day | Topic | File |
|-----|-------|------|
| 8 | Object-Oriented Programming | `OPPS.ipynb` |
| 9 | Mini practice project | `mini.ipynb` |
| 10 | Turtle/geometry basics | `circle.ipynb`, `cal.py` |
| 11 | NumPy fundamentals | `numpy.ipynb` |
| 12 | Pandas fundamentals | `pandas.ipynb` |
| 13 | Data visualization with Matplotlib | `matplot.ipynb` |
| 14 | Blank canvas / plotting practice | `blank_plot.png` |

### Week 3 — Supervised Learning: Classification (Days 15–21)
| Day | Topic | File |
|-----|-------|------|
| 15 | Iris dataset — first classifier | `iris.ipynb`, `iris1.ipynb` |
| 16 | K-Nearest Neighbors (KNN) | `knn.ipynb`, `knntest.ipynb` |
| 17 | Naive Bayes | `naviebayes.ipynb`, `naviebayes12.ipynb` |
| 18 | Decision Trees | `decision.ipynb` |
| 19 | Breast Cancer dataset classification | `load_breast.ipynb`, `breast.ipynb` |
| 20 | Digits dataset (image classification) | `load_digits.ipynb` |
| 21 | Wine dataset classification | `wine.ipynb`, `wine12.ipynb` |

### Week 4 — Regression, Clustering & Dimensionality Reduction (Days 22–27)
| Day | Topic | File |
|-----|-------|------|
| 22 | Linear Regression | `linear.ipynb` |
| 23 | Regression case study — loan prediction | `loan.ipynb`, `loan.csv` |
| 24 | Regression case study — placement prediction | `placement.ipynb`, `placement.csv` |
| 25 | K-Means clustering | `kmeans.ipynb`, `kmeans12.ipynb`, `Mall_Customers.csv` |
| 26 | Agglomerative (hierarchical) clustering | `agg.ipynb`, `agglomerative.ipynb` |
| 27 | Principal Component Analysis (PCA) | `pca.ipynb` |

### Week 5 — Deep Learning, Real-World Data & Deployment (Days 28–30)
| Day | Topic | File |
|-----|-------|------|
| 28 | Introduction to Deep Learning (Neural Networks) | `deep learning.ipynb` |
| 29 | End-to-end EDA — e-commerce sales analytics | `ecommerce.ipynb`, `ecommerce_sales_analytics_5000.csv` |
| 30 | Model deployment with Flask | `templates/home.html`, `templates/input.html` |

---

## 🧠 Topics Covered

- **Python Core:** variables, data types, lists, tuples, sets, dictionaries, functions, modules, exception handling, file I/O, OOP
- **Data Analysis:** NumPy arrays & operations, Pandas DataFrames, data cleaning, exploratory data analysis (EDA)
- **Visualization:** Matplotlib plotting, chart customization
- **Supervised Learning:** Linear Regression, K-Nearest Neighbors, Naive Bayes, Decision Trees
- **Unsupervised Learning:** K-Means Clustering, Agglomerative/Hierarchical Clustering, PCA
- **Deep Learning:** Neural network basics
- **Deployment:** Flask web app serving a trained model via HTML forms

## 📊 Datasets Used

| Dataset | Used In | Description |
|---------|---------|--------------|
| `Iris` (sklearn built-in) | `iris.ipynb`, `iris1.ipynb` | Classic flower species classification |
| `Wine` (sklearn built-in) | `wine.ipynb`, `wine12.ipynb` | Wine quality/type classification |
| `Digits` (sklearn built-in) | `load_digits.ipynb` | Handwritten digit image classification |
| `Breast Cancer` (sklearn built-in) | `load_breast.ipynb`, `breast.ipynb` | Tumor malignancy classification |
| `loan.csv` | `loan.ipynb` | Loan approval prediction |
| `placement.csv` | `placement.ipynb` | Student placement prediction |
| `Mall_Customers.csv` | `kmeans.ipynb`, `kmeans12.ipynb` | Customer segmentation clustering |
| `ecommerce_sales_analytics_5000.csv` | `ecommerce.ipynb` | 5,000-row e-commerce sales EDA |

## 🛠️ Tech Stack

- **Language:** Python 3
- **Notebook environment:** Jupyter (`.ipynb`)
- **Libraries:** NumPy, Pandas, Matplotlib, scikit-learn
- **Web framework:** Flask (`templates/home.html`, `templates/input.html`)
- **Environment management:** `.venv`

## ▶️ Getting Started

```bash
# 1. Clone the repository
git clone <your-repo-url>
cd <repo-folder>

# 2. Activate the virtual environment
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# 3. Install dependencies
pip install numpy pandas matplotlib scikit-learn flask jupyter

# 4. Launch Jupyter to explore the notebooks
jupyter notebook

# 5. Run the Flask app (Day 30 deployment demo)
python app.py   # or the relevant entry-point script
```

## 📌 Notes

- Files with numeric suffixes (e.g. `kmeans12.ipynb`, `naviebayes12.ipynb`, `wine12.ipynb`) are second-pass/revision notebooks revisiting the same topic — kept for comparison of approaches.
- `mini.ipynb` is a small standalone practice project bridging Python basics and early ML work.
- `blank_plot.png` is a saved Matplotlib output used for plotting practice.

## 📅 Progress

- [x] Week 1 — Python Foundations
- [x] Week 2 — OOP & Core Libraries
- [x] Week 3 — Classification Algorithms
- [x] Week 4 — Regression, Clustering & PCA
- [x] Week 5 — Deep Learning & Deployment

---

*Maintained as a personal learning log for the 30 Days of ML with Python course.*

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
