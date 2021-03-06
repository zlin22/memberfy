from .models import MembershipConfig, Membership
from .serializers import MembershipConfigSerializer, MembershipSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action


class MembershipConfigViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `is_active` action.
    """
    serializer_class = MembershipConfigSerializer

    def get_queryset(self):
        """
        This view should return a list of all the memberships configs for
        the org as determined by the org_id portion of the URL.
        """
        org_id = self.kwargs['org_id']
        return MembershipConfig.objects.filter(org_id=org_id)

    # if table has an owner column, can update owner with user who created item
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class MembershipViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    serializer_class = MembershipSerializer

    def get_queryset(self):
        """
        This view should return a list of all the memberships configs for
        the org as determined by the org_id portion of the URL.
        """
        org_id = self.kwargs['org_id']
        return Membership.objects.filter(membership_config__org_id=org_id)

    @action(detail=True)
    def is_active(self, request, *args, **kwargs):
        membership = self.get_object()
        return Response(membership.is_active)
