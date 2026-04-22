# Sentiment Analysis Tool

NLP-powered sentiment analysis application that processes customer reviews and provides sentiment scores using TextBlob and NLTK.

## 🚀 Features

- **Text Preprocessing**: Tokenization, lemmatization, stopword removal
- **Sentiment Scoring**: Polarity and subjectivity analysis
- **Batch Processing**: Analyze multiple reviews at once
- **Real-time Analysis**: Interactive CLI for live testing
- **Confidence Metrics**: Sentiment confidence percentage
- **Summary Statistics**: Aggregated insights

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| NLTK | NLP Processing |
| TextBlob | Sentiment Analysis |
| Flask | Web Framework |

## 📊 Analysis Output

The tool provides:
- Sentiment classification (Positive/Negative/Neutral)
- Polarity score (-1 to +1)
- Subjectivity score (0 to 1)
- Confidence percentage

## 🚦 Getting Started

```bash
# Clone the repository
git clone https://github.com/likithanelluri303-gif/sentiment-analysis.git

# Navigate to project folder
cd sentiment-analysis

# Install dependencies
pip install -r requirements.txt

# Run sentiment analyzer
python sentiment_analyzer.py
```

## 📁 Project Structure

```
sentiment-analysis/
├── sentiment_analyzer.py  # Main analysis script
├── requirements.txt       # Python dependencies
└── README.md          # Project documentation
```

## 💡 Sample Output

```
=================================================================
   SENTIMENT ANALYSIS TOOL   
   NLP-Powered Customer Review Analyzer   
=================================================================

[STEP 1] Analyzing Sample Reviews...
-----------------------------------------------------------------

  [1]  📝 Review: "This product is absolutely amazing! Best purchase ever."
       😊 Sentiment: POSITIVE
       📊 Polarity: 0.7500  |  Subjectivity: 0.6000
       🎯 Confidence: 75.0%

  [2]  📝 Review: "Very disappointed with the quality. Not worth the money."
       😟 Sentiment: NEGATIVE
       📊 Polarity: -0.5000  |  Subjectivity: 0.3000
       🎯 Confidence: 50.0%

[STEP 2] Summary Statistics
-----------------------------------------------------------------
  📈 Total Reviews Analyzed: 10
  😊 Positive: 4 (40.0%)
  😟 Negative: 3 (30.0%)
  😐 Neutral: 3 (30.0%)
```

## 🎯 Key Learnings

- Natural Language Processing (NLP)
- Text preprocessing techniques
- Sentiment analysis algorithms
- Tokenization and lemmatization

## 📝 License

MIT License

## 👤 Author

Your Name | B.Tech AI Student | Gitam University