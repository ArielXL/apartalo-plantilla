# Escenarios BDD (Ejercicio 4)

Escribe aquí tus archivos `.feature`: **uno por característica** (*feature*). Por ejemplo, `total.feature` para R1 y `cancelacion.feature` para R2.

Reglas del Tema 7:
- Cada escenario tiene **una sola transición**: Dado (precondición) → Cuando (acción) → Entonces (consecuencia).
- Un escenario valida **una sola función**.
- Usa una tabla de **Ejemplos** con los **valores límite** de tu regla.

## Ejemplo (de otro negocio, solo para que veas la forma)

Una biblioteca cobra multa por devolver tarde un libro: **0 a 2 días** de retraso no se cobra; **3 días o más** se cobran **$5 por día**.

```gherkin
# language: es
Característica: Multa por devolver tarde un libro

  Esquema del escenario: Calcular la multa según los días de retraso
    Dado que un lector devuelve un libro con <dias> días de retraso
    Cuando la biblioteca calcula la multa
    Entonces la multa es de <multa> pesos

    Ejemplos:
      | dias | multa |
      | 0    | 0     |
      | 2    | 0     |
      | 3    | 15    |
      | 10   | 50    |
```

Fíjate en las filas **2** y **3**: son los **valores límite**, justo donde cambia la regla.

## De escenario a prueba de aceptación (Ejercicio 6)

La tabla de Ejemplos se vuelve un `parametrize`, y cada paso, un comentario:

```python
import pytest
from apartalo.biblioteca import calcular_multa   # ← en tu caso: from apartalo.reglas import ...


@pytest.mark.aceptacion
@pytest.mark.parametrize("dias, multa", [
    (0, 0),
    (2, 0),
    (3, 15),
    (10, 50),
])
def test_multa_por_retraso(dias, multa):
    # Dado que un lector devuelve un libro con <dias> días de retraso
    retraso = dias
    # Cuando la biblioteca calcula la multa
    resultado = calcular_multa(retraso)
    # Entonces la multa es de <multa> pesos
    assert resultado == multa
```

> No necesitas instalar nada para los `.feature`: en esta evidencia son **especificaciones** que tú conviertes a mano en pruebas de pytest.
