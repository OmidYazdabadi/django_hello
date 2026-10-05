from django.test import TestCase
from django.urls import reverse
from .models import Member


class MemberViewsTests(TestCase):
	def test_member_list_page_loads(self):
		response = self.client.get(reverse('member-list'))

		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'members/member_list.html')

	def test_member_create_page_loads(self):
		response = self.client.get(reverse('member-create'))

		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'members/member_form.html')

	def test_valid_member_form_saves_and_redirects(self):
		response = self.client.post(reverse('member-create'), {
			'first_name': 'Ada',
			'last_name': 'Lovelace',
			'phone': '123456789',
		})

		self.assertRedirects(response, reverse('member-success'))
		self.assertEqual(Member.objects.count(), 1)

	def test_invalid_member_form_keeps_errors(self):
		response = self.client.post(reverse('member-create'), {
			'first_name': 'Ada',
		})

		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'members/member_form.html')
		self.assertTrue(response.context['form'].errors)
		self.assertEqual(Member.objects.count(), 0)
