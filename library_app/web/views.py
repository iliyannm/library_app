from django.shortcuts import render, redirect

from library_app.web.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm, CreateBookForm
from library_app.web.models import Profile, Book


# ready
def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


# ready
def show_index(request):
    profile = get_profile()
    books = Book.objects.all()

    context = {
        'profile': profile,
        'books': books,
    }

    if profile:
        return render(request, 'home-with-profile.html', context)

    return redirect('create profile')


# ready
def create_book(request):
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateBookForm()

    context = {
        'form': form,
    }

    return render(request, 'add-book.html', context)


# ready
def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = CreateBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateBookForm(instance=book)

    context = {
        'form': form,
        'book': book,
    }

    return render(request, 'edit-book.html', context)


# ready
def show_book_details(request, pk):
    book = Book.objects.get(pk=pk)

    context = {
        'book': book,
    }
    return render(request, 'book-details.html', context)


# ready
# def delete_book(request, pk):
#     book = Book.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = DeleteBookForm(request.POST, instance=book)
#         if form.is_valid():
#             form.save()
#             return redirect('show index')
#     else:
#         form = DeleteProfileForm(instance=book)
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'delete-book.html', context)


# ready
def show_profile(request):
    profile = get_profile()

    context = {
        'profile': profile,
    }

    return render(request, 'profile.html', context)


# ready
def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show profile')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'edit-profile.html', context)


# ready
def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'delete-profile.html', context)


# ready
def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
    }

    return render(request, 'home-no-profile.html', context)
