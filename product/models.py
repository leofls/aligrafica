from django.db import models
import base64

prioridade = (
    ('1', 'A'),
    ('2', 'B'),
)

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="nome")
    price = models.FloatField(verbose_name="preço")
    unit = models.IntegerField(verbose_name="unidade")
    priority = models.CharField(max_length=20, verbose_name="prioridade", choices=prioridade)
    #image_file = models.ImageField(verbose_name="Arquivo", upload_to='images/')
    image_b64 = models.BinaryField(blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.image_file:
            img_file = open(self.image_file.url, "rb")
            data = base64.b64encode(img_file.read())
            self.image_b64 = format_html('<img src="data:;base64,{}">', data)
            super(Product, self).save(*args, **kwargs)

    class Meta: 
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
