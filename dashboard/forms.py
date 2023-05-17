# Developed by Peace Oloruntoba aka Prof Prince Peace
# you can contact me on whatsapp and phone call @+2348166846226
# email @ profprincepeace@gmail.com or peascainc@gmail.com
# social media @ Peace Oloruntoba or PeaceOloruntoba including LinkedIn, Facebook, Twitter, etc.
#
# copyright 2022.

from django import forms
from django.forms import widgets
from . models import *
from django.contrib.auth.forms import UserCreationForm

class NotesForm(forms.ModelForm):
   class Meta:
      model = Notes
      fields = ['title','description']

class DateInput(forms.DateInput):
   input_type = 'date'

class HomeworkForm(forms.ModelForm):
   class Meta:
      model = Homework
      widgets = {'due':DateInput()}
      fields = ['subject','title','description','due','is_finished']
      
class DashboardForm(forms.Form):
   text = forms.CharField(max_length=100,label="Enter Your Search")
   
class TodoForm(forms.ModelForm):
   class Meta:
      model = Todo
      fields = ['title','is_finished'] 
   
class UserRegistrationForm(UserCreationForm):
   class Meta:
      model = User
      fields = ['username','password1','password2']

CHOICES = (
    ('1', 'Addition'),
    ('2', 'Subtraction'),
    ('3', 'Multiplication'),
    ('4', 'Division'),
    ('5', 'Exponentiation'),
    ('6', 'Square Root'),
    ('7', 'Logarithm'),
    ('8', 'Sine'),
    ('9', 'Cosine'),
    ('10', 'Tangent'),
    ('11', 'Factorial'),
    ('12', 'Absolute Value'),
)

class CalculatorForm(forms.Form):
    choice = forms.ChoiceField(label='Operation', choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    num1 = forms.FloatField(label='Number 1', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    num2 = forms.FloatField(label='Number 2', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    num = forms.FloatField(label='Number', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    base = forms.FloatField(label='Base', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    angle = forms.FloatField(label='Angle', widget=forms.NumberInput(attrs={'class': 'form-control'}))
