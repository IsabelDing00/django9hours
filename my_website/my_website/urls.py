"""my_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

# First, I want to create a url path for my app01 and the it will be called as test,
# then I go to the app01/views.py and create a function called test_view
# re_path is the old way to give the urls, and now we use path
# re_path(r'^article/2021/$',views.article_2021),
# re_path(r'^article/(?P<year>[0-9]{4})/(?P<month>[0-1][0-9])/$',views.article_archive),
# re_path(r'^article/([0-9]{4})/([0-1][0-9])$', views.article_archive2),
# re_path(r'^article/(?P<arg1>[0-9]{4})/(?P<arg2>\d+)/(?P<slug>[\w-]+)/$', views.article_archive3),    #[\w-]+:[a-zA-Z0-9] and -, _
#
# Path Converts
# str (no '/'), int, slug, uuid(Matches any slug string consisting of ASCII letters or numbers)
# path    matches any non-empty string including the path separator '/'  eg. <path:name> for scrap a website

"""
from django.contrib import admin
from django.urls import path, re_path, register_converter, include
# from app01 import views    when I import include above for manage multiple apps' urls, I can comment out this line
from . import converters

register_converter(converters.YearConverter, "yyyy")

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('test', views.test_view),
    # path('login', views.login_view),
    # path("article/2021/", views.article_2021),
    # #path("article/<str:name>/", views.article_str),
    # path("article/<yyyy:year>/", views.article_year),
    # path("article/<int:year>/<int:month>/", views.article_archive),
    # path("article/<int:arg1>/<int:arg2>/<slug:slug>", views.article_archive3),
    # comment out line 37-44 for managing multiple apps' urls and then type line 46
    path("app01/", include("app01.urls")),
]
