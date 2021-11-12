from django.test import TestCase
from muebles.models import muebles

class MueblesTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        muebles.objects.create(name='Mesa', price='500', lenght='100', width = '200', height = '300', status = 'Nuevo')

    def test_name_label(self):
        mueble=muebles.objects.get(id=1)
        field_label = mueble._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'Nombre')

    def test_price_label(self):
        mueble=muebles.objects.get(id=1)
        field_label = mueble._meta.get_field('price').verbose_name
        self.assertEquals(field_label,'Precio')

    def test_lenght_label(self):
        mueble=muebles.objects.get(id=1)
        field_label = mueble._meta.get_field('lenght').verbose_name
        self.assertEquals(field_label,'Largo')    

    def test_width_label(self):
        mueble=muebles.objects.get(id=1)
        field_label = mueble._meta.get_field('width').verbose_name
        self.assertEquals(field_label,'Ancho')

    def test_height_label(self):
        mueble=muebles.objects.get(id=1)
        field_label = mueble._meta.get_field('height').verbose_name
        self.assertEquals(field_label,'Alto')   
    
    def test_status_label(self):
        mueble=muebles.objects.get(id=1)
        field_label = mueble._meta.get_field('status').verbose_name
        self.assertEquals(field_label,'Estado')   

    def test_name_max_length(self):
        mueble=muebles.objects.get(id=1)
        max_length = mueble._meta.get_field('name').max_length
        self.assertEquals(max_length,200)

    def test_price_max_length(self):
        mueble=muebles.objects.get(id=1)
        max_length = mueble._meta.get_field('price').max_length
        self.assertEquals(max_length,200)

    def test_lenght_max_length(self):
        mueble=muebles.objects.get(id=1)
        max_length = mueble._meta.get_field('lenght').max_length
        self.assertEquals(max_length,200)    
    
    def test_width_max_length(self):
        mueble=muebles.objects.get(id=1)
        max_length = mueble._meta.get_field('width').max_length
        self.assertEquals(max_length,200)
    
    def test_height_max_length(self):
        mueble=muebles.objects.get(id=1)
        max_length = mueble._meta.get_field('height').max_length
        self.assertEquals(max_length,200)

    def test_status_max_length(self):
        mueble=muebles.objects.get(id=1)
        max_length = mueble._meta.get_field('status').max_length
        self.assertEquals(max_length,200)