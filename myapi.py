from nltk.sentiment import SentimentIntensityAnalyzer

class Api:
    def __init__(self):
        pass
    def sentiment_analysis(self,text):
        sia = SentimentIntensityAnalyzer()
        score = sia.polarity_scores(text)
        if score['compound'] >= 0.05:
            return "Positive Sentiment"
        elif score['compound'] <= -0.05:
            return "Negative Sentiment"
        else:
            return "Neutral Sentiment"

    def emotion_analysis(self,text):
        pass
    
    
    def ner(self,text):
        pass
    




