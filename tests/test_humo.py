"""Prueba de humo de la plantilla: confirma que pytest encuentra el paquete apartalo.

Si esta prueba pasa, tu entorno está listo. Puedes dejarla.
"""
import apartalo


def test_el_paquete_se_importa():
    assert apartalo.__doc__ is not None
