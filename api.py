from fastapi import FastAPI
from fastapi.responses import FileResponse
import os
from previsao import get_coordenadas, get_previsao
from exportar import exportar_pdf

app = FastAPI(title="Previsão do Tempo API")

ultimo_dados = {}

@app.get("/previsao/{cidade}")
def previsao(cidade: str):
    local = get_coordenadas(cidade)
    if not local:
        return {"erro": "Cidade não encontrada"}
    data = get_previsao(local["latitude"], local["longitude"])
    datas = data["daily"]["time"]
    maximas = data["daily"]["temperature_2m_max"]
    minimas = data["daily"]["temperature_2m_min"]
    media = sum(maximas + minimas) / (len(maximas) + len(minimas))

    ultimo_dados["local"] = local
    ultimo_dados["datas"] = datas
    ultimo_dados["maximas"] = maximas
    ultimo_dados["minimas"] = minimas
    ultimo_dados["media"] = media

    return {
        "cidade": local["name"],
        "pais": local.get("country", ""),
        "previsao": [
            {"data": datas[i], "min": minimas[i], "max": maximas[i]}
            for i in range(len(datas))
        ]
    }

@app.get("/previsao/{cidade}/pdf")
def previsao_pdf(cidade: str):
    if not ultimo_dados:
        return {"erro": "Consulte uma cidade primeiro!"}
    
    local = ultimo_dados["local"]
    datas = ultimo_dados["datas"]
    maximas = ultimo_dados["maximas"]
    minimas = ultimo_dados["minimas"]
    media = ultimo_dados["media"]

    exportar_pdf(local["name"], local.get("country", ""), datas, maximas, minimas, media)
    nome_arquivo = f"previsao_{local['name'].lower().replace(' ', '_')}.pdf"
    return FileResponse(nome_arquivo, media_type="application/pdf", filename=nome_arquivo)
