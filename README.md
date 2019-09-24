# recommender-system-backend
Back-end para una sistema de aplicación web dirigido a establecer recomendaciones turísticas a grupos.

La versión recomendada de MySQL Server es la 5.7, dado que las siguientes todavía no tienen compatibilidad con el stack de tecnologías.

Crear los archivos de migración después de realizar cambios en los modelos:
- python manage.py makemigrations

Aplicar los cambios del esquema en la base de datos:
- python manage.py migrate

Iniciar servidor:
- python manage.py runserver 0.0.0.0:8000
