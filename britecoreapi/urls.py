from django.conf.urls import url, include
from . import views

urlpatterns = [
    # /api/data-tables: Access data tables
    url(r'^data-tables/?$', views.DataTableView.as_view(),
        name='data-table'),
    # /api/data-table/<pk>: Access a single data table
    url(r'^data-table/(?P<pk>\d+)/?$',
        views.DataTableDetailView.as_view(), name='data-table-detail'),

    # /api/data-table/<tpk>/fields: Access data table fields
    url(r'^data-table/(?P<tpk>\d+)/fields/?$',
        views.DataFieldView.as_view(), name='data-field'),
    # /api/data-table/<tpk>/field/<fpk>: Access a single data table field
    url(r'^data-table/(?P<tpk>\d+)/field/(?P<fpk>\d+)/?$',
        views.DataFieldDetailView.as_view(), name='data-field-detail'),

    # /api/data-table/<tpk>/rows: Access data table rows
    url(r'^data-table/(?P<tpk>\d+)/rows/?$',
        views.DataRowView.as_view(), name='data-row'),
    # /api/data-table/<tpk>/row/<rpk>: Access a single data table row
    url(r'^data-table/(?P<tpk>\d+)/row/(?P<rpk>\d+)/?$',
        views.DataRowDetailView.as_view(), name='data-row-detail'),

    # /api/data-table/<tpk>/row/<rpk>/contents: Access data table row contents
    url(r'^data-table/(?P<tpk>\d+)/row/(?P<rpk>\d+)/contents/?$',
        views.DataRowContentView.as_view(), name='data-row-content'),
    # /api/data-table/<tpk>/row/<fpk>/content/<cpk>: Access a single data table row content
    url(r'^data-table/(?P<tpk>\d+)/row/(?P<rpk>\d+)/content/(?P<cpk>\d+)/?$',
        views.DataRowContentDetailView.as_view(), name='data-row-content-detail'),

    # /api/data-table/<tpk>/field/<fpk>/contents: Access data table field contents
    url(r'^data-table/(?P<tpk>\d+)/field/(?P<fpk>\d+)/contents/?$',
        views.DataFieldContentView.as_view(), name='data-field-content'),
    # /api/data-table/<tpk>/field/<fpk>/content/<cpk>: Access a single data table field content
    url(r'^data-table/(?P<tpk>\d+)/field/(?P<fpk>\d+)/content/(?P<cpk>\d+)/?$',
        views.DataFieldContentDetailView.as_view(), name='data-field-content-detail'),

    # /api/data-row/count: Count data rows
    url(r'^data-rows/count/?$',
        views.DataRowCountView.as_view(), name='data-rows-count'),

    # /api/user: Get currently logged in user
    url(r'^user/?', views.UserView.as_view(), name='user'),
    url(r'^token-auth/?', views.CustomAuthToken.as_view(),
        name='api-token-auth'),  # /api/token-auth: Authenticate user and generate jwt token
]
