from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.core import serializers
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .serializers import DataTableSerializer, DataFieldSerializer

from .models import DataTable, DataField, DataContent


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        # pylint: disable=maybe-no-member
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user': {
                'id': user.pk,
                'email': user.email,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name
            }
        })


class UserView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response({
            'id': request.user.pk,
            'email': request.user.email,
            'username': request.user.username,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name
        })


class DataFieldView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, tpk, format=None):
        # pylint: disable=maybe-no-member
        data_fields = DataField.objects.filter(
            table_id=tpk, user_id=request.user.id)
        serializer = DataFieldSerializer(data_fields, many=True)
        return Response(serializer.data)

    def post(self, request, tpk, format=None):
        data = request.data
        data['table_id'] = tpk
        data['user_id'] = request.user.id
        serializer = DataFieldSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DataFieldDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, tpk, fpk, user_id):
        try:
            # pylint: disable=maybe-no-member
            return DataField.objects.get(id=fpk, table_id=tpk, user_id=user_id)
        except DataField.DoesNotExist:
            raise Http404

    def get(self, request, tpk, fpk, format=None):
        data_field = self.get_object(tpk, fpk, request.user.id)
        serializer = DataFieldSerializer(data_field)
        return Response(serializer.data)

    def put(self, request, tpk, fpk, format=None):
        data_field = self.get_object(tpk, fpk, request.user.id)
        data = request.data
        data['table_id'] = tpk
        data['user_id'] = request.user.id
        serializer = DataFieldSerializer(data_field, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, tpk, fpk, format=None):
        data_field = self.get_object(tpk, fpk, request.user.id)
        data_field.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DataTableView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        # pylint: disable=maybe-no-member
        data_tables = DataTable.objects.filter(user_id=request.user.id)
        serializer = DataTableSerializer(data_tables, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        data['user_id'] = request.user.id
        serializer = DataTableSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DataTableDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk, user_id):
        try:
            # pylint: disable=maybe-no-member
            return DataTable.objects.get(id=pk, user_id=user_id)
        except DataTable.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        data_table = self.get_object(pk, request.user.id)
        serializer = DataTableSerializer(data_table)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        data_table = self.get_object(pk, request.user.id)
        data = request.data
        data['user_id'] = request.user.id
        serializer = DataTableSerializer(data_table, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        data_table = self.get_object(pk, request.user.id)
        data_table.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
