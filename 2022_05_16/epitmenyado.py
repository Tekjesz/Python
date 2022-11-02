import pandas as pd
import numpy as np


def beolvasas():
    df  = pd.read_csv("utca.txt", sep = " ", skiprows = 1, names = ["id", "s_name", "h_number", "tax_class", "area"])
    return df

def masodik_feladat(df):
    print(f"A mintában {df.shape[0]} telek szerepel")

def harmadik_feladat(df):
    inp_adoszam = 79906 #int(input("Irjon be egy adószámot"))
    for index, adoszam in enumerate(df.id):
        if adoszam == inp_adoszam:
            print(f"Egy tulajdonos adószáma: {adoszam} {df.s_name[index]} {df.h_number[index]}")
            break
        print("Nem szerepel az adatállományban.")

def ado(df, adosav, alapterulet, epulet):
    for index, adoszam in enumerate(df.id):
        if adoszam == epulet:
            if adosav[index] == "A":
                ado = 800
            elif adosav[index] == "B":
                ado = 600
            else:
                ado = 100
            fizetendo_ado = alapterulet[index] * ado
    return fizetendo_ado

"""def otodik_feladat(df):
    tax_class_num = {"A" : 0,
                     "B" : 0,
                     "C" : 0}
    tax_overall = {"A" : 0,
                   "B" : 0,
                   "C" : 0}
    for index, osztaly in enumerate(df.tax_class):
        
        if osztaly == "A":
                tax_class_num["A"] += 1 #number of tax payers
                tax_overall["A"] += ado(df, df.tax_class, df.area, df.id[index])   #calculate and add the tax
        elif osztaly == "B":
                tax_class_num["B"] += 1 #number of tax payers
                tax_overall["B"] += ado(df, df.tax_class, df.area, df.id[index])   #calculate and add the tax
        elif osztaly == "C":
                tax_class_num["C"] += 1 #number of tax payers
                tax_overall["C"] += ado(df, df.tax_class, df.area, df.id[index])   #calculate and add the tax
    print(f"A sávba {tax_class_num["A"]} telek esik, az adó {tax_overall["A"]} Ft.\n B sávba {tax_class_num["B"]} telek esik, az adó {tax_overall["B"]} Ft.\n C sávba {tax_class_num["C"]} telek esik, az adó {tax_overall["C"]} Ft.")
"""
def hatodik_feladat(df):
    mask = df.duplicated(keep = False)
        
        



if __name__ == "__main__":
    df = beolvasas()
    masodik_feladat(df)
    harmadik_feladat(df)
    #TODO building (int)
    building = 79906
    fizetendo_ado = ado(df, df.tax_class, df.area, building)
    """ossz_ado = otodik_feladat(df)"""
    hatodik_feladat(df)
