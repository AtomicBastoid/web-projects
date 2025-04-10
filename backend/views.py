from django.shortcuts import render
from . import forms
from django.core.mail import send_mail

def index(request):
    return render(request, 'backend/index.html')

def contact(request):
    if request.method == 'POST':
        form = forms.contactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            subject = "Email from: " + name
            recipient_list = ["keshwanieishal001@gmail.com"]  # List of recipients (can include yourself)

            send_mail(
                subject,
                message,
                None,  # Uses DEFAULT_FROM_EMAIL from settings.py
                recipient_list,
                fail_silently=False,
            )
            msg = "Email sent successfully!"
            form = forms.contactForm()  # Reset the form after successful submission
            success = True
    else:
        msg = ""
        form = forms.contactForm()
        success = False
    
    return render(request, 'backend/contact.html', {
        "form": form,
        "msg": msg,
        "success": success
    })
