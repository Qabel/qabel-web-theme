"""theme_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.template.response import TemplateResponse as render
from django.utils.translation import ugettext_lazy as _

from qabel_web_theme import urls as theme_urls


def test_view(request):
    return render(request, 'base_menu.html')


def test_menu_view(request):
    return render(request, 'base_menu.html')


def test_page1(request):
    return render(request, 'base_menu.html')


def test_page2(request):
    return render(request, 'base.html')


def test_mail(request):
    return render(request, 'mail_base.html')


def menu(request, menu_items):
    menu_items += (
        {
            'title': _('Page 1'),
            'view': test_page1,
        },
        {
            'title': _('No menu'),
            'view': 'test-page2',
        },
        {
            'title': _('Base mail'),
            'view': test_mail,
        },
        {
            'title': _('Visit qabel.de'),
            'url': 'https://www.qabel.de/',
        }
    )


urlpatterns = [
    url(r'^', include(theme_urls)),
    url(r'^$', test_view),
    url(r'^menu/$', test_menu_view),
    url(r'^menu/page1/$', test_page1),
    url(r'^menu/page2/$', test_page2, name='test-page2'),
    url(r'^menu/mail/$', test_mail),
    url(r'^admin/', admin.site.urls),
]
