import pandas as pd

# 1. Carregamento da base estruturada de vacinação (Carapicuíba/SP)
arquivo_excel = "Dashboard_Vacinacao_Carapicuiba_UNINTER.xlsx"
df = pd.read_excel(arquivo_excel, sheet_name="Base_Dados")

print("=== RESUMO DA BASE DE DADOS DE VACINAÇÃO - CARAPICUÍBA/SP ===")
print(f"Total de registros analisados: {len(df)}")

# 2. Consolidação de doses aplicadas por imunizante
resumo_vacinas = (
    df.groupby("Imunizante")[["Doses_Aplicadas", "Meta_Estimada"]]
    .sum()
    .reset_index()
)
resumo_vacinas["Cobertura_%"] = (
    (resumo_vacinas["Doses_Aplicadas"] / resumo_vacinas["Meta_Estimada"]) * 100
).round(2)

print("\n--- Cobertura por Imunizante ---")
print(resumo_vacinas.to_string(index=False))

# 3. Consolidação de atendimentos por Unidade Básica de Saúde (UBS)
resumo_ubs = (
    df.groupby("UBS")["Doses_Aplicadas"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

print("\n--- Total de Doses por UBS ---")
print(resumo_ubs.to_string(index=False))

# 4. Exportação da tabela tratada para auditoria
resumo_vacinas.to_csv("resumo_cobertura_carapicuiba.csv", index=False, encoding="utf-8-sig")
print("\nProcessamento concluído com sucesso! Arquivo CSV gerado.")