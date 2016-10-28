from django.contrib import admin
# from django.contrib.contenttypes.models import ContentType

# Register your models here.
from .models.Asociacion import Asociacion
from .models.Lote import Lote
from .models.Manzana import Manzana
from .models.CuentaBanco import CuentaBanco
from .models.RelacionManzanaLote import RelacionManzanaLote
from .models.InformacionLote import InformacionLote

# admin.site.register(ContentType)

admin.site.register(Asociacion)
admin.site.register(Lote)
admin.site.register(Manzana)
# admin.site.register(ManzanaLote)
admin.site.register(CuentaBanco)
admin.site.register(RelacionManzanaLote)
admin.site.register(InformacionLote)
