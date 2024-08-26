from django.shortcuts import render, get_object_or_404, redirect
from .models import Menu, Book, Table
from .forms import BookForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    menus = Menu.objects.all()[0:3]
    context = {
        'menus' : menus,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')



def menu_view(request):
    menus = Menu.objects.all()
    context = {
        'menus' : menus,
    }
    return render(request, 'pages/menu.html', context)

def menu_detail(request, id, slug):
    menu = get_object_or_404(Menu, id=id, slug=slug)
    context = {
        'menu' : menu,
    }
    return render(request, 'pages/menu_detail.html',context)

@login_required
def booking_vieW(request):
    table = Table.objects.count()
    book = Book.objects.count()
    if table <= book:
        return render(request, 'pages/menu_table.html')
    else:
        if request.method == 'POST':
            form = BookForm(request.POST)
            if form.is_valid():
                booking = form.save(commit=False)
                booking.user = request.user
                booking.save()
                return redirect('home')
        else:
            form = BookForm()
    return render(request, 'pages/reserve.html', {'form' : form})


@login_required
def booking(request):
    if request.user.is_staff or request.user.is_superuser:
        book = Book.objects.all()
    else:    
        user = request.user
        book = Book.objects.filter(user=user)
    
    book_count = book.count()
    context = {

        'book' : book,
        'book_count' : book_count,
    }
    return render(request, 'pages/book.html', context)


def delete_booking(request):
    book = Book.objects.filter(user=request.user)
    book.delete()
    return redirect('reserve')

@login_required
def update_booking(request, pk):
    booking = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=booking)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('home')
    else:
        form = BookForm(instance=booking)
    return render(request, 'pages/reserve.html', {'form' : form})
