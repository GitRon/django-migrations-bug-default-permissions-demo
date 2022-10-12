from django.db import models


class ModelMixin:
    class Meta:
        default_permissions = ()


class ModelUsesMixin(ModelMixin, models.Model):
    class Meta:
        permissions = (
            ('view_stuff', "Can view stuff"),
        )


class ModelNoMixin(models.Model):
    class Meta:
        default_permissions = ()
        permissions = (
            ('view_stuff', "Can view stuff"),
        )
