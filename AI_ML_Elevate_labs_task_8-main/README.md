

# **Decision Tree Classification Report**

## **Bank Marketing Dataset (Customer Subscription Prediction)**

---

## **1. Dataset Loading & Feature Understanding**

The Bank Marketing dataset was loaded to analyze customer attributes and their relationship with **subscription behavior**.

### **Key Features Related to Subscription**

* **Age** – Customer age
* **Job** – Type of job
* **Marital** – Marital status
* **Education** – Education level
* **Balance** – Average yearly balance
* **Housing Loan** – Yes / No
* **Personal Loan** – Yes / No
* **Contact Type** – Communication channel
* **Campaign** – Number of contacts performed
* **Outcome (y)** – Target variable (Subscribed: Yes / No)

### **Observation**

* Dataset contains both numerical and categorical features.
* Target variable is **binary**, making it suitable for classification.

---

## **2. Handling Missing Values & Data Cleaning**

### **Issues Identified**

* Some categorical columns contained values such as `"unknown"`.
* Inconsistent text formatting across categorical values.

### **Cleaning Strategy**

* `"unknown"` values were treated as missing and replaced using **mode**.
* Text values were standardized (lowercase, consistent naming).

### **Result**

* Dataset became clean, consistent, and ready for encoding.

---

## **3. Encoding Categorical Features**

Categorical features were converted into numerical form using:

* **One-Hot Encoding** → For nominal features (job, marital, contact, education)
* **Label Encoding** → For binary features (housing, loan, target variable)

### **Reason**

* Machine learning models require numeric inputs.
* One-Hot Encoding avoids incorrect ordinal assumptions.

---

## **4. Train–Test Split**

The dataset was split into **training and testing sets** using a fixed `random_state`.

### **Purpose**

* Ensures reproducibility of results.
* Provides a fair evaluation on unseen data.

---

## **5. Training Decision Tree Classifier**

A **Decision Tree Classifier** was trained with a limited `max_depth`.

### **Reason for Limiting Depth**

* Prevents overfitting.
* Improves generalization.
* Keeps rules interpretable.

### **Observation**

* The model learned meaningful splits based on customer attributes.

---

## **6. Decision Tree Visualization**

The trained decision tree was visualized using `plot_tree()`.

### **Insights**

* Root node represents the most important feature.
* Each split shows a clear decision rule.
* Leaf nodes indicate final subscription predictions.

📌 *Visualization makes model decisions transparent and explainable.*

---

## **7. Prediction & Classification Report**

Predictions were generated on the test dataset and evaluated using a **classification report**.

### **Metrics Used**

* Precision
* Recall
* F1-Score
* Support

### **Observation**

* Balanced performance across metrics.
* Model successfully identifies both subscribers and non-subscribers.

---

## **8. Train vs Test Accuracy Comparison**

| Metric            | Observation              |
| ----------------- | ------------------------ |
| Training Accuracy | Higher                   |
| Testing Accuracy  | Slightly lower but close |

### **Conclusion**

* Small gap between train and test accuracy.
* Indicates **controlled overfitting** due to depth limitation.

---

## **9. Key Decision Rules Explaining Subscription Behavior**

Based on the trained decision tree, the following **rules** were observed:

### **Rule 1**

If **contact type = cellular** AND **campaign ≤ 2**,
→ Customer is **more likely to subscribe**.

### **Rule 2**

If **housing loan = yes** AND **balance is low**,
→ Customer is **less likely to subscribe**.

### **Rule 3**

If **previous campaign outcome = success**,
→ Customer has a **high probability of subscription**.

📌 *These rules provide actionable business insights.*

---

## **Final Conclusion**

The Decision Tree model effectively captured customer subscription patterns in the Bank Marketing dataset. Proper data cleaning, encoding, and depth control ensured good generalization and interpretability. The extracted rules clearly explain customer behavior, making the model useful for real-world marketing decisions.

---

### ✅ **Key Takeaways**

* Decision Trees are powerful and interpretable.
* Limiting depth avoids overfitting.
* Campaign history and contact type strongly influence subscriptions.

