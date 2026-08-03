import pandas as pd
import json

def clean_num(val):
    if pd.isna(val):
        return 0
    if isinstance(val, (int, float)):
        return val
    s = str(val).replace('bu/ft', '').replace('bu', '').replace('"', '').replace("'", '').replace(',', '').strip()
    try:
        return float(s)
    except:
        return 0

def convert():
    # Load physical bin specs CSV
    df = pd.read_csv('data/bin_specs.csv')
    df = df.dropna(subset=['Bin ID'])
    
    js_entries = []
    for idx, row in df.iterrows():
        bin_id = str(row['Bin ID']).strip()
        brand = str(row['Brand / Model']).strip() if pd.notna(row['Brand / Model']) else '-'
        dim_raw = str(row['Diameter']).strip() if pd.notna(row['Diameter']) else '-'
        circ_raw = str(row['Circumference']).strip() if pd.notna(row['Circumference']) else '-'
        corr_raw = str(row['Corrugation (in)']).strip() if pd.notna(row['Corrugation (in)']) else '-'
        
        bu_ft = clean_num(row['Bu / Foot'])
        eave_ht = clean_num(row['Eave Height'])
        rings = clean_num(row['Rings / Type'])
        cone_bu = clean_num(row['Cone Bu'])
        bot_cone_bu = clean_num(row['Bot Cone Bu']) if 'Bot Cone Bu' in row and pd.notna(row['Bot Cone Bu']) else 0
        
        max_bu_raw = clean_num(row['Max Bu']) if 'Max Bu' in row and pd.notna(row['Max Bu']) else 0
        if max_bu_raw == 0:
            max_bu = round(bu_ft * eave_ht + cone_bu + bot_cone_bu)
        else:
            max_bu = int(max_bu_raw)
            
        obj = {
            "brand": brand,
            "diameter": dim_raw,
            "circumference": circ_raw,
            "corrugation": corr_raw,
            "buPerFt": int(bu_ft) if bu_ft == int(bu_ft) else bu_ft,
            "eveHeight": int(eave_ht) if eave_ht == int(eave_ht) else eave_ht,
            "rings": int(rings) if rings == int(rings) else rings,
            "coneBu": int(cone_bu),
            "botConeBu": int(bot_cone_bu),
            "maxBu": int(max_bu)
        }
        
        props_str = ",\n".join([f'    {k}: {json.dumps(v)}' for k, v in obj.items()])
        js_entries.append(f'  "{bin_id}": {{\n{props_str}\n  }}')

    full_js = "// bin-specs.js - Structural Hardware Specifications\nconst binHardwareSpecs = {\n" + ",\n".join(js_entries) + "\n};\n"
    
    with open('bin-specs.js', 'w') as f:
        f.write(full_js)
    print("Successfully updated bin-specs.js!")

if __name__ == '__main__':
    convert()