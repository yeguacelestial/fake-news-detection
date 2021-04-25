import joblib

from django.shortcuts import render
from django.http import HttpResponse

from sklearn.feature_extraction.text import TfidfVectorizer

from fake_news_detection.models import NewsArticle
from fake_news_detection.forms import NewsArticleForm


tfidf_vectorizer = joblib.load('vectorizer.sav')
pac = joblib.load('model.sav')


def index(request):
	news_article_model = NewsArticle()

	if request.method == 'GET':
		form = NewsArticleForm()
		return render(request, 'index.html', {'form': form})

	else:
		form = NewsArticleForm(request.POST)
		if form.is_valid():
			form.save()

		return render(request, "result.html", {'news_text': form.instance.news_text})


def result(request):
	news_text = request.GET['news_text']

	vec_news_text = tfidf_vectorizer.transform([news_text])
	ans = pac.predict(vec_news_text)

	return render(request, "result.html", {'ans': ans[0]})


def satisfaction(request):
	args_sent_by_user = request.GET

	if "user_choice" in args_sent_by_user:
		print("The user was satisfied with the results.")

	return render(request, "satisfaction.html", {'args_sent_by_user': args_sent_by_user})