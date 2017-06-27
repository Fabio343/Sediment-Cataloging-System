# arquivo que valida os models assim eles podem ser usados como tabelas no banco de dados e apresentados no site
from django.contrib import admin


# Register your models here.

from .models import Amostra
admin.site.register(Amostra)

from .models import Continente
admin.site.register(Continente)

from .models import País
admin.site.register(País)

from .models import Estado
admin.site.register(Estado)

from .models import Cidade
admin.site.register(Cidade)

from .models import Ambiente
admin.site.register(Ambiente)

from .models import Clima
admin.site.register(Clima)