from django import forms
import django_filters
from django_filters import CharFilter
from .models import *



# class PostFilter(django_filters.FilterSet):
# 	handel = CharFilter(field_name='headline', lookup_expr="icontains", label='Headline')
# 	tag = django_filters.ModelMultipleChoiceFilter(queryset=Tag.objects.all(),
# 		widget=forms.CheckboxSelectMultiple
# 		)
# 	class Meta:
# 		model = Por
# 		fields = ['handel', 'tag']



class PostFilter(django_filters.FilterSet):
	handel = CharFilter(field_name='handel', lookup_expr="icontains", label='Headline')
	tag = django_filters.ModelMultipleChoiceFilter(queryset=Tag.objects.all(),
		widget=forms.CheckboxSelectMultiple
		)
	class Meta:
		model = Por
		fields = ['handel', 'tag']