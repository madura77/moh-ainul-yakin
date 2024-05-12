from rest_framework import serializers
from .models import Teknik, Computer, Elit


class TeknikSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teknik
        fields = ["id", "title", "content", "published_date"]

class ComputerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Computer
        fields = ["id", "title", "content", "published_date"]

class ElitSerializers(serializers.ModelSerializer):
    class Meta:
        model = Elit
        fields = ["id", "title", "content", "published_date"]
