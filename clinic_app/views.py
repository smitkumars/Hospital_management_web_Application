from django.forms.forms import Form
from django.shortcuts import render,redirect,get_object_or_404
from .models import Contact
from .forms import ContactForm
from django.views.generic import ListView,DetailView

# Create your views here.
from django.http import HttpResponse

class IndexView(ListView):
    model= Contact
    template_name= "clinic_app/index.html"
    context_object_name= 'contact_list'

    def get_queryset(self):
        return Contact.objects.all()

    


class ContactDetailView(DetailView):
    model= Contact
    template_name= "clinic_app/detail.html"
    context_object_name= 'detail1'

    


    



def create(request):
    if request.method=='POST':
        form= ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form= ContactForm()

    return render(request,'clinic_app/create.html',{'form':form})


def edit(request,pk,template_name='clinic_app/edit.html'):
    contact= get_object_or_404(Contact,pk=pk)
    form= ContactForm(request.POST or None, instance=contact)
    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, template_name,{'form':form})

def delete(request, pk , template_name='clinic_app/confirm_delete.html'):
    contact= get_object_or_404(Contact,pk=pk)
    if request.method=='POST':
        contact.delete()
        return redirect('index')

    return render(request, template_name, {'object':contact})


