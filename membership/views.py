from .models import MembershipConfig, Membership, AuxMembership
from .serializers import MembershipConfigSerializer, MembershipSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class MembershipConfigList(APIView):
    """
    List all membership configs or create new membership config
    """

    def get(self, request, format=None):
        membership_configs = MembershipConfig.objects.all()
        serializer = MembershipConfigSerializer(membership_configs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MembershipConfigSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MembershipConfigDetail(APIView):
    """
    retrieve, update or delete a membership config instance
    """

    def get_object(self, pk):
        try:
            return MembershipConfig.objects.get(pk=pk)
        except MembershipConfig.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        membership_config = self.get_object(pk)
        serializer = MembershipConfigSerializer(membership_config)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        membership_config = self.get_object(pk)
        serializer = MembershipConfigSerializer(
            membership_config, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        membership_config = self.get_object(pk)
        membership_config.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MembershipList(APIView):
    """
    List all memberships or create new memberships
    """

    def get(self, request, format=None):
        memberships = Membership.objects.all()
        serializer = MembershipSerializer(memberships, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MembershipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MembershipDetail(APIView):
    """
    retrieve, update or delete a membership instance
    """

    def get_object(self, pk):
        try:
            return Membership.objects.get(pk=pk)
        except Membership.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        membership = self.get_object(pk)
        serializer = MembershipSerializer(membership)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        membership = self.get_object(pk)
        serializer = MembershipSerializer(
            membership, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        membership = self.get_object(pk)
        membership.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MembershipIsActive(APIView):
    """
    retrieve status of "is_active" of a membership instance
    """

    def get_object(self, pk):
        try:
            return Membership.objects.get(pk=pk)
        except Membership.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        membership = self.get_object(pk)

        serializer = MembershipSerializer(membership)
        return Response(serializer.data)
