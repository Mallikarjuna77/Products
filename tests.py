from django.test import TestCase
from .models import Item

class Basictests(TestCase):
    def setUp(self):
        Item.objects.create(Name='Samsung Galaxy Mobile',
                           Description='Samsung Galaxy Mobile',
                           Cost_per_Item=45000.00,
                           Stock_quantity=2.00,
                           Volume=90000.00)
        def test_get_method(self):
            url="http://127.0.0.1:8000/students/"
            response=self.client.get(url)
            self.assertEqual(response.status_code,200)
            qs = Item.objects.filter(Name='Samsung Galaxy Mobile')
            self.assertEqual(qs.count(), 0)
