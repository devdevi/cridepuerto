circles = [
    ["Facultad de Ciencias, UNAM", "unam-fciencias", 1, 1, 0],
    ["Tec de Monterrey, Campos Santa Fé", "itesm-csf", 1, 1, 0],
    ["Inventive", "inventive", 0, 1, 30],
    ["Platzi Bogotá", "platzi-bog", 0, 1, 120],
    ["Platzi México", "platzi-mex", 0, 1, 30],
    ["Google México", "google-mx", 0, 1, 250],
    ["Curso de Fotografía, UVA", "curso-foto-uva", 1, 0, 25],
    ["Equipo de futbol, chapinero", "fut-chapinero", 1, 0, 40],
    ["Grupo 3340, Prácticas de campo", "grupo-3340-campo", 1, 0, 50],
    ["Generación 2018 Escuela de enfermería", "enfermeria-2018", 1, 0, 0],
    ["Facultad de Ingeniería, UNAM", "unam-fi", 1, 1, 0],
    ["Facultad de Medicina, UNAM", "unam-fm", 1, 1, 0],
    ["Platzi Developer Circle - Bogotá", "platzi-dev", 1, 0, 0],
    ["Platzi Developer Circle - CDMX", "platzi-dev-mx", 1, 0, 0],
    ["IBM Santa Fé", "ibm-santafe", 0, 1, 0],
    ["P&G - Santa Fé", "p-n-g", 1, 0, 1000],
    ["Amigos de Centraal", "comunidad-centraal", 1, 0, 0],
    ["Central Academy", "centraal-academy", 1, 1, 0],
    ["Estado de México - CDMX", "edomex", 1, 0, 0],
    ["Satelite - Santa Fé entre semana", "sat-sfe-week", 1, 0, 0],
    ["Sable Digital", "sable", 0, 0, 30],
]
for cirlce in circles:
    name = cirlce[0]
    slug_name = cirlce[1]
    is_public = cirlce[2]
    verified = cirlce[3]
    members_limit = cirlce[4]
    print(f'Processed { name } { slug_name } { is_public } { verified } { members_limit }')
    Circle.objects.create(
        name=name,
        slug_name=slug_name,
        is_public=is_public,
        verified=verified,
        members_limit=members_limit,
    )
