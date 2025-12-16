import pytest
# ✅ 1. Si el nombre coincide con un fixture registrado → es un fixture
@pytest.fixture
def usuario():
    return {"nombre": "Alejandro"}
# Ahora Pytest sabe que existe un fixture llamado usuario.

# Entonces, si ve:

# python
# def test_algo(usuario):
#     ...
# Pytest piensa:

# “Ah, usuario es un fixture. Lo tengo que ejecutar y pasar su valor al test.”

#######################################################

# ✅ 2. Si NO coincide con un fixture → es un parámetro normal de Python
# def test_suma(a, b):
#     assert a + b == 3
# Si no existen fixtures llamados a o b, Pytest no sabe qué hacer y falla:

# Código
# fixture 'a' not found
# Porque Pytest asume que todo argumento de un test es un fixture, 
# salvo que sea un fixture parametrizado con @pytest.mark.parametrize.

#######################################################
# ✅ 3. ¿Y cómo sabe si es un parámetro de parametrize?
@pytest.mark.parametrize("a, b", [(1, 2), (3, 4)])
def test_suma(a, b):
    ...
# Aquí Pytest ve:

# parametrize declara explícitamente que a y b son parámetros, no fixtures.

# Entonces Pytest hace:

# Detecta que a y b vienen de parametrize.

# No intenta buscarlos como fixtures.

# Los pasa directamente al test.

#######################################################
# ✅ 4. ¿Y el famoso request?
# request es un fixture especial que Pytest provee automáticamente.

def mi_fixture(request):
    ...
# Pytest piensa:

# “Ah, request es un fixture interno mío. Lo inyecto.”

# No tenés que declararlo. Pytest ya lo conoce.

#######################################################

# ✅ 5. ¿Y si es un callback?

def helper():
    return 123

def test_algo(helper):
    helper()

# ojo pq no le podemos pasar funciones normales como argumentos
def helper():
    return 123

def test_algo(helper):
    pass
# Pytest NO usa funciones normales como fixtures.

# Si no existe un fixture llamado helper

# Y no está en parametrize

# fixture 'helper' not found
# Porque Pytest no mira funciones normales para resolver fixtures.

#######################################################

# ✅ 6. ¿Cómo Pytest decide el orden de resolución?
# Pytest sigue este orden:

# ¿El argumento está declarado en parametrize? → ✅ Es un parámetro.

# ¿Existe un fixture con ese nombre? → ✅ Es un fixture.

# ¿Es un fixture interno de Pytest (como request)? → ✅ Lo inyecto.

# Si nada coincide → ❌ Error: “fixture not found”.