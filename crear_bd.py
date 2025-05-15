<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>POS - La Nueva Estrella</title>
</head>
<body>
  <h1>POS - Minimarket La Nueva Estrella</h1>
  <form action="/buscar" method="post">
    <label for="codigo">Código del producto:</label>
    <input type="text" name="codigo" required>
    <button type="submit">Buscar</button>
  </form>
  <hr>
  {% if producto %}
    <h3>Producto:</h3>
    <p><strong>Nombre:</strong> {{ producto[1] }}</p>
    <p><strong>Precio:</strong> ${{ producto[2] }}</p>
  {% elif mensaje %}
    <p>{{ mensaje }}</p>
  {% endif %}
</body>
</html>
