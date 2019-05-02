from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.core import serializers
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import DataTableSerializer, DataFieldSerializer, DataContentSerializer, DataRowSerializer
from .models import DataTable, DataField, DataContent, DataRow
import time

#########
# POST
# Custom Authentication Token to return user as well as token key
#########


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


#########
# GET
# View Authenticated User Information
#########
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


#########
# GET, POST
# View Data rows, Create new rows with data content
#########
class DataRowView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, tpk, format=None):
        # pylint: disable=maybe-no-member
        data_contents = DataRow.objects.filter(
            table_id=tpk, user_id=request.user.id)
        serializer = DataRowSerializer(data_contents, many=True)
        return Response(serializer.data)

    def post(self, request, tpk, format=None):
        data = request.data
        serializer = DataRowSerializer(
            data={'table_id': tpk, 'user_id': request.user.id})
        if serializer.is_valid():
            serializer.save()
            for d in data:
                d['table_id'] = int(serializer.data['table_id'])
                d['user_id'] = request.user.id
                d['row_id'] = int(serializer.data['id'])

            data_serializer = DataContentSerializer(data=data, many=True)
            if data_serializer.is_valid():
                data_serializer.save()
                return Response(data_serializer.data, status=status.HTTP_201_CREATED)
            return Response(data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#########
# GET, DELETE
# View and delete Data rows
#########
class DataRowDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, tpk, rpk, user_id):
        try:
            # pylint: disable=maybe-no-member
            return DataRow.objects.get(id=rpk, table_id=tpk, user_id=user_id)
        except DataRow.DoesNotExist:
            raise Http404

    def get(self, request, tpk, rpk, format=None):
        data_row = self.get_object(tpk, rpk, request.user.id)
        serializer = DataContentSerializer(data_row)
        return Response(serializer.data)

    def delete(self, request, tpk, rpk, format=None):
        data_row = self.get_object(tpk, rpk, request.user.id)
        data_row.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#########
# GET, POST
# view and Create Data row content using the DataContent model but targeting
# a single data row
#########
class DataRowContentView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, tpk, rpk, format=None):
        # pylint: disable=maybe-no-member
        data_contents = DataContent.objects.filter(
            table_id=tpk, row_id=rpk, user_id=request.user.id)
        serializer = DataContentSerializer(data_contents, many=True)
        return Response(serializer.data)

    def post(self, request, tpk, rpk, format=None):
        data = request.data
        data['table_id'] = tpk
        data['row_id'] = rpk
        data['user_id'] = request.user.id
        serializer = DataContentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#########
# GET, UPDATE, DELETE
# View, update and delete Data row content using the DataContent model
# targeting a single row and a single data content
#########
class DataRowContentDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, tpk, rpk, cpk, user_id):
        try:
            # pylint: disable=maybe-no-member
            return DataContent.objects.get(id=cpk, row_id=rpk, table_id=tpk, user_id=user_id)
        except DataContent.DoesNotExist:
            raise Http404

    def get(self, request, tpk, rpk, cpk, format=None):
        data_content = self.get_object(tpk, rpk, cpk, request.user.id)
        serializer = DataContentSerializer(data_content)
        return Response(serializer.data)

    def put(self, request, tpk, rpk, cpk, format=None):
        data_content = self.get_object(tpk, rpk, cpk, request.user.id)
        data = request.data
        data['table_id'] = tpk
        data['row_id'] = rpk
        data['user_id'] = request.user.id
        serializer = DataContentSerializer(data_content, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, tpk, rpk, cpk, format=None):
        data_content = self.get_object(tpk, rpk, cpk, request.user.id)
        data_content.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#########
# GET, POST
# view and Create Data field content using the DataContent model but targeting
# a single data field
#########
class DataFieldContentView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, tpk, fpk, format=None):
        # pylint: disable=maybe-no-member
        data_contents = DataContent.objects.filter(
            table_id=tpk, field_id=fpk, user_id=request.user.id)
        serializer = DataContentSerializer(data_contents, many=True)
        return Response(serializer.data)

    def post(self, request, tpk, fpk, format=None):
        data = request.data
        data['table_id'] = tpk
        data['field_id'] = fpk
        data['user_id'] = request.user.id
        serializer = DataContentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#########
# GET, UPDATE, DELETE
# View, update and delete Data field content using the DataContent model
# targeting a single field and a single data content
#########
class DataFieldContentDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, tpk, fpk, cpk, user_id):
        try:
            # pylint: disable=maybe-no-member
            return DataContent.objects.get(id=cpk, field_id=fpk, table_id=tpk, user_id=user_id)
        except DataContent.DoesNotExist:
            raise Http404

    def get(self, request, tpk, fpk, cpk, format=None):
        data_content = self.get_object(tpk, fpk, cpk, request.user.id)
        serializer = DataContentSerializer(data_content)
        return Response(serializer.data)

    def put(self, request, tpk, fpk, cpk, format=None):
        data_content = self.get_object(tpk, fpk, cpk, request.user.id)
        data = request.data
        data['table_id'] = tpk
        data['field_id'] = fpk
        data['user_id'] = request.user.id
        serializer = DataContentSerializer(data_content, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, tpk, fpk, cpk, format=None):
        data_content = self.get_object(tpk, fpk, cpk, request.user.id)
        data_content.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#########
# GET, POST
# View and add new Data fields
#########
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


#########
# GET, UPDATE, DELETE
# View, update and delete a single Data field
#########
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


#########
# GET, POST
# View and add new Data tables
#########
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


#########
# GET, UPDATE, DELETE
# View, update and delete a single Data table
#########
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
