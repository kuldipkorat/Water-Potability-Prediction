# 🌊 Water Potability Prediction

This project predicts whether water is potable (safe to drink) based on various chemical properties of water. The machine learning model classifies water as **Potable** or **Not Potable** using nine key features.

---

## 📋 Table of Contents
- [📖 Overview](#-overview)
- [✨ Features](#-features)
- [💻 Technologies Used](#-technologies-used)
- [📊 Dataset](#-dataset)
- [🚀 How to Run the Application](#-how-to-run-the-application)

---

## 📖 Overview
Clean drinking water is a global necessity, and ensuring its safety is a critical challenge. This project leverages machine learning to predict water potability based on nine chemical parameters like pH, hardness, and turbidity.

The project includes a **Streamlit web application** that allows users to input water parameters and get real-time predictions along with potability probabilities.

---

## ✨ Features
- Interactive **user interface** for predicting water potability.
- Provides **probability scores** for the predictions.
- **Visual insights** using heatmaps, bar charts, and statistical plots.
- Easy-to-use **Streamlit app** for seamless interaction.

---

## 💻 Technologies Used
- **Python**: Core programming language.
- **Streamlit**: Web framework for building interactive applications.
- **Scikit-learn**: For model training and predictions.
- **Pandas**: Data handling and analysis.
- **Matplotlib/Seaborn**: For creating visualizations.

---

## 📊 Dataset
The dataset consists of water quality parameters with the following features:
- **Features**: pH, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic Carbon, Trihalomethanes, Turbidity.
- **Target**: Potability (0 = Not Potable, 1 = Potable).

**Source**: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php).

---

## 🚀 How to Run the Application

1. **Clone the Repository**:
   ```bash
   https://github.com/kuldipkorat/Water-Potability-Prediction.git
   cd water-potability-prediction

   pip install -r requirements.txt

   streamlit run app.py

## 🌟 Credits
- Made and deployed by Kuldip Korat.