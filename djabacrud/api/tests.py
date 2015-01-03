from rest_framework.test import APITestCase
from rest_framework import status
from django.core.urlresolvers import reverse

# Create your tests here.


# This section will be the api test
class APIPostTests(APITestCase):
    def test_create_post(self):
        print "\nTry to create a valid post from api\n" \
            "Expect to get the right title and body\n"
        url = reverse("post-list")
        data = {"body": u"test_api_1 body", "title": u"test_api_1"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], data["title"])
        self.assertEqual(response.data["body"], data["body"])
