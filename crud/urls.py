from django.conf.urls import url, include

from . import views


# v1 = [
#     url(r'^person/$', views.PersonListV1.as_view()),
#     url(r'^person/(?P<pk>[0-9]+)/$',  views.PersonDetailV1.as_view()),
# ]
#
# v2 = [
#     url(r'^person/$', views.PersonListV2.as_view()),
#     url(r'^person/(?P<pk>[0-9]+)/$',  views.PersonDetailV2.as_view()),
# ]

urlpatterns = [
    # url(r'^v1/', include(v1)),
    # url(r'^v2/', include(v2)),
    url(r'^person/$', views.PersonListV1.as_view()),
    url(r'^person/(?P<pk>[0-9]+)/$',  views.PersonDetailV1.as_view()),
]
