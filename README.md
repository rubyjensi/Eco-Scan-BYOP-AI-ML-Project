# Eco-Scan: AI Waste Classifier

## Overview
Eco-Scan is a Bring Your Own Project (BYOP) submission for the Fundamentals of AI and ML course. It is a lightweight Natural Language Processing (NLP) tool that helps accurately classify everyday campus waste into **Organic**, **Recyclable**, or **Landfill** categories using a Multinomial Naive Bayes algorithm.

## The Problem
Improper waste segregation is a daily issue on campus and in hostels. People often get confused about where to throw items like "greasy pizza boxes" or "biscuit wrappers," leading to contaminated recycling bins. This project aims to solve that using text-based AI classification.

## Features
* Simple and fast Command Line Interface (CLI).
* Built using `scikit-learn` for machine learning and `pandas` for data handling.
* Custom dataset tailored to common campus and hostel waste.

## How to Set Up and Run

**1. Clone the repository:**
```bash
git clone [https://github.com/rubyjensi/Eco-Scan-BYOP-AI-ML-Project.git](https://github.com/rubyjensi/Eco-Scan-BYOP-AI-ML-Project.git)
cd Eco-Scan-BYOP-AI-ML-Project

**2. Install dependencies:**
Make sure you have Python installed. Then run the following command in your terminal:
pip install -r requirements.txt

**3. Run the application:**
python app.py

**Usage**
Simply type the name of the garbage item when prompted (e.g., "plastic bottle" or "apple core") and the AI will predict the correct bin. Type exit to close the application.


