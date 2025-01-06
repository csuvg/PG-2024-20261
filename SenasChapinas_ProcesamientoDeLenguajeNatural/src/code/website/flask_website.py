from flask import Flask, render_template, request
from openai import OpenAI

# Flask API definition
app = Flask(__name__)

# Variable global para almacenar el historial de mensajes
chat_history = []

# Ruta para la página principal
@app.route('/')
def index():
    return render_template('index.html', chat_history=chat_history)

# Ruta para procesar la entrada del usuario
@app.route('/chat', methods=['POST'])
def chat():
    global chat_history

    # OpenAI API client gets initialized with the API key
    client = OpenAI(
        api_key=''
    )

    try:

        # Obtener el texto ingresado por el usuario y la selección del modelo
        input_text = request.form['user_input']
        selected_model = request.form['model_selection']

        # Agregar el mensaje del usuario al historial
        chat_history.append({"role": "user", "model":selected_model, "content": input_text})

        # Llamada a la API de OpenAI según el modelo seleccionado
        if selected_model == "lensegua":
            print("Modelo seleccionado: LENSEGUA")
            # Chatbot personalizado LENSEGUA
            respuesta = client.chat.completions.create(
                model="ft:gpt-3.5-turbo-0125:personal:lensegua-16-02-2:9wdLYlLV:ckpt-step-262",
                messages=[
                    {"role": "system", "content": "Eres un intérprete experto en Lengua de Señas de Guatemala (LENSEGUA). El usuario te proporcionará frases en español escritas utilizando la gramática de LENSEGUA. Tu tarea es interpretarlas y convertirlas en español gramaticalmente correcto, teniendo en cuenta las siguientes reglas específicas: Las palabras “pasado”, “futuro” y “antes” indican la conjugación verbal. Debes conjugar correctamente los verbos en tu respuesta sin incluir las palabras “pasado”, “futuro” o “antes”. La frase “carro mucho” debe interpretarse como “tráfico”. La frase “bien mucho” debe interpretarse como “muy bien”. Si una frase incluye las palabras “pregunta” o “si o no”, se interpreta como una pregunta. De lo contrario, las frases no son preguntas"},
                    {"role": "user", "content": input_text}
                ],
                max_tokens=150
            )
        else:
            # ChatGPT 3.5 turbo básico
            print("Modelo seleccionado: GPT-3.5 Turbo")
            respuesta = client.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                messages=[
                    {"role": "system", "content": "Eres un intérprete experto en Lengua de Señas de Guatemala (LENSEGUA). El usuario te proporcionará frases en español escritas utilizando la gramática de LENSEGUA. Tu tarea es interpretarlas y convertirlas en español gramaticalmente correcto."},
                    {"role": "user", "content": input_text}
                ],
                max_tokens=150
            )

        # Extracts the generated text from the response
        texto_generado = respuesta.choices[0].message.content

        print(input_text)
        print(texto_generado, "\n")

        # Agregar la respuesta del bot al historial
        chat_history.append({"role": "bot", "model":selected_model, "content": texto_generado})

        # Retornar la página con el historial actualizado
        return render_template('index.html', chat_history=chat_history)
    

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)