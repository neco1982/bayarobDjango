from django import forms
#from tinymce import TinyMCE
from .models import Project, Comment


""" class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False
 """

class ProjectForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = Project
        fields = '__all__'

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Type your comment',
        'id': 'usercomment',
        'rows': '3',
    }))
    class Meta:
        model = Comment
        fields = ('content',)