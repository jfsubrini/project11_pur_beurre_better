"""All the tests for the food app of the pur_beurre project."""


# Django imports
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


# Imports from my app
from .models import NutritionGrade, Category, Food, MySelection


################################################################
#                      PUR BEURRE HOMEPAGE                     #
################################################################

class HomepageTestCase(TestCase):
    """Testing that the homepage will be returned with a HTTP 200
    and the home template.
    """

    def test_homepage(self):
        """Testing that all home named views returns HTTP 200 and the right template.
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'food/home.html')

    def test_homepage2(self):
        """Testing that typing '/' returns HTTP 200 and the right template.
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'food/home.html')

    def test_homepage3(self):
        """Testing that typing '/index/' returns HTTP 200 and the right template.
        """
        response = self.client.get('/index/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'food/home.html')

    def test_homepage4(self):
        """Testing that typing '/home/' returns HTTP 200 and the right template.
        """
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'food/home.html')


################################################################
#                       IMPRINT - CREDITS                      #
################################################################

class ImprintTestCase(TestCase):
    """Testing that typing '/imprint'
    returns HTTP 200 and the imprint template.
    """

    def test_imprint_page(self):
        """Testing that typing '/imprint/' returns HTTP 200 and the right template.
        """
        response = self.client.get(reverse('imprint'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'food/imprint.html')


################################################################
#                          MY ACCOUNT                          #
################################################################

class MyAccountTestCase(TestCase):
    """Testing the User Account page.
    """

    def setUp(self):
        """Data samples to run the tests.
        """
        self.username = 'jeanfrancois'
        self.email = 'jfsubrini@yahoo.com'
        self.password = 'monsupermotdepasse'
        self.user = User.objects.create_user(self.username, self.email, self.password)

    def test_account_logged_in(self):
        """Accessing the user account page while logged in
        that renders HTTP 200 and the right template.
        """
        # The user is logged in.
        self.client.login(username=self.username, password=self.password)
        # Testing the access while logged in.
        response = self.client.get(reverse('account'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'food/account/account.html')

    def test_account_logged_out(self):
        """Trying to access the user account page while logged out that renders
        HTTP 302, redirection to the user register page.
        """
        response = self.client.get(reverse('account'))
        self.assertRedirects(
            response, (reverse('register'))+'?redirection_vers='+(reverse('account')))


################################################################
#                       ACCOUNT CREATION                       #
################################################################

class RegisterTestCase(TestCase):
    """
    Testing the User Register page.
    """

    def setUp(self):
        """Data samples to run the tests.
        """
        self.username = 'jeanfrancois'
        self.email = 'jfsubrini@yahoo.com'
        self.password = 'monsupermotdepasse'
        # self.user = User.objects.create_user(self.username, self.email, self.password)

    def test_register_page(self):
        """Connexion to the Register page that must return HTTP 200 and the right template.
        """
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'food/account/register.html')

    def test_register_valid(self):
        """Post a valid form from the Register page that must return
        the account page (HTTP 302 url redirection).
        The user must be registered into the database.
        """
        response = self.client.post(reverse('register'), {
            'username': self.username,
            'email': self.email,
            'password': self.password
        })
        self.assertRedirects(response, '/account/')
        self.assertTrue(
            User.objects.filter(
                username=self.username, email=self.email).exists())

    def test_register_invalid(self):
        """Post an invalid form from the Sign In page that must return
        HTTP 200 and stay in the same page with the right template.
        The user mustn't be registred into the database.
        """
        response = self.client.post(reverse('register'), {
            'username': 'blabla',
            'email': 'blablaagain',
            'password': 'moreblabla'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'food/account/register.html')
        self.assertFalse(
            User.objects.filter(
                username=self.username, email=self.email, password=self.password).exists())


################################################################
#                            LOGIN                             #
################################################################

class SignInTestCase(TestCase):
    """
    Testing the Sign In page.
    """

    def setUp(self):
        """Data samples to run the tests.
        """
        self.username = 'jeanfrancois'
        self.email = 'jfsubrini@yahoo.com'
        self.password = 'monsupermotdepasse'
        self.user = User.objects.create_user(self.username, self.email, self.password)

    def test_signin_page(self):
        """Connexion to the Sign In page that must return HTTP 200 and the right template.
        """
        response = self.client.get(reverse('signin'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'food/account/signin.html')

    def test_signin_valid(self):
        """Post a valid form from the Sign In page that must return
        the account page (HTTP 302 url redirection).
        """
        response = self.client.post(reverse('signin'), {
            'username': self.username,
            'password': self.password
        })
        self.assertRedirects(response, '/account/')

    def test_signin_invalid(self):
        """Post an invalid form from the Sign In page that must return
        HTTP 200 and stay in the same page with the right template.
        """
        response = self.client.post(reverse('signin'), {
            'username': 'blabla',
            'password': 'moreblabla'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'food/account/signin.html')


################################################################
#                            LOGOUT                            #
################################################################

class SignOutTestCase(TestCase):
    """
    Testing the Sign Out process.
    """

    def setUp(self):
        """Data samples to run the tests.
        """
        self.username = 'jeanfrancois'
        self.email = 'jfsubrini@yahoo.com'
        self.password = 'monsupermotdepasse'
        self.user = User.objects.create_user(self.username, self.email, self.password)

    def test_signout(self):
        """The user is already logged in and wants to log out.
        """
        # The user is logged in.
        self.client.login(username=self.username, password=self.password)
        # Testing the log out with the return HTTP 200 and the display of the homepage template.
        response = self.client.get(reverse('signout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'food/home.html')


################################################################
#                          FOOD RESULTS                        #
################################################################

class FoodResultTestCase(TestCase):
    """
    Testing the Food Result page.
    """

    def setUp(self):
        """Data samples to run the tests.
        """
        self.username = 'jeanfrancois'
        self.email = 'jfsubrini@yahoo.com'
        self.password = 'monsupermotdepasse'
        self.user = User.objects.create_user(self.username, self.email, self.password)

        # Sample of origin (Nutella) and substitute (Gerblé) foods data in a category.
        category = Category.objects.create(name="Pâtes à tartiner")
        nutella = {
            'id': '312',
            'name': 'Nutella',
            'brand': 'Ferrero',
            'category': Category.objects.get(name=category),
            'nutrition_grade': NutritionGrade.e,
            'nutrition_score': 26,
            'url': 'https://fr.openfoodfacts.org/produit/3017620429484/nutella-ferrero',
            'image_food': 'https://blablanut',
            'image_nutrition': 'https://blablablanut',
        }
        nutella = Food.objects.create(**nutella)
        self.nutella = nutella
        gerble = {
            'id': '3178',
            'name': 'Pâte à tartiner - Gerblé - 220g',
            'brand': 'Gerblé, Glucoregul',
            'category': self.nutella.category,
            'nutrition_grade': NutritionGrade.a,
            'nutrition_score': -4,
            'url': 'https://fr.openfoodfacts.org/produit/3175681105393/pate-a-tartiner-gerble',
            'image_food': 'https://blabla',
            'image_nutrition': 'https://blablabla',
        }
        gerble = Food.objects.create(**gerble)
        self.gerble = gerble

    def test_foodresult_valid(self):
        """Accessing the foodresult page while the user query is valid.
        This must return HTTP 200 and the right template.
        """
        response = self.client.get(reverse('foodresult'), {'query': 'Nutella'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'food/foodresult.html')

    def test_foodresult_invalid_404(self):
        """Accessing the foodresult page while the user query is invalid.
        This must return HTTP 404 and the right template.
        """
        response = self.client.get(reverse('foodresult'), {'query': '????????????'})
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')

    def test_foodresult_save(self):
        """Saving a substitute food into MySelection table while the user
        is logged in and return HTTP 302."""
        # The user is logged in.
        self.client.login(username=self.username, password=self.password)
        # Testing the saving of the Gerblé food by the user.
        url = reverse('foodresult')
        data = {"substitute": self.gerble.id}
        response = self.client.post(url, data)
        # Redirect to the same Selection page.
        self.assertEqual(response.status_code, 302)
        # The substitute food must be saved into MySelection table for that user.
        self.assertTrue(MySelection.objects.all().exists())


################################################################
#                           FOOD PAGE                          #
################################################################

class FoodInfoTestCase(TestCase):
    """
    Testing the Food Info page.
    """

    def setUp(self):
        """Data sample to run the tests.
        """
        # Sample of a substitute (Gerblé) food data.
        category = Category.objects.create(name="Pâtes à tartiner")
        gerble = {
            'id': '3178',
            'name': 'Pâte à tartiner - Gerblé - 220g',
            'brand': 'Gerblé, Glucoregul',
            'category': Category.objects.get(name=category),
            'nutrition_grade': NutritionGrade.a,
            'nutrition_score': -4,
            'url': 'https://fr.openfoodfacts.org/produit/3175681105393/pate-a-tartiner-gerble',
            'image_food': 'https://blabla',
            'image_nutrition': 'https://blablabla',
        }
        gerble = Food.objects.create(**gerble)
        self.gerble = gerble

    def test_foodinfo_200(self):
        """Connexion to the FoodInfo page that must return HTTP 200
        if the pk exists (food id). Returns the right template.
        """
        pk = self.gerble.id
        response = self.client.get(reverse('foodinfo', args=(pk,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'food/foodinfo.html')

    def test_foodinfo_404(self):
        """Connexion to the FoodInfo page that must return HTTP 404
        if the pk doesn't exist (food id). Returns the 404 page.
        """
        pk = 0
        response = self.client.get(reverse('foodinfo', args=(pk,)))
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')


################################################################
#                       MY FOODS SELECTION                     #
################################################################

class SelectionTestCase(TestCase):
    """
    Testing the Selection page.
    """

    def setUp(self):
        """Data samples to run the tests.
        """
        self.username = 'jeanfrancois'
        self.email = 'jfsubrini@yahoo.com'
        self.password = 'monsupermotdepasse'
        self.user = User.objects.create_user(self.username, self.email, self.password)

        # Sample of a selection of one saved food (Gerblé).
        category = Category.objects.create(name="Pâte à tartiner")
        gerble = {
            'id': '3178',
            'name': 'Pâte à tartiner - Gerblé - 220g',
            'brand': 'Gerblé, Glucoregul',
            'category': Category.objects.get(name=category),
            'nutrition_grade': NutritionGrade.a,
            'nutrition_score': -4,
            'url': 'https://fr.openfoodfacts.org/produit/3175681105393/pate-a-tartiner-gerble',
            'image_food': 'https://blabla',
            'image_nutrition': 'https://blablabla',
        }
        gerble = Food.objects.create(**gerble)
        self.gerble = gerble

        # Gerblé food as a saved food by the user.
        self.saved_food = MySelection.objects.create(user=self.user)
        self.saved_food.my_healthy_foods.add(self.gerble)

    def test_selection_logged_in(self):
        """Connexion to the Selection page that must return HTTP 200,
        if logged in, with the right food selection and the right template.
        """
        # The user is logged in.
        self.client.login(username=self.username, password=self.password)
        # Testing the access while logged in.
        response = self.client.get(reverse('selection'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'food/selection.html')

    def test_selection_logged_out(self):
        """Trying to access the Selection page while logged out that renders
        HTTP 302, redirection to the Sign In page.
        """
        response = self.client.get(reverse('selection'))
        self.assertRedirects(
            response, (reverse('signin'))+'?redirection_vers='+(reverse('selection')))

    def test_selection_delete(self):
        """Delete a saved product (Gerblé) of the Selection page that must return HTTP 200,
        and the selected food must be deleted from the MySelection table for that user.
        """
        # The user is logged in.
        self.client.login(username=self.username, password=self.password)
        # The user deletes the Gerblé food from his/her portfolio.
        url = reverse('selection')
        data = {"food_saved_delete": self.gerble.id}
        response = self.client.post(url, data)
        # Stays in the same Selection page.
        self.assertEqual(response.status_code, 200)
        # Testing that this deleted food is not in MySelection table anymore, for that user.
        self.assertFalse(MySelection.objects.filter(id=self.gerble.id).exists())



################################################################
#                   FOOD RESULTS BY CATEGORY                   #
################################################################

class CategoriesTestCase(TestCase):
    """
    Testing the Food Categories page.
    """

    def setUp(self):
        """Data samples to run the tests.
        """
        self.username = 'jeanfrancois'
        self.email = 'jfsubrini@yahoo.com'
        self.password = 'monsupermotdepasse'
        self.user = User.objects.create_user(self.username, self.email, self.password)

        # Sample of origin (Nutella) and substitute (Gerblé) foods data in a category.
        self.category = Category.objects.create(name="Pâtes à tartiner")
        gerble = {
            'id': '3178',
            'name': 'Pâte à tartiner - Gerblé - 220g',
            'brand': 'Gerblé, Glucoregul',
            'category': self.category,
            'nutrition_grade': NutritionGrade.a,
            'nutrition_score': -4,
            'url': 'https://fr.openfoodfacts.org/produit/3175681105393/pate-a-tartiner-gerble',
            'image_food': 'https://blabla',
            'image_nutrition': 'https://blablabla',
        }
        gerble = Food.objects.create(**gerble)
        self.gerble = gerble

    def test_display_per_category_logged_out(self):
        """Trying to access the foodcategories page while logged out that renders
        HTTP 302, redirection to the user signin page.
        """
        response = self.client.get(reverse('categories'))
        self.assertRedirects(
            response, (reverse('signin'))+'?redirection_vers='+(reverse('categories')))

    def test_display_per_category_valid(self):
        """Accessing the foodcategories page while the user category choice is valid.
        This must return HTTP 200 and the right template.
        """
        # The user is logged in.
        self.client.login(username=self.username, password=self.password)
        # The user selects an option (one category).
        response = self.client.get(reverse('categories'), {'category': 'Pâtes à tartiner'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'food/foodcategories.html')

    def test_display_per_category_save(self):
        """Saving a substitute food into MySelection table while the user
        is logged in and return HTTP 302."""
        # The user is logged in.
        self.client.login(username=self.username, password=self.password)
        # Testing the saving of the Gerblé food by the user.
        url = reverse('categories')
        data = {"substitute": self.gerble.id}
        response = self.client.post(url, data)
        # Redirect to the same Selection page.
        self.assertEqual(response.status_code, 302)
        # The substitute food must be saved into MySelection table for that user.
        self.assertTrue(MySelection.objects.all().exists())



################################################################
#                        PASSWORD RESET                        #
################################################################

class ResetTestCase(TestCase):
    """
    Testing the Password Reset pages.
    """

    def setUp(self):
        """Data samples to run the tests.
        """
        self.username = 'jeanfrancois'
        self.email = 'jfsubrini@yahoo.com'
        self.password = 'monsupermotdepasse'
        self.user = User.objects.create_user(self.username, self.email, self.password)

    # def test_account_logged_in(self):
    #     """Accessing the user account page while logged in
    #     that renders HTTP 200 and the right template.
    #     """
    #     # The user is logged in.
    #     self.client.login(username=self.username, password=self.password)
    #     # Testing the access while logged in.
    #     response = self.client.get(reverse('account'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'food/account/account.html')
