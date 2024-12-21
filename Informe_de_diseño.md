# Informe de Funcionalidad y Diseño

## Introducción
Este documento describe la funcionalidad y diseño de un programa desarrollado en Python que interactúa con el usuario mediante la terminal para consultar información financiera. El programa permite buscar datos de Apertura/Cierre Diario, donde se le solicitará el ticker a buscar y una fecha en formato, luego realizará la búsqueda de los datos en la base de datos SQLite o realiza la consulta por medio de una API externa si no están disponibles, para luego permitir la descarga del gráfico de diferencias de precios de entrada y salida de cada ticker para el día correspondiente.

## Descripción del funcionamiento

El programa sigue una lógica secuencial con los siguientes pasos principales:

1. Ingreso de datos por el usuario:

    - El usuario introduce un ticker y una fecha a través de la terminal.

2. Consulta en la base de datos:

    - El programa verifica si existen datos relacionados con el ticker y la fecha proporcionados en la base de datos.

    - Si los datos están disponibles, los muestra al usuario.

3. Consulta a la API:

    - Si los datos no se encuentran en la base de datos, el programa consulta una API externa para obtenerlos.

    - Si la API devuelve resultados:

        - Los datos se muestran al usuario.

        - Los datos se guardan en la base de datos para futuras consultas.

    - Si la API no tiene información, el programa informa al usuario y solicita una nueva combinación de ticker y fecha.

4. Realización del gráfico de diferencias de precios entre tickers:

    - Si solamente existe un ticker guardado para la fecha indicada, el programa solicitará al usuario que consulte más tickers para esa fecha.
    - Si el programa encuentra más de un ticker para la fecha solicitada muestra el gráfico de diferencia para el día consultado y lo guarda en la carpeta img con el nombre "grafico" más la fecha del ticker en formato png.

5. Finalización del programa
    - Luego de realizar las búsquedas el usuario tiene la posibilidad de detener el programa, se le preguntará si desea seguir consultando y al introducir NO el programa finaliza.

## Diseño del programa

El programa se organiza en módulos para facilitar su mantenimiento y escalabilidad. Las partes principales son:

1. Estructura de archivos:

   - app: Contiene los archivos de la aplicación.
  
       - api_client.py: Contiene las funciones para interactuar con la API.
    
        - db.py: Gestiona las operaciones con la base de datos.
    
        - terminal_app.py: Maneja la interacción con el usuario y la lógica principal del programa.
    
        - utis.py: Contiene funciones generales de utilidad.
      
        - config.py: Contiene valores de configuración para la aplicación.
    - img: Contiene las imágenes graficadas para el usuario.
    - notebooks: Contiene las notebooks para pruebas.
      
3. Flujo de datos:
    - El usuario interactúa con terminal_app.py.
    - Valida los datos utilizando utils.py
    - Para verificar la disponibilidad de datos consulta a db.py.
    - Si no hay datos en la base de datos, api_client.py realiza una consulta a la API.
    - Los resultados de la API, si están disponibles, se guardan mediante db.py.
    - Los datos se visualizan en la terminal o mediante gráficos generados en una función alojada en utils.py.
      
4. Especificaciones técnicas:
    - Base de Datos:
        - Nombre: financial_data
     
        - Tabla principal: daily_open_close.
     
        - Campos: date, ticker, open, close, high, low, volume,  afterHours, preMarket.

    - API:
  
        - Se utiliza la API de polygon.io
              
    - Gráficos:

        - Librería utilizada: matplotlib.

        - Tipo de gráfico: De barras para comparar las diferencias entre tickers.

## Consideraciones Adicionales

1. Manejo de Errores:

    - Validación de entradas del usuario.
    - Manejo de excepciones para consultas fallidas a la base de datos o a la API.

3. Persistencia:

    - Datos obtenidos de la API se almacenan para evitar consultas redundantes.

5. Interfaz de Usuario:

    - Diseñada para ser intuitiva y guiar al usuario en cada paso del proceso

## Conclusión
El programa proporciona una solución eficiente para gestionar consultas financieras, integrando la funcionalidad de una base de datos y una API externa con herramientas de visualización. La estructura modular asegura la extensibilidad y el mantenimiento a largo plazo.

## Anexo
- Ejemplo de salida en la terminal:  
![Terminal](https://raw.githubusercontent.com/vani98/TP-Python-2024/main/img/CapturaTerminal.PNG)
- Ejemplo de gráfico:
![Grafico](https://raw.githubusercontent.com/vani98/TP-Python-2024/main/img/grafico_2023-03-02.png)