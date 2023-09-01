from django.shortcuts import render,redirect

# Create your views here.
from .forms import CustomerRegistrationForm


def registration_form(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the data to the database
            return redirect('success_page')  # Redirect to a success page
    else:
        form = CustomerRegistrationForm()
    
    return render(request, 'registration_form.html', {'form': form})

