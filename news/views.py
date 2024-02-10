from django.http import HttpResponse
from django.shortcuts import render
from .models import *


# Create your views here.
def home(request):
    # load all the post from db(10)
    posts = Dailynews.objects.all()[:1]
    daily = Dailynews.objects.all()[:6]
    weaktop = Weeklynews.objects.all()[:3]
    weakes = Weeklynews.objects.all()
    side = sidecontent.objects.all()[:4]
    vido= vedio.objects.all()[:4]
    poli = politics.objects.all()

    cats = Category.objects.all()
    news = newnewsforegin.objects.all()

    data = {
        'posts': posts,
        'cats': cats,
        'weaks': weaktop,
        'dailys':daily,
        'sides':side,
        'weakey':weakes,
        'video':vido,
        'politics':poli,
        'new':news
    }
    return render(request, 'home.html', data)



def about(request):
    return render(request,'about.html')



def latest_news(request):
    vediobar=vedio.objects.all()
    poli = politics.objects.all()
    data={
        'vio':vediobar,
        'politics':poli
    }
    return render(request,'latest_news.html',data)



def contact(request):
    return render(request,'contact.html')

# E:\myprojects\nayan01\blog\template\base.html
# def dailypost(request,id):

#     post = Dailynews.objects.get(news_id=id)
#     cats = Category.objects.all()

#     # print(post)
#     return render(request, 'posts.html',{'post':post,"cat":cats})

def weekpost(request,id):

    cat = Weeklynews.objects.filter(week_id=id) 

    # print(post)
    return render(request, 'post.html',{"cats":cat})

# def videopost(request,id):

#     post = Weeklynews.objects.get(week_id=id)
#     cats = Category.objects.all()

#     # print(post)
#     return render(request, 'posts.html',{'post':post,"cat":cats})




# def category(request):
#     return render(request,'category.html')


def category(request):
    cat = Category.objects.all()[:4]
    data={
        "cats":cat
    }
    # posts = Post.objects.filter(cat=cat)
    
    return render(request, "category.html",data)


 
def postiddetail(request,id):
    cat = Dailynews.objects.filter(news_id=id)    
    return render(request, "post.html",{"cats":cat})

def post(request,id):
    cat = Dailynews.objects.filter(news_id=id)    
    return render(request, "post.html",{"cats":cat})

def sidecont(request,id):
    cat = sidecontent.objects.filter(id=id)    
    return render(request, "post.html",{"cats":cat})


def newnews(request,id):
    cat = newnewsforegin.objects.filter(new_id=id)    
    return render(request, "post.html",{"cats":cat})


