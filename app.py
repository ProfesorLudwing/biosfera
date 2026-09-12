import streamlit as st
import os

# Configuración del Pizarrón Escolar
st.set_page_config(page_title="De la Roca a la Vida", page_icon="🌍", layout="wide")

st.title("🌍 De la Roca a la Vida: Litosfera, Pedosfera y Biosfera")
st.markdown("### CBTIS 303 | Ciencias Naturales, Experimentales y Tecnología III")
st.write("Explora las capas que conectan la geología con la vida. Selecciona una pestaña para ver esquemas, datos clave y poner a prueba tus conocimientos.")

# --- RUTAS DE IMÁGENES ---
IMAGENES = {
    "Litosfera_Esquema": "litosfera_esquema.png",
    "Litosfera_Placas": "placas_tectonicas.jpg",
    "Litosfera_Tipos": "tipos_litosfera.png",
    "Pedosfera_Perfil": "pedosfera_perfil.png",
    "Pedosfera_Edafogenesis": "edafogenesis.jpg",
    "Biosfera_Esquema": "biosfera_esquema.png",
    "Biosfera_Quimiosintesis": "quimiosintesis.png"
}

# --- BANCO DE PREGUNTAS ---
CUESTIONARIO = {
    "litosfera": [
        {
            "id": "lit1",
            "pregunta": "¿Qué capas componen la Litosfera?",
            "opciones": [
                "Corteza + manto superior rígido",
                "Corteza + manto completo",
                "Solo la corteza"
            ],
            "correcta": "Corteza + manto superior rígido",
            "pista": "Revisa la definición exacta: no es solo la corteza."
        },
        {
            "id": "lit2",
            "pregunta": "¿Cuál es la diferencia principal entre la litosfera oceánica y la continental?",
            "opciones": [
                "La oceánica es más densa y delgada",
                "La continental es más caliente",
                "No hay diferencia"
            ],
            "correcta": "La oceánica es más densa y delgada",
            "pista": "Mira la composición y el grosor de cada una."
        },
        {
            "id": "lit3",
            "pregunta": "¿Por qué la Litosfera está fragmentada en placas?",
            "opciones": [
                "Por el movimiento de la Astenosfera",
                "Por la temperatura del núcleo",
                "Por la presión de la atmósfera"
            ],
            "correcta": "Por el movimiento de la Astenosfera",
            "pista": "La capa sobre la que flota es plástica."
        },
        {
            "id": "lit4",
            "pregunta": "¿Cuál es el límite inferior de la Litosfera?",
            "opciones": [
                "La Astenosfera",
                "El Manto inferior",
                "El Núcleo externo"
            ],
            "correcta": "La Astenosfera",
            "pista": "Es donde la roca deja de ser rígida."
        }
    ],
    "pedosfera": [
        {
            "id": "ped1",
            "pregunta": "¿Qué es la Pedosfera?",
            "opciones": [
                "La capa de suelo fértil",
                "La capa de roca profunda",
                "La capa de agua subterránea"
            ],
            "correcta": "La capa de suelo fértil",
            "pista": "Es la 'piel' de la Tierra."
        },
        {
            "id": "ped2",
            "pregunta": "¿Cuál es el orden correcto de los horizontes del suelo, de arriba a abajo?",
            "opciones": [
                "O, A, B, C",
                "A, B, C, O",
                "B, A, O, C"
            ],
            "correcta": "O, A, B, C",
            "pista": "Revisa el esquema de horizontes."
        },
        {
            "id": "ped3",
            "pregunta": "¿Qué procesos intervienen en la formación del suelo (Edafogénesis)?",
            "opciones": [
                "Meteorización y mezcla con materia orgánica",
                "Solo erosión eólica",
                "Solo actividad volcánica"
            ],
            "correcta": "Meteorización y mezcla con materia orgánica",
            "pista": "Necesita roca triturada y humus."
        },
        {
            "id": "ped4",
            "pregunta": "¿Por qué es importante la Pedosfera para la vida?",
            "opciones": [
                "Porque almacena nutrientes y agua",
                "Porque genera oxígeno",
                "Porque regula la temperatura global"
            ],
            "correcta": "Porque almacena nutrientes y agua",
            "pista": "Piensa en lo que las plantas necesitan para crecer."
        }
    ],
    "biosfera": [
        {
            "id": "bio1",
            "pregunta": "¿Qué es la Biosfera?",
            "opciones": [
                "El conjunto global de todos los ecosistemas y seres vivos",
                "Solo los animales terrestres",
                "Solo las plantas"
            ],
            "correcta": "El conjunto global de todos los ecosistemas y seres vivos",
            "pista": "Piensa en el alcance de la vida en el planeta."
        },
        {
            "id": "bio2",
            "pregunta": "¿Cuál es la principal fuente de energía que sostiene a la Biosfera?",
            "opciones": [
                "La fotosíntesis",
                "La quimiosíntesis",
                "La energía geotérmica"
            ],
            "correcta": "La fotosíntesis",
            "pista": "Representa el 99.9% de la energía."
        },
        {
            "id": "bio3",
            "pregunta": "¿Cómo transforma la Biosfera a la Litosfera?",
            "opciones": [
                "Mediante el biodeterioro y la edafogénesis",
                "Generando terremotos",
                "Creando montañas"
            ],
            "correcta": "Mediante el biodeterioro y la edafogénesis",
            "pista": "Piensa en cómo las raíces y líquenes rompen las rocas."
        },
        {
            "id": "bio4",
            "pregunta": "¿Qué proceso permite que exista vida en el fondo oceánico sin luz solar?",
            "opciones": [
                "Quimiosíntesis",
                "Fotosíntesis",
                "Respiración anaeróbica"
            ],
            "correcta": "Quimiosíntesis",
            "pista": "Recuerda el 0.1% de excepción."
        }
    ]
}

# --- FUNCIÓN PARA MOSTRAR IMÁGENES ---
def mostrar_imagen(nombre_archivo, texto_alternativo):
    if os.path.exists(nombre_archivo):
        st.image(nombre_archivo, caption=texto_alternativo, use_container_width=True)
    else:
        st.warning(f"⚠️ Guarda una imagen llamada '{nombre_archivo}' en tu carpeta para verla aquí.")

# --- PESTAÑAS PRINCIPALES ---
tab_litosfera, tab_pedosfera, tab_biosfera = st.tabs([
    "🪨 Litosfera",
    "🌱 Pedosfera",
    "🧬 Biosfera"
])

# ============================================================
# PESTAÑA 1: LITOSFERA
# ============================================================
with tab_litosfera:
    st.header("🪨 La Litosfera: La Capa Rígida")
    
    col1, col2 = st.columns([1.2, 1])
    
    with col1:
        subtab_esquema, subtab_placas, subtab_tipos = st.tabs([
            "📏 Esquema General",
            "🗺️ Placas Tectónicas",
            "⚖️ Tipos de Litosfera"
        ])
        with subtab_esquema:
            mostrar_imagen(IMAGENES["Litosfera_Esquema"], "Esquema de la Litosfera sobre la Astenosfera.")
        with subtab_placas:
            mostrar_imagen(IMAGENES["Litosfera_Placas"], "Mapa de placas tectónicas y sus límites.")
        with subtab_tipos:
            mostrar_imagen(IMAGENES["Litosfera_Tipos"], "Comparación entre litosfera oceánica y continental.")
    
    with col2:
        st.success("### 📖 Definición")
        st.markdown("""
        La **Litosfera** es la capa externa y rígida de la Tierra. 
        Incluye **toda la corteza** (continental y oceánica) **+ la parte superior del manto**.
        """)
        
        st.info("### 📊 Datos Clave")
        st.markdown("""
        - **Grosor:** 50-70 km (oceánica) a 100-200 km (continental).
        - **Límite inferior:** La **Astenosfera** (capa plástica).
        - **Composición:**
            - Oceánica: **Basalto** (SIMA) → más densa.
            - Continental: **Granito** (SIAL) → menos densa.
        - **Fragmentación:** ~15 placas tectónicas que flotan sobre la Astenosfera.
        """)
    
    st.write("---")
    with st.expander("📝 Pon a prueba tus conocimientos sobre la Litosfera"):
        for q in CUESTIONARIO["litosfera"]:
            ans = st.radio(q["pregunta"], q["opciones"], key=q["id"])
            if st.button("Validar Respuesta", key=f"btn_{q['id']}"):
                if ans == q["correcta"]:
                    st.success("🎉 ¡Excelente! Respuesta correcta.")
                else:
                    st.error(f"❌ Incorrecto. Pista: {q['pista']}")

# ============================================================
# PESTAÑA 2: PEDOSFERA
# ============================================================
with tab_pedosfera:
    st.header("🌱 La Pedosfera: La Piel Viva")
    
    col1, col2 = st.columns([1.2, 1])
    
    with col1:
        subtab_perfil, subtab_edafo = st.tabs([
            "📏 Perfil del Suelo",
            "🔄 Edafogénesis"
        ])
        with subtab_perfil:
            mostrar_imagen(IMAGENES["Pedosfera_Perfil"], "Perfil del suelo con horizontes O, A, B y C.")
        with subtab_edafo:
            mostrar_imagen(IMAGENES["Pedosfera_Edafogenesis"], "Proceso de formación del suelo (edafogénesis).")
    
    with col2:
        st.success("### 📖 Definición")
        st.markdown("""
        La **Pedosfera** es la capa más superficial de la Litosfera, 
        transformada por la acción de la vida y el clima. Es el **suelo fértil**.
        """)
        
        st.info("### 📊 Datos Clave")
        st.markdown("""
        - **Grosor:** 0.5 a 2 metros (¡una película finísima!).
        - **Formación (Edafogénesis):**
            1. **Meteorización** de la roca madre.
            2. **Mezcla** con materia orgánica (humus).
        - **Horizontes del suelo:**
            - **O:** Hojarasca y materia orgánica fresca.
            - **A:** Humus + minerales (suelo fértil).
            - **B:** Acumulación de arcilla y óxidos.
            - **C:** Roca madre fragmentada.
        - **Importancia:** Almacena nutrientes y agua; hábitat del 25% de la biodiversidad.
        """)
    
    st.write("---")
    with st.expander("📝 Pon a prueba tus conocimientos sobre la Pedosfera"):
        for q in CUESTIONARIO["pedosfera"]:
            ans = st.radio(q["pregunta"], q["opciones"], key=q["id"])
            if st.button("Validar Respuesta", key=f"btn_{q['id']}"):
                if ans == q["correcta"]:
                    st.success("🎉 ¡Excelente! Respuesta correcta.")
                else:
                    st.error(f"❌ Incorrecto. Pista: {q['pista']}")

# ============================================================
# PESTAÑA 3: BIOSFERA
# ============================================================
with tab_biosfera:
    st.header("🧬 La Biosfera: La Vida que Conecta")
    
    col1, col2 = st.columns([1.2, 1])
    
    with col1:
        subtab_esquema, subtab_quimio = st.tabs([
            "🌍 Esquema General",
            "⚗️ Quimiosíntesis"
        ])
        with subtab_esquema:
            mostrar_imagen(IMAGENES["Biosfera_Esquema"], "La Biosfera como una película delgada de vida.")
        with subtab_quimio:
            mostrar_imagen(IMAGENES["Biosfera_Quimiosintesis"], "Comparación entre fotosíntesis y quimiosíntesis.")
    
    with col2:
        st.success("### 📖 Definición")
        st.markdown("""
        La **Biosfera** es el conjunto global de todos los ecosistemas y seres vivos. 
        Es una capa delgada (~20 km) que impregna la Litosfera, Hidrosfera y Atmósfera.
        """)
        
        st.info("### 📊 Datos Clave")
        st.markdown("""
        - **Motores energéticos:**
            - **Fotosíntesis (99.9%):** Energía solar.
            - **Quimiosíntesis (0.1%):** Energía química de la Litosfera.
        - **Transforma la Litosfera:**
            - **Biodeterioro:** Rompe rocas (raíces, líquenes).
            - **Edafogénesis:** Crea suelo fértil.
        - **Relación con la Pedosfera:** La Biosfera es la que "fabrica" el humus.
        """)
    
    st.write("---")
    with st.expander("📝 Pon a prueba tus conocimientos sobre la Biosfera"):
        for q in CUESTIONARIO["biosfera"]:
            ans = st.radio(q["pregunta"], q["opciones"], key=q["id"])
            if st.button("Validar Respuesta", key=f"btn_{q['id']}"):
                if ans == q["correcta"]:
                    st.success("🎉 ¡Excelente! Respuesta correcta.")
                else:
                    st.error(f"❌ Incorrecto. Pista: {q['pista']}")