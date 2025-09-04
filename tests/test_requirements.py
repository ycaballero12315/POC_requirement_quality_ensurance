import pytest
from app.models import Requirement
from app.routes import bp

def test_requirement_coverage():
    # Simulación: recorrer requisitos y verificar si la función de test existe
    for req in Requirement.query.all():
        try:
            test_func = globals()[req.test_function]
            assert callable(test_func)
        except KeyError:
            pytest.fail(f"Función de test no encontrada: {req.test_function}")
