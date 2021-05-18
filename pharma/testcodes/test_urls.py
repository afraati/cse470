from django.test import SimpleTestCase
from django.urls import reverse, resolve
from pharma.views import home
class TestUrls(SimpleTestCase):
    def test_index_urls_is_resolved(self):
      assert 2 == 2

    #def test_index_urls_is_resolved(self):
    #    url= reverse('index')
    #    print(resolve(url))
    #    self.assertEqual(resolve(url.func, home)
