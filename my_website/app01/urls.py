from django.urls import path, include
from . import views

extra_urls = [
    path("<int:year>/<int:month>/", views.article_archive),
    path("<int:arg1>/<int:arg2>/<slug:slug>", views.article_archive3),

]


urlpatterns = [
    path("article/<int:year>/", views.article_year, {"version":"v1.0"}),
    # path("article/<int:year>/<int:month>/", views.article_archive),
    # path("article/<int:arg1>/<int:arg2>/<slug:slug>", views.article_archive3),
    path("article/", include(extra_urls)),
    path('login', views.login_view),
    path('file',views.download_file),

]
