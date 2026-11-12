import sqlite3
from pathlib import Path

message = """"
'a' => Add New Task
'd' => Delete A Task
's' => Show All Task
'u' => Update A Task
'q' => Quit The App
PLease choose an option:
"""
user_input = input(message).strip().lower()
commands_list = ["a", "d", "s", "u", "q", "p"]
user_id = 2

try:
    sqliteConnection = sqlite3.connect(Path.home() / Path("Desktop", 'TodoAPP.db'))
    crsr = sqliteConnection.cursor()

except:
    print("connection error")

finally:
    if (sqliteConnection):
        # create Table
        sql_command = """CREATE TABLE IF NOT EXISTS tasks (
        user_id INTEGER,
        task_name VARCHAR(20),
        description TEXT)"""
        crsr.execute(sql_command)


        def show_tasks():
            crsr.execute(f"SELECT * FROM tasks WHERE user_id = '{user_id}'")
            result = crsr.fetchall()
            print(f'You have {len(result)} tasks')
            if len(result) > 0:
                for task in result:
                    print(f'Task Name: {task[1]}, Description: {task[2]}')
            sqliteConnection.commit()

        def add_task():
            task_name = input("Enter new task name: ").strip().lower()
            des = input("Enter new description: ").strip()
            crsr.execute(f"INSERT INTO tasks (user_id, task_name, description) VALUES ('{user_id}', '{task_name}', '{des}')")
            sqliteConnection.commit()


        def delete_task():
            task_name = input("Enter the task name you want to delete: ").strip()
            crsr.execute(f"DELETE FROM tasks where task_name='{task_name}' and user_id='{user_id}'")
            sqliteConnection.commit()

        def update_task():
            task_name = input("Enter The name of the task you want to Modify: ").strip()
            crsr.execute(f"SELECT * FROM tasks WHERE task_name='{task_name}' AND user_id='{user_id}'")
            result = crsr.fetchall()
            if not result:
                print("Ther is no task with this name")
            else:
                des = input("Enter new description: ").strip()
                crsr.execute(
                    "UPDATE tasks SET description=? WHERE task_name=? AND user_id=?",
                    (des, task_name, user_id)
                )
                sqliteConnection.commit()
                print("Task has been updated")

        def end_app():
            print("Programe closed")
            exit()

        if user_input in commands_list:
            if user_input == "a":
                add_task()
            elif user_input == "d":
                delete_task()
            elif user_input == "s":
                show_tasks()
            elif user_input == "u":
                update_task()
            else:
                end_app()
        else:
            print("\nSorry this cammand is not found!... ")


    sqliteConnection.close()