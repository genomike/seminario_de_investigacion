import json, pathlib

data = json.loads(pathlib.Path(r"e:\Maestria\Seminario_De_Investigacion\Investigación\datos\articulos-seleccionados.json").read_text(encoding="utf-8"))
targets = ["Gazzarata","Pedrera","Chatterjee","Gaudet","Mukhiya","Fernandez","Esparza","Arias Ger","Sanchez Calle","Huarac","Bran","Morales-Camargo"]
seen = set()
for art in data:
    blob = json.dumps(art, ensure_ascii=False).lower()
    for t in targets:
        if t.lower() in blob and t not in seen:
            seen.add(t)
            print(f"=== {t} ===")
            for k in ["primer_autor","year","titulo","authors","journal","volume","issue","pages","doi","url","tipo"]:
                print(f"  {k}: {art.get(k,'')}")
            print()
