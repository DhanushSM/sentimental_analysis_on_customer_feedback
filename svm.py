from flask import Flask, render_template, request
from nltk.sentiment import SentimentIntensityAnalyzer

app = Flask(__name__)

# Initialize Sentiment Intensity Analyzer (VADER)
sia = SentimentIntensityAnalyzer()

# Function to perform sentiment analysis
def analyze_sentiment(input_text):
    scores = sia.polarity_scores(input_text)
    if scores['compound'] >= 0.2:
        return "Positive"
    elif scores['compound'] <= -0.2:
        return "Negative"
    else:
        return "Neutral"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        user_input = request.form['feedback']
        sentiment = analyze_sentiment(user_input)
        return render_template('result.html', sentiment=sentiment)

if __name__ == "__main__":
    app.run(debug=True)
