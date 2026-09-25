import time

palavras_sensiveis = ["religião", "etnia", "biometria", "diagnóstico"]

def classificador(texto):
    encontradas = []
    for palavra in palavras_sensiveis:
        if palavra in texto:
            encontradas.append(palavra)
    return encontradas

if __name__ == "__main__":
    print("Olá! Bem-vindo(a) ao Analisador de Dados!")
    time.sleep(1)
    print("\nEsta ferramenta analisa textos em busca de dados pessoais sensíveis conforme classificados pela Lei Geral de Proteção de Dados (LGPD, Lei nº 13.709/2020).")
    time.sleep(1)
    texto = input("Por favor, insira o texto para análise logo abaixo:\n").lower()
    print("\nObrigada! Estamos analisando...")
    time.sleep(2)
    encontradas = classificador(texto)
    if encontradas:
        print(f"\nEncontramos: {', '.join(encontradas)}")
    else:
        print("\nNenhum dado sensível encontrado! ✅")
    time.sleep(2)
    for palavra in encontradas:
        if palavra == "religião":
            print("\nReligião → crença religiosa é dado sensível pela LGPD (Art. 5º, II). Sua exposição pode gerar discriminação e viola a liberdade de consciência.")
        if palavra == "etnia":
            print("\nEtnia → origem racial ou étnica é dado sensível pela LGPD (Art. 5º, II). Pode expor a pessoa a preconceito e tratamento discriminatório.")
        if palavra == "biometria":
            print("\nBiometria → dado biométrico identifica a pessoa de forma única e irreversível. É sensível pela LGPD (Art. 5º, II) pois não pode ser alterado em caso de vazamento.")
        if palavra == "diagnóstico":
            print("\nDiagnóstico → dado de saúde é sensível pela LGPD (Art. 5º, II). Pode impactar empregabilidade, seguros e gerar estigma social.")
    time.sleep(1)
    print("\n⚠️ Recomendamos revisar o texto antes de compartilhar ou armazenar. Dados sensíveis expostos sem necessidade violam os princípios da LGPD.")
    time.sleep(1)
    print("\nObrigada por usar o Analisador de Dados! Proteger informações sensíveis é responsabilidade de todos. 🛡️")

#Teste: Fui ao médico hoje e recebi meu diagnóstico. Ele pediu também minha biometria para o cadastro.
#Teste: Hoje tive uma reunião de trabalho para discutir o planejamento do próximo trimestre.