import os
import re
import string
from typing import List
import spacy

LANGUAGE: str = os.environ.get("LANGUAGE", "pt_BR")
ENVIRONMENT: str = os.environ.get("ENVIRONMENT", "development")

if LANGUAGE == "pt_BR":
    from spacy.lang.pt.stop_words import STOP_WORDS


class TextProcessor:
    def __init__(self) -> None:
        if ENVIRONMENT == "development":
            self.nlp = spacy.load("pt_core_news_sm")
        else:
            self.nlp = spacy.load("pt_core_news_md")

    def preprocess_pipeline(self, text: str) -> List[str]:
        tokens = self.tokenize(text)
        lemmatized = self.lemmatize(tokens)
        without_stop_words = self.remove_stop_words(lemmatized)
        without_punctuation = self.remove_punctuation(without_stop_words)
        without_special_chars = self.remove_special_characters(without_punctuation)

        return without_special_chars

    def process_text(self, text: str) -> List[str]:
        return self.preprocess_pipeline(text)

    def tokenize(self, text: str) -> List[str]:
        doc = self.nlp(text)
        return [token.text for token in doc]

    def lemmatize(self, tokens: List[str]) -> List[str]:
        text = " ".join(tokens)
        doc = self.nlp(text)
        return [token.lemma_ for token in doc]

    def remove_stop_words(self, tokens: List[str]) -> List[str]:
        return [token for token in tokens if token not in STOP_WORDS]

    def remove_punctuation(self, tokens: List[str]) -> List[str]:
        clean_words = [
            "".join(char for char in word if char not in string.punctuation)
            for word in tokens
        ]

        return [word for word in clean_words if word]

    def remove_special_characters(self, tokens: List[str]) -> List[str]:
        return [
            re.sub(r"[^a-zA-ZáéíóúÁÉÍÓÚâêîôûÂÊÎÔÛãõÃÕçÇ0-9]+", "", token)
            for token in tokens
        ]
