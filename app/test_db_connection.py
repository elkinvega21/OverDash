import psycopg2

DB_URL = "postgresql://postgres:postgres@localhost/fastapi_db" # La misma URL por defecto

print(f"Intentando conectar a: {DB_URL}")

try:
    conn = psycopg2.connect(DB_URL)
    print("¡Conexión exitosa!")
    conn.close()
    print("Conexión cerrada.")
except UnicodeDecodeError as ude:
    print(f"Error de UnicodeDecodeError al conectar: {ude}")
    print(f"  Byte problemático: {ude.object[ude.start:ude.end]}")
    print(f"  En la posición: {ude.start} a {ude.end}")
except Exception as e:
    print(f"Ocurrió otro error al conectar: {e}")