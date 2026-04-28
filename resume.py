import streamlit as st

# ---------------------------
# CONFIGURACIÓN DE LA PÁGINA
# ---------------------------
st.set_page_config(
    page_title="Francisco Bustamante | CV Profesional",
    page_icon="⚡",
    layout="wide"
)

# ---------------------------
# ESTILOS
# ---------------------------
st.markdown(
    """
    <style>
    .title {
        font-size:42px;
        font-weight:700;
    }
    .subtitle {
        font-size:22px;
        color: #555;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------
# HEADER
# ---------------------------
col1, col2 = st.columns([1, 3])

with col1:
    st.image("imagen.jpg", width=180)

with col2:
    st.markdown('<div class="title">Francisco Bustamante Álvarez</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle">Especialista Senior en Planificación, Operaciones y Performance</div>',
        unsafe_allow_html=True
    )
    st.write("📍 Santiago, Chile")
    st.write("📧 francisco.bustamante.alvarez@gmail.com")
    

st.divider()

# ---------------------------
# PERFIL PROFESIONAL
# ---------------------------
st.header("🧠 Perfil Profesional")
st.write(
    """
    Ingeniero Civil en Electricidad con experiencia en **operación del sistema eléctrico, planificación,
    performance operacional y gestión de contratos**, en empresas de **generación, transmisión y distribución
    de energía**.

    Profesional analítico, curioso y con alta **honestidad intelectual**, orientado a la mejora continua,
    optimización de procesos y toma de decisiones basada en datos. Fuerte interés en el diseño de nuevos
    procesos, automatización y visualización de indicadores.
    """
)

# ---------------------------
# FORTALEZAS
# ---------------------------
st.header("💪 Fortalezas")
st.markdown(
    """
    - Especialista en **operación de redes eléctricas** y análisis de sistemas de potencia  
    - Gestión de **performance operacional** y KPIs  
    - Análisis y simulación de escenarios complejos del sistema eléctrico  
    - Automatización de visualizadores para gestión de riesgos  
    - Integración de **datos, regulación y operación**
    - Promueve la integración en el grupo
    """
)

# ---------------------------
# EXPERIENCIA PROFESIONAL
# ---------------------------
st.header("💼 Experiencia Profesional")

with st.expander("ENEL Generación Chile | Especialista Senior OP, Performance y Planificación"):
    st.write("**Periodo:** Abril 2024 – Actualidad")
    st.markdown(
        """
        - Gestión comercial y operativa asociada a la **compraventa de combustibles**
        - Coordinación de **logística** para generación de energía
        - Soporte a la comercialización con grandes clientes
        - Seguimiento de indicadores de desempeño operacional
        """
    )

with st.expander("ENEL Distribución Chile | Especialista Senior Estudios"):
    st.write("**Periodo:** Octubre 2018 – Abril 2024")
    st.markdown(
        """
        - Análisis y ejecución de **estudios y simulaciones** del sistema eléctrico
        - Evaluación de condiciones críticas y escenarios de alta complejidad
        - Desarrollo de **visualizadores automáticos** para gestión de riesgos operativos
        - Soporte a la toma de decisiones estratégicas
        """
    )

with st.expander("Superintendencia de Electricidad y Combustibles | Fiscalizador ERNC"):
    st.write("**Periodo:** Mayo 2018 – Septiembre 2018")
    st.markdown(
        """
        - Fiscalización del marco normativo asociado a **generación distribuida**
        - Análisis de controversias y reclamos asociados al **DS 244 PMGD**
        - Aplicación de la **Ley 20.571**
        """
    )

with st.expander("ENEL Distribución Chile | Especialista en Planificación e Inversiones"):
    st.write("**Periodo:** Octubre 2016 – Abril 2018")
    st.markdown(
        """
        - Desarrollo de proyectos de **ingeniería de distribución eléctrica**
        - Evaluación técnica y económica de inversiones
        """
    )

with st.expander("INACAP | Docente"):
    st.write("**Periodo:** Enero 2025 – Febrero 2026")
    st.markdown(
        """
        - Docente en **Almacenamiento Eléctrico**
        - Docente en **Redes Inteligentes**
        """
    )

# ---------------------------
# EDUCACIÓN
# ---------------------------
st.header("🎓 Educación")

st.markdown(
    """
    **Diplomado en los Mercados Eléctricos del Futuro y su Regulación**  
    Pontificia Universidad Católica de Chile – 2025  

    **Diplomado en Machine Learning y Técnicas de Big Data**  
    Pontificia Universidad Católica de Chile – 2021  

    **Ingeniero Civil en Electricidad – Sistemas Eléctricos de Potencia**  
    Universidad de Santiago de Chile – 2009 a 2016
    """
)

# ---------------------------
# HABILIDADES
# ---------------------------
st.header("🛠️ Habilidades")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Técnicas")
    st.write("- Operación sistema eléctrico")
    st.write("- Planificación y performance")
    st.write("- Estudios eléctricos")
    st.write("- Regulación eléctrica")

with col2:
    st.subheader("Herramientas")
    st.write("- Cymdist")
    st.write("- Digsilent")
    st.write("- ETAP")
    st.write("- EMTP")
    st.write("- Python")
    st.write("- SQL")

with col3:
    st.subheader("Idiomas")
    st.write("🇬🇧 Inglés: Intermedio")
    st.write("🇯🇵 Japonés: Básico")

# ---------------------------
# INTERESES
# ---------------------------
st.header("🎯 Intereses")
st.write("📷 Fotografía | ♟️ Ajedrez | 🎵 Música (melómano)")

# ---------------------------
# FOOTER
# ---------------------------
st.divider()
st.caption("© 2026 – Francisco Bustamante | CV desarrollado en Streamlit")
