

# **Exploratory Data Analysis (EDA) Report**

## **1. Dataset Loading & Initial Inspection**

The dataset was loaded using the Pandas library.
To understand its structure, the first few (`df.head()`) and last few (`df.tail()`) records were examined.

**Observation:**

* The dataset consists of **10,000 rows and 6 columns**.
* Each row represents a student’s study-related attributes and their performance outcome.
* Data appears structured and consistent across records.

---

## **2. Feature Type Identification (Manual Inspection)**

Based on column names and values, features are categorized as follows:

### **Numerical Features**

* **Hours Studied** – Number of hours spent studying.
* **Previous Scores** – Previous academic score.
* **Sleep Hours** – Average daily sleep duration.
* **Sample Question Papers Practiced** – Number of practice papers solved.
* **Performance Index** – Continuous performance score.

### **Categorical Feature**

* **Extracurricular Activities** – Indicates participation (`Yes` / `No`).

### **Binary Feature**

* **Extracurricular Activities** (Binary categorical: Yes/No)

### **Ordinal Features**

* None explicitly present.
  (All numeric values represent quantities, not rankings.)

---

## **3. Data Type & Statistical Summary Analysis**

### **Using `df.info()`**

* All columns have **non-null values (100%)**.
* Data types:

  * `int64`: 4 columns
  * `float64`: 1 column
  * `object`: 1 column
* Memory usage is low (~469 KB), making it computationally efficient.

### **Using `df.describe()`**

Key statistical observations:

* **Hours Studied** ranges from **1 to 9**, with a mean of ~5.
* **Previous Scores** range from **40 to 99**, indicating moderate to high academic history.
* **Sleep Hours** average around **6.5 hours**, suggesting realistic student behavior.
* **Performance Index** ranges from **10 to 100**, suitable as a prediction target.

---

## **4. Categorical Feature Distribution**

For **Extracurricular Activities**:

* Two unique values: **Yes** and **No**
* Distribution is fairly balanced:

  * `No`: ~50.5%
  * `Yes`: ~49.5%

**Observation:**

* No major class imbalance exists in the categorical feature.

---

## **5. Target Variable & Input Features**

### **Target Variable**

* **Performance Index**

  * Continuous numerical variable
  * Suitable for **regression-based machine learning models**

### **Input Features**

* Hours Studied
* Previous Scores
* Extracurricular Activities
* Sleep Hours
* Sample Question Papers Practiced

These features are logically related to academic performance, making them strong predictors.

---

## **6. Dataset Size & ML Suitability**

* **10,000 records** is a solid dataset size.
* Adequate for:

  * Linear Regression
  * Decision Tree
  * Random Forest
  * Gradient Boosting models
* Low risk of overfitting with proper validation.

**Conclusion:**
The dataset is **well-suited for machine learning**, especially supervised regression tasks.

---

## **7. Data Quality Observations**

### **Positive Aspects**

✅ No missing values
✅ No duplicate records observed
✅ Balanced categorical feature
✅ Clean and well-structured dataset

### **Potential Considerations**

⚠ Categorical column requires encoding before ML
⚠ Feature scaling may improve performance for distance-based models

---

## **Final Conclusion**

This dataset is **high-quality, clean, and ML-ready**. Minimal preprocessing is required, making it ideal for educational purposes, EDA practice, and regression model development.

