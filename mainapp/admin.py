from django.contrib import admin
from django.utils.safestring import mark_safe #цвет уведомления(текста)
from .models import *
from PIL import Image
from django.forms import ModelChoiceField, ModelForm, ValidationError






class ProductAdminForm(ModelForm): ##Проверка на валидность изображения

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe(
            """'<span style="color:red;font-size:14px;">При загрузке изображения с разрешением больше {}x{} оно будет обрезано!</span>'""".format(
            *Product.MAX_RESOLUTION ##с класса Product
            ))


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    change_form_template = 'custom_admin/change_form.html'
    #exclude = ('features',)


admin.site.register(Category)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product, ProductAdmin)
