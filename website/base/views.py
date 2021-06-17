from django.shortcuts import render
from . forms import UserCreationForm
from django.views.generic.edit import CreateView, FormView
# Create your views here.




def index(request):
    return render(request, 'index.html',{})

def login(request):
    return render(request, 'base/login.html',{})

class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)


