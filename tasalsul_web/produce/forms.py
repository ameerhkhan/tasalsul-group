from django import forms
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from crispy_forms.bootstrap import Field
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Submit, Layout, Fieldset, Div, ButtonHolder, Reset, HTML
from crispy_forms.layout import Row, Column



unit_choices = (
    (1, "TONS"),
    (2, "BAGS"),
    (3, "BOXES"),
    (4, "KILOGRAMS")
)

shipping_choices = (
    (1, "SEA FREIGHT"),
    (2, "AIR FREIGHT"),
    (3, "LAND FREIGHT"),
    (4, "EXPRESS (for urgent)")
)

class ProductForm(forms.Form):
    name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    number = forms.CharField(max_length=20)
    product = forms.CharField(max_length=30, required=True)
    quantity = forms.IntegerField()
    delivery_port = forms.CharField(max_length=30, required=True)
    unit_scale = forms.TypedChoiceField(label='Choose Unit', choices=unit_choices, coerce=str)
    shipping = forms.TypedChoiceField(choices=shipping_choices, coerce=str)
    message = forms.CharField(max_length=1000, required=True, widget=forms.Textarea())

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        # for visible in self.visible_fields():
        #     visible.field.widget.attrs['class'] = 'form-control'


        # https://www.merixstudio.com/blog/django-crispy-forms-what-are-they-about/

        self.helper = FormHelper()
        self.helper.attrs = {'novalidate': ''}
        # self.helper.form_id = 'id-contact-product-form'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('produce:index')
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-succes'))
        # self.helper.add_input(Submit('save', 'save', css_class = 'btn-primary'))
        # self.helper.form_class = 'form-row form-horizontal'
        # self.helper.form_class = 'form-row'
        self.use_custom_control = True

        self.helper.layout = Layout(
            Row(
                Column('name', title='Your Name', placeholder='Name', css_class='form-group col-md-4 mb-0'),
                Column('email', css_class='form-group col-md-4 mb-0'),
                Column('number', placeholder='Mobile Number' , css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('product', css_class='form-group col-md-4 mb-0'),
                Column('quantity', css_class='form-group col-md-4 mb-0'),
                Column('unit_scale', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('delivery_port', css_class='form-group col-md-6 mb-0'),
                Column('shipping', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            # Fieldset('Message'
            # 'message'),
            'message',
            # Submit('submit', 'Submit')
        )

        # self.helper.layout = Layout(
        #     Fieldset('Information',
        #         Field('name', title='Your Name', placeholder='Name', css_class="form-group col-md-6 mb-0"),
        #         Field('from_email', title='Email Address', css_class="form-group col-md-6 mb-0"),
        #         Field('phone_number', title='Phone Number', css_class="form-group col-md-6 mb-0"),
        #         Field('product_name', title='Your Name', css_class="form-group col-md-6 mb-0"),
        #         Field('quantity', title='Your Name', css_class="form-group col-md-6 mb-0"),
        #         Field('delivery_port', title='Your Name', css_class="form-group col-md-6 mb-0"),
        #         Field('unit_scale', title='Your Name', css_class="form-group col-md-2 mb-0"),
        #         Field('shipping', title='Your Name', css_class="form-group col-md-2 mb-0")),
        #     Fieldset('Message',
        #         Field('message', placeholder='Your Name', css_class='form-group'),
        #     ButtonHolder(
        #         Submit('submit', 'Submit', css_class='btn-primary'))),
        #     HTML("{% if success %} <p>Operation was successful</p> {% endif %}")
            # Submit('submit', 'SUBMIT'),
            # Reset('reset', 'RESET'),
        # )
        # self.helper.layout = Layout(
        #    Fieldset('Name',
        #             Field('name', placeholder='Your Name',css_class="form-group col-md-6"),
        #    ButtonHolder(
        #         Submit('submit', 'Submit', css_class='button white')
        #     )))

    def send_email(self):
        sub = 'Query | Tasalsul | Products'
        from_name = self.cleaned_data['name']
        from_mail = self.cleaned_data['email']
        ph_number = self.cleaned_data['number']
        message_raw = self.cleaned_data['message']
        prod_name = self.cleaned_data['product']
        quanti = self.cleaned_data['quantity']
        del_port = self.cleaned_data['delivery_port']
        unit_s = self.cleaned_data['unit_scale']
        shipping_method = self.cleaned_data['shipping']

        quant = str(quanti)

        message_1 = sub + '\n\n' + 'Name: ' + from_name + '\n' + 'Email: ' + '\n' + 'Phone: ' + ph_number + '\n'
        message_2 = 'Inquiry for: ' + prod_name + '\n' + 'Quantity: ' + quant + '\n' + 'Units :' + unit_s + '\n'
        message_3 = 'Delivery Port: ' + del_port + '\n' + 'Shipping Method: '+ shipping_method + '\n'
        message_4 = '\n' + 'Message: ' + '\n' + message_raw
        message = message_1 + message_2 + message_3 + message_4
        try:
            send_mail(sub, message, from_mail, ['admin@example.com'])
        except BadHeaderError:
            return HttpResponse('Invalid Header Found.')
        # return redirect("homepage:index") # put in the page to goto after succesful submission over here.
        return redirect("homepage:message_sent")