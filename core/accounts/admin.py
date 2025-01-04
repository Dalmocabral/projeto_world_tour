from django.contrib import admin
from .models import User, Award, FlightLeg, AllowedAircraft, UserAward, AllowedIcao
# Register your models here.


class PirepsFlightAdmin(admin.ModelAdmin):
    list_display = ('get_pilot_first_name', 'registration_date', 'status')

    def get_pilot_first_name(self, obj):
        return obj.pilot.first_name

class FlightLegInline(admin.TabularInline):
    model = FlightLeg
    extra = 1

class AllowedAircraftInline(admin.TabularInline):
    model = AllowedAircraft
    extra = 1

class AllowedIcaoInline(admin.TabularInline):
    model = AllowedIcao
    extra = 1

@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    inlines = [FlightLegInline, AllowedAircraftInline, AllowedIcaoInline]

@admin.register(UserAward)
class UserAwardAdmin(admin.ModelAdmin):
    list_display = ('user', 'award', 'progress', 'start_date', 'end_date')
    list_filter = ('award', 'progress')
''' 
@admin.register(PilotAward)
class PilotAwardAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Exibe o nome e a descrição na lista de awards
    filter_horizontal = ('participants',)  # Facilita a seleção de participantes existentes

    '''
# Registro dos outros modelos
admin.site.register(User)



