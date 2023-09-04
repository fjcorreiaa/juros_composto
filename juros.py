valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())

def calcular_valor_final(valor_inicial, taxa_juros, periodo):
  valor_final = valor_inicial * ((1 + taxa_juros)** periodo)
  return valor_final

resultado = calcular_valor_final(valor_inicial, taxa_juros, periodo)

print(f"Valor final do investimento: R$ {resultado:.2f}")
