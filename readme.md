# Práctica 2 - API Flask

Este proyecto corresponde a la **Práctica 2** del curso de Plataformas Abiertas con el profesor **M. Da Ros** del **BTS SIO - Lycée Gustave Eiffel (Bordeaux)**.

## 📌 Descripción

Se construye una pequeña API REST con Flask que responde al endpoint `/usuarios/api/v1/saludo`.

### Funcionalidad:
- Si se envía el parámetro `id`, devuelve:
  ```json
  { "mensaje": "El id del usuario es 123" }
