from flask import Flask, request, render_template_string, session
import os
from openai import OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET KEY", "clave secreta")

class CCCResuelve:
    def __init__(self):
        self.materia = None
        self.paso = 0

    def iniciar(self, materia):
        self.materia = materia.lower()
        self.paso = 1
        return self.guia()

    class CCCResolve:
    def __init__(self):
        self.paso = 1

    def guia(self, pregunta):
        respuesta = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Eres CCCResolve, un tutor que ayuda a estudiantes sin hacerles la tarea completa. Explica paso a paso y haz preguntas."
                },
                {
                    "role": "user",
                    "content": pregunta
                }
            ],
            temperature=0.7
        )

        return respuesta.choices[0].message.content

    def matematicas(self, respuesta):
        if self.paso == 1:
            self.paso = 2
            return "📐 ¿Qué datos te da el problema? (números, variables, etc.)"
        if self.paso == 2:
            self.paso = 3
            return "🧠 ¿Qué variable necesitas encontrar?"
        if self.paso == 3:
            self.paso = 4
            return "🔍 ¿Qué regla o fórmula podrías usar?"
        return "¡Perfecto! Ahora intenta resolverlo con esos pasos y dime qué te falta."

    def fisica(self, respuesta):
        if self.paso == 1:
            self.paso = 2
            return "🧲 ¿Qué fenómeno ocurre? (movimiento, fuerza, energía, etc.)"
        if self.paso == 2:
            self.paso = 3
            return "📏 ¿Qué magnitudes conoces? (velocidad, masa, tiempo, etc.)"
        if self.paso == 3:
            self.paso = 4
            return "⚙️ ¿Qué ley física se relaciona con esto?"
        return "¡Excelente! Con eso ya puedes armar la solución paso a paso."

    def quimica(self, respuesta):
        if self.paso == 1:
            self.paso = 2
            return "⚗️ ¿Es una reacción o un cálculo?"
        if self.paso == 2:
            self.paso = 3
            return "🧪 ¿Qué sustancias participan?"
        if self.paso == 3:
            self.paso = 4
            return "🔍 ¿Qué concepto químico se aplica aquí?"
        return "¡Listo! Ahora intenta resolverlo con esos datos y dime si te queda duda."

    def historia(self, respuesta):
        if self.paso == 1:
            self.paso = 2
            return "📜 ¿En qué periodo ocurrió?"
        if self.paso == 2:
            self.paso = 3
            return "🧠 ¿Cuáles fueron las causas?"
        if self.paso == 3:
            self.paso = 4
            return "📌 ¿Qué consecuencias tuvo?"
        return "¡Muy bien! Con eso ya puedes hacer un resumen histórico completo."

ccc = CCCResuelve()

html = """
<!DOCTYPE html>
<html>
<head>
    <title>CCCResuelve Chat</title>
    <style>
        body {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(135deg, #1f3b7a, #2b7a78);
            color: #fff;
            text-align: center;
            margin: 0;
            padding: 0;
        }
        h1 { margin-top: 20px; font-size: 38px; }
        p { font-size: 18px; }
        .chatbox {
            width: 80%;
            max-width: 900px;
            height: 350px;
            margin: 20px auto;
            background: rgba(255, 255, 255, 0.12);
            border-radius: 15px;
            padding: 15px;
            overflow-y: scroll;
        }
        .chatbox p { text-align: left; margin: 8px 0; }
        .user { color: #ffeb3b; }
        .bot { color: #a8ffb0; }
        select, textarea {
            width: 80%;
            max-width: 600px;
            padding: 12px;
            border-radius: 10px;
            border: none;
            font-size: 16px;
        }
        textarea { height: 80px; resize: none; }
        button {
            margin-top: 10px;
            padding: 12px 25px;
            border-radius: 10px;
            border: none;
            font-size: 16px;
            cursor: pointer;
            background: #ffd166;
            color: #1f3b7a;
            font-weight: bold;
        }
    </style>
</head>
<body>

<h1>CCCResuelve 🤖</h1>
<p>Chat educativo (preparatoria)</p>

<div class="chatbox">
    {% for msg in historial %}
        <p class="{{ 'user' if msg[0]=='Tú' else 'bot' }}">
            <b>{{ msg[0] }}:</b> {{ msg[1] }}
        </p>
    {% endfor %}
</div>

<form method="post">
    <select name="materia">
        <option value="">Selecciona materia</option>
        <option value="matematicas">Matemáticas</option>
        <option value="fisica">Física</option>
        <option value="quimica">Química</option>
        <option value="historia">Historia</option>
    </select><br><br>

    <textarea name="pregunta" placeholder="Escribe tu duda o respuesta..." required></textarea><br><br>

    <button type="submit">Enviar</button>
</form>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"] 
        
def index():
    if "historial" not in session:
        session["historial"] = []
    historial = session["historial"]

    if request.method == "POST":
        materia = request.form["materia"]
        pregunta = request.form["pregunta"]

        historial.append(("Tú", pregunta))

        if materia != "":
            respuesta = ccc.iniciar(materia)
        else:
            respuesta = ccc.guia(pregunta)

        historial.append(("CCCResuelve", respuesta))
        session["historial"] = hustorial 

    return render_template_string(html, historial=historial)

if __name__ == "__main__":
    app.run(debug=True)
