from flask import Flask, render_template
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

app = Flask(__name__)

@app.route('/')
def index():
    # Load the dataset (replace 'sample_data.csv' with your file path)
    data = pd.read_csv('sample_data.csv')

    # Encode categorical variables (e.g., Gender) using LabelEncoder
    label_encoder = LabelEncoder()
    data['Gender'] = label_encoder.fit_transform(data['Gender'])

    # Encode cartoon preferences using one-hot encoding
    data = pd.get_dummies(data, columns=['Cartoon_Preferences'], prefix='Pref', drop_first=True)

    # Exclude the "Name" column from features
    X = data.drop(['Party', 'Name'], axis=1)
    Y = data['Party']

    # Split the data into a training and testing set
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    # Create and train a logistic regression model
    model = LogisticRegression()
    model.fit(X_train, Y_train)

    # Make predictions on the test set
    predictions = model.predict(X_test)

    # Calculate accuracy on the test set
    accuracy = accuracy_score(Y_test, predictions) * 100

    # Predict the winner for the entire dataset
    predicted_winner = model.predict(X)
    party_votes = pd.Series(predicted_winner).value_counts()
    winning_party = party_votes.idxmax()

    return render_template('index.html', accuracy=accuracy, winning_party=winning_party)

if __name__ == '__main__':
    app.run(debug=True)
