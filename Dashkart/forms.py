from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class SignupForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=30)
    last_name = forms.CharField(label='Last name', max_length=30)
    email = forms.EmailField(label='Email', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class AddpatForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=30)
    last_name = forms.CharField(label='Last name', max_length=30)
    email = forms.EmailField(label='Email', max_length=100)
    address = forms.CharField(label='Address',widget=forms.Textarea)
    age  = forms.IntegerField(label='Age')
    gender = forms.CharField(label='Gender',max_length=10)
    contact_no= forms.CharField(label='Contact no',max_length=10)

class SearchpatForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=30,required=False)
    mobile = forms.CharField(label='Phone number', max_length=10,required=False)


# class ProdRegistration(forms.Form):
#     category = forms.CharField(label='category')
#     product_name = forms.CharField(label='product_name', max_length=100)
#     age = forms.IntegerField(label='age')
#     additional_information = forms.CharField(label='additional_information', max_length=500)
#     address = forms.CharField(label='address', max_length=200)
#     city = forms.CharField(label='city', max_length=50)
#     state = forms.CharField(label='state', max_length=20)
#     zip_code = forms.IntegerField(label='zip_code')
#     phone = forms.IntegerField(label='phone')
#     price = forms.IntegerField(label='price')

# class PriceForm(forms.Form):
#     minPrice = forms.IntegerField(label='Min Price')
#     maxPrice = forms.IntegerField(label='Max Price')