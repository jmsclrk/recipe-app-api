from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    # set up function - runs before each test
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@jamesclark.com',
            password='Testpass123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='testuser@jamesclark.com',
            password='Testpass123',
            name='Test User'
        )

    def test_users_listed(self):
        """Tests that users are listed on user page"""
        # use reverse to prevent having to change when url changes
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        # also checks for status 200 code
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_edit_page(self):
        """Test the user edit page loads correctly"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        # reverse creates: /admin/core/user/1
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_user_create_page(self):
        """Test the user create page loads correctly"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
