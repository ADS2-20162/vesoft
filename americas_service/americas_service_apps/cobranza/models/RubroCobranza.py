from django.db import models


class RubroCobranza(models.Model):

    concepto_cobranza = models.CharField(
        max_length=80, unique=True, null=False, blank=False)
    importe = models.DecimalField(
        decimal_places=2, max_digits=5, null=False, blank=False)
    mora = models.DecimalField(
        decimal_places=2, max_digits=5, null=True, blank=True)
    detalle = models.TextField(max_length=500)
    fecha_inicio = models.DateField(null=False, blank=False)
    fecha_fin = models.DateField(null=False, blank=False)

    class Meta:
        verbose_name = "RubroCobranza"
        verbose_name_plural = "RubroCobranzas"

    def __str__(self):
        return '%s %s' % (self.concepto_cobranza, self.importe)