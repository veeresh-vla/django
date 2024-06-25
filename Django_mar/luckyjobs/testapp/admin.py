from django.contrib import admin
from testapp.models import HydJobs,PuneJobs,BglJobs

# Register your models here.
class HydJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibillity','address','email','phonenumber']
admin.site.register(HydJobs,HydJobsAdmin)

class PuneJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibillity','address','email','phonenumber']
admin.site.register(PuneJobs,PuneJobsAdmin)

class BglJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibillity','address','email','phonenumber']
admin.site.register(BglJobs,BglJobsAdmin)