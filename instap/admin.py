from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
from django.contrib.auth.models import User
from .models import DisLiked, Employee, Followers, LikeClass, Post, commets



class EmployeeInline(admin.StackedInline):
    model=Employee
    can_delete=False
    verbose_name_plural='employee'


class UserAdmin(BaseUserAdmin):
    inlines=(EmployeeInline,)

admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.register(Post)
admin.site.register(Followers)
admin.site.register(LikeClass)
admin.site.register(DisLiked)
admin.site.register(commets)