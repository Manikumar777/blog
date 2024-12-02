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
    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(),'/post/1')
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

    def test_post_create_view(self):
        response = self.client.post(reverse('post_new'),{'title':'Mani','body':'new','author':self.user.id,})
        self.assertEqual(response.status_code,302)
        self.assertEqual(Post.objects.last().title,'Mani')
        self.assertEqual(Post.objects.last().body, 'new')

# self.client.post:
#
# This simulates a POST request to the URL associated with the post_new view.
# The data provided in the POST request includes:
# title: 'Mani'
# body: 'new'
# author: self.user.id (the ID of a user stored in self.user).
# reverse('post_new'):
#
# It resolves the URL for the view named 'post_new' (typically specified in your urls.py file).
# It ensures the test is not dependent on hardcoding URLs.
# self.assertEqual(response.status_code, 302):
#
# After the POST request, this line checks if the response status code is 302.
# A 302 status code indicates a successful redirection (common after creating an object in Django, typically redirecting to a detail or list view).
# Post.objects.last():
#
# This retrieves the most recently created Post object from the database.
# self.assertEqual(Post.objects.last().title, 'Mani'):
#
# Verifies that the title of the most recently created Post object matches 'Mani'.
# self.assertEqual(Post.objects.last().body, 'new'):
#
# Ensures the body of the most recently created Post object matches 'new'.
    def test_update_view(self):
        response = self.client.post(reverse('post_edit',args='1'),{'title':'Updated title','body':'updated text'})
        self.assertEqual(response.status_code,302)
    def test_delete_view(self):
        response = self.client.post(reverse('post_delete',args='1'))
        self.assertEqual(response.status_code,302)

