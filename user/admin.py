from django.contrib import admin

from .models import User
from xodim.models import Xodim


admin.site.register(User)
admin.site.register(Xodim)