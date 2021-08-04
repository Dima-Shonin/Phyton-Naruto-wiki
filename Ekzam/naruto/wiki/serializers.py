from rest_framework import serializers
from  . models import *


class ShinobiSerializer1(serializers.ModelSerializer):
    village = serializers.StringRelatedField()
    # battle = serializers.StringRelatedField()
    class Meta:
        model = Shinobi
        fields = ['name','village','battle','technics']