
# **Exploratory Data Analysis Report**

## **Iris Dataset**

---

## **1. Distribution of Numerical Features (Histograms)**

Histograms were plotted for the numerical features:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

### **Insights**

* **Sepal Length** shows a near-normal distribution with slight right skew.
* **Sepal Width** is moderately normally distributed but slightly left-skewed.
* **Petal Length** shows clear separation between species, indicating strong predictive power.
* **Petal Width** also shows distinct clusters, making it highly informative.

📌 *Petal-based features display clearer class separation than sepal-based features.*

---

## **2. Analysis of Categorical Feature (Count Plot)**

A count plot was used to visualize the categorical feature:

* **Species** (Setosa, Versicolor, Virginica)

### **Insights**

* Each species has an **equal number of samples (50 each)**.
* No class imbalance is present.
* Balanced classes make the dataset ideal for classification models.

📌 *Balanced target variable improves model fairness and evaluation.*

---

## **3. Outlier Detection Using Box Plots**

Box plots were created for all numerical features.

### **Insights**

* **Sepal Width** contains a few mild outliers.
* **Petal Length** and **Petal Width** show minimal to no extreme outliers.
* Outliers are not severe enough to require removal.

📌 *The dataset is clean and robust, requiring minimal preprocessing.*

---

## **4. Correlation Heatmap**

A correlation heatmap was plotted to examine relationships between numerical features.

### **Insights**

* **Petal Length & Petal Width** have a **strong positive correlation**.
* **Sepal Length** shows moderate correlation with petal features.
* **Sepal Width** has weak correlation with other variables.

📌 *Highly correlated features indicate shared information useful for prediction.*

---

## **5. Visualization-Based Insights Summary**

| Visualization | Key Insight                          |
| ------------- | ------------------------------------ |
| Histograms    | Petal features show clear separation |
| Count Plot    | Dataset is perfectly balanced        |
| Box Plot      | Minimal outliers present             |
| Heatmap       | Petal features are highly correlated |

---

## **6. Important Features for Prediction**

Based on visual analysis:

* ✅ **Petal Length**
* ✅ **Petal Width**

These features:

* Clearly separate species
* Show strong correlation
* Have minimal overlap across classes

⚠ **Sepal Width** is least informative due to overlap and weak correlation.

---

## **7. Final Summary (Bullet Points)**

* Iris dataset is **clean, balanced, and well-structured**.
* No missing values or serious outliers detected.
* Petal features are the **most important predictors**.
* Sepal features provide supplementary information.
* Dataset is ideal for:

  * Logistic Regression
  * KNN
  * Decision Trees
  * Random Forest
* Minimal preprocessing required before model training.
