from django.db import models
from django.contrib.auth.models import User


# Table containing the data tables and the tabel description
class DataTable(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Table containing the data fields and field description
class DataField(models.Model):
    TEXT = 0
    NUMBER = 1
    DATE = 2
    ENUM = 3
    FIELD_TYPE_CHOICES = (
        (TEXT, 'Text'),
        (NUMBER, 'Number'),
        (DATE, 'Date'),
        (ENUM, 'Enum'),
    )
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    table_id = models.ForeignKey(
        DataTable, related_name='data_fields', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    field_type = models.SmallIntegerField(
        choices=FIELD_TYPE_CHOICES, default=TEXT)
    # should contain comma separated values when the field type is an enum
    field_options = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('table_id', 'name')


# Table containing the data rows to keep track of which rows data eneterd is for
class DataRow(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    table_id = models.ForeignKey(
        DataTable, related_name='data_rows', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Table containing the data content in text field
class DataContent(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    table_id = models.ForeignKey(
        DataTable, related_name='data_contents', on_delete=models.CASCADE)
    row_id = models.ForeignKey(
        DataRow, related_name='row_contents', on_delete=models.CASCADE)
    field_id = models.ForeignKey(
        DataField, related_name='field_contents', on_delete=models.CASCADE)
    content = models.TextField()
