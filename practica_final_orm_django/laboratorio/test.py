from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date  # Importar date desde datetime
from .models import Laboratorio, Producto

class LaboratorioModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='12345')
        
        cls.laboratorio = Laboratorio.objects.create(
            nombre='Laboratorio de Prueba',
            ciudad='Santiago',
            pais='Chile'
        )
        cls.producto = Producto.objects.create(
            nombre='Producto de Prueba',
            laboratorio=cls.laboratorio,
            f_fabricacion=date(2024, 1, 1),  
            p_costo=100.00,
            p_venta=150.00
        )

    def test_producto_data(self):
        producto = Producto.objects.get(id=self.producto.id)
        self.assertEqual(producto.nombre, 'Producto de Prueba')
        self.assertEqual(producto.laboratorio, self.laboratorio)
        self.assertEqual(producto.f_fabricacion, date(2024, 1, 1)) 
        self.assertEqual(producto.p_costo, 100.00)
        self.assertEqual(producto.p_venta, 150.00)

    def test_url_http_status(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(f'/editar_laboratorio/{self.laboratorio.id}/')
        self.assertEqual(response.status_code, 200)

    def test_reverse_url_template_and_content(self):
        self.client.login(username='testuser', password='12345')
        url = reverse('editar_laboratorio', args=[self.laboratorio.id])  
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'editar_laboratorio.html')
        self.assertContains(response, 'Laboratorio de Prueba')
        self.assertContains(response, 'Santiago')
        self.assertContains(response, 'Chile')

