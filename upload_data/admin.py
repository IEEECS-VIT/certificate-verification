from django.contrib import admin
from .models import ParticipantData, Certificate, FontStyle
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.



class ParticipantResource(resources.ModelResource):
    Event_Name = fields.Field(column_name='Event_Name', attribute='Event_Name', widget=ForeignKeyWidget(Certificate, 'Event_Name'))
    class Meta:
        model = ParticipantData
        import_id_fields = ('Full_Name', 'Event_Name', "Description")
        fields = ('Full_Name', 'Event_Name', "Description")
        

class ParticipantDataAdmin(ImportExportActionModelAdmin):
    resource_class = ParticipantResource
    exclude = ('id', 'slug')
    




admin.site.register(ParticipantData, ParticipantDataAdmin)
admin.site.register(Certificate)
admin.site.register(FontStyle)