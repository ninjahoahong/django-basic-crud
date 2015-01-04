from rest_framework.test import APITestCase
from rest_framework import status
from django.core.urlresolvers import reverse

# Create your tests here.


# This section will be the api test
class APIPostTests(APITestCase):
    fixtures = ["fixtures.json"]

    def test_url_available(self):
        print "\n Try if the links are available\n" \
            "Expect to get the success code\n"
        index_url = reverse("index")
        response = self.client.get(index_url)
        self.assertTrue(status.is_success(response.status_code))
        print "got index\n"

        post_list_url = reverse("post-list")
        response = self.client.get(post_list_url)
        self.assertTrue(status.is_success(response.status_code))
        print "got api blog list\n"

    def test_create_post(self):
        print "\nTry to create a valid post from api\n" \
            "Expect to get the right title and body\n"
        url = reverse("post-list")
        data = {"body": u"test_api_1 body", "title": u"test_api_1"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], data["title"])
        self.assertEqual(response.data["body"], data["body"])

    def test_delete_post(self):
        print"\n Try to delete post 7 with the data: \n"
        print self.client.get("/api/blog/7")
        print"\n Expect to get the content not found after the delete call\n"
        response = self.client.delete("/api/blog/7")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
