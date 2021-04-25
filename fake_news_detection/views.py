import joblib

from django.shortcuts import render
from django.http import HttpResponse

from sklearn.feature_extraction.text import TfidfVectorizer

from fake_news_detection.models import NewsArticle
from fake_news_detection.forms import NewsArticleForm


tfidf_vectorizer = joblib.load('vectorizer.sav')
pac = joblib.load('model.sav')

def base(request):
	return render(request, 'base.html')


def index(request):
	if request.method == 'GET':
		form = NewsArticleForm()
		return render(request, 'fake_news_detection/index.html', {'form': form})


def result(request):
	form_params = request.GET
	news_text = form_params['news_text']

	vec_news_text = tfidf_vectorizer.transform([news_text])
	ans = pac.predict(vec_news_text)

	context = {
		'ans': ans[0], 
		'form_params': form_params
	}

	request.session['results'] = context

	return render(request, "fake_news_detection/result.html", context)


def satisfaction(request):
	results = request.session.get('results')
	print(f"[D] We're on satisfaction page => {results}")
	print(f"[***] NEWSPAPER => {results['form_params']['newspaper']}")
	print(f"[***] CATEGORY => {results['form_params']['category']}")
	print(f"[***] NEWSTEXT => {results['form_params']['news_text']}")
	print(f"[***] LABEL => {results['ans']}")

	args_sent_by_user = request.GET

	if "user_choice" in args_sent_by_user:
		print("[+] USER IS SATISFIED. SAVE THE MODEL TO THE DATABASE.")

		newspaper = results['form_params']['newspaper']
		category = results['form_params']['category']
		news_text = results['form_params']['news_text']
		label = results['ans']

		form = NewsArticleForm(results['form_params'])
		if form.is_valid():
			NewsArticle.objects.create(newspaper=newspaper, category=category, news_text=news_text, label=label)

	return render(request, "fake_news_detection/satisfaction.html", {'args_sent_by_user': args_sent_by_user})