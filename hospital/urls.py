from django.urls import path
from .views import PatientRequest, promise, PatientListView,PatientDeleteView, DoctorMessage, home, MessageListView, MessageDeleteView
urlpatterns = [
	path('', PatientRequest.as_view(), name='patient_form'),
	path('home/', home, name='home'),
	path('patient/list/', PatientListView.as_view(), name='patient_list'),
	path('patient/list/<int:id>/delete', PatientDeleteView.as_view(), name='patient_delete'),
	path('doctor/message/', DoctorMessage.as_view(), name='message'),
	path('message/list/', MessageListView.as_view(), name='message_list'),
	path('message/list/<int:id>/delete', MessageDeleteView.as_view(), name='message_delete'),
	path('promise/', promise, name='promise'),
]