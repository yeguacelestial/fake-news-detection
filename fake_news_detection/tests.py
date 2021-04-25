import joblib

from django.test import TestCase
from fake_news_detection.models import NewsArticle


class NewsArticleTestCase(TestCase):
    def setUp(self):
        # Load model
        self.tfidf_vectorizer = joblib.load('vectorizer.sav')
        self.pac = joblib.load('model.sav')

        # Load real news article
        with open('real_news_article.txt', 'r') as real_news_article:
            self.real_news_text = real_news_article.read()
        
        # Load fake news article
        with open('fake_news_article.txt', 'r') as real_news_article:
            self.fake_news_text = real_news_article.read()


    def test_model_predicts_real_news_article(self):
        """
        Predicts an example of a verified real news article.
        """

        vec_news_text = self.tfidf_vectorizer.transform([self.real_news_text])
        result = self.pac.predict(vec_news_text)[0]

        self.assertEqual(result, 'Real')


    def test_model_predicts_fake_news_article(self):
        """
        Predicts an example of a verified fake news article.
        """
        vec_news_text = self.tfidf_vectorizer.transform([self.fake_news_text])
        result = self.pac.predict(vec_news_text)[0]

        self.assertEqual(result, 'Fake')