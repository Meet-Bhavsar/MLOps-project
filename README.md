# 🛡️ Phishing Website Classification - MLOps Pipeline Project

This project is a complete MLOps pipeline built to classify phishing websites using machine learning. It includes data ingestion, validation, transformation, model training, batch prediction, and a web application built with **FastAPI** for interaction and inference.

---

## 🚀 How It Works

The pipeline includes the following stages:

1. **Data Ingestion**: Collects and stores raw data.
2. **Data Validation**: Checks data schema and cleanliness.
3. **Data Transformation**: Prepares features for training.
4. **Model Training**: Trains a classifier to detect phishing websites.
5. **Batch Prediction**: Runs predictions on bulk/unseen data.
6. **Web Interface**: A FastAPI-based UI for interacting with the model.

---

## ⚙️ Tech Stack

- **Language**: Python 3.x  
- **Framework**: FastAPI  
- **Libraries**: scikit-learn, pandas, numpy, pymongo  
- **Model Type**: Classification  
- **Deployment**: FastAPI (locally), Docker (optional)  
- **Database**: MongoDB (for data storage)
  
---

## ▶️ How to Run the Project

### 1. Clone the Repository
### 2. Install Requirements
  ```bash
    pip install -r requirements.txt
```
### 3. Run ML pipeline
  ```bash
    python main.py
```
### 4. Launch FastAPI app
  ```bash
    python app.py
```
Thanks for checking out this project! 😊
