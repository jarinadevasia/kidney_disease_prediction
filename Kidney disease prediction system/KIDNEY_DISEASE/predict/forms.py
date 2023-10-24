from django import forms

class KidneyDiseaseForm(forms.Form):
    rbc = forms.FloatField(label='Red Blood Cells (0-1):')
    sg = forms.FloatField(label='Specific Gravity (1-1.02):')
    al = forms.FloatField(label='Albumin (0-5):')
    su = forms.FloatField(label='Sugar (0-5):')
    htn = forms.BooleanField(label='Hypertension', required=False)
