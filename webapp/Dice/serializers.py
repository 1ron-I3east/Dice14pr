# from rest_framework import serializers
# class HTMLtextSerializers(serializers.Serializer):
    # text = serializers.ListField(child=serializers.CharField())
    # name = serializers.ListField(child=serializers.CharField())
    # Hero = serializers.ListField(child=serializers.CharField())
    # Race = serializers.ListField(child=serializers.CharField())
    # Strength = serializers.ListField(child=serializers.CharField())
    # Constitution= serializers.ListField(child=serializers.CharField())
    # Dexterity = serializers.ListField(child=serializers.CharField())
    # Intelligence= serializers.ListField(child=serializers.CharField())
    # Wisdom = serializers.ListField(child=serializers.CharField())
    # Charisma = serializers.ListField(child=serializers.CharField())
from rest_framework import serializers


class HTMLtextSerializers(serializers.Serializer):
    text = serializers.DictField(child=serializers.CharField())