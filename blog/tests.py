from django.test import TestCase
from .models import Article

class ArticleModelTest(TestCase):
    def setUp(self):
        self.article = Article.objects.create(
            title="Test Article",
            content="Test content for article.",
        )

    def test_article_str(self):
        self.assertEqual(str(self.article), "Test Article")

    def test_home_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Article")
