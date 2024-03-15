from django.core.management.base import BaseCommand
from data_rollup.models import Payment, PayType, Provider, EmployeeType

from data_rollup.database import get_session

class Command(BaseCommand):
    help = 'Clears all data in the database'

    def handle(self, *args, **options):
        session = get_session()

        session.query(Payment).delete()
        session.query(PayType).delete()
        session.query(Provider).delete()
        session.query(EmployeeType).delete()

        session.commit()

        self.stdout.write(self.style.SUCCESS('Data cleared successfully'))
