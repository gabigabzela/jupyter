
import requests
import json

url = 'http://localhost:11434/api/generate'

data = {
    "model": "gemma3:4b",
    "prompt": "Dime un chiste.",
    "stream": False
}

# Encabezados de la solicitud
headers = {
    'Content-Type': 'application/json'
}

try:
    # Envía la solicitud POST a la API
    response = requests.post(url, data=json.dumps(data), headers=headers)

    # Verifica si la solicitud fue exitosa
    if response.status_code == 200:
        # Analiza la respuesta JSON
        respuesta_json = response.json()
        
        # Extrae el texto de la respuesta del modelo
        # La respuesta completa está en la clave 'response'
        texto_generado = respuesta_json.get('response', 'No se encontró la respuesta.')
        print("Respuesta generada por Ollama:")
        print(texto_generado)
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

except requests.exceptions.RequestException as e:
    print(f"Error de conexión: {e}")