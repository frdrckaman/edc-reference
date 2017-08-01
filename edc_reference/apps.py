import sys

from django.apps import AppConfig as DjangoAppConfig

from .site import site_reference_configs


class AppConfig(DjangoAppConfig):
    name = 'edc_reference'
    verbose_name = 'Edc Reference'

    def ready(self):
        from .signals import reference_post_delete
        sys.stdout.write(f'Loading {self.verbose_name} ...\n')

        site_reference_configs.autodiscover()

        sys.stdout.write(f' Done loading {self.verbose_name}.\n')
