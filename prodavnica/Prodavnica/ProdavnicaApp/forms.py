from .models import Product
from django import forms


class FoodForm(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super(FoodForm,self).__init__(*args,**kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Product
        exclude = ('user',)