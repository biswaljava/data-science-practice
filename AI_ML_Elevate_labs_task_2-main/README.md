

# **Exploratory Data Analysis & Data Cleaning Report**

## **Medical Appointment No Shows Dataset**

---

## **1. Dataset Overview**

The *Medical Appointment No Shows* dataset contains information about patients, their medical conditions, appointment details, and whether they attended their scheduled appointment.

Each row represents **one medical appointment**, and the dataset includes both numerical and categorical features relevant to patient behavior and healthcare outcomes.

---

## **2. Identification of Missing Values**

Missing values were identified using the Pandas function:

```python
df.isnull().sum()
```

### **Observation**

Missing values were found in the following columns:

* **Age**
* **Gender**
* **AppointmentDay**
* **Scholarship**
* **Diabetes**
* **SMS_Received**

These missing values indicate incomplete patient records and inconsistencies during data collection.

---

## **3. Visualization of Missing Data**

Missing data patterns were visualized using a **bar chart**, showing the number of missing values per column.

### **Observation**

* Numerical column **Age** had noticeable missing entries.
* Categorical columns such as **Gender** and **AppointmentDay** also showed gaps.
* No column showed extremely high missing values (greater than 50%).

This visualization helped in selecting appropriate data-cleaning strategies.

---

## **4. Numerical Data Imputation**

Numerical columns were handled using **median imputation**.

### **Column Imputed**

* **Age**

### **Reason**

* Median is preferred over mean to reduce the impact of outliers and skewed distributions.
* Ensures realistic age values without distorting the dataset.

---

## **5. Categorical Data Imputation**

Categorical columns were handled using **mode imputation**.

### **Columns Imputed**

* Gender
* AppointmentDay
* Scholarship
* Diabetes
* SMS_Received

### **Reason**

* Mode represents the most frequent category.
* Maintains consistency in categorical distributions.
* Suitable when missing values are relatively low.

---

## **6. Removal of Columns with High Missing Values**

Each column was evaluated for the percentage of missing values.

### **Observation**

* No column exceeded the threshold of **extremely high missing values**.
* Therefore, **no columns were removed** from the dataset.

This ensured that all important features were retained for analysis.

---

## **7. Dataset Validation After Cleaning**

After applying all imputation techniques, the dataset was validated again.

### **Observation**

* All missing values were successfully handled.
* The dataset now contains **no null values**.
* Data types and distributions are consistent.

---

## **8. Before vs After Dataset Comparison**

| Aspect            | Before Cleaning | After Cleaning |
| ----------------- | --------------- | -------------- |
| Number of Rows    | Same            | Same           |
| Number of Columns | Same            | Same           |
| Missing Values    | Present         | None           |
| Data Consistency  | Low             | High           |
| ML Readiness      | ❌ Not Suitable  | ✅ Suitable     |

---

## **9. Data Quality Assessment**

### **Issues Identified**

* Missing values in patient demographic and appointment-related columns.
* Incomplete medical condition records.

### **Issues Resolved**

* Numerical missing values handled using median imputation.
* Categorical missing values handled using mode imputation.
* Dataset cleaned without loss of records.

---

## **10. Final Conclusion**

The *Medical Appointment No Shows* dataset initially contained missing and incomplete values that could negatively affect analysis and machine learning models. After applying systematic data cleaning techniques, the dataset became **clean, reliable, and suitable for further analysis**, including predictive modeling such as **No-Show classification**.

This cleaned dataset can now be safely used for **EDA, visualization, and machine learning tasks**.

---
