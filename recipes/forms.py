from django import forms
from .models import Recipe


# class AddRecipe(forms.Form):
#     title = forms.CharField(label="Recipe Title", max_length=100)
#     prepMinutes = forms.IntegerField(label="Prep Time (Minutes)", min_value=1, max_value=360)
#     cookMinutes = forms.IntegerField(label="Cook Time (Minutes)", min_value=1, max_value=360)
#     servings = forms.IntegerField(label="Servings", min_value=1, max_value=16)
#     ingredients = forms.CharField(widget=forms.Textarea)
#     instructions = forms.CharField(widget=forms.Textarea)
#     prev_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'title',
            'prepMinutes',
            'cookMinutes',
            'servings',
            'ingredients',
            'instructions',
            'tags',
            'image',
            'public'
        ]
