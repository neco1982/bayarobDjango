from django.db.models import Count, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, reverse
from projects.forms import CommentForm
from projects.models import Project, Category, Comment
from django.core.mail import send_mail

def search(request):
    queryset = Project.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset
    }
    return render(request, 'search_results.html', context)

def get_category_count():
    queryset = Project.objects.values('category__name').annotate(Count('category__name'))
    return queryset

def category_detail(request, cats):
    category_count = get_category_count()
    category_posts = Project.objects.filter(category__name=cats)#('category__name'.replace('-',' '))      
    paginator = Paginator(category_posts, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    latest = Project.objects.order_by('-timestamp')[0:3]
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
        'latest': latest,
        'category_count': category_count,
        'category_posts': category_posts,
        'cats': cats.title().replace('-',' '),
        
    } 

    return render(request, 'category.html', context)



def index(request):
    last = Project.objects.order_by('-timestamp')[:1]
    context = {
        'last': last
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html', {})

def contact(request):
    if request.method == 'POST':       
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        phone = request.POST['phone']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        #send e-mail
        send_mail(
            firstname, #subject
            message, #message
            email, #from email
            ['bayapazarlama@gmail.com', 'necati.cicek@batingroup.com.tr'], #to email
        )

        return render(request, 'contact.html', {'firstname': firstname})
            
    else:
        return render(request, 'contact.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def otomasyon(request):
    category_count = get_category_count()
    project_list = Project.objects.filter(featured=True)
    paginator = Paginator(project_list, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    latest = Project.objects.order_by('-timestamp')[0:3]
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
        'latest': latest,
        'category_count': category_count
    }
    return render(request, 'otomasyon.html', context)

def otomasyon_detail(request, slug):    
    category_count = get_category_count()    
    #project = get_object_or_404(Project, id=id)
    project = Project.objects.filter(slug = slug)    
    latest = Project.objects.order_by('-timestamp')[0:3]
    
    # form = CommentForm(request.POST or None)
    # if request.method == "POST":
    #     if form.is_valid():
    #         form.instance.user = request.user
    #         form.instance.project = project
    #         form.save()
    context = {
        #'form': form,
        'projects': project,
        'category_count': category_count,
        'latest': latest,
        
    }
    return render(request, 'otomasyon_detail.html', context)

