from django.shortcuts import render,  redirect
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy

from django.views.generic import CreateView

from core.forms import ContactForm

def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('core:home_page')

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, _("Your message has been submitted!"))
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, _("Your message has not been submitted!"))
        return super().form_invalid(form)



def contact(request):
    form = ContactForm()
    print("GET")

    if request.method == "POST":
        form = ContactForm(data = request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, _("Your message has been submitted!"))
            return redirect("core:home_page")
        else:
            messages.add_message(request, messages.ERROR, _("Your message has not been submitted!"))


    context = {
        "form": form
    }
    return render(request, "contact.html", context=context)