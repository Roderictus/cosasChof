import pandas as pd
import re

# Leer el archivo de Excel
df_original = pd.read_excel("C:/Users/rodri/Desktop/2023-09-12-BDD GENALOGIA.xlsx")

# Leer el archivo original

# Funciones de limpieza refinadas
def refined_clean_declaratoria(cell):
    matches = re.findall(r'(\d{1,2}/\d{1,2}/\d{4})', str(cell))
    return matches[0] if matches else cell

def refined_clean_zmh(cell):
    matches = re.findall(r'\((\d{1,2}/\d{1,2}/\d{4})\)', str(cell))
    return matches[0] if matches else cell

def clean_unesco(cell):
    return "" if cell == 0 or str(cell) == "0" else cell

# Aplicar las funciones de limpieza refinadas a las columnas completas
#df_original["Declaratoria"] = df_original["Declaratoria"].apply(refined_clean_declaratoria)
df_original["Declaratoria"] = df_original["Declaratoria"].apply(refined_clean_zmh)

df_original["Declaratoria"] = df_original["Declaratoria"].strftime('%d/%m/%Y')
df_original["Declaratoria"] = df_original["Declaratoria"].apply(clean_unesco)
#df_original["ZMH"] = df_original["ZMH"].apply(refined_clean_declaratoria)
df_original["ZMH"] = df_original["ZMH"].apply(refined_clean_zmh)

df_original["ZMH"] = df_original["ZMH"].apply(clean_unesco)
df_original["ZMH"] = df_original["ZMH"].strftime('%d/%m/%Y')
df_original["Unesco"] = df_original["Unesco"].apply(clean_unesco)

# Guardar el DataFrame limpio en un archivo Excel
#output_excel_path_final_refined = "/path/to/save/cleaned_data_final_refined.xlsx"
df_original.to_csv("tempChof2.csv", index=False, encoding='utf-8')
