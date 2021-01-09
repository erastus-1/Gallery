from django.test import TestCase
from .models import Image,Location,Category

# Create your tests here.
class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.image= Image(title = 'smoothie', category ='self.category', description ='best smoothie in nairobi area and surrounding', location = 'nairobi', image_url = 'https://moringaschool.instructure.com/courses/329/pages/tuesday-testing-django-apps?module_item_id=2449' )
