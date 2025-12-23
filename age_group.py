def get_age_group(age):
    if age < 0 or age > 150:
        return 'desconocido'
    if 0 <= age <= 14:
        return 'infancia'
    elif 15 <= age <= 24:
        return 'juventud'
    elif 25 <= age <= 64:
        return 'adulto'
    elif age >= 65:
        return 'vejez'  # Para edades negativas o mayores a 150

def test_get_age_group():
    """Prueba unitaria para get_age_group"""
    assert get_age_group(-1) == 'desconocido'
    assert get_age_group(0) == 'infancia'
    assert get_age_group(14) == 'infancia'
    assert get_age_group(15) == 'juventud'
    assert get_age_group(24) == 'juventud'
    assert get_age_group(25) == 'adulto'
    assert get_age_group(64) == 'adulto'
    assert get_age_group(65) == 'vejez'
    assert get_age_group(80) == 'vejez'
    assert get_age_group(150) == 'desconocido'

# Para ejecutar las pruebas
test_get_age_group()
print("Todas las pruebas pasaron correctamente.")