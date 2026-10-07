from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import DonorRegistration, Contact, Search
from .models import donor_Registration


def home(request):
    return render(request, 'polls/base.html')


def about(request):
    return render(request, 'polls/about.html')


def donor_registration(request):
    if request.method == 'POST':
        form = DonorRegistration(request.POST)
        if form.is_valid():
            donor = form.save()
            context = {
                'donor': donor,
                'forms': form
            }
            return render(request, 'polls/donor_list.html', context)
    else:
        form = DonorRegistration()

    context_form = {
        'forms': form
    }
    return render(request, 'polls/donor_registration.html', context_form)


def search(request):
    if request.method == 'POST':
        form = Search(request.POST)
        if form.is_valid():
            bloodgroup = form.cleaned_data.get('blood_group')
            state = form.cleaned_data.get('state', '').strip()
            city = form.cleaned_data.get('city', '').strip()

            donor_filter = donor_Registration.objects.filter(
                blood_group=bloodgroup,
                state__icontains=state,
                city__icontains=city,
            )
            context = {
                'donor_filter': donor_filter,
                'searched_group': bloodgroup,
                'searched_state': state,
                'searched_city': city,
            }
            return render(request, 'polls/search_list.html', context)
    else:
        form = Search()

    context_form = {
        'forms': form
    }
    return render(request, 'polls/search.html', context_form)


def search_info(request, id):
    detail = get_object_or_404(donor_Registration, id=id)
    context = {
        'details': detail
    }
    return render(request, 'polls/search_info.html', context)


def contact(request):
    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! Your message has been sent successfully. We will get back to you soon.')
            form = Contact()  # Reset form after successful submission
    else:
        form = Contact()

    context = {
        'forms': form
    }
    return render(request, 'polls/contact.html', context)