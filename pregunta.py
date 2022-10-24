"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    # df = pd.read_csv("C:/Users/jlopezl/OneDrive - Renting Colombia S.A/Archivos/Personal/Especialización/Ciencia de los datos/data-cleaning-solicitudes-credito-JuanesLopez/solicitudes_credito.csv", sep=";")
    #
    # Inserte su código aquí
    #
    df.dropna(inplace=True)
    df.drop(['Unnamed: 0'], axis=1, inplace=True)
    
    df.sexo = df.sexo.str.lower()
    
    df.tipo_de_emprendimiento = df.tipo_de_emprendimiento.str.lower()
    
    df.idea_negocio = [i.strip() for i in df.idea_negocio]
    df.idea_negocio = df.idea_negocio.str.replace("-"," ")
    df.idea_negocio = df.idea_negocio.str.replace("_"," ")
    df.idea_negocio = df.idea_negocio.str.lower()
    
    df.barrio = [str(i).strip() for i in df.barrio]
    df.barrio = df.barrio.str.replace("-"," ")
    df.barrio = df.barrio.str.replace("_"," ")
    df.barrio = df.barrio.str.lower()
    
    
    df.fecha_de_beneficio = pd.to_datetime(df.fecha_de_beneficio)
    df.fecha_de_beneficio = df.fecha_de_beneficio.astype('datetime64[ns]')
    
    df.monto_del_credito = df.monto_del_credito.str.replace("%","")
    df.monto_del_credito = df.monto_del_credito.str.replace("$","")
    df.monto_del_credito = df.monto_del_credito.str.replace(",","")
    df.monto_del_credito = df.monto_del_credito.str.replace(".00","") 
    df.monto_del_credito = [i.strip() for i in df.monto_del_credito]
    
    df.línea_credito = df.línea_credito.str.replace("-"," ")
    df.línea_credito = df.línea_credito.str.replace("_"," ")
    df.línea_credito = df.línea_credito.str.lower()
    df.línea_credito = [i.strip() for i in df.línea_credito]
    
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)

    return df
