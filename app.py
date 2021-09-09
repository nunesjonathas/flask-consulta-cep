from flask import Flask, jsonify, render_template, request
from zeep import Client

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


# def consultar_cep():
#     client = Client(
#         "https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl"
#     )
#     data = client.service.consultaCEP(request.form.get("vapNuEtiquetaEncomenda"))
#     data = data.__dict__

#     return jsonify(data["__values__"])


@app.route("/consultar-cep", methods=["POST"])
def consultar_cep():
    client = Client("https://correios.contrateumdev.com.br/api/rastreio")
    data = client.service.consultaCEP(request.form.post("LB249234094HK"))
    data = data.__dict__

    return jsonify(data["__values__"])


@app.errorhandler(404)
def page_not_found(err):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(err):
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run()
