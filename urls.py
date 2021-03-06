# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.urls import path
from aldryn_django.utils import i18n_patterns
import aldryn_addons.urls


urlpatterns = [
    path('', include('mainbank.urls')),
    # add your own patterns here
] + aldryn_addons.urls.patterns() + i18n_patterns(
    # add your own i18n patterns here
    *aldryn_addons.urls.i18n_patterns()  # MUST be the last entry!
)
