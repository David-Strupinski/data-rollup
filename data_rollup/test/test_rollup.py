from django.test import TestCase

from data_rollup.utils import roll_values

class RollupTest(TestCase):
    def test_full_rollup(self):
        data = [
            {
                "paytype_id": 1,
                "amount": 100,
                "date": "2021-01-01",
                "provider_id": "1",
                "employee_type_id": 1
            },
            {
                "paytype_id": 1,
                "amount": 200,
                "date": "2021-01-01",
                "provider_id": "1",
                "employee_type_id": 1
            },
            {
                "paytype_id": 1,
                "amount": 300,
                "date": "2021-01-01",
                "provider_id": "1",
                "employee_type_id": 1
            },
            {
                "paytype_id": 1,
                "amount": 400,
                "date": "2021-01-01",
                "provider_id": "1",
                "employee_type_id": 1
            },
            {
                "paytype_id": 1,
                "amount": 500,
                "date": "2021-01-01",
                "provider_id": "1",
                "employee_type_id": 1
            }
        ]
        result = roll_values(data)
        self.assertEqual(result[0]['amount'], 1500)
    
    def test_rollup_separate_groups(self):
        data = [
            {
                "paytype_id": 1,
                "amount": 100,
                "date": "2021-01-01",
                "provider_id": "1",
                "employee_type_id": 1
            },
            {
                "paytype_id": 2,
                "amount": 200,
                "date": "2021-01-01",
                "provider_id": "1",
                "employee_type_id": 1
            },
            {
                "paytype_id": 1,
                "amount": 300,
                "date": "2021-02-01",
                "provider_id": "1",
                "employee_type_id": 1
            },
            {
                "paytype_id": 2,
                "amount": 400,
                "date": "2021-01-02",
                "provider_id": "1",
                "employee_type_id": 1
            },
            {
                "paytype_id": 3,
                "amount": 500,
                "date": "2021-01-01",
                "provider_id": "1",
                "employee_type_id": 1
            }
        ]
        result = roll_values(data)
        self.assertEqual(len(result), 5)

