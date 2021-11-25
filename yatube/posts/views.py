from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Group, Post, User


def index(request):
    title = 'Последние обновления на сайте'
    posts = Post.objects.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': title,
        'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    title = f'Записи сообщества {group.title}'
    posts = Post.objects.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': title,
        'group': group,
        'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author__username=username)
    num_post = posts.count()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'author': author,
        'posts': posts,
        'page_obj': page_obj,
        'num_post': num_post,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    author = User.objects.get(pk=post.author.id)
    num_post = Post.objects.filter(author__username=author).count()
    context = {
        'post': post,
        'num_post': num_post,
    }
    return render(request, 'posts/post_detail.html', context)


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(f'/profile/{post.author.username}/')
        return render(request, 'posts/create_post.html', {'form': form})
    form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})


@login_required
def post_edit(request, post_id,):
    post = get_object_or_404(Post, id=post_id,)
    if post.author == request.user:
        is_edit = True
        if request.method == 'GET':
            form = PostForm(instance=post)
            return render(
                request, 'posts/create_post.html',
                {'form': form, 'is_edit': is_edit, 'post': post}
            )
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect(f'/posts/{post_id}/')
        return render(
            request, 'posts/create_post.html',
            {'form': form}
        )
    return redirect(f'/posts/{post_id}/')
