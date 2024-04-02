from rest_framework.serializers import ModelSerializer

from core.models import Cafe


class CafeSerializer(ModelSerializer):
    class Meta:
        model = Cafe
        fields = "__all__"