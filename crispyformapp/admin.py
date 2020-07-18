from django.contrib import admin
from .models import Course,College,Location,Branch,Institute
admin.site.register(College)
admin.site.register(Course)
admin.site.register(Location)
admin.site.register(Branch)
admin.site.register(Institute)
