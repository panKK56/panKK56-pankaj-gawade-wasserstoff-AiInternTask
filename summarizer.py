from nltk.tokenize import sent_tokenize

class Summarizer:
    def summarize(self, text, max_length=5):
        sentences = sent_tokenize(text)
        if len(sentences) <= max_length:
            return text
        return ' '.join(sentences[:max_length])

