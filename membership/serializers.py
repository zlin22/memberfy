from rest_framework import serializers
from .models import MembershipConfig, Membership, AuxMembership, Snippet
from django.contrib.auth.models import User


class MembershipConfigSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MembershipConfig
        fields = ['org_id', 'price_plan_id', 'days_valid', 'price', 'title', 'description',
                  'banner_message', 'is_displayed_on_site', 'is_subscription', 'display_order']


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
        view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
        many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']
