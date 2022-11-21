from django.shortcuts import render
from django.http import HttpResponse
from .models import Country, Diseasetype,Users,Disease,Discover,Publicservant,Doctor,Specialize
from django.views.generic import ListView,DetailView,CreateView,UpdateView, DeleteView
from .forms import CountryForm,DiseaseTypeForm,UsersForm,DiseaseForm,DiscoverForm,PublicServantForm,DoctorForm


def main(request):
	return render(request,'main.html')



########### Country ###############
# Create
class AddCountry(CreateView):
	model = Country
	template_name = 'country/add_country.html'
	form_class = CountryForm
	queryset = Country.objects.all()
# Read
class ListCountry(ListView):
	model = Country
	template_name = 'country/countries.html'
# Update	
class UpdateCountry(UpdateView):
	model = Country
	template_name = 'country/update_country.html'
	form_class = CountryForm
	pk_url_kwarg = 'cname'
# Delete
class DeleteCountry(DeleteView):
	model = Country
	template_name = 'country/delete_country.html'
	pk_url_kwarg = 'cname'
########### DiseaseType ###############
# Create
class AddDiseaseType(CreateView):# ID issue
	model = Diseasetype
	template_name = 'disease_type/add_disease_type.html'
	form_class = DiseaseTypeForm
	queryset = Country.objects.all()
	success_url = '/disease-types'
# Read
class ListDiseaseType(ListView):
	model = Diseasetype
	template_name = 'disease_type/disease_types.html'
# Update
class UpdateDiseaseType(UpdateView):
	model = Diseasetype
	template_name = 'disease_type/update_disease_type.html'
	form_class = DiseaseTypeForm
	pk_url_kwarg = 'id'
# Delete
class DeleteDiseaseType(DeleteView):
	model = Diseasetype
	template_name = 'disease_type/delete_disease_type.html'
	pk_url_kwarg = 'id'
########### Users ###############
# Create
class AddUser(CreateView):# ID issue
	model = Users
	template_name = 'users/add_user.html'
	form_class = UsersForm
	queryset = Users.objects.all()
	success_url = '/users'
# Read
class ListUsers(ListView):
	model = Users
	template_name = 'users/users.html'
# Update
class UpdateUser(UpdateView):
	model = Users
	template_name = 'users/update_user.html'
	form_class = UsersForm
	pk_url_kwarg = 'email'
	success_url = '/users'
# Delete
class DeleteUser(DeleteView):
	model = Users
	template_name = 'users/delete_user.html'
	pk_url_kwarg = 'email'
	success_url = '/users'

########### Disease ###############
# Create
class AddDisease(CreateView):# ID issue
	model = Disease
	template_name = 'diseases/add_disease.html'
	form_class = DiseaseForm
	queryset = Disease.objects.all()
	success_url = '/diseases'
# Read
class ListDiseases(ListView):
	model = Disease
	template_name = 'diseases/diseases.html'
# Update
class UpdateDisease(UpdateView):
	model = Disease
	template_name = 'diseases/update_disease.html'
	form_class = DiseaseForm
	pk_url_kwarg = 'disease_code'
	success_url = '/diseases'
# Delete
class DeleteDisease(DeleteView):
	model = Disease
	template_name = 'diseases/delete_disease.html'
	pk_url_kwarg = 'disease_code'
	success_url = '/diseases'
########### Discover ############### Need to be solved
# Create
class AddDiscover(CreateView):# ID issue
	model = Discover
	template_name = 'discovers/add_discover.html'
	form_class = DiscoverForm
	queryset = Discover.objects.all()
	success_url = '/discovers'
# Read
class ListDiscovers(ListView):
	model = Discover
	template_name = 'discovers/discovers.html'
# Update
class UpdateDiscover(UpdateView):
	model = Discover
	template_name = 'discovers/update_discover.html'
	form_class = DiscoverForm
	pk_url_kwarg = 'cname'
	success_url = '/discovers'
# Delete
class DeleteDiscover(DeleteView):
	model = Discover
	template_name = 'discovers/delete_discover.html'
	pk_url_kwarg = 'cname'
	success_url = '/discovers'
########### PublicServant ###############
# Create
class AddPublicServant(CreateView):# ID issue
	model = Publicservant
	template_name = 'public_servant/add_public_servant.html'
	form_class = PublicServantForm
	queryset = Publicservant.objects.all()
	success_url = '/public-servants'
# Read
class ListPublicServant(ListView):
	model = Publicservant
	template_name = 'public_servant/public_servants.html'
# Update
class UpdatePublicServant(UpdateView):
	model = Publicservant
	template_name = 'public_servant/update_public_servant.html'
	form_class = PublicServantForm
	pk_url_kwarg = 'email'
	success_url = '/public-servants'
# Delete
class DeletePublicServant(DeleteView):
	model = Publicservant
	template_name = 'public_servant/delete_public_servant.html'
	pk_url_kwarg = 'email'
	success_url = '/public_servants'
########### Doctor ###############
# Create
class AddDoctor(CreateView):# ID issue
	model = Doctor
	template_name = 'doctor/add_doctor.html'
	form_class = DoctorForm
	queryset = Doctor.objects.all()
	success_url = '/doctors'
# Read
class ListDoctor(ListView):
	model = Doctor
	template_name = 'doctor/doctors.html'
# Update
class UpdateDoctor(UpdateView):
	model = Doctor
	template_name = 'doctor/update_doctor.html'
	form_class = DoctorForm
	pk_url_kwarg = 'email'
	success_url = '/doctors'
# Delete
class DeleteDoctor(DeleteView):
	model = Doctor
	template_name = 'doctor/delete_doctor.html'
	pk_url_kwarg = 'email'
	success_url = '/doctors'
########### Specialize ###############
# Create
class AddSpecialize(CreateView):# ID issue
	model = Specialize
	template_name = 'specialize/add_specialize.html'
	form_class = DoctorForm
	queryset = Doctor.objects.all()
	success_url = '/specializes'
# Read
class ListSpecialize(ListView):
	model = Specialize
	template_name = 'specialize/specializes.html'
# Update
class UpdateSpecialize(UpdateView):
	model = Specialize
	template_name = 'specialize/update_specialize.html'
	form_class = DoctorForm
	pk_url_kwarg = 'email'
	success_url = '/specializes'
# Delete
class DeleteSpecialize(DeleteView):
	model = Specialize
	template_name = 'specialize/delete_specialize.html'
	pk_url_kwarg = 'email'
	success_url = '/specializes'
########### Record ###############