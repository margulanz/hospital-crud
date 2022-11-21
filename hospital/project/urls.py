from django.urls import include, path
from .views import (
	main,
	ListCountry,AddCountry,DeleteCountry,UpdateCountry,
	AddDiseaseType,ListDiseaseType,UpdateDiseaseType,DeleteDiseaseType,
	AddUser,ListUsers,UpdateUser,DeleteUser,
	AddDisease,ListDiseases,UpdateDisease,DeleteDisease,
	AddDiscover,ListDiscovers,UpdateDiscover,DeleteDiscover,
	AddPublicServant,ListPublicServant,UpdatePublicServant,DeletePublicServant,
	AddDoctor,ListDoctor,UpdateDoctor,DeleteDoctor,
	)


urlpatterns = [
	path('',main),
	# Country
	path("countries/",ListCountry.as_view()),
	path("add-country/",AddCountry.as_view()),
	path('delete-country/<str:cname>/',DeleteCountry.as_view()),
	path('update-country/<str:cname>/',UpdateCountry.as_view()),
	# DiseaseType
	path("disease-types/",ListDiseaseType.as_view()),
	path("add-disease-type/",AddDiseaseType.as_view()),
	path("update-disease-type/<int:id>/",UpdateDiseaseType.as_view()),
	path('delete-disease-type/<int:id>/',DeleteDiseaseType.as_view()),
	# Users
	path("users/",ListUsers.as_view()),
	path("add-user/",AddUser.as_view()),
	path("update-user/<str:email>/",UpdateUser.as_view()),
	path('delete-user/<str:email>/',DeleteUser.as_view()),
	# Disease
	path("diseases/",ListDiseases.as_view()),
	path("add-disease/",AddDisease.as_view()),
	path("update-disease/<str:disease_code>/",UpdateDisease.as_view()),
	path('delete-disease/<str:disease_code>/',DeleteDisease.as_view()),

	# Public Servant
	path("public-servants/",ListPublicServant.as_view()),
	path("add-public-servant/",AddPublicServant.as_view()),
	path("update-public-servant/<str:email>/",UpdatePublicServant.as_view()),
	path('delete-public-servant/<str:email>/',DeletePublicServant.as_view()),
	# Doctors
	path("doctors/",ListDoctor.as_view()),
	path("add-doctor/",AddDoctor.as_view()),
	path("update-doctor/<str:email>/",UpdateDoctor.as_view()),
	path('delete-doctor/<str:email>/',DeleteDoctor.as_view()),
]