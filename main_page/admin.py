from django.contrib import admin
from django.contrib.auth.models import Group, User
from admin_interface.models import Theme
from .models import *

admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.unregister(Theme)
admin.site.register(MetaTags)
