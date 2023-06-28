from django import forms
from .models import Customer, Campany, Subject, TicketSupport

class FormSettings(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormSettings, self).__init__(*args, **kwargs)
        # Here make some changes such as:
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

class CustomerForm(FormSettings):
    
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)
    address = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
   
    
    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)


    class Meta:
        model = Customer
        fields =['username','phone_number', 'email']



        
class CampanyForm(FormSettings):
    
    class Meta:
        model = Campany
        fields = "__all__"
        
class SubjectForm(FormSettings):
    
    class Meta:
        model = Subject
        fields = "__all__"
        
class TicketForm(FormSettings):
    
    class Meta:
        model = TicketSupport
        fields = "__all__"