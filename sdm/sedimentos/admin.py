from django.contrib import admin

# Register your models here.
from .models import amostra
admin.site.register(amostra)

from .models import continente
admin.site.register(continente)

from .models import país
admin.site.register(país)

from .models import estado
admin.site.register(estado)

from .models import cidade
admin.site.register(cidade)

from .models import ambiente
admin.site.register(ambiente)

from .models import clima
admin.site.register(clima)