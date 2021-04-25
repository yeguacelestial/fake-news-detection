from django import forms
from fake_news_detection.models import NewsArticle


class NewsArticleForm(forms.ModelForm):
    
    class Meta:
        model = NewsArticle
        # fields = '__all__'
        fields = ('newspaper', 'category', 'news_text', )
        labels = {
            'newspaper': 'What is the newspaper of the article?',
            'category': 'Select the category of the news article',
            'news_text': "Write down the text you want to predict whether it's fake or not."
        }
        widgets = {'text': forms.Textarea(attrs={'rows': 5, 'cols': 20, 'style': 'resize: none'})}

    def __init__(self, *args, **kwargs):
        super(NewsArticleForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Select a category..."