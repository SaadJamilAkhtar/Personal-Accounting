from django.contrib import admin
from .models import *

admin.site.register(Account)
admin.site.register(Entry)
admin.site.register(DebitAccount)
admin.site.register(CreditAccount)
admin.site.register(AccuUser)
