from django.test import TestCase

# Create your tests here.
class DjangeTest(TestCase):
    def test(self):
		response = self.client.post('/test/')
