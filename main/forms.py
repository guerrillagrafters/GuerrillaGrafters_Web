from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from main.models import UserProfile


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label = "First name")
    last_name = forms.CharField(label = "Last name")
    email = forms.EmailField(label = "Email")
    email2 = forms.EmailField(label = "Email confirmation",
                              help_text = "Enter the same email as above, for verification.")
    username = forms.CharField(widget=forms.HiddenInput, required=False)
    
    def clean_username(self):
            "This function is required to overwrite an inherited username clean"
            return self.cleaned_data['username']
        
    def clean_email2(self):
        if self.cleaned_data.get("email2", '') != self.cleaned_data.get("email", ''):
            raise forms.ValidationError("The two email fields didn't match.")
        if User.objects.filter(email__iexact=self.cleaned_data.get("email", '')):
            raise forms.ValidationError("That email is already in use in the system.")
        return self.cleaned_data['email2']

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        if commit:
            user.save()

            try:
                profile = user.get_profile()
            except:
                profile = UserProfile(user=user)

            profile.save()

        return user

    def clean(self):
        if not self.errors:
            generated_username = self.cleaned_data['email'].split('@',1)[0][:25]
            c = User.objects.filter(username = generated_username).count()
            if c > 1:
                generated_username += c
            self.cleaned_data['username'] = generated_username
        super(CustomUserCreationForm, self).clean()
        return self.cleaned_data
    
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "email2")

        

        
class AddTreeForm(forms.Form):
  address = forms.CharField(label="Nearest street address")
  species = forms.CharField(label="Select species of tree (optional)")
  variety = forms.CharField(label="Select variety (optional)")
  age = forms.IntegerField(min_value=0, required=False, label="Approximate age of tree")
  height = forms.IntegerField(min_value=0, required=False, label="Approximate height of tree")
  condiiton = forms.IntegerField(min_value=0, label="Condition of tree")
  steward = forms.ChoiceField(choices=[(x,x) for x in ["Yes","No","Maybe"]], widget=forms.RadioSelect, label="Will you steward the tree?")
  track = forms.ChoiceField(choices=[(x,x) for x in ["Yes","No"]], widget=forms.RadioSelect, label="Do you want to be able to track your submission?")
  
  