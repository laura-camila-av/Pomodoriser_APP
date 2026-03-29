from flask import Flask, render_template, request

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

if __name__ == '__main__':
    app.run(debug=True)
