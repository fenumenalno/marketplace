from django.contrib import admin
from marketplace import models

admin.site.register([models.User, models.Tovari, models.Korzina])