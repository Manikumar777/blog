from django.test import TestCase
from django.contrib.auth import get_user_model
# Instead of referring to User directly, you should reference the user model using django.contrib.auth.get_user_model() . This method will return the currently active user model – the custom user model if one is specified, or User otherwise.
from django.urls import reverse
from .models import Post
# Create your tests here.

# A manager is a class attribute on a Django model that acts as an interface to interact with the database.
# It provides methods to perform database queries, like retrieving, filtering, and creating objects.
# By default, Django adds a manager named objects to every model.
class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='mani',
            email='mani@gmail.com',
            password='mani'
        )
        self.post = Post.objects.create(
            title = 'Eat that frog',
            body = 'Good book',
            author= self.user,
        )
    def test_string_representation(self):
        post = Post(title = "Atomic Habits")
        self.assertEqual(str(post),post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}','Eat that frog')
        self.assertEqual(f'{self.post.author}','mani')
        self.assertEqual(f'{self.post.body}','Good book')

    def test_post_list_view(self):
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'Good book')
        self.assertTemplateUsed(response,'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1')
        no_response = self.client.get('/post/10000/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response,'Good book')
        self.assertTemplateUsed(response,'post_detail.html')

