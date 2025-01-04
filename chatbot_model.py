import json
import spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load Spacy NLP model
nlp = spacy.load("en_core_web_sm")

class Chatbot:
    def __init__(self, faq_file):
        # Load FAQ data
        with open(faq_file, "r") as f:
            self.faqs = json.load(f)
        
        self.questions = [faq['question'] for faq in self.faqs]
        self.answers = [faq['answer'] for faq in self.faqs]
        
        # Fit the vectorizer on the FAQ questions
        self.vectorizer = CountVectorizer().fit(self.questions)
        self.question_vectors = self.vectorizer.transform(self.questions)

    def get_response(self, query):
        # Preprocess the query
        query_vec = self.vectorizer.transform([query])
        similarities = cosine_similarity(query_vec, self.question_vectors)
        index = similarities.argmax()
        if similarities[0, index] > 0.5:  # Confidence threshold
            return self.answers[index]
        else:
            return "I'm sorry, I didn't understand that. Can you please rephrase?"
# Example usage
if __name__ == "__main__":
    bot = Chatbot("faq.json")
    print(bot.get_response("How can I reset my password?"))
