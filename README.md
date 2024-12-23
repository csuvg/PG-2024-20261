# Señas Chapinas: Módulo de Procesamiento de Lenguaje Natural

## Descripción del Proyecto

El presente proyecto se centra en la adaptación de un *large language model* (LLM) utilizando la técnica de *fine-tuning*. El propósito de este enfoque es permitir que el modelo GPT-3.5 Turbo detecte y aprenda la gramática de LENSEGUA mediante el análisis de frases ilustrativas. A partir de este aprendizaje, se espera que el modelo pueda recibir palabras asociadas a señas, previamente detectadas por un modelo de visión por computadora, para luego interpretarlas y generar oraciones coherentes en español. La necesidad de esta adaptación se fundamenta en la considerable diferencia gramatical entre la lengua de señas y el español, lo que hace insuficiente la simple detección de señas para una comunicación efectiva.

---

## 1. Características Principales
- Procesamiento avanzado de lenguaje natural adaptado a LENSEGUA.
- Interpretación precisa de frases escritas utilizando un modelo *fine-tuneado*.
- Implementación accesible mediante una API desarrollada con Flask.
- Herramientas adicionales para análisis, generación y preparación de datos.

---

## 2. Instrucciones de Instalación

### Requisitos Previos

Antes de ejecutar la aplicación, asegúrate de tener lo siguiente instalado:
- Python 3.9 o superior.
- Git.
- pip (administrador de paquetes de Python).

### Comandos para Instalar el Proyecto

1. **Clona el repositorio**:

   ```bash
   git clone https://github.com/stefanoaragoni/PG-2024-20261
   ```

2. **Instala las dependencias**:

   ```bash
   cd PG-2024-20261
   pip install -r SenasChapinas_ProcesamientoDeLenguajeNatural/src/requirements.txt
   ```

### Ejecución de la Aplicación

Para iniciar la aplicación Flask e interactuar con la API, sigue los siguientes pasos:

1. Ve a la carpeta que contiene el archivo principal de la página web:

   ```bash
   cd SenasChapinas_ProcesamientoDeLenguajeNatural/src/code/website
   ```
2. Ejecuta el siguiente comando:

   ```bash
   python flask_website.py
   ```
   La página estará disponible en `http://localhost:5000`.


### Herramientas Adicionales


#### Generación de Datos Adicionales:

Durante la preparación de los datos, se desarrolló un script para generar datos adicionales mediante la técnica de *data augmentation*. Para ejecutarlo, abre el notebook ubicado en:

```
SenasChapinas_ProcesamientoDeLenguajeNatural/src/code/data processing/data_augmentation.ipynb
```

#### Preparación del Dataset para *Fine-Tuning*:

Asimismo, se desarrolló un script para preparar el dataset en formato JSONL, necesario para el *fine-tuning* del modelo. Para ejecutarlo, abre el archivo ubicado en:

```
SenasChapinas_ProcesamientoDeLenguajeNatural/src/code/data processing/jsonl_generator.py
```

#### Evaluación del Modelo:

Para evaluar el impacto del *fine-tuning* en el modelo, se desarrolló un script para comparar la calidad de las predicciones antes y después del proceso. Para ejecutarlo, abre el notebook ubicado en:

```
SenasChapinas_ProcesamientoDeLenguajeNatural/src/code/eval/levenshtein_calc.ipynb
```

---

## 3. Demo

En la carpeta `/demo/` encontrarás un video demostrativo que muestra el funcionamiento del proyecto. Puedes acceder a él directamente [aquí](SenasChapinas_ProcesamientoDeLenguajeNatural/demo/Demo.mp4) o utilizando la siguiente ruta relativa:

```
SenasChapinas_ProcesamientoDeLenguajeNatural/demo/Demo.mp4
```


---

## 4. Informe Final
El informe final del proyecto de graduación se encuentra en formato PDF y está almacenado en la carpeta `/docs/`. Puedes acceder a él directamente [aquí](SenasChapinas_ProcesamientoDeLenguajeNatural/docs/Informe.pdf) o utilizando la siguiente ruta relativa:

```
SenasChapinas_ProcesamientoDeLenguajeNatural/docs/Informe.pdf
```


---

## 5. Contacto
Para más información o consultas, por favor contacta a:
- **Nombre:** Stefano Aragoni
- **Email:** ara20261@uvg.edu.gt
- **GitHub:** https://github.com/stefanoaragoni