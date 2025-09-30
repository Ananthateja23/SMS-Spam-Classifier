# SMS Spam Classifier

This project aims to classify SMS messages as either **spam** or **ham** (non-spam) using machine learning techniques. It leverages Natural Language Processing (NLP) and various machine learning algorithms to accurately detect unwanted messages.

## Table of Contents

* [Overview](#overview)
* [Features](#features)
* [Dataset](#dataset)
* [Model Training](#model-training)
* [Files](#files)
* [Installation](#installation)
* [Usage](#usage)
* [Deployment](#deployment)



## Overview

Spam messages are a persistent challenge in communication systems. This project utilizes machine learning techniques to automatically categorize SMS messages as either spam or ham. The model is trained on a labeled dataset, enabling it to identify and filter out unwanted messages.

## Features

* **SMS Classification**: Classifies messages as spam or ham.
* **Data Preprocessing**: Cleans and prepares text data for modeling.
* **Model Training**: Trains machine learning models on the preprocessed data.
* **Model Evaluation**: Assesses model performance using appropriate metrics like precision_score, accuracy_score, confusion_matrix

## Dataset

The dataset used in this project is the "SMSSpamCollection," which contains labeled SMS messages. Each message is tagged as either spam or ham, providing the basis for supervised learning. 

## Model Training

The model training process involves several steps:

1. **Data Preprocessing**: Cleaning and transforming the raw SMS messages into a suitable format for training.
2. **Feature Extraction**: Converting the preprocessed messages into numerical features that can be used by the machine learning algorithm.
3. **Model Training**: Training a machine learning model using the labeled SMS messages.
4. **Model Evaluation**: Assessing the model's performance using appropriate metrics like precision_score, accuracy_score, confusion_matrix

## Files

* `app.py`: The main application file that runs the Streamlit app.
* `SMS-Spam-Classifier.ipynb`: Jupyter notebook containing the model training and evaluation code.
* `model.pkl`: Pickled machine learning model used for making predictions.
* `vectorizer.pkl`: Pickled vectorizer used for transforming text data.
* `spam.csv`: CSV file containing the raw SMS data.
* `requirements.txt`: File listing the required Python packages for the project.

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/Ananthateja23/SMS-Spam-Classifier.git
   cd SMS-Spam-Classifier
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Download necessary NLTK data:

   ```bash
   python -m nltk.downloader stopwords wordnet punkt
   ```

## Usage

To run the application locally:

```bash
streamlit run app.py
```

This command will start a local server and open the application in your default web browser.

## Deployment

You can deploy this Streamlit app on **Render** by following these steps:

1. **Sign up / Log in** to [Render](https://render.com/).

2. **Create a new Web Service**:

   * Click on **New** → **Web Service**.
   * Connect your GitHub account and select the repository: `SMS-Spam-Classifier`.

3. **Configure the service**:

   * **Environment**: Python 3
   * **Build Command**:

     ```bash
     pip install -r requirements.txt
     ```
   * **Start Command**:

     ```bash
     streamlit run app.py --server.port $PORT --server.address 0.0.0.0
     ```

4. **Deploy the service**:

   * Click **Create Web Service** and Render will automatically build and deploy your app.
   * Once deployed, you will get a public URL where anyone can access your 
    SMS Spam Classifier app.

**Tip**: Make sure your `requirements.txt` file includes all necessary dependencies for Streamlit and model prediction.



