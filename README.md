# Plantilla Backend API Rest

Esta plantilla está diseñada para servicios de servidor usando Node.js, Express u otro entorno backend.

## Buenas Prácticas de Seguridad
* **¡NUNCA!** subas el archivo `.env`. Asegúrate de que esté siempre en el `.gitignore`.
* En su lugar, crea un archivo `.env.example` con variables vacías para que el equipo sepa qué configurar.
* Ignora siempre la carpeta `node_modules/`.

## Estructura Sugerida (kebab-case)
* `src/routes/` - Controladores de rutas.
* `src/models/` - Esquemas de bases de datos.
* `src/middlewares/` - Interceptores de seguridad.
