from flask import Flask
from flask import url_for
from worker import celery
import celery.states as states

app = Flask(__name__)

@app.route('/factors/<int:param1>')
def add(param1: int) -> str:
    task = celery.send_task('tasks.add', args=[param1], kwargs={})
    response = f"<a href='{url_for('check_task', task_id=task.id, external=True)}'>check status of {task.id} </a>"
    return response

@app.route('/check/<string:task_id>')
def check_task(task_id: str) -> str:
    res = celery.AsyncResult(task_id)
    if res.state == states.PENDING:
        return res.state
    else:
        return str(res.result)
