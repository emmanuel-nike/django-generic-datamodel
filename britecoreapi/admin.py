from django.contrib import admin
from django.contrib.auth.models import User
from .models import DataTable, DataField, DataContent, DataRow

# admin.site.register(User)
admin.site.register(DataTable)
admin.site.register(DataField)
admin.site.register(DataContent)
admin.site.register(DataRow)
