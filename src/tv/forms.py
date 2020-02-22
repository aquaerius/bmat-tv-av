from django import forms
from tv.models import COUNTRY_CHOICES

class DateInput(forms.DateInput):
	input_type = 'date'

class ProgramForm(forms.Form):
	
	def __init__(self, *args, **kwargs):
		super(ProgramForm, self).__init__(*args, **kwargs)
		# assign a 'N/A' default value to the choice field
		self.initial['country_code'] = 'N/A'

	start_date = forms.DateField(widget=DateInput)
	end_date = forms.DateField(widget=DateInput)
	local_title = forms.CharField(label='Local title', max_length=255, required=False)
	country_code = forms.ChoiceField(label='Country', widget=forms.Select, choices=COUNTRY_CHOICES, required=False)
