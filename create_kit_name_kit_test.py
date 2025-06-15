import sender_stand_request
import data

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

#Prueba positiva
def positive_assert(name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == name


#Prueba negativa
def negative_assert_code_400(name):
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400

#Prueba 1. Crear kit "name" 1 caracter
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")

#Prueba 2. Crear kit "name" 511 caracteres
def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd \ "
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda \ "
                    "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabc \ "
                    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc \ "
                    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda \ "
                    "bcdabcdabcdabcdabcdabC")

#Prueba 3. Error "name" contiene 0 caracteres
def test_create_kit_0_letter_in_name_get_error_response():
    negative_assert_code_400("")

#Prueba 4. Error "name" contiene 512 caracteres
def test_create_kit_512_letter_in_name_get_error_response():
    negative_assert_code_400("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda \ "
                             "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab \ "
                             "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc \ "
                             "dAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd \ "
                             "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda \ "
                             "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

#Prueba 5. Se permiten caracteres especiales
def test_create_kit_has_special_symbol_in_name_get_success_response():
    positive_assert("°%@,")

#Prueba 6. Se permiten espacios
def test_create_kit_has_space_in_name_get_success_response():
    positive_assert(" A Aaa ")

#Prueba 7. Se permiten números
def test_create_kit_has_numbers_in_name_get_success_response():
    positive_assert("123")

#Función prueba negativa
def negative_assert_no_name(name, respose):
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert respose.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["messsage"] == "No se han aprobado todos los parámetros requeridos" \
                                          "El nombre debe contener sólo letras latino, un espacio y un guión. De 2 a 15 caracteres"

#Prueba 8. La solicitud no contiene el parámetro "name"
def test_create_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_no_name(kit_body)

#Prueba 9. El parámetro "name" es un número
def test_create_kit_number_type_name_get_error_response():
    kit_body = get_kit_body(123)
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400