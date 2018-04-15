from django.shortcuts import render
from app import forms
# Create your views here.

def index(request):
  return render(request, 'app/index.html')

def form_name_view(request):
  form = forms.FormName()
  if request.method == "POST":
    form = forms.FormName(request.POST)
    if form.is_valid():
      print("Validation successful")
      print("User Name", form.clean_data['name'])
      print("Email", form.clean_data['email'])
      print("Text Area", form.clean_data['text'])
  return render(request, "app/form_page.html", {'form':form})
  
