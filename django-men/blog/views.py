from django.utils import timezone
from .models import Post, Comment
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, RegisterForm, LoginForm, ChangePasswordForm, CommentForm
from django.shortcuts import redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


def post_list(request):
    posts = (Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date'))
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


# rejestracja, widok zawiera od razu posta do bazy danych w sobie.
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
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Tworzenie nowego usera
            new_user = User.objects.create_user(username=form.cleaned_data['username'],
                                                email=form.cleaned_data['email'],
                                                password=form.cleaned_data['password1'])

            blog_user_group = Group.objects.get(name='blog_user')
            new_user.groups.add(blog_user_group)
            new_user.save()

            # Logowanie jak user stworzony
            login(request, new_user)
            return redirect('post_list')  # Redirect to some page after registration
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {"form": form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data.get('username_or_email')
            password = form.cleaned_data.get('password')
            if "@" in username_or_email:
                user = authenticate(username=username_or_email, password=password)
            else:
                user = authenticate(email=username_or_email, password=password)

            if user is not None:
                login(request, user)
                return redirect('post_list')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


def profile_view(request):
    user = request.user
    return render(request, 'user_profiles/profile_page.html', {'user': user})


def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  # Podtrzymanie sesji z hasłem
            return redirect('post_list')
    else:
        form = ChangePasswordForm(request.user)
    return render(request, 'user_profiles/change_password.html', {'form': form})


def comment_new(request, pk):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            post = get_object_or_404(Post, pk=pk)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'blog/post_comment_edit.html', {'form': form})


def comment_edit(request, post_pk, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('post_detail', pk=post_pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/post_comment_edit.html', {'form': form})
