from django.shortcuts import render

# Create your views here.
from . import forms

def index(req):
    return render(req,'basicapp/index.html')

def form_name_view(req):

    form=forms.formName()

    if req.method=='POST':
        form=forms.formName(req.POST)

        if form.is_valid():
            print("VALIDATION SUCCESS");
            print("NAMe: "+form.cleaned_data['name'])
            print("EMAIL: "+form.cleaned_data['email'])
            print("TEXT: "+form.cleaned_data['text'])


    return render(req,'basicapp/form_page.html',{'form':form})
