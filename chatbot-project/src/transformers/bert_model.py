from transformers import BertTokenizer, BertModel
import torch

class BERTModel:
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.model = BertModel.from_pretrained('bert-base-uncased')

    def encode(self, text):
        inputs = self.tokenizer(text, return_tensors='pt', padding=True, truncation=True)
        with torch.no_grad():
            outputs = self.model(**inputs)
        return outputs.last_hidden_state

    def get_similarity(self, text1, text2):
        vec1 = self.encode(text1)
        vec2 = self.encode(text2)
        cosine_sim = torch.nn.functional.cosine_similarity(vec1.mean(dim=1), vec2.mean(dim=1)
        return cosine_sim.item()