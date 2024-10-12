import nltk
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords

class KeywordExtractor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))

    def extract_keywords(self, text, num_keywords=5):
        words = nltk.word_tokenize(text)
        filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in self.stop_words]
        word_counts = Counter(filtered_words)
        keywords = [word for word, _ in word_counts.most_common(num_keywords)]
        return keywords
