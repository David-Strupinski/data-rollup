from rest_framework import viewsets
from rest_framework.response import Response

from data_rollup.utils import roll_values
from data_rollup.database import get_session
from data_rollup.models import Payment, Provider, PayType, EmployeeType
from data_rollup.serializers import PaymentSerializer, ProviderSerializer, \
    PayTypeSerializer, EmployeeTypeSerializer


class RollupViewSet(viewsets.ViewSet):
    session = get_session()

    def list(self, request):
        payments = self.session.query(Payment).all()
        serializer = PaymentSerializer(payments, many=True)
        rolled_values = roll_values(serializer.data)
        return Response(rolled_values)

class PaymentsViewSet(viewsets.ViewSet):
    session = get_session()

    def list(self, request):
        payments = self.session.query(Payment).all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        data = request.data
        serializer = PaymentSerializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        
        new_payments = [Payment(**obj) for obj in serializer.data]

        self.session.add_all(new_payments)
        self.session.commit()

        return Response(status=201)
    
    def destroy(self, request, pk=None):
        self.session.query(Payment).filter(Payment.payment_id == pk).delete()
        self.session.commit()
        return Response(status=204)

class ProvidersViewSet(viewsets.ViewSet):
    session = get_session()

    def list(self, request):
        providers = self.session.query(Provider).all()
        serializer = ProviderSerializer(providers, many=True)
        return Response(serializer.data)

    def create(self, request):
        data = request.data

        new_providers = [Provider(
            provider_id=id,
            provider_name=name
        ) for id, name in data.items()]

        self.session.add_all(new_providers)
        self.session.commit()

        return Response(status=201)
    
    def destroy(self, request, pk=None): 
        self.session.query(Provider).filter(Provider.provider_id == pk).delete()
        self.session.commit()
        return Response(status=204)

class PayTypesViewSet(viewsets.ViewSet):
    session = get_session()

    def list(self, request):
        paytypes = self.session.query(PayType).all()
        serializer = PayTypeSerializer(paytypes, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        data = request.data

        new_pay_types = [PayType(
            paytype_id=id,
            paytype_name=name
        ) for id, name in data.items()]

        self.session.add_all(new_pay_types)
        self.session.commit()

        return Response(status=201)
    
    def destroy(self, request, pk=None):
        self.session.query(PayType).filter(PayType.paytype_id == pk).delete()
        self.session.commit()
        return Response(status=204)

class EmployeeTypesViewSet(viewsets.ViewSet):
    session = get_session()

    def list(self, request):
        employeetypes = self.session.query(EmployeeType).all()
        serializer = EmployeeTypeSerializer(employeetypes, many=True)
        return Response(serializer.data)

    def create(self, request):
        data = request.data

        new_employee_types = [EmployeeType(
            employee_type_id=id,
            employee_type_name=name
        ) for id, name in data.items()]

        self.session.add_all(new_employee_types)
        self.session.commit()

        return Response(status=201)

    def destroy(self, request, pk=None):
        self.session.query(EmployeeType).filter(EmployeeType.employee_type_id == pk).delete()
        self.session.commit()
        return Response(status=204)
