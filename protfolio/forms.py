from django import forms
from protfolio.models import*

class projectForm(forms.ModelForm):
    class Meta:
        model=projectModel
        fields='__all__'
        exclude=['created_by']
        widgets={
            'completed_date':forms.DateInput(attrs={
                'type':'date'
            })
        }
class workForm(forms.ModelForm):
    class Meta:
        model=workExModel
        fields='__all__'
        exclude=['created_by']
        widgets={
            'start_date':forms.DateInput(attrs={
                'type':'date'
            }),
            'end_date':forms.DateInput(attrs={
                'type':'date'
            })
        }
class eduForm(forms.ModelForm):
    class Meta:
        model=EduModel
        fields='__all__'
        exclude=['created_by']
        widgets={
            'passing_year':forms.DateInput(attrs={
                'type':'date'
            })
        }       
