from django.db import models
import base64

from django.dispatch import receiver
from django.db.models.signals import post_save, m2m_changed


def upload_image_category(instance, filename):
    return f"{instance.id}-{filename.replace(' ', '_')}"

class Category (models.Model):
    name = models.CharField(verbose_name="categoria", max_length=150)
    image = models.ImageField(blank=True, null=True)
    image_b64 = models.BinaryField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def save(self, *args, **kwargs):
    #     if self.image:
    #         img_file = open(self.image.url, "rb")
    #         data = base64.b64encode(img_file.read())
    #         self.image_b64 = format_html('<img src="data:;base64,{}">', data)
    #         super(Category, self).save(*args, **kwargs)

def image_to_b64(image_file):

    with open(image_file.path, "rb") as f:
        encoded_string = base64.b64encode(f.read())
        return encoded_string

@receiver(post_save, sender=Category)
def create_base64_str(sender, instance=None, created=False, **kwargs):
    if created:
        instance.image = image_to_b64(instance.logo_image)
        instance.logo_image.delete()
        instance.save()
