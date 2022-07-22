import logging
from sqlite3 import connect

from flask import Flask, request

app = Flask(__name__)
conn = connect("database.sqlite", check_same_thread=False)
logger = logging.Logger("example")

@app.post("/write_call")
def write_call():
    """
    Данная функция демонстрирует идею записи звонков в колл-лист, параметры их кол-во может отличаться от настоящих.
    В качестве примера используется таблица Call_list cо столбцами:
    Call_ID - ID номер звонка;
    Phone_number - телефонный номер клиента;
    Call_date - дата звонка;
    Call_time - время звонка;
    Is_called_back - столбец с булевым значением, отображающий статус перезвона, где 0 означает, что сотрудник еще не перезвонил клиенту, а 1 - перезвонил;
    """
    if request.is_json:
        data = request.json # предполагается, что json имеет ключи: {"phone_number", "call_date", "call_time"}
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM Call_list WHERE Phone_number = "{data["phone_number"]}" ')
        result = cursor.fetchall()

        if result:
            for i in reversed(result):
                if i[4] == 0 or i[4] == "0": # проверка Is_callen_back в каждой записи.
                    return 400, "THIS NUMBER HAS BEEN ALREADY RECORDED"
            cursor.execute(f'INSERT INTO Call_list VALUES(Null, "{data["phone_number"]}", "{data["call_date"]}", "{data["call_time"]}", 0)')
            conn.commit()
            return 200, "DONE"
        else:
            cursor.execute(f'INSERT INTO Call_list VALUES(Null, "{data["phone_number"]}", "{data["call_date"]}", "{data["call_time"]}", 0)')
            conn.commit()
            return 200, "DONE"
    else:
        return 400, "NOT JSON"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
