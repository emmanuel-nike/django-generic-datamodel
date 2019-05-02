from rest_framework import serializers
from .models import DataTable, DataField, DataContent, DataRow


class DataContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataContent
        fields = '__all__'


class DataRowSerializer(serializers.ModelSerializer):
    row_contents = DataContentSerializer(many=True, read_only=True)

    class Meta:
        model = DataRow
        fields = '__all__'


class DataFieldSerializer(serializers.ModelSerializer):
    field_contents = DataContentSerializer(many=True, read_only=True)

    class Meta:
        model = DataField
        fields = '__all__'


class DataTableSerializer(serializers.ModelSerializer):
    data_fields = DataFieldSerializer(many=True, read_only=True)

    class Meta:
        model = DataTable
        fields = '__all__'
