import sender_stand_request4
import data
from create_user_test import get_user_body


# Función de prueba positiva
def negative_assert_symbol(first_name):
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    user_body = get_user_body(first_name)
    # El resultado de la solicitud para crear un/a nuevo/a usuario/a se guarda en la variable user_response
    response = sender_stand_request4.post_new_user(user_body)

    # Comprueba si la respuesta contiene el codigo 400
    assert response.status_code == 400
    # Comprueba si el atributo "code" en el cuerpo de respuesta es 400.
    assert response.json()["code"] == 400
    # Comprueba si el atributo "message" en el cuerpo de respuesta se ve así:
    assert response.json()["message"] == "El nombre que ingresaste es incorrecto. " \
                                          "Los nombres solo pueden contener caracteres latinos,  " \
                                          "los nombres deben tener al menos 2 caracteres y no más de 15 caracteres"



# Prueba 6. Error
# El parámetro "firstName" contiene un string de caracteres especiales
def test_create_user_has_special_symbol_in_first_name_get_error_response():
    negative_assert_symbol("\"№%@\",")
