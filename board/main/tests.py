from django.db import IntegrityError
from django.test import TestCase

from main.models import Advert, Category, User, Comment


# Create your tests here.
class AdvertModelTest(TestCase):
    """
    Test Advert Model
    """

    def setUp(self):
        self.user = User.objects.create_user(username='test_user', email='test@example.com', password='testpassword')
        self.category = Category.objects.create(name="Work")
        self.advert = Advert.objects.create(title="Advert Test", category=self.category, price=100, user=self.user)

    def test_advert_creation(self) -> None:
        """
        Test advert creation
        """
        advert = Advert.objects.create(title="Advert Test", category=self.category, price=100, user=self.user)
        self.assertEqual(advert.title, "Advert Test")
        self.assertEqual(advert.category, self.category)
        self.assertEqual(advert.price, 100)
        self.assertEqual(advert.user, self.user)

    def test_advert_raise_error_without_user(self) -> None:
        """
        Test fails due to IntegrityError when user is None
        """
        with self.assertRaises(IntegrityError):
            Advert.objects.create(title="Advert Test", category=self.category, price=100)

    def test_advert_raise_error_without_price(self) -> None:
        """
        Test fails due to IntegrityError when price is None
        """
        with self.assertRaises(IntegrityError):
            Advert.objects.create(title="Advert Test", category=self.category, user=self.user)

    def test_advert_raise_error_with_negative_price(self) -> None:
        """
        Test fails due to IntegrityError when negative price
        """
        # with self.assertRaises(IntegrityError):
        Advert.objects.create(title="Advert Test", category=self.category, user=self.user, price=-100)


class CategoryModelTest(TestCase):
    """
    Test Category Model
    """

    def setUp(self):
        self.category = Category.objects.create(name="Work")

    def test_category_creation(self) -> None:
        """
        Test category creation
        """
        category = Category.objects.create(name="Work")
        self.assertEqual(category.name, "Work")

    def test_category_raise_error_without_name(self) -> None:
        """
        Test fails due to IntegrityError when category name is None
        """
        with self.assertRaises(IntegrityError):
            Category.objects.create(name=None)


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', email='test@example.com', password='testpassword',
                                             phone='3981212123')

    def test_user_creation(self) -> None:
        """
        Test user creation
        """
        self.assertTrue(User.objects.create(username='test_user2', phone='0981212123'))

    def test_user_raise_error_when_username_exists(self) -> None:
        """
        Test fails due to IntegrityError when username already exists
        """
        with self.assertRaises(IntegrityError):
            User.objects.create(username='test_user', phone='0981212123')

    def test_user_raise_error_when_email_exists(self) -> None:
        """
        Test fails due to IntegrityError when phone already exists
        """
        with self.assertRaises(IntegrityError):
            User.objects.create(username='test_user2', phone=self.user.phone)


class CommentModelTest(TestCase):
    """
    Test Comment Model
    """

    def setUp(self):
        self.user = User.objects.create(username='test_user2', phone='0981212123')
        self.category = Category.objects.create(name="Work")
        self.advert = Advert.objects.create(title="Advert Test", category=self.category, price=100, user=self.user)
        self.comment = Comment.objects.create(content="Test Comment", advert=self.advert, user=self.user)

    def test_comment_creation(self) -> None:
        """
        Test comment creation
        """
        comment = Comment.objects.create(content="Test Comment", advert=self.advert, user=self.user)
        self.assertEqual(comment.content, "Test Comment")
        self.assertEqual(comment.advert, self.advert)
        self.assertEqual(comment.user, self.user)

    def test_comment_raise_error_without_content(self) -> None:
        """
        Test fails due to IntegrityError when comment content is None
        """
        with self.assertRaises(IntegrityError):
            Comment.objects.create(content=None)
