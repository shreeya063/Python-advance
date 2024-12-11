from flask import Flask, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

sql_host = "127.0.0.1"
sql_port = 3306
sql_database = "flight_game"
sql_user = "root"
sql_password = "machapuchre"

def get_airport_info(identity):
    try:
        connection = mysql.connector.connect(
            host=sql_host,
            port=sql_port,
            database=sql_database,
            user=sql_user,
            password=sql_password
        )

        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)

            query = f"SELECT ident, name, municipality FROM airport WHERE ident = %s"
            cursor.execute(query, (identity,))
            result = cursor.fetchone()

            if result:
                return result
            else:
                return None

    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route("/airport/<icao_code>", methods=['GET'])
def get_airport(icao_code):
    airport = get_airport_info(icao_code)

    if airport:
        return jsonify({
            "ICAO": airport["ident"],
            "Name": airport["name"],
            "Location": airport["municipality"]
        })
    else:
        return jsonify({"Error": "No airport found"}), 404

if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1', port=5000)