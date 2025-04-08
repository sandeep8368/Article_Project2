from django.shortcuts import render
from myapp.models import ArticleModel
# Create your views here.
def display_home(request):
    submitted = False
    if request.method == 'POST':
        submitted = True
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        ArticleModel.objects.create(title = name , desc= desc)
    return render(request, 'html/index.html', {'submitted':submitted})



def display_allArticles(request):
    all_article = ArticleModel.objects.all()
    return render(request, 'html/all_article.html' ,{"data":all_article})

def display_spec(request,id):
    spec_article = ArticleModel.objects.get(id=id)
    print(spec_article.title)
    print(spec_article.desc)
    return render(request, 'html/specific.html', {"data":spec_article})