import random
from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article



def home_view(request, *args, **kwargs):
    article_list = Article.objects.all()
    context = {
        "object_list" : article_list,
    }
    HTML_STRING = render_to_string("home-view.html", context = context)
    return HttpResponse(HTML_STRING)