from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    return render(request, "index.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)
            send_mail(
                subject=f"New Portfolio Contact from {name}",
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=True,
            )
            messages.success(request, "Thank you for reaching out! I'll get back to you soon.")
            return redirect('contact')
        else:
            messages.error(request, "Please fill in all fields.")
    return render(request, "index.html")