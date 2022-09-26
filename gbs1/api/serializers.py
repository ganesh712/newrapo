from rest_framework import serializers
class StudentSerilalizer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    roll_no =serializers.IntegerField()
    city = serializers.CharField(max_length=100)