from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Div, Field, Button
from crispy_forms.bootstrap import Modal

from prices_comparator_tool.models import Product, ProductCategory




class ProductCategoryForm(forms.Form):
    product_name = forms.CharField(label="Product Name", max_length=100)
    class Meta:
        model = ProductCategory
        fields = ['product_name']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
                Field('product_name', title='Product Name'),
                Submit('submit', 'Submit', css_class='button white'),
                
            )
        

class ProductForm(forms.Form):
    product_name = forms.CharField(label="Product Name", max_length=100)
    product_weight = forms.FloatField(label='Weight in grams')
    product_price = forms.FloatField(label='Product price')
    total_units = forms.IntegerField(label='Total of units')
    class Meta:
        model = Product
        fields = ['product_name','product_weight','product_price','total_units']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
                Field('product_name', title='Product Name'),
                Field('product_weight', title='Product weigth'),
                Field('product_price', title='Product price'),
                Field('total_units', title='Total units'),
                Submit('submit', 'Submit', css_class='button white'),
                
            )