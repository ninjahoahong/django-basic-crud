from django.test import TestCase
from django.http import HttpRequest, HttpResponse
from django.template.loader import render_to_string
from django.core.urlresolvers import resolve
from blog.views import index
from blog.models import Post
from blog.forms import PostForm
from django.core.exceptions import ValidationError

# Create your tests here.


# This section will be for basic tests using selenium and firefox browser
class PostModelTest(TestCase):
    def test_default_body_and_title(self):
        print "\n test model Post"
        post = Post()
        self.assertEqual(post.body, "")
        self.assertEqual(post.title, "")


class PostFormTest(TestCase):
    def test_form_validation_for_blank_items(self):
        print "\n test Form \n"
        form = PostForm(data={"title": "", "body": ""})
        self.assertFalse(form.is_valid())


class IndexPageTest(TestCase):
    def test_root_url_to_index(self):
        found_url = resolve("/")
        self.assertEqual(found_url.func, index)

    def test_render_correct_index_page(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, 'index.html')


class BasicBlogActivityTest(TestCase):
    fixtures = ["fixtures.json"]

    def test_create_post(self):
        response = self.client.get("/blog/create/")
        self.assertTemplateUsed(response, "post/post_create.html")

    # Create post with empty title or body will be fail
    def test_create_empty_post(self):
        print "\nTry to create post with empty title or body \n" \
            "Expect form failure since default the fields are required\n"
        response = self.client.post("/blog/create/", {
            "title": "",
            "body": "",
            })
        self.assertFormError(response, "form", "title",
                             "This field is required.")
        self.assertFormError(response, "form", "body",
                             "This field is required.")

    # Create success post with redirect to the index
    def test_create_post(self):
        print "\nTry to create a valid post\n" \
            "Expect to get a success redirect to index\n"
        response = self.client.post("/blog/create/", {
            "title": "test_title_1",
            "body": "tess_title_1 body",
            })
        self.assertRedirects(response, "/")

    def test_delete_post(self):
        print "\n Try to delete post 7 \n" \
            "Expect error when access to the post"
        self.client.post("/blog/delete/7")
        response = self.client.get("/blog/7")
        self.assertEqual(response.status_code, 404)

    def test_update_post(self):
        print "\n Try to update post \n" \
            "Expect to get new body and title"
        self.client.post("/blog/edit/8", {
            "title": "updated title",
            "body": "updated body",
            })
        response = Post.objects.get(id=8)
        self.assertEqual(response.title, u"updated title")
        self.assertEqual(response.body, u"updated body")


class IndividualPostTest(TestCase):
    fixtures = ["fixtures.json"]

    def test_correct_template_use_for_individual_post(self):
        response = self.client.get("/blog/7")
        self.assertTemplateUsed(response, "post/post.html")
