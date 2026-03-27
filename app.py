from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("Home_page.html", name="Laura")

@app.route('/pomodoriser')
def pomodoriser():
    return render_template('Pom.html')

@app.route('/generate', methods=['POST'])
def addTask():
    if request.method == 'POST':
        time_available = request.form.get('time_available')
        task_name = request.form.get('task_name')
        taskTimeUnit = request.form.get('taskTimeUnit')
        task_time = request.form.get('task_time')
        print(time_available, task_name, taskTimeUnit, task_time)
        return "Received!"    

if __name__ == '__main__':
    app.run(debug=True)
