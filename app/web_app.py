import streamlit as st
import pandas as pd

# Inicializamos los mensajes en la sesión si no existen
if 'mensajes' not in st.session_state:
    st.session_state["mensajes"] = list()

# Inicializamos los datos ingresados en la sesión si no existen
if 'ticker' not in st.session_state:
    st.session_state['ticker'] = None
if 'fecha' not in st.session_state:
    st.session_state['fecha'] = None

# Función para mostrar los datos ficticios
def mostrar_data(ticker, fecha):
    # Crear datos ficticios
    data_ficticia = {
        "Ticker": [ticker],
        "Fecha": [fecha],
        "Apertura": [100.5],
        "Cierre": [102.3],
        "Volumen": [1500000]
    }
    df = pd.DataFrame(data_ficticia)
    return df.to_html(index=False)

# Contenedor para los mensajes
messages = st.container()

# Lógica para controlar el flujo de la conversación
if 'estado' not in st.session_state:
    st.session_state["mensajes"].append(("assistant", "¡Hola! Por favor, ingresa el Ticker."))
    st.session_state['estado'] = 'esperar_ticker'

# Pregunta inicial si el estado es 'esperar_ticker'
if st.session_state['estado'] == 'esperar_ticker':
    st.session_state["mensajes"].append(("assistant", "¡Hola! Por favor, ingresa el la fecha."))
    st.session_state['estado'] = 'esperar_fecha'  # Cambiamos el estado para esperar el ticker

# Esperamos la entrada del usuario
if prompt := st.chat_input("Say something"):
    st.session_state["mensajes"].append(("user", prompt))

    # Si el estado es 'esperar_ticker', el usuario debe ingresar el Ticker
    if st.session_state['estado'] == 'esperar_ticker':
        st.session_state['ticker'] = prompt
        st.session_state["mensajes"].append(("assistant", "¡Perfecto! Ahora, ingresa la fecha en formato YYYY-MM-DD."))
        st.session_state['estado'] = 'esperar_fecha'  # Cambiamos el estado para esperar la fecha

    # Si el estado es 'esperar_fecha', el usuario debe ingresar la fecha
    elif st.session_state['estado'] == 'esperar_fecha':
        try:
            # Validar la fecha
            pd.to_datetime(prompt, format='%Y-%m-%d')
            st.session_state['fecha'] = prompt
            resp = mostrar_data(st.session_state['ticker'], st.session_state['fecha'])
            st.session_state["mensajes"].append(("assistant", resp))
            st.session_state['estado'] = 'completado'  # El proceso ha terminado

        except ValueError:
            st.session_state["mensajes"].append(("assistant", "Formato de fecha incorrecto. Por favor, ingresa una fecha en formato YYYY-MM-DD."))
    
    # Si el proceso se completó, el bot muestra los resultados y pregunta si desea ingresar otro ticker
    elif st.session_state['estado'] == 'completado':
        st.session_state["mensajes"].append(("assistant", "Los datos han sido procesados. ¿Quieres intentar con otro ticker y fecha?"))
        st.session_state['estado'] = 'esperar_ticker'  # Reinicia el proceso

# Mostrar los mensajes previos
for mensaje in st.session_state["mensajes"]:
    messages.chat_message(mensaje[0]).write(mensaje[1])

# Mostrar los datos ingresados si ya se completó el proceso
if st.session_state['estado'] == 'completado':
    st.write(f"**Ticker guardado**: {st.session_state['ticker']}")
    st.write(f"**Fecha guardada**: {st.session_state['fecha']}")
