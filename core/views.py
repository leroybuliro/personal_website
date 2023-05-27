from core.models import Comment, Article, ArticleStat, Stat
from core.forms import feedbackForm, commentForm, mailingForm
from django.shortcuts import redirect, render, get_object_or_404
from core.models import Stat
from core.utils import get_client_ip
from django.contrib import messages
from django.urls import reverse
from datetime import datetime
# from django.contrib.auth.decorators import login_required
# from django.conf import settings

def LandpageView(request):
    context = {}
    request.session['next'] = '/'

    ip = get_client_ip(request)
    Stat.objects.get_or_create(
        page="landing_page",
        IPAddres=ip,
        device = request.META.get('HTTP_USER_AGENT')
    )

    return render(request, 'core/landpage.html', context)



def HomepageView(request):
    context = {}
    context['current_year'] = datetime.now().year
    context['featured'] = Article.objects.filter(status='P').order_by('-publishdate').first()
    context['articles'] = Article.objects.filter(status='P').order_by('-publishdate')[1:]
    request.session['next'] = '/home/'

    ip = get_client_ip(request)
    Stat.objects.get_or_create(
        page="home",
        IPAddres=ip,
        device = request.META.get('HTTP_USER_AGENT')
    )

    if 'submitfeedback' in request.POST:
        form = feedbackForm(request.POST)
        if form.is_valid(): 
            form.instance.source = 'home'
            form.save()
            messages.add_message(request,messages.SUCCESS, 'Thank you for your feedback')
            return redirect(reverse('core:home'))

    if 'mailing' in request.POST:
        form = mailingForm(request.POST)
        if form.is_valid(): 
            form.save()
            messages.add_message(request,messages.SUCCESS, 'Successfully submitted')
            return redirect(reverse('core:home'))

    return render(request, 'core/homepage.html', context)

def BlogView(request):
    context = {}
    context['current_year'] = datetime.now().year
    context['articles'] = Article.objects.filter(status='P').order_by('-publishdate')
    request.session['next'] = '/logs/'

    ip = get_client_ip(request)
    Stat.objects.get_or_create(
        page="blog",
        IPAddres=ip,
        device = request.META.get('HTTP_USER_AGENT')
    )

    if 'submitfeedback' in request.POST:
        form = feedbackForm(request.POST)
        if form.is_valid(): 
            form.instance.source = 'blog'
            form.save()
            messages.add_message(request,messages.SUCCESS, 'Thank you for your feedback')
            return redirect(reverse('core:blog'))

    if 'mailing' in request.POST:
        form = mailingForm(request.POST)
        if form.is_valid(): 
            form.save()
            messages.add_message(request,messages.SUCCESS, 'Successfully submitted')
            return redirect(reverse('core:blog'))

    return render(request, 'core/blog.html', context)

def ArticleView(request, pk, slug):
    context = {}
    context['current_year'] = datetime.now().year
    obj = get_object_or_404(Article, id=pk, slug=slug)
    context['article'] = obj
    next = obj.get_absolute_url()
    request.session['next'] = next

    ip = get_client_ip(request)
    post_details=Article.objects.get(pk=obj.pk)
    ArticleStat.objects.get_or_create(
        article=post_details,
        IPAddres=ip,
        device = request.META.get('HTTP_USER_AGENT')
    )
    
    form = commentForm(request.POST or None)
    context['form'] = form
    if 'submitcomment' in request.POST:
        if form.is_valid():
            user = request.user
            content = form.cleaned_data.get('content')
            content_type = obj.get_content_type
            # content_type = ContentType.objects.get(model=c_type)
            object_id = obj.pk
            parent = None

            try:
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None

            if parent_id:
                parent_qs = Comment.objects.filter(pk=parent_id)
                if parent_qs.exists() and parent_qs.count() == 1:
                    parent = parent_qs.first()

            Comment.objects.get_or_create(
                user = user,
                content_type = content_type,
                object_id = object_id,
                content = content, 
                parent = parent
            )

            messages.add_message(request,messages.SUCCESS, 'Comment successfully added')
            
            return redirect(reverse('core:article', kwargs={'pk':obj.pk, 'slug':obj.slug}))

    if 'deletecomment' in request.POST:
        comment_id = request.POST.get('comment_id')
        instance = Comment.objects.get(pk=comment_id)
        # instance = get_object_or_404(Comment, pk=comment_id)
        instance.delete()
        messages.add_message(request,messages.SUCCESS, 'Comment successfully deleted')
        return redirect(reverse('core:article', kwargs={'pk':obj.pk, 'slug':obj.slug}))

    if 'submitfeedback' in request.POST:
        form = feedbackForm(request.POST)
        if form.is_valid():
            form.instance.source = obj
            form.save()
            messages.add_message(request,messages.SUCCESS, 'Thank you for your feedback')
            return redirect(reverse('core:article', kwargs={'pk':obj.pk, 'slug':obj.slug}))

    if 'mailing' in request.POST:
        form = mailingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS, 'Successfully submitted')
            return redirect(reverse('core:article', kwargs={'pk':obj.pk, 'slug':obj.slug}))

    return render(request, 'core/articlelayout.html', context)
    