import pandas as pd
import datetime as dt
import re



import datetime


# def format_date(value):
#     # If the value is of type datetime.datetime, convert it to the desired format
#     if isinstance(value, datetime.datetime):
#         return value.strftime('%d/%m/%Y')
#
#     # Try to extract date from strings with the pattern 'Sí ...'
#     if isinstance(value, str) and 'Sí' in value:
#         date_part = value.split('Sí')[-1].strip()
#         try:
#             # Convert the extracted date to datetime and then to desired format
#             date_obj = datetime.datetime.strptime(date_part, '%d/%m/%Y')
#             return date_obj.strftime('%d/%m/%Y')
#         except ValueError:
#             pass
#
#     # If neither of the above cases, return the value as is
#     return value
# # Leer el archivo de Excel
#



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


# df_original = pd.read_excel("C:/Users/rodri/Desktop/2023-09-12-BDD GENALOGIA.xlsx", header = 0,
#                             engine="openpyxl",
#                             converters = {"Declaratoria":str})

df_original = pd.read_csv("C:/Users/rodri/Desktop/2023-09-12-BDD GENALOGIA CSV.csv")



df_original["Declaratoria"] = df_original["Declaratoria"].apply(format_date)

# Aplicar las funciones de limpieza refinadas a las columnas completas
df_original["Declaratoria"] = df_original["Declaratoria"].apply(refined_clean_declaratoria)
df_original["Declaratoria"] = df_original["Declaratoria"].apply(refined_clean_zmh)
#df_original["Declaratoria"] = df_original["Declaratoria"].dt.strftime('%d/%m/%Y')
df_original["Declaratoria"] = df_original["Declaratoria"].apply(clean_unesco)

#df_original["ZMH"] = df_original["ZMH"].apply(refined_clean_declaratoria)
df_original["ZMH"] = df_original["ZMH"].apply(refined_clean_zmh)
df_original["ZMH"] = df_original["ZMH"].apply(clean_unesco)
#df_original["ZMH"] = df_original["ZMH"].dt.strftime('%d/%m/%Y')

df_original["Unesco"] = df_original["Unesco"].apply(clean_unesco)




# Guardar el DataFrame limpio en un archivo Excel
#output_excel_path_final_refined = "/path/to/save/cleaned_data_final_refined.xlsx"
df_original.to_csv("TempChofFin.csv", index=False, encoding='utf-8', date_format="%s")
#df_original.to_excel("TempChofFin2.xlsx", index=False, encoding='utf-8', date_format="%d%m%Y")
