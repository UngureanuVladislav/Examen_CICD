from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():
    try:
        connection = mysql.connector.connect(
            host="db",
            user="root",
            password="root",
            database="Myapp_base"
        )

        cursor = connection.cursor()
        cursor.execute("SELECT mesaj FROM info LIMIT 1")
        result = cursor.fetchone()

        cursor.close()
        connection.close()

        return f"""
        <h1>Aplicație Python Flask conectată la MySQL</h1>
        <p>{result[0]}</p>
        """

    except Exception as e:
        return f"Eroare la conectarea cu baza de date: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)