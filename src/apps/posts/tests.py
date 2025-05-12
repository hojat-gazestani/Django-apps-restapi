from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post

class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@email.com",
            password="secret",
        )

        cls.post = Post.objects.create(
            author=cls.user,
            title="Test Post",
            body="This is a test post content",
        )

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/posts/list/")
        self.assertEqual(response.status_code, 200)

    def test_postpage(self):
        response = self.client.get(reverse("posts"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts.html")
        self.assertContains(response, "Newspaper App")  

    def test_post_model(self):
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.body, "This is a test post content")
        self.assertEqual(str(self.post), "Test Post")
