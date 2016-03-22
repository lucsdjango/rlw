from django.contrib import admin
from .models import *



class TextPageInline(admin.TabularInline):
	model = TextPage

class TextAdmin(admin.ModelAdmin):
	list_display = ['description',]
	#list_filter = ('trialIdx',NOScores, 'participant')
	fields = ('description', 'video', 'audio')
	inlines = [TextPageInline]
	
	
# Register your models here.
admin.site.register(Text, TextAdmin)
admin.site.register(Condition)
admin.site.register(Experiment)