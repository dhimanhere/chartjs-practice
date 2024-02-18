from django.forms import ModelForm
from myapp.models import myModel

class InsightForm(ModelForm):
	class Meta:
		model = myModel
		fields = "__all__"