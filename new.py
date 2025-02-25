from flask import Flask, render_template, request
from nltk.sentiment import SentimentIntensityAnalyzer

app = Flask(__name__)

# Train the Sentiment Intensity Analyzer (VADER)
sia = SentimentIntensityAnalyzer()

# Function to perform sentiment analysis on user input
def analyze_sentiment(input_text):
    # Analyze sentiment using VADER
    scores = sia.polarity_scores(input_text)
    # Determine sentiment based on compound score and adjusted threshold
    if scores['compound'] >= 0.2:
        return "Positive"  # Positive sentiment
    elif scores['compound'] <= -0.2:
        return "Negative"  # Negative sentiment
    else:
        return "Neutral"  # Neutral sentiment

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        user_input = request.form['feedback']
        # Perform sentiment analysis
        sentiment = analyze_sentiment(user_input)
        return render_template('result.html', sentiment=sentiment)

if __name__ == "__main__":
    app.run(debug=True)
