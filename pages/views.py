import html
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.messages.views import SuccessMessageMixin

from common.utils.email import send_email

from .models import ContactUs
from .forms import ContactUsForm


class ContactUsPageView(SuccessMessageMixin, CreateView):
    model = ContactUs
    form_class = ContactUsForm
    success_message = "We've received your message. Thank you for getting in touch!"
    success_url = reverse_lazy("pages:thanks")

    def form_valid(self, form):
        data = form.cleaned_data
        to = "nicolenorah49@gmail.com"
        subject = "A New Message Awaits You From a Website Visitor"
        content = f"""<h1>Greetings Team P2L Gamer,</h1>
                      <p>A new message has made its way through our website contact form:</p>
                      <ol>"""
        for key, value in data.items():
            label = key.replace("_", " ").title()
            entry = html.escape(str(value), quote=False)  # Ensuring special characters are properly escaped.
            content += f"<li><strong>{label}:</strong> {entry}</li>"

        content += "</ol><p>Please take a moment to review and address the message at your earliest convenience.</p>"

        send_email(to, subject, content)
        return super().form_valid(form)

class ContactUsThanksView(TemplateView):
    template_name = "pages/thanks.html"


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutUsView(TemplateView):
    template_name = "pages/about_us.html"