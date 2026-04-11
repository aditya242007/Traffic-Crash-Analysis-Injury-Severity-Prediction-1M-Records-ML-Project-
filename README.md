# 🚦 Traffic Crash Severity Analysis & Prediction

## 📌 Project Overview

Road accidents are a major public safety concern, but not all crashes result in severe injuries.
This project analyzes large-scale traffic crash data to uncover **patterns, risk factors, and predictive insights** related to injury severity.

The goal is to:

* Understand **when, where, and why crashes happen**
* Identify **factors influencing injury severity**
* Build a **machine learning model** to predict crash outcomes

---

## 🎯 Objectives

* Perform **Exploratory Data Analysis (EDA)** on crash data
* Analyze crash patterns by:

  * Time (hour, day, month)
  * Weather conditions
  * Speed limits
  * Geographic distribution
* Handle **class imbalance** in injury severity
* Build and evaluate a **classification model**
* Improve model performance using **threshold tuning**

---

## 📊 Key Insights from Data

### 🧠 Injury Severity Distribution

* Majority of crashes result in **no injury**
* Severe injuries and fatalities are **extremely rare**
* Dataset is **highly imbalanced**, which impacts model performance

---

### ⏰ Time-Based Patterns

* Peak crash hour: **3 PM (15:00)**
* Crashes increase during:

  * Morning commute (7–9 AM)
  * Evening rush (3–6 PM)
* Lowest crash frequency during early morning (2–5 AM)

👉 Insight: **Traffic volume is a major driver of crashes**

---

### 📅 Day-wise Trends

* **Weekdays > Weekends** in crash frequency
* Friday shows the **highest number of crashes**

👉 Insight: Work-related travel increases accident risk

---

### 🌦️ Weather Impact

* Most crashes occur during **clear weather**
* Rain and snow contribute far less comparatively

👉 Insight:
Crashes are more influenced by **traffic density than weather conditions**

---

### 🚗 Speed Limit Distribution

* Most crashes occur around **~30 mph zones**

👉 Insight:
Urban areas (moderate speed zones) are **high-risk zones**

---

### 🗺️ Geographic Distribution

* Crashes are densely concentrated in **urban regions**
* Indicates correlation with **traffic congestion and population density**

---

### ⚠️ Primary Causes of Crashes

Top contributors:

* Unable to determine (data limitation)
* Failure to yield right-of-way
* Following too closely
* Improper overtaking

👉 Insight:
Human driving behavior plays a **major role in accidents**

---

## 🤖 Machine Learning Model

### Model Used:

* **XGBoost Classifier**

### Evaluation Metrics:

| Metric      | Test Set | Synthetic Set |
| ----------- | -------- | ------------- |
| Accuracy    | 89.1%    | 88.9%         |
| Weighted F1 | 0.90     | 0.86          |
| Macro F1    | 0.54     | 0.36          |

---

## ⚠️ Important Observation (Critical Insight)

Despite high accuracy:

* Model performs poorly on **minority classes (serious injuries)**
* **Serious Injury detection = 0 recall**

👉 Why?

* Severe **class imbalance**
* Majority class dominates predictions

---

## 🔧 Improvements Applied

* Threshold tuning to improve classification balance
* Performance comparison on synthetic dataset

---

## 🚧 Limitations

* Severe class imbalance affects model fairness
* Large number of **"Unable to Determine"** causes reduces interpretability
* Model struggles with **rare but critical cases (serious injuries)**

---

## 🚀 Future Improvements

* Apply **SMOTE / Oversampling techniques**
* Use **class-weighted models**
* Try **ensemble models (LightGBM, CatBoost)**
* Focus on **recall optimization for severe injuries**
* Feature engineering for better signal extraction

---

## 🧰 Tech Stack

* Python
* Pandas, NumPy
* Matplotlib, Seaborn
* Scikit-learn
* XGBoost

---

## 📁 Project Structure

```
├── data/
├── notebooks/
├── outputs/
│   ├── visualizations/
│   ├── model_results/
├── README.md
```

---

## 💡 Key Takeaways

* Traffic crashes are **more about human behavior than environment**
* Peak accident times align with **traffic congestion**
* High model accuracy can be **misleading in imbalanced datasets**
* Detecting **rare but critical events** is the real challenge

---

## 🧠 What This Project Demonstrates

* Strong **EDA & visualization skills**
* Understanding of **real-world data challenges**
* Ability to **interpret model performance critically**
* Awareness of **bias-variance & class imbalance issues**
* Focus on **business and safety impact**

---

## 🙌 Final Note

This project is not just about predicting crashes —
it's about understanding **risk, safety, and decision-making in real-world systems**.

---
