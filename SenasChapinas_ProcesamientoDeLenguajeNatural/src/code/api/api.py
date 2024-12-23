from flask import Flask, request, jsonify
from openai import OpenAI

# Flask API definition
app = Flask(__name__)

# API endpoint for the model
@app.route('/api/generar', methods=['POST'])
def generar():
    # OpenAI API client gets initialized with the API key
    client = OpenAI(
        api_key=''
    )

    try:

        # Receives the input text from the request
        data = request.get_json()
        input_text = data.get('texto', '')

        # Validates the input text
        if not input_text:
            return jsonify({'error': 'No se proporcionó ningún texto.'}), 400

        # Calls the OpenAI API to generate the response
        respuesta = client.chat.completions.create(
            model="ft:gpt-3.5-turbo-0125:personal:lensegua-16-02-2:9wdLYfpx",
            messages=[
                {"role": "system", "content": 'Eres un intérprete experto en Lengua de Señas de Guatemala (LENSEGUA). El usuario te proporcionará frases en español escritas utilizando la gramática de LENSEGUA. Tu tarea es interpretarlas y convertirlas en español gramaticalmente correcto, teniendo en cuenta las siguientes reglas específicas: 1. No debes interpretar las frases como preguntas, ni agregar una entonación interrogativa, a menos que incluyan las palabras "pregunta" o "sí o no". 2. Las palabras “pasado”, “futuro” y “antes” indican la conjugación verbal. Debes conjugar correctamente los verbos en tu respuesta sin incluir las palabras “pasado”, “futuro” o “antes”. 3. La frase “carro mucho” debe interpretarse como “tráfico”. 4. La frase “bien mucho” debe interpretarse como “muy bien”. 5. Mantén el orden de los elementos de la interpretación final lo más similar posible al texto original cuando sea gramaticalmente válido en español. Por ejemplo, si la frase en LENSEGUA es "Por favor cuando tu salir luz apagar", la interpretación debe ser "Por favor cuando salgas apaga la luz" en lugar de "Por favor apaga la luz cuando salgas".'},
                {"role": "user", "content": input_text}
            ],
            max_tokens=150
        )

        # Extracts the generated text from the response
        texto_generado = respuesta.choices[0].message.content


        # Returns the generated text as the response
        return jsonify({'respuesta': texto_generado})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Initializes the Flask API
if __name__ == '__main__':
    app.run(debug=True)