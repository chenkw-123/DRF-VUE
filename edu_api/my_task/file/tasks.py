from my_task.main import app


@app.task(name="delete_file")
def delete_file():
    print("删除文件调用此方法")

    return "delete_file"