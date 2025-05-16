import streamlit as st

st.set_page_config(page_title="Calculadora de Clarificantes", page_icon="🍻", layout="centered")

# --- Mensaje superior con enlace ---
st.markdown(
    "[Mirá más calculadoras para productores de bebidas en www.nosoynormalcerveceria.com](https://www.nosoynormalcerveceria.com)",
    unsafe_allow_html=True,
)

# --- Título principal de la app ---
st.title("Calculadora de clarificantes")

# -------------------- Datos base --------------------
clarificante_data = {
    "Bentonita": {
        "range": (0.2, 1.0),
        "unit": "g/L",
        "procedure": (
            "Dispersar la bentonita en 10-20 partes de agua a 60 °C, agitar 10 min y dejar hinchar 8-12 h. Añadir la papilla con agitación y dejar sedimentar 48-72 h antes de trasvasar o filtrar."
        ),
    },
    "Gelatina": {
        "range": (0.015, 0.12),
        "unit": "g/L",
        "procedure": (
            "Hidratar en 10× su peso de agua fría durante 30 min. Fundir a 40 °C, añadir a 15-20 °C, agitar suavemente y dejar 24-72 h (ideal mantener a 0-5 °C las últimas horas)."
        ),
    },
    "Kieselsol + Quitosano": {
        "range": (1.0, 0.5),  # etapa A y B en mL/L
        "unit": "mL/L",
        "procedure": (
            "Añadir 1 mL/L de Kieselsol, mezclar y esperar 30 min. Disolver el Quitosano en un poco de agua tibia y añadir a 0,5 mL/L. Sedimentar 12-48 h y trasvasar."
        ),
    },
    "PVPP": {
        "range": (0.1, 0.5),
        "unit": "g/L",
        "procedure": (
            "Preparar suspensión al 10 % en agua. Dosificar 0,1-0,5 g/L con agitación. Contacto 10-15 min y filtrar inmediatamente, ya que no sedimenta bien por sí solo."
        ),
    },
    "Carbón activado": {
        "range": (0.024, 0.06),
        "unit": "g/L",
        "procedure": (
            "Preparar suspensión al 5 % en agua, añadir 0,024-0,06 g/L con agitación y mantener contacto 2-4 h; filtrar con placas de carbón o tierra diatomea."
        ),
    },
    "Irish Moss/Whirlfloc": {
        "range": (0.04, 0.125),
        "unit": "g/L",
        "procedure": (
            "Disolver y añadir al mosto a falta de 10-15 min del hervor (≈1 tableta Whirlfloc por 19 L). Facilita la coagulación de proteínas en caliente."
        ),
    },
    "Isinglass": {
        "range": (2, 14),  # mL/L de solución lista
        "unit": "mL/L",
        "procedure": (
            "Usar solución lista o rehidratar el polvo en agua acidificada (pH 2,8). Añadir 2-14 mL/L a la cerveza fría (0-5 °C), mezclar y dejar 24-72 h."
        ),
    },
    "Biofine Clear": {
        "range": (0.6, 1.5),
        "unit": "mL/L",
        "procedure": (
            "Agitar el envase, purgar oxígeno. Dosificar 0,6-1,5 mL/L en el fermentador a <4 °C, recircular 5-10 min y dejar sedimentar 24-72 h."
        ),
    },
    "Silica+PVPP (Brewbrite)": {
        "range": (0.2, 0.4),
        "unit": "g/L",
        "procedure": (
            "Añadir 0,2-0,4 g/L después de la fermentación; mezclar, reposar y filtrar para eliminar polifenoles y proteínas responsables de turbidez."
        ),
    },
    "Brewer's Clarex": {
        "range": (0.01, 0.03),
        "unit": "g/L",
        "procedure": (
            "Añadir 1-3 g/hL (0,01-0,03 g/L) al mosto justo al inocular la levadura; degrada proteínas responsables de la turbidez y reduce el gluten. No genera poso."
        ),
    },
    "Sparkolloid": {
        "range": (0.13, 0.53),
        "unit": "g/L",
        "procedure": (
            "Disolver 0,13-0,53 g/L en agua hirviendo durante 30 min, mantener agitación suave y añadir caliente al hidromiel. Clarifica en 5-7 días."
        ),
    },
    "Pectic enzyme": {
        "range": (0.5, 0.6),
        "unit": "g/L",
        "procedure": (
            "Añadir 0,5-0,6 g/L antes de la fermentación en sidra para romper pectinas. Reposar 8-12 h a 20 °C antes de inocular la levadura."
        ),
    },
    "CMC": {
        "range": (0.05, 0.1),
        "unit": "g/L",
        "procedure": (
            "Añadir 0,05-0,1 g/L (solución al 5 %) justo antes de la microfiltración para prevenir la turbidez fría y la precipitación de tartratos."
        ),
    },
    "Goma arábiga": {
        "range": (0.3, 0.8),
        "unit": "g/L",
        "procedure": (
            "Añadir 0,3-0,8 g/L (solución al 30 %) al final del proceso; estabiliza coloides, aumenta cuerpo y protege el color en amaros y vermuts."
        ),
    },
}

# --- Bebida -> Clarificantes permitidos ---
beverage_clarificants = {
    "Cerveza": [
        "Irish Moss/Whirlfloc",
        "Isinglass",
        "Gelatina",
        "Biofine Clear",
        "Silica+PVPP (Brewbrite)",
        "Brewer's Clarex",
        "PVPP",
        "Bentonita",
        "Carbón activado",
    ],
    "Vino": [
        "Bentonita",
        "Gelatina",
        "Kieselsol + Quitosano",
        "PVPP",
        "Carbón activado",
    ],
    "Sidra": [
        "Pectic enzyme",
        "Bentonita",
        "Gelatina",
        "Kieselsol + Quitosano",
        "PVPP",
        "Carbón activado",
    ],
    "Hidromiel": [
        "Bentonita",
        "Sparkolloid",
        "Kieselsol + Quitosano",
        "Gelatina",
    ],
    "Hard-Seltzer": [
        "Carbón activado",
        "PVPP",
        "Bentonita",
        "Gelatina",
    ],
    "Vermut": [
        "Bentonita",
        "Gelatina",
        "Kieselsol + Quitosano",
        "PVPP",
        "Carbón activado",
        "CMC",
        "Goma arábiga",
    ],
    "Bitter": [
        "Bentonita",
        "Gelatina",
        "PVPP",
        "Carbón activado",
        "Goma arábiga",
        "CMC",
    ],
    "Amaro": [
        "Bentonita",
        "Gelatina",
        "PVPP",
        "Carbón activado",
        "Goma arábiga",
        "CMC",
    ],
}

# Para "Otra" mostramos todos los clarificantes disponibles
all_clarificants = sorted({c for lst in beverage_clarificants.values() for c in lst}.union(clarificante_data.keys()))
beverage_clarificants["Otra"] = all_clarificants

# -------------------- Interfaz de usuario --------------------
units = st.radio("Selecciona la unidad de trabajo:", ["Litros", "Mililitros"], index=0)

beverage = st.selectbox(
    "Bebida a clarificar:",
    list(beverage_clarificants.keys()),
    index=list(beverage_clarificants.keys()).index("Cerveza"),
)

vol_default = 20 if units == "Litros" else 500
volume = st.number_input(
    f"Cantidad de {units.lower()}:",
    min_value=0.0,
    value=float(vol_default),
    step=0.1 if units == "Litros" else 10.0,
)

clar_options = beverage_clarificants.get(beverage, all_clarificants)
clarificant = st.selectbox("Clarificante a utilizar:", clar_options)

# -------------------- Cálculo --------------------
if st.button("Calcular"):
    data = clarificante_data.get
