from dataclasses import fields
from django.forms import ModelForm
from .models import * 




'''class ShopForm(ModelForm):
    class Meta:
        model= Elect_shop
        fields= ['shop_name','item_name']    
        labels= {
            'shop_name': 'SHOP',
            'item_name':'ITEM NAME'

        }'''

'''def __init__(self, *args, **kwargs):
    super(ShopForm,self).__init__(*args,**kwargs)
    self.fields['shop_name'].empty_label='select'
'''


class ShopForm(ModelForm):
    class Meta:
        model= Shop
        fields= ['shop_name']

class ItemForm(ModelForm):
    class Meta:
        model= Elect_shop
        fields= ['item_name']
        