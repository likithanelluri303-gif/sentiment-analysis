import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob
import string

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('punkt_tab', quiet=True)

class SentimentAnalyzer:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        
    def preprocess(self, text):
        text = text.lower()
        tokens = word_tokenize(text)
        tokens = [t for t in tokens if t not in string.punctuation]
        tokens = [t for t in tokens if t not in self.stop_words]
        tokens = [self.lemmatizer.lemmatize(t) for t in tokens]
        return tokens
    
    def analyze_textblob(self, text):
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity
        
        if polarity > 0.1:
            sentiment = "POSITIVE"
        elif polarity < -0.1:
            sentiment = "NEGATIVE"
        else:
            sentiment = "NEUTRAL"
            
        confidence = abs(polarity) * 100
        
        return {
            'text': text,
            'sentiment': sentiment,
            'polarity': round(polarity, 4),
            'subjectivity': round(subjectivity, 4),
            'confidence': round(confidence, 2)
        }
    
    def analyze_batch(self, texts):
        results = []
        for text in texts:
            result = self.analyze_textblob(text)
            results.append(result)
        return results
    
    def get_summary(self, results):
        total = len(results)
        positive = sum(1 for r in results if r['sentiment'] == 'POSITIVE')
        negative = sum(1 for r in results if r['sentiment'] == 'NEGATIVE')
        neutral = sum(1 for r in results if r['sentiment'] == 'NEUTRAL')
        
        avg_polarity = sum(r['polarity'] for r in results) / total
        avg_subjectivity = sum(r['subjectivity'] for r in results) / total
        
        return {
            'total': total,
            'positive': positive,
            'negative': negative,
            'neutral': neutral,
            'positive_percent': round(positive/total*100, 2),
            'negative_percent': round(negative/total*100, 2),
            'neutral_percent': round(neutral/total*100, 2),
            'avg_polarity': round(avg_polarity, 4),
            'avg_subjectivity': round(avg_subjectivity, 4)
        }


def print_banner():
    print("\n" + "=" * 65)
    print("   SENTIMENT ANALYSIS TOOL   ")
    print("   NLP-Powered Customer Review Analyzer   ")
    print("=" * 65)


def print_results(result):
    emoji = {"POSITIVE": "😊", "NEGATIVE": "😟", "NEUTRAL": "😐"}
    
    print(f"\n  📝 Review: \"{result['text'][:60]}{'...' if len(result['text']) > 60 else ''}\"")
    print(f"     {emoji[result['sentiment']]} Sentiment: {result['sentiment']}")
    print(f"     📊 Polarity: {result['polarity']:.4f}  |  Subjectivity: {result['subjectivity']:.4f}")
    print(f"     🎯 Confidence: {result['confidence']:.1f}%")


def main():
    print_banner()
    
    analyzer = SentimentAnalyzer()
    
    sample_reviews = [
        "This product is absolutely amazing! Best purchase ever.",
        "Very disappointed with the quality. Not worth the money.",
        "The product is okay, nothing special but works fine.",
        "I love this! Exceeded my expectations. Will buy again!",
        "Terrible experience. Product broke after one week.",
        "Good value for money. Decent quality.",
        "Outstanding! Best in the market. Highly recommend!",
        "Not recommended. Poor customer service too.",
        "Average product. Does what it's supposed to do.",
        "Wow! Amazing quality and fast delivery. Very happy!"
    ]
    
    print("\n[STEP 1] Analyzing Sample Reviews...")
    print("-" * 65)
    
    results = analyzer.analyze_batch(sample_reviews)
    
    for i, result in enumerate(results, 1):
        print(f"\n  [{i}] ", end="")
        print_results(result)
    
    summary = analyzer.get_summary(results)
    
    print("\n" + "-" * 65)
    print("\n[STEP 2] Summary Statistics")
    print("-" * 65)
    print(f"\n  📈 Total Reviews Analyzed: {summary['total']}")
    print(f"  😊 Positive: {summary['positive']} ({summary['positive_percent']}%)")
    print(f"  😟 Negative: {summary['negative']} ({summary['negative_percent']}%)")
    print(f"  😐 Neutral: {summary['neutral']} ({summary['neutral_percent']}%)")
    print(f"\n  📊 Average Polarity: {summary['avg_polarity']:.4f}")
    print(f"  📊 Average Subjectivity: {summary['avg_subjectivity']:.4f}")
    
    print("\n[STEP 3] Live Demo")
    print("-" * 65)
    print("\n  Type your own review to analyze (or 'quit' to exit):\n")
    
    while True:
        user_input = input("  ➤ Enter review: ").strip()
        
        if user_input.lower() == 'quit':
            print("\n  Thanks for using Sentiment Analyzer!")
            break
            
        if not user_input:
            continue
            
        result = analyzer.analyze_textblob(user_input)
        print_results(result)


if __name__ == "__main__":
    main()