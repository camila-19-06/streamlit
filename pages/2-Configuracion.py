import streamlit as st

st.title("⚙️ Configuración de la Aplicación")

st.write("Ajusta las preferencias de la aplicación:")

# ========================
# Preferencias de usuario
# ========================
st.subheader("👤 Preferencias de Usuario")

nombre = st.text_input("Nombre de usuario", "Camila")
email = st.text_input("Correo electrónico", "usuario@email.com")

# ========================
# Tema de la aplicación
# ========================
st.subheader("🎨 Apariencia")

tema = st.selectbox(
    "Selecciona el tema",
    ["Claro", "Oscuro", "Sistema"]
)

# ========================
# Notificaciones
# ========================
st.subheader("🔔 Notificaciones")

notificaciones = st.checkbox("Activar notificaciones", value=True)
email_notif = st.checkbox("Recibir notificaciones por correo")

# ========================
# Configuración avanzada
# ========================
st.subheader("⚡ Configuración Avanzada")

modo_debug = st.toggle("Modo desarrollador (Debug)")
guardar_logs = st.toggle("Guardar registros (logs)")

# ========================
# Botón guardar
# ========================
if st.button("💾 Guardar Configuración"):
    st.success("Configuración guardada correctamente")

    st.write("### 📋 Resumen de configuración:")
    st.write(f"Nombre: {nombre}")
    st.write(f"Email: {email}")
    st.write(f"Tema: {tema}")
    st.write(f"Notificaciones: {'Sí' if notificaciones else 'No'}")
    st.write(f"Email Notif: {'Sí' if email_notif else 'No'}")
    st.write(f"Debug: {'Activo' if modo_debug else 'Inactivo'}")
    st.write(f"Logs: {'Activo' if guardar_logs else 'Inactivo'}")