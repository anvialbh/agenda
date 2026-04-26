from django.shortcuts import render
from django.db.models import Q

from contact.forms import ConctactForm

def create(request):
    if request.method == 'POST':
        context = {
            'form': ConctactForm(request.POST),
            'site_title': 'Criar contato - ',
        }

        return render(
            request,
            'contact/create.html',
            context
        )
    
    context = {
            'form': ConctactForm(),
            'site_title': 'Criar contato - ',
        }

    return render(
        request,
        'contact/create.html',
        context
    )