from django.test import TestCase, Client
from rest_framework.test import APITestCase
from rest_framework import status
from django.core.urlresolvers import reverse
from blog.models import Post
from blog.views import index

# Create your tests here.


# This section will be for basic tests
class BasePostTests(TestCase):

    @classmethod
    def get_posts_count(cls):
        return len(Post.objects.filter(published=True))

    def setUp(self):
        self.client = Client()
        self.url = "/blog/create/"
        self.title = "test_create_post"
        self.body = "test_create_post body"
        self.fields = {
            "title": self.title,
            "body": self.body
            }

        # Get the number of published post
        self.num_of_pub_post = BasePostTests.get_posts_count()

    def tearDown(self):
        self.client.logout()

    # Create post with empty title or body will be fail
    def test_create_empty_post(self):
        print "\nTry to create post with empty title or body \n" \
            "Expect form failure since default the fields are required\n"
        response = self.client.post(self.url, {
            "title": "",
            "body": ""
            })
        self.assertFormError(response, "form", "title",
                             "This field is required.")
        self.assertFormError(response, "form", "body",
                             "This field is required.")

        # Create success post with redirect to the index
    def test_create_post(self):
        print "\nTry to create a valid post\n" \
            "Expect to get a success redirect to index\n"
        response = self.client.post(self.url, {
            "title": "test_title_1",
            "body": "tess_title_1 body",
            })
        self.assertRedirects(response, reverse(index))


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
