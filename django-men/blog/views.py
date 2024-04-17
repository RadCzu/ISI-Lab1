from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, RegisterForm
from django.shortcuts import redirect


def post_list(request):
    posts = (Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date'))
    # posts = (Post.objects.all)
    print(posts)
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def register(request):
    if request.method == "GET":
        form = RegisterForm(request.GET)

        if not form.is_valid():
            form = RegisterForm()
        else:
            form.save()
            return redirect("/")

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if not form.is_valid():
            form = RegisterForm()
        else:
            form.save()
            return redirect("/")

    return render(request, "registration/register.html", {"form": form})
