from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display="emp_id","emp_name","emp_desig"

admin.site.register(Member,MemberAdmin)
