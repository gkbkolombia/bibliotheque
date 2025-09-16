import os, json

EXCLUDES = {"json", "scripts", ".github"}

ICONS = {
    "mathematiques": "fas fa-square-root-alt",
    "svt": "fas fa-leaf",
    "francais": "fas fa-book-open",
    "anglais": "fas fa-language",
    "histoire-geographie": "fas fa-globe",
    "pct": "fas fa-flask",
    "ecm": "fas fa-users",
    "bepc": "fas fa-graduation-cap",
    "bac1": "fas fa-graduation-cap",
    "bac2": "fas fa-graduation-cap"
}

os.makedirs("json", exist_ok=True)

matieres_data = []
matieres = [d for d in os.listdir(".") if os.path.isdir(d) and d not in EXCLUDES]

for matiere in matieres:
    fichiers = [f"{matiere}/{f}" for f in os.listdir(matiere) if f.lower().endswith(".pdf")]
    if not fichiers:
        continue
    titre = matiere.replace("-", " ").capitalize()
    icone = ICONS.get(matiere, "fas fa-book-open")
    data = {"titre": titre, "icone": icone, "pdfs": sorted(fichiers)}
    
    with open(f"json/{matiere}.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    matieres_data.append({"id": matiere, "titre": titre, "icone": icone})
    print(f"✅ {matiere}.json généré ({len(fichiers)} PDF)")

with open("json/matieres.json", "w", encoding