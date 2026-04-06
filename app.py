print(">>> THIS IS THE CORRECT APP.PY <<<")
from flask import Flask, render_template, request, send_from_directory
from conversions import (
    mm_to_cm, cm_to_mm, cm_to_m, m_to_cm,
    inch_to_mm, mm_to_inch,
    g_to_kg, kg_to_g,
    c_to_f, f_to_c
)


app = Flask(__name__)

@app.route('/service-worker.js')
def service_worker():
    return send_from_directory('.', 'service-worker.js', mimetype='application/javascript')

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        value = float(request.form["value"])
        conversion = request.form["conversion"]

        if conversion == "mm_to_cm":
            result = mm_to_cm(value)
        elif conversion == "cm_to_mm":
            result = cm_to_mm(value)
        elif conversion == "cm_to_m":
            result = cm_to_m(value)
        elif conversion == "m_to_cm":
            result = m_to_cm(value)
        elif conversion == "inch_to_mm":
            result = inch_to_mm(value)
        elif conversion == "mm_to_inch":
            result = mm_to_inch(value)
        elif conversion == "g_to_kg":
            result = g_to_kg(value)
        elif conversion == "kg_to_g":
            result = kg_to_g(value)

        elif conversion == "c_to_f":
            result = c_to_f(value)
        elif conversion == "f_to_c":
            result = f_to_c(value)
    return render_template("index.html", result=result)

app.run(host="0.0.0.0", port=5000, debug=True)





