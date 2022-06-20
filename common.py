import os
# ------------------------------------------------------------------
def get_channel_name_by_code(channel_code):
    return {
        "c192": "TF1",
        "c4": "France 2",
        "c80": "France 3",
        "c34": "Canal+",
        "c47": "France 5",
        "c118": "M6",        
        "c111": "Arte",
        "c445": "C8",
        "c119": "W9",
        "c195": "TMC",
        "c446": "TFX",
        "c444": "NRJ 12",
        "c78": "France 4",
        "c234": "La Chaîne parlementaire",
        "c481": "BFMTV",
        "c226": "CNEWS",
        "c458": "CSTAR",
        "c482": "Gulli",
        "c1404": "TF1 Séries Films",
        "c1401": "L'Equipe",
        "c1403": "6ter",
        "c1402": "RMC Story",
        "c1400": "RMC Découverte",
        "c1399": "Chérie 25",
        "c112": "LCI",
        "c2111": "Franceinfo"
    }.get(channel_code, "c00")
# ------------------------------------------------------------------
def check_file(file_name, path_name):    
    for _, _, files in os.walk(path_name):
        for name in files:            
            if(name.strip() == file_name):
                return True
    return False
# ------------------------------------------------------------------
def map_channel(channel_code):
    return {
        "c192": "c0",
        "c4": "c1",
        "c80": "c2", 
        "c111": "c3",
        "c234": "c4",
        "c481": "c5",
        "c226": "c6",
        "c2111": "c7"      
    }.get(channel_code, "c")
# ------------------------------------------------------------------
