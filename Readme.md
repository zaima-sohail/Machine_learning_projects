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

## ⭐ Key / Portfolio-Worthy Projects

These stand out from the rest because they use **real-world-scale datasets**, involve **end-to-end workflows** (not just algorithm syntax practice), or result in a **deployable product** — the ones worth showing off in a portfolio or resume.

| Project | File(s) | Why it matters |
|---------|---------|-----------------|
| 🥇 **E-commerce Sales Analytics** | `ecommerce.ipynb` + `ecommerce_sales_analytics_5000.csv` | Largest real dataset (5,000 rows) in the repo. Full EDA workflow — cleaning, aggregation, trend analysis, visualization — closest to a real business analytics task. |
| 🥈 **Model Deployment (Flask Web App)** | `templates/home.html`, `templates/input.html` | The only project that goes beyond the notebook: takes a trained model and serves it through a web form. Demonstrates the full ML lifecycle (train → save → deploy → predict via UI). |
| 🥉 **Customer Segmentation (K-Means)** | `kmeans.ipynb`, `kmeans12.ipynb` + `Mall_Customers.csv` | Classic, interview-relevant unsupervised learning case study with real customer data — commonly asked about in ML interviews. |
| **Loan Prediction** | `loan.ipynb` + `loan.csv` | Realistic binary classification/regression business problem (loan approval) — good for demonstrating applied ML on tabular data. |
| **Placement Prediction** | `placement.ipynb` + `placement.csv` | Common beginner-to-intermediate portfolio project; demonstrates regression/classification on student outcome data. |
| **Deep Learning Basics** | `deep learning.ipynb` | Only neural-network notebook in the repo — signals progress beyond classical ML into DL fundamentals. |
| **Breast Cancer Classification** | `load_breast.ipynb`, `breast.ipynb` | Widely recognized benchmark dataset; good for showcasing classification metrics (accuracy, precision, recall, confusion matrix) on a medical use case. |

Everything else (`iris`, `wine`, `digits`, `knn`, `naive bayes`, `decision`, `pca`, `agglomerative`, Python-basics files) is valuable for **learning/practice** but is closer to standard textbook/tutorial exercises using built-in sklearn datasets rather than original applied work.

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

## 📖 Full Project Details

### Python Foundations
| File | Description |
|------|-------------|
| `hello.py` | First script — print statements, basic syntax, running `.py` files. |
| `datatypes.ipynb` | Int, float, string, boolean, type casting, and type-checking examples. |
| `lists.ipynb` | List creation, indexing, slicing, list methods (append, sort, etc.). |
| `datastructures.ipynb` | Tuples, sets, dictionaries — creation, methods, and use cases compared to lists. |
| `module.py` / `modules.ipynb` | Writing a custom module (`module.py`) and importing/using it in a notebook — demonstrates code reuse. |
| `excep.py` / `exception.ipynb` | Try/except/finally blocks, raising custom exceptions, handling multiple error types. |
| `file.ipynb` / `demo.txt` | Reading from and writing to text files; `demo.txt` is the sample file used for I/O practice. |
| `OPPS.ipynb` | Object-Oriented Programming — classes, objects, constructors, inheritance, encapsulation. |
| `mini.ipynb` | Small combined practice project applying multiple Python basics together. |
| `circle.ipynb` / `cal.py` | Simple geometry/arithmetic calculator scripts — functions and math operations. |

### Data Analysis & Visualization
| File | Description |
|------|-------------|
| `numpy.ipynb` | NumPy arrays, indexing, broadcasting, array math, reshaping. |
| `pandas.ipynb` | Pandas Series/DataFrame basics — reading CSVs, filtering, grouping, cleaning data. |
| `matplot.ipynb` | Matplotlib charting — line, bar, scatter plots, labels, subplots. |
| `blank_plot.png` | Saved output image from a Matplotlib plotting exercise. |

### Classification Projects
| File | Description |
|------|-------------|
| `iris.ipynb` / `iris1.ipynb` | First classification models on the Iris flower dataset; likely comparing two approaches/algorithms. |
| `knn.ipynb` / `knntest.ipynb` | K-Nearest Neighbors implementation and a separate testing/evaluation notebook. |
| `naviebayes.ipynb` / `naviebayes12.ipynb` | Naive Bayes classifier — first pass and a revised/second version. |
| `decision.ipynb` | Decision Tree classifier — building, visualizing, and evaluating a tree model. |
| `load_breast.ipynb` / `breast.ipynb` | Breast Cancer Wisconsin dataset — loading data and building a classifier with evaluation metrics. |
| `load_digits.ipynb` | Handwritten digits dataset (8x8 images) — image classification with a standard ML model. |
| `wine.ipynb` / `wine12.ipynb` | Wine dataset classification — first version and a revised version, likely comparing model performance. |

### Regression Projects
| File | Description |
|------|-------------|
| `linear.ipynb` | Simple/multiple Linear Regression from scratch or with scikit-learn — fitting a line, evaluating R²/MSE. |
| `loan.ipynb` + `loan.csv` | Predicting loan approval outcomes from applicant data — real business use case. |
| `placement.ipynb` + `placement.csv` | Predicting student placement outcomes based on academic/other features. |

### Clustering & Dimensionality Reduction
| File | Description |
|------|-------------|
| `kmeans.ipynb` / `kmeans12.ipynb` + `Mall_Customers.csv` | Customer segmentation using K-Means clustering; elbow method for choosing K. |
| `agg.ipynb` / `agglomerative.ipynb` | Hierarchical/Agglomerative clustering, likely with dendrogram visualization. |
| `pca.ipynb` | Principal Component Analysis — dimensionality reduction and variance explained. |

### Deep Learning
| File | Description |
|------|-------------|
| `deep learning.ipynb` | Introductory neural network — building/training a basic model (likely with TensorFlow/Keras or from scratch). |

### Real-World Analytics
| File | Description |
|------|-------------|
| `ecommerce.ipynb` + `ecommerce_sales_analytics_5000.csv` | Full exploratory data analysis on a 5,000-row e-commerce sales dataset — trends, top products/categories, revenue analysis. |

### Deployment
| File | Description |
|------|-------------|
| `templates/home.html` | Landing page for the Flask web app. |
| `templates/input.html` | Form page where a user inputs data to get a live model prediction. |

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
