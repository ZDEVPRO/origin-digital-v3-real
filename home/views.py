from django.shortcuts import render, redirect
from home.forms import ContactForm
from home.models import Contact, Projects
from django.contrib import messages
from django.utils.translation import gettext, gettext_lazy as _, pgettext
import requests


def index(request):
    return render(request, 'index/base.html')


def pricing(request):
    return render(request, 'pricing/base.html')


def blog(request):
    return render(request, 'blog/base.html')


def about(request):
    return render(request, 'about/base.html')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = Contact()
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.phone = form.cleaned_data['phone']
            data.message = form.cleaned_data['message']
            data.ip = get_client_ip(request)
            data.save()
            messages.success(request, _('Xabaringiz qabul qilindi! Sizga qisqa fursat ichida javob beramiz. Raxmat!'))

            text = f'🇺🇿 YANGI XABAR KELDI! 🇺🇿 \n' \
                   f'\n 👨  FISH: {data.first_name} {data.last_name}' \
                   f'\n 📲  Telefon raqam: {data.phone}' \
                   f'\n 🌐  IP RAQAM: {data.ip}' \
                   f'\n 🕒  VAQT: {data.create_time.strftime("%H:%M")}' \
                   f'\n 📆  SANA: {data.create_date.strftime("%d-%b, %Y-Yil")}' \
                   f'\n 📩  XABAR: {data.message}'
            text1 = "".join(text)

            bot_token = '5260192605:AAEGRPGEAyN-g6ygFy-pvZNFsgZk9eQu6Gc'
            bot_chatID = '1255807110'

            url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chatID}&parse_mode=Markdown&text={text1}'

            response = requests.get(url)

        return redirect('contact')
    form = ContactForm
    context = {'form': form, }
    return render(request, 'contact/base.html', context)


def blog_detail(request):
    return render(request, 'blog_detail/base.html')


def services(request):
    return render(request, 'services/base.html')


def projects_view(request):
    projects_all = Projects.objects.all().order_by('-id')
    context = {
        'projects_all': projects_all,
    }
    return render(request, 'projects/base.html', context)
