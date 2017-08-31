from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from sales_tool.models import Event
from . import views

urlpatterns =[
    #url(r'^$', ListView.as_view(queryset=Event.objects.all().order_by("-date")[:25],
    #                                       template_name="sales_tool/calendar.html")),
    #url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Post,
    #                                          template_name = 'blog/post.html')),
    #url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Event,
    #                                          template_name = 'sales_tool/event.html')),

    url(r'^$', views.main, name='update'),
    url(r'^(?P<pk>\d+)/$', views.EventUpdate.as_view(), name='add')
    ]

