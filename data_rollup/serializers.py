from rest_framework import serializers


class PaymentSerializer(serializers.Serializer):
    paytype_id = serializers.IntegerField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    date = serializers.DateField()
    provider_id = serializers.CharField()
    employee_type_id = serializers.IntegerField()

class ProviderSerializer(serializers.Serializer):
    provider_id = serializers.CharField()
    provider_name = serializers.CharField()

class PayTypeSerializer(serializers.Serializer):
    paytype_id = serializers.IntegerField()
    paytype_name = serializers.CharField()

class EmployeeTypeSerializer(serializers.Serializer):
    employee_type_id = serializers.IntegerField()
    employee_type_name = serializers.CharField()
