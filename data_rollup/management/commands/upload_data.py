from django.core.management.base import BaseCommand, CommandParser

from data_rollup.models import PayType, Provider, EmployeeType, Payment
from data_rollup.database import get_session
from data_rollup.serializers import PaymentSerializer, ProviderSerializer, \
    PayTypeSerializer, EmployeeTypeSerializer

import json

class Command(BaseCommand):
    help = 'Uploads json data to the database'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('json_file', type=str, help='The json file to upload')

    def handle(self, *args, **options):
        json_file = options['json_file']
        session = get_session()

        with open(json_file, 'r') as f:
            data = json.load(f)
            categories = data['categories']
            paytypes = categories['paytype_id']
            providers = categories['provider_id']
            employee_types = categories['employee_type_id']
            payments = data['values']

            new_paytypes = []
            for paytype_id, name in paytypes.items():
                new_paytypes.append(PayType(paytype_id=paytype_id, paytype_name=name))
            session.add_all(new_paytypes)

            new_providers = []
            for provider_id, name in providers.items():
                new_providers.append(Provider(provider_id=provider_id, provider_name=name))
            session.add_all(new_providers)

            new_employee_types = []
            for employee_type_id, name in employee_types.items():
                new_employee_types.append(EmployeeType(employee_type_id=employee_type_id, employee_type_name=name))
            session.add_all(new_employee_types)

            new_payments = [Payment(**obj) for obj in payments]
            session.add_all(new_payments)

            session.commit()

        self.stdout.write(self.style.SUCCESS('Data uploaded successfully'))
