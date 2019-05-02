from rest_framework import serializers
from .models import DataTable, DataField, DataContent


class DataFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataField
        fields = '__all__'


class DataTableSerializer(serializers.ModelSerializer):
    data_fields = DataFieldSerializer(many=True, read_only=True)

    class Meta:
        model = DataTable
        fields = '__all__'
