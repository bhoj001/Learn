from django.conf.urls import url
from myapplibrary import views

urlpatterns = [
        url(r'^main_page_home$', views.main_page_home, name='main_page_home'),
        url(r'^$', views.index, name='index'),
        url(r'^morning$', views.morning, name='morning'),
        url(r'^hello_with_parameter$', views.hello_with_parameter, name='hello_with_parameter'),
        url(r'^article/(\d+)/', views.viewArticle, name = 'article'),
        url(r'^articles/(\d{2})/(\d{4})', views.viewArticles, name = 'articles'),
]
