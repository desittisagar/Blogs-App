from django.test import Client, TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post
# Create your tests here.

class BlogTest(TestCase):

	def setUp(self):
		self.user = get_user_model().objects.create_user(
			username = 'testuser',
			email = 'test@gmail.com',
			password = 'qwerty'
			)

		self.post = Post.objects.create(
			title = 'A title',
			author = self.user,
			body = 'this is the body'
			)

	def test_string_representation(self):
		post = Post(title = 'A sample title')
		self.assertEqual(str(post), post.title)

	def test_get_absolute_url(self):
		self.assertEqual(self.post.get_absolute_url(), '/post/1/')	

	def test_post_content(self):
		self.assertEqual(f'{self.post.title}', 'A title')
		self.assertEqual(f'{self.post.author}', 'testuser')
		self.assertEqual(f'{self.post.body}', 'this is the body')

	def test_list_view(self):
		response = self.client.get(reverse('home'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'this is the body')
		self.assertTemplateUsed(response, 'home.html')


	def test_detail_view(self):
		response = self.client.get('/post/1/')
		no_response = self.client.get('/post/1000/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(no_response.status_code, 404)
		self.assertContains(response, 'A title')
		self.assertTemplateUsed(response, 'detail.html')

	def test_create_view(self):
		response = self.client.post(reverse('post_new'), {
			'title': 'New title',
			'author':self.user,
			'body': 'new body'
			})	
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'New title')
		self.assertContains(response, 'new body')

	def test_update_view(self):
		response = self.client.post(reverse('post_update', args = '1'), {
			'title': 'updated title',
			'body': 'updated body'
			})	
		self.assertEqual(response.status_code, 302)

	def test_delete_view(self):
		response = self.client.get(reverse('post_delete', args = '1'))
		self.assertEqual(response.status_code, 200)	
