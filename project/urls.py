from django.conf.urls import include, url
from django.contrib import admin
from main import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # url(r'^state_detail/(?P<name>.+)/$', 'main.views.state_detail'),

    # url(r'^state_list/$', 'main.views.state_list'),

    # url(r'^first_view/(?P<starts_with>\w+)/$', 'main.views.first_view'),

    # url(r'^get_post/', 'main.views.get_post'),

    # url(r'^template_view/', 'main.views.template_view'),

    #reg views
    url(r'^state_list/$', 'main.views.state_list'),
    url(r'^state_detail/(?P<pk>[0-9]+)$', 'main.views.state_detail'),

    #cbv views
    url(r'^cbv_list/$', views.StateListView.as_view()),
    url(r'^cbv_detail/(?P<pk>[0-9]+)/$', views.StateListView.as_view()),
    url(r'^city_search/$', 'main.views.city_search'),
    url(r'^city_create/$', 'main.views.city_create'),
    url(r'^city_edit/(?P<pk>[0-9]+)/$', 'main.views.city_edit'),
    url(r'^city_delete/(?P<pk>[0-9]+)/$', 'main.views.city_delete'),

]
