import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

# Sample dataset (replace with actual data)
data = {
    'description': ['Uber ride to the airport', 'Lunch at a restaurant', 'Movie tickets', 
                    'Grocery shopping', 'Flight ticket to London'],
    'category': ['Travel', 'Food', 'Entertainment', 'Food', 'Travel'],
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Step 1: Preprocessing text data
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['description'])  # Features from descriptions
y = df['category']  # Labels (target variable)

# Step 2: Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Train the model
model = MultinomialNB()
model.fit(X_train, y_train)

# Step 4: Evaluate the model
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Example of classifying new expenses
new_expenses = ['Pizza dinner with friends', 'Hotel stay in New York', 'Cinema ticket for a movie']
new_expenses_vectorized = vectorizer.transform(new_expenses)
predictions = model.predict(new_expenses_vectorized)

for expense, category in zip(new_expenses, predictions):
    print(f'Expense: "{expense}" is categorized as {category}')
