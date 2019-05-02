from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^data-tables/?$', views.DataTableView.as_view(), name='data-table'),
    url(r'^data-table/(?P<pk>\d+)/?$',
        views.DataTableDetailView.as_view(), name='data-table-detail'),

    url(r'^data-table/(?P<tpk>\d+)/fields/?$',
        views.DataFieldView.as_view(), name='data-field'),
    url(r'^data-table/(?P<tpk>\d+)/field/(?P<fpk>\d+)/?$',
        views.DataFieldDetailView.as_view(), name='data-field-detail'),

    url(r'^user/?', views.UserView.as_view(), name='user'),
    url(r'^token-auth/?', views.CustomAuthToken.as_view(), name='api-token-auth'),
]
