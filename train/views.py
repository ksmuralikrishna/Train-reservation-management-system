from django.shortcuts import render, get_object_or_404, redirect
from .models import Train, Reservation, Payment
from django.contrib.auth.models import User

def home(request):
    return render(request, 'train/home.html')

def user_profile(request):
    user = request.user
    bookings = Reservation.objects.filter(user=user)
    return render(request, 'train/user_profile.html', {'user': user, 'bookings': bookings})

def admin_dashboard(request):
    trains = Train.objects.all()
    bookings = Reservation.objects.all()
    return render(request, 'train/admin.html', {'trains': trains, 'bookings': bookings})

def add_train(request):
    if request.method == 'POST':
        # Handle form submission and add train logic here
        pass
    return render(request, 'train/add_train.html')

def edit_train(request, train_id):
    train = get_object_or_404(Train, id=train_id)
    if request.method == 'POST':
        # Handle form submission and edit train logic here
        pass
    return render(request, 'train/edit_train.html', {'train': train})

def delete_train(request, train_id):
    train = get_object_or_404(Train, id=train_id)
    if request.method == 'POST':
        train.delete()
        return redirect('admin_dashboard')
    return render(request, 'train/delete_train.html', {'train': train})

def edit_booking(request, booking_id):
    booking = get_object_or_404(Reservation, id=booking_id)
    if request.method == 'POST':
        # Handle form submission and edit booking logic here
        pass
    return render(request, 'train/edit_booking.html', {'booking': booking})

def delete_booking(request, booking_id):
    booking = get_object_or_404(Reservation, id=booking_id)
    if request.method == 'POST':
        booking.delete()
        return redirect('admin_dashboard')
    return render(request, 'train/delete_booking.html', {'booking': booking})
