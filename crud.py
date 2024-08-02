from flask import Flask, jsonify, request

app = Flask (__name__)

inform = {
    "prescricoes": [
        {
            "id": 1,
            "paciente": "Jo\u00e3o Silva",
            "medico": "Dr. Roberto Oliveira",
            "medicamento": "Amoxicilina",
            "dosagem": "500mg",
            "frequencia": "2x ao dia",
            "duracao": "7 dias",
            "data": "2024-07-28"
        },
        {
            "id": 2,
            "paciente": "Maria Santos",
            "medico": "Dra. Ana Souza",
            "medicamento": "Ibuprofeno",
            "dosagem": "200mg",
            "frequencia": "3x ao dia",
            "duracao": "5 dias",
            "data": "2024-07-29"
        }
    ],
    "relatorios_pacientes": [
        {
            "id": 1,
            "paciente": "Jo\u00e3o Silva",
            "medico": "Dr. Roberto Oliveira",
            "data": "2024-07-28",
            "relatorio": "Paciente com infec\u00e7\u00e3o respirat\u00f3ria. Prescrito antibi\u00f3tico. Recomendada repouso e ingest\u00e3o de l\u00edquidos."
        },
        {
            "id": 2,
            "paciente": "Maria Santos",
            "medico": "Dra. Ana Souza",
            "data": "2024-07-29",
            "relatorio": "Paciente com dores de cabe\u00e7a frequentes. Exames solicitados. Prescrito analg\u00e9sico para dor."
        }
    ],
    "pesquisas_clinicas": [
        {
            "id": 1,
            "titulo": "Estudo sobre os efeitos da Amoxicilina em infec\u00e7\u00f5es respirat\u00f3rias",
            "descricao": "Pesquisa focada em avaliar a efic\u00e1cia da Amoxicilina no tratamento de infec\u00e7\u00f5es respirat\u00f3rias em adultos.",
            "data_inicio": "2024-01-15",
            "data_fim": "2024-12-15"
        },
        {
            "id": 2,
            "titulo": "An\u00e1lise dos efeitos colaterais do Ibuprofeno",
            "descricao": "Estudo observacional sobre os efeitos colaterais comuns do uso prolongado de Ibuprofeno.",
            "data_inicio": "2024-02-01",
            "data_fim": "2024-11-30"
        }
    ],
    "diagnosticos": [
        {
            "id": 1,
            "paciente": "Jo\u00e3o Silva",
            "medico": "Dr. Roberto Oliveira",
            "data": "2024-07-28",
            "diagnostico": "Infec\u00e7\u00e3o respirat\u00f3ria"
        },
        {
            "id": 2,
            "paciente": "Maria Santos",
            "medico": "Dra. Ana Souza",
            "data": "2024-07-29",
            "diagnostico": "Cefaleia"
        }
    ]
}


@app.route('/inform', methods = ['GET'])
def dados_empresa():
   return jsonify (inform)


    #ENDOINTS PRECRICOES
 
#GET
#retorno prescricoes

@app.route('/inform/prescricoes', methods = ['GET'])
def buscar_prescricoes():
    return jsonify(inform["prescricoes"])


# UPDATE
# atualizando prescricoes

@app.route('/inform/prescricoes/<int:id>', methods=['PUT'])
def atualizar_prescricao(id):
        alte_prescricao = request.get_json()
        for prescricao in inform["prescricoes"]:
            if prescricao.get('id') == id:
                prescricao.update(alte_prescricao)
                return jsonify(prescricao)
     
#CREATE
#adicionando nova prescricao

#@app.route('/inform/prescricoes', methods=['POST'])
#def nova_prescricao():
  #  nova_prescricao = request.get_json()  # Capturando os dados da nova prescrição
   # nova_prescricao["id"] = len(inform["prescricoes"]) + 1  # Gerando um ID único para a nova prescrição
    #inform["prescricoes"].append(nova_prescricao)  # Adicionando a nova prescrição à lista
    #return jsonify(nova_prescricao) # Retornando a nova prescrição com o status de criado


    #ENPOINTS RELATORIOS_PACIENTES


#GET
#Retorno relatorios_pacientes

@app.route('/inform/relatorios')
def info_relatorios():
    return jsonify(inform["relatorios_pacientes"])


#UPDATE
#atualizando relatorios_pacientes


# CREATE
#adicionando um novo relaório 

#@app.route('/inform/relatorios', methods = ['POST'])
#def adc_relatorio():
 #   novo_relatorio = request.get_json()
  #  inform["relatorios_pacientes"].append(novo_relatorio)
   # return jsonify(inform["relatorios_pacientes"])


app.run(port= 5000, host= 'localhost', debug= True)
    