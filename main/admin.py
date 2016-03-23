from django.contrib import admin
from main.models import State, StateCapital, City

# Register your models here.

class StateCapitalInLine(admin.TabularInline):
	model = StateCapital 


class StateAdmin(admin.ModelAdmin):
	list_display = ("name", "abbreviation")
	search_fields = ["name"]
	inlines = [StateCapitalInLine]


class StateCapitalAdmin(admin.ModelAdmin):
	list_display = ('name', 'capital_population')
	search_fields = ('name',)



admin.site.register(State, StateAdmin)
admin.site.register(StateCapital, StateCapitalAdmin)
admin.site.register(City)