from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, TemplateView, DeleteView
from .models import *
from django.urls import reverse_lazy
from .forms import *
# Create your views here.

class PatientRequest(CreateView):
	form_class = PatientForm
	success_url = reverse_lazy('patient_list')
	template_name = 'patient_form.html'

def promise(request):
	length = len(Message.objects.all())
	if not length-1 < 0:
		message = Message.objects.all()[length-1]
		return render(request, 'promise.html', {'message': message})	
	return render(request, 'promise.html')	
	


def home(request):
	length = len(Message.objects.all())
	if not length-1 < 0:
		message = Message.objects.all()[length-1]
		return render(request, 'index.html', {'message': message})	
	return render(request, 'index.html')	
	

class PatientListView(ListView):
	model = Patient
	template_name = 'patient_list.html'	

class MessageListView(ListView):
	model = Message
	template_name = 'message_list.html'	

class PatientDeleteView(DeleteView):
	
	template_name = 'delete.html'
	success_url = reverse_lazy('patient_list')
	def get_object(self):
		id_ = self.kwargs.get('id')
		return get_object_or_404(Patient, id=id_)	

class MessageDeleteView(DeleteView):
	
	template_name = 'message_delete.html'
	success_url = reverse_lazy('message_list')
	def get_object(self):
		id_ = self.kwargs.get('id')
		return get_object_or_404(Message, id=id_)	


class DoctorMessage(CreateView):
	form_class = MessageForm
	success_url = reverse_lazy('home')
	template_name = 'doctor_message_form.html'		