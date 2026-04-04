from flask import Flask, render_template, request
import json
from datetime import datetime, timedelta


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("pomodoriser-welcome.html", name="Laura")

@app.route('/pomodoriser')
def pomodoriser():
    return render_template('pomodoriser-welcome.html')

@app.route('/pomodoriser/how-it-works')
def how_pomodoriser_works():
    return render_template('how-it-works.html')

@app.route('/pomodoriser/task-adder', methods=['GET', 'POST'])
def task_form():
    if request.method == 'POST':
        time_available = request.form.get('time_available')

        return render_template(
            'task-input.html',
            time_available = time_available  
        )

    return render_template('task-input.html')

@app.route('/getPlanLength', methods=['POST'])
def planLength():
    if request.method == 'POST':
        time_available = request.form.get('time_available')
        print(time_available)
        return "Received Plan Length!"    

@app.route('/getTaskInputs', methods=['POST'])
def addTask():
    if request.method == 'POST':
        task_name = request.form.get('task_name')
        taskTimeUnit = request.form.get('taskTimeUnit')
        task_time = request.form.get('task_time')
        print(task_name, taskTimeUnit, task_time)
        return "Received Task Inputs!" 

@app.route('/pomodoriser/plan-output')
def plan_output():
    return render_template('output.html')

@app.route('/generatePlan', methods=['POST'])
def generate_plan():
    data = request.get_json()

    tasks = data.get('tasks')
    plan_length = int(data.get('planLength'))

    # Step 1: convert all tasks → pomodoro sessions
    converted_tasks = []
    total_used = 0

    for task in tasks:
        name = task["name"]
        duration = int(task["duration"])
        unit = task["unit"]

        # Convert to pomodoros
        if unit == "Pomodoro Sessions":
            pomodoros = duration
        elif unit == "Hours":
            pomodoros = duration * 2
        elif unit == "Minutes":
            pomodoros = duration / 25
        else:
            continue

        # Respect plan length (same logic as CLI)
        if total_used + pomodoros > plan_length:
            pomodoros = plan_length - total_used

        if pomodoros <= 0:
            break

        # Add each pomodoro as a separate slot
        for _ in range(pomodoros):
            converted_tasks.append(name)

        total_used += pomodoros

        if total_used >= plan_length:
            break

    # Step 2: assign numbers (like assignRanks)
    numbered_tasks = []
    for i, task_name in enumerate(converted_tasks):
        numbered_tasks.append((i + 1, task_name))

    # Step 3: generate times (reuse your logic)
    start_time = datetime.strptime("09:00", "%H:%M")  # temp default
    times = []
    current_time = start_time

    for _ in numbered_tasks:
        times.append(current_time.strftime("%H:%M"))
        current_time += timedelta(minutes=30)

    # Step 4: build output (MVP = simple structure)
    plan = []
    for i in range(len(numbered_tasks)):
        plan.append({
            "no": numbered_tasks[i][0],
            "task": numbered_tasks[i][1]
        })

    return {
        "status": "success",
        "plan": plan
    }


if __name__ == '__main__':
    app.run(debug=True)
