from rest_framework import serializers


class NumSerializer(serializers.Serializer):
    num = serializers.IntegerField(min_value=2, max_value=10 ** 14)
