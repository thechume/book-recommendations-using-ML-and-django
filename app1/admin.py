from django.contrib import admin

# Register your models here.

#from .models import Question
from .models import Books, Authors, ReadBooks, Users, Recs
#admin.site.register(Question)
admin.site.register(Books)
admin.site.register(Authors)
admin.site.register(ReadBooks)
admin.site.register(Users)
admin.site.register(Recs)
