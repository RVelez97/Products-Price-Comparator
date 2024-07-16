from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Div, Field, Button
from crispy_forms.bootstrap import Modal

from prices_comparator_tool.models import Product, ProductCategory, Units




class ProductCategoryForm(forms.Form):
    product_name = forms.CharField(label="Product Name", max_length=100)
    class Meta:
        model = ProductCategory
        fields = ['product_name','units']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
                Field('product_name', title='Product Name'),
                Field('units', title='Measure units'),
                Submit('submit', 'Submit', css_class='button white'),
                
            )
    units = forms.ChoiceField(
        choices=[(unit.value, unit.name) for unit in Units],
    )
        

class ProductForm(forms.Form):
    product_name = forms.CharField(label="Product Name", max_length=100)
    product_weight_volume_longitude = forms.FloatField(label='Net weight/volume/longitude')
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
                Field('product_weight_volume_longitude', title='Product weigth/volume/longitude'),
                Field('product_price', title='Product price'),
                Field('total_units', title='Total units'),
                Submit('submit', 'Submit', css_class='button white'),
                
            )