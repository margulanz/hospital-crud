from django import forms
from .models import Country,Diseasetype,Users,Disease,Discover,Publicservant,Doctor


class CountryForm(forms.ModelForm):
	class Meta:
		model = Country
		fields = [
			'cname',
			'population',
			
		]
class DiseaseTypeForm(forms.ModelForm):
	class Meta:
		model = Diseasetype
		fields = [
			'id',
			'description',
		]

class UsersForm(forms.ModelForm):
	class Meta:
		model = Users
		fields = [
			'email',
			'name',
			'surname',
			'salary',
			'phone',
			'cname',
		]

class DiseaseForm(forms.ModelForm):
	class Meta:
		model = Disease
		fields = [
			'disease_code',
			'pathogen',
			'description',
			'id',
		]

class DateInput(forms.DateInput):
    input_type = 'date'


class DiscoverForm(forms.ModelForm):
	class Meta:
		model = Discover
		fields = [
			'cname',
			'disease_code',
			'first_enc_date',
		]
		widgets = {
            'first_enc_date': DateInput()
        }

class PublicServantForm(forms.ModelForm):
	class Meta:
		model = Publicservant
		fields = [
			'email',
			'department',
		]
class DoctorForm(forms.ModelForm):
	class Meta:
		model = Doctor
		fields = [
			'email',
			'degree',
		]