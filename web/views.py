from django.shortcuts import render,get_object_or_404
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.contrib.postgres.search import SearchVector,SearchRank,SearchQuery

from posts.models import Post, Category, Author
from main.functions import paginate_instances

def index(request):
    posts = Post.objects.filter(is_deleted=False, is_draft=False)

    categories = Category.objects.all()[:8]
    authors = Author.objects.all()[:9]

    q = request.GET.get('q')
    if q:
        # posts = posts.filter(title__search=q) // for beginner search
        # posts=posts.annotate(search=SearchVector("title","author__name","categories__title")).filter(search=q) // this is  advanced
        vector = SearchVector("title","author__name","categories__title")
        query = SearchQuery(q)

        posts = posts.annotate(rank=SearchRank(vector,query)).filter(rank__gte=0.0001).order_by("-rank")

    search_authors = request.GET.getlist("author")
    if search_authors:
        posts = posts.filter(author__in=search_authors)

    search_category = request.GET.getlist("category")
    if search_category:
        posts = posts.filter(categories__in=search_category).distinct()

    sort = request.GET.get("sort")
    if sort:
        if sort == "title-asc":
            posts = posts.order_by("title")
        elif sort == "title-desc":
            posts = posts.order_by("-title")
        elif sort == "date-asc":
            posts = posts.order_by("published_date")
        elif sort == "date-desc":
            posts = posts.order_by("-published_date")

    instances = paginate_instances(posts, request=request,per_page=9)

    context = {
        "instances": instances,
        "authors": authors,
        "categories": categories,
    }

    return render(request, 'web/includes/index.html', context=context)


def post(request,id):
    instance = get_object_or_404(Post.objects.filter(id=id))
    context={
        "title":  "Blog",
        "instance": instance,
    }
    return render(request,"web/includes/post.html",context=context)