# from django import forms
# from .models import Task, Proyect
#
#
# class TaskForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = ['title', 'description', 'proyect']  # Asegúrate de incluir 'proyect'
#
#     # Si necesitas personalizar el widget del campo 'proyect', para mostrarlo como un select:
#     proyect = forms.ModelChoiceField(queryset=Proyect.objects.all(), empty_label="Selecciona un Proyecto")