from django.urls import path

from core.views import index, about, contact, ContactView, export

app_name = "core"

urlpatterns = [
    path("", index, name="home_page"),
    path("about/", about, name="about_page"),
    # path("contact/", contact, name="contact_page"),

    path("contact/", ContactView.as_view(), name="contact_page"),

    path("export/", export, name="export"),
]


# http://127.0.0.1:8000/core/