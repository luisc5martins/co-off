from rest_framework.serializers import ModelSerializer

from core.models import Doce


class DoceSerializer(ModelSerializer):
    class Meta:
        model = Doce
        fields = "__all__"