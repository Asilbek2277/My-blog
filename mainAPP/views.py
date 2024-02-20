from django.shortcuts import render, redirect
from django.views import View
from .models import *

class Home(View):
    def get(self, request):
        return render(request, 'home.html')


class About(View):
    def get(self, request):
        return render(request, 'about.html')


class Blog(View):

    def get(self, request):
        months_dict = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June',
                  '07': 'July', '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'}
        years=[]
        months=[]
        articles=Article.objects.all()
        for article in articles:
            years.append(str(article.date)[:4])
            months.append(str(article.date)[:4] + months_dict[str(article.date)[5:7]])
        years=set(years)
        months=set(months)


        context={
            'years': years,
            'months': months,
            'articles': articles,
            'titles': Article.objects.all()
        }

        return render(request, 'blog.html', context)
class Maqola(View):
    def get(self, request, pk):
        context={
            'title': ArticleItems.objects.filter(article__title=pk),
            'sana': Article.objects.all()
        }
        return render(request, 'maqola.html', context)


class Delete(View):
    def delete(self, request, pk):
        ArticleItems.objects.delete(id=pk)
        return redirect('/blog/')
