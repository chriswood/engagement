from django import forms

class EngagementForm(forms.Form):
    #All elements with the 'weight' suffix will be treated as an event.
    #So to add/remove an event, you just add/remove the form element
    number_of_users = forms.IntegerField(min_value=1, max_value=100, required=True, initial=5)
    scale = forms.IntegerField(min_value=1, max_value=100, initial=30)
    opens_weight = forms.IntegerField(min_value=0, max_value=100, required=True, initial=0)
    clicks_weight = forms.IntegerField(min_value=0, max_value=100, required=True, initial=0)
    forwards_weight = forms.IntegerField(min_value=0, max_value=100, required=True, initial=0)
    shares_weight = forms.IntegerField(min_value=0, max_value=100, required=True, initial=0)
