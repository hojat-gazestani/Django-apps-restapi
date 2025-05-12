from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import BlogPost

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@email.com", password="secret"
        )

        cls.post = BlogPost.objects.create(
            title="A good title",
            body="Nice body content",
            author=cls.user,
        )

    def test_post_model(self):
        self.assertEqual(self.post.title, "A good title")
        self.assertEqual(self.post.body, "Nice body content")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post), "A good title")
        self.assertEqual(self.post.get_absolute_url(), "/blog/1/")

    def test_url_exists_at_correct_location_listview(self):
        response = self.client.get("/blog/")
        self.assertEqual(response.status_code, 200)

#    def test_url_exists_at_correct_location_detailview(self):
#        response = self.client.get("/blog/1/")
#        self.assertEqual(response.status_code, 200)

    def test_post_listview(self):
        response = self.client.get(reverse("blog"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nice body content")
        self.assertTemplateUsed(response, "blog.html")

#    def test_post_detail_view(self):
#        response = self.client.get(reverse("post_detail", kwargs={"pk": self.post.pk}))
#        no_response = self.client.get("/blog/100000/")
#        self.assertEqual(response.status_code, 200)
#        self.assertEqual(no_response.status_code, 404)
#        self.assertContains(response, "A good title")
#        self.assertTemplateUsed(response, "post_detail.html")

    def test_post_createview(self):
        response = self.client.post(
            reverse("post_new"),
            {
                "title": "New title",
                "body": "New text",
                "author": self.user.id,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(BlogPost.objects.last().title, "New title")
        self.assertEqual(BlogPost.objects.last().body, "New text")

    def test_post_updateview(self):
        response = self.client.post(
            reverse("post_edit", kwargs={"pk": self.post.pk}),
            {
                "title": "Update title",
                "body": "Update text",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.post.refresh_from_db()
        self.assertEqual(BlogPost.objects.last().title, "Update title")
        self.assertEqual(BlogPost.objects.last().body, "Update text")

    def test_post_deleteview(self):
        response = self.client.post(reverse("post_delete", kwargs={"pk":
        self.post.pk}))
        self.assertEqual(response.status_code, 302)






