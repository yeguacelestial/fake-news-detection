import joblib

from django.shortcuts import render
from django.http import HttpResponse

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf_vectorizer = joblib.load('vectorizer.sav')
pac = joblib.load('model.sav')


def index(request):
	return render(request, "index.html")


def result(request):
	news_text = request.GET['news_text']

	vec_news_text = tfidf_vectorizer.transform([news_text])
	ans = pac.predict(vec_news_text)

	return render(request, "result.html", {'ans': ans})