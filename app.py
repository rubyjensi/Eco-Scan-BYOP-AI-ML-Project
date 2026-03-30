import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import warnings

# Suppress warnings for cleaner terminal output
warnings.filterwarnings("ignore")

def run_eco_scan():
    # 1. Load the Dataset
    try:
        data = pd.read_csv('dataset.csv')
    except FileNotFoundError:
        print("Error: 'dataset.csv' file not found! Please ensure it is in the same folder.")
        return

    # 2. Vectorize the Text Data
    # AI models require numerical input, so we convert text words into token counts.
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(data['item'])
    y = data['category']

    # 3. Train the Naive Bayes Model
    model = MultinomialNB()
    model.fit(X, y)

    print("-" * 50)
    print("   🌱 Eco-Scan AI Model Trained Successfully! 🌱   ")
    print("-" * 50)

    # 4. Interactive Command Line Interface
    while True:
        query = input("\nEnter the waste item you want to dispose (or type 'exit' to quit): ").strip().lower()
        
        if query == 'exit':
            print("Thank you for keeping the environment clean. Goodbye!")
            break
        
        if not query:
            print("Please enter a valid item name.")
            continue
        
        # Predict the category for the user's input
        query_vector = vectorizer.transform([query])
        prediction = model.predict(query_vector)
        
        print(f"--> Result: Please dispose of this in the [{prediction[0].upper()}] bin.")

if __name__ == "__main__":
    run_eco_scan()