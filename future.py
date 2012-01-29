# coding: utf-8

""" Exibe a lista de recursos __future__ do Python
com a versão onde o recurso foi introduzido como opcional
e a versão onde o recurso se tornou padrão.
"""

import __future__

for feature_name in __future__.all_feature_names:
    feature = getattr(__future__, feature_name)
    print feature_name.rjust(20), feature.optional, feature.mandatory
