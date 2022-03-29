from django.shortcuts import render,HttpResponse
from django.views import View
from .forms import contactForm

# Create your views here.
def home(request):
      return HttpResponse('<h1>This is function based home page</h1>')

class my_view(View):
     
      def get(self,request):
            context ={'msg':'welcome to class based view'}
            return render(request, 'myapp/home.html', context)

class contactclass(View):
      def get(self,request):
            form = contactForm()
            return render(request, 'myapp/contact.html', {'form':form})
      def post(self, request):
            form = contactForm(request.POST)
            if form.is_valid():
                  print(form.cleaned_data['name'])
                  return HttpResponse('thank you for you submission')


def formFun(request):
      if request.method == 'POST':
            form = contactForm(request.POST)
            if form.is_valid():
                  print(form.cleaned_data['name'])
                  return HttpResponse('thank you for you submission')
      else:
            form = contactForm()
            return render(request, 'myapp/contact.html', {'form':form})

