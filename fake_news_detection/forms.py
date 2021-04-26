from django import forms
from fake_news_detection.models import NewsArticle


class NewsArticleForm(forms.ModelForm):
    
    class Meta:
        model = NewsArticle
        # fields = '__all__'
        fields = ('newspaper', 'category', 'news_text', )
        labels = {
            'newspaper': 'Write down the name of the newspaper (Example: CNN):',
            'category': 'Select the category of the news article',
            'news_text': "Write down the text you want to predict whether it's fake or not."
        }
        widgets = {
            'news_text': forms.Textarea(
                attrs={
                    'rows': 5, 
                    'cols': 20, 
                    'style': 'resize: none; display: block;',
                }
            )
        }

    def __init__(self, *args, **kwargs):
        super(NewsArticleForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Select a category..."