from previsao import get_coordenadas, get_previsao
from exportar import exportar_pdf

alto_contraste = False
texto_maiusculo = False
cor_atual = "\033[32m"
cor_anterior = "\033[32m"
reset = "\033[0m"

CORES = {
    "1": "\033[32m",  # verde
    "2": "\033[34m",  # azul
    "3": "\033[35m",  # roxo
    "4": "\033[33m",  # amarelo
}

def formatar(texto):
    if texto_maiusculo:
        return texto.upper()
    return texto

while True:
    print(cor_atual)
    print("=" * 38)
    print(formatar("       PREVISÃO DO TEMPO"))
    print("=" * 38)
    print(formatar("  1 - Digite uma cidade"))
    print(formatar("  2 - Mudar cor do terminal"))
    print(formatar("  3 - Acessibilidade"))
    print(formatar("  4 - Sair do programa"))
    print("=" * 38)
    opcao = input(formatar("Escolha uma opção: "))

    if opcao == "1":
        cidade = input(formatar("Digite o nome da cidade: "))
        local = get_coordenadas(cidade)
        if not local:
            print(formatar("Cidade não encontrada!"))
            continue
        data = get_previsao(local["latitude"], local["longitude"])
        datas = data["daily"]["time"]
        maximas = data["daily"]["temperature_2m_max"]
        minimas = data["daily"]["temperature_2m_min"]
        media = sum(maximas + minimas) / (len(maximas) + len(minimas))
        print(f"\n{'=' * 38}")
        print(formatar(f"  Previsão para: {local['name']}, {local.get('country', '')}"))
        print(f"{'=' * 38}")
        print(formatar(f"  Periodo: {datas[0][5:]} a {datas[-1][5:]}"))
        print(formatar(f"  Temperatura média: {media:.1f}°C"))
        print(formatar(f"  Máxima do periodo: {max(maximas)}°C ({datas[maximas.index(max(maximas))][5:].replace('-','/')})"))
        print(formatar(f"  Mínima do periodo: {min(minimas)}°C ({datas[minimas.index(min(minimas))][5:].replace('-','/')})"))
        print(f"{'-' * 40}")
        for i in range(len(datas)):
            data_fmt = datas[i][5:].replace("-", "/")
            print(formatar(f"  {data_fmt}  Min: {minimas[i]}°C  Max: {maximas[i]}°C"))
        print(f"{'=' * 38}\n")
        salvar = input(formatar("Deseja exportar para PDF? (s/n): "))
        if salvar == "s":
            exportar_pdf(local["name"], local.get("country", ""), datas, maximas, minimas, media)

    elif opcao == "2":
        if alto_contraste:
            print(formatar("Desative o alto contraste primeiro!"))
        else:
            print(formatar("Escolha uma cor:"))
            print(formatar("  1 - Verde"))
            print(formatar("  2 - Azul"))
            print(formatar("  3 - Roxo"))
            print(formatar("  4 - Amarelo"))
            escolha = input(formatar("Opção: "))
            if escolha in CORES:
                cor_atual = CORES[escolha]
                print(formatar("Cor alterada!"))
            else:
                print(formatar("Opção inválida!"))

    elif opcao == "3":
        print(formatar("1 - Alto Contraste (on/off)"))
        print(formatar("2 - Texto Maiusculo (on/off)"))
        escolha = input(formatar("Opção: "))
        if escolha == "1":
            alto_contraste = not alto_contraste
            if alto_contraste:
                cor_anterior = cor_atual
                cor_atual = "\033[97m\033[40m"
            else:
                cor_atual = cor_anterior
                print(reset)
            print(formatar("Alto contraste ativado!" if alto_contraste else "Alto contraste desativado!"))
        elif escolha == "2":
            texto_maiusculo = not texto_maiusculo
            print(formatar("Texto maiúsculo ativado!" if texto_maiusculo else "Texto maiúsculo desativado!"))

    elif opcao == "4":
        print(f"Saindo...{reset}")
        break

    else:
        print(formatar("Opção inválida!"))
