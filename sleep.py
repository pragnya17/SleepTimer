import os
import time
import subprocess
import signal
from flask import Flask, render_template, request,  redirect, url_for, Response
from elevate import elevate

app = Flask(__name__)

def close_task(app):       
    if app == "Spotify":
        os.system("taskkill /f /im spotify.exe")
    elif app == "Hulu":
        os.system("taskkill /f /im hulu.exe")
    else:
        os.system("taskkill /f /im WWAHost.exe") # specifically for netflix

@app.route('/')
def index():
    return render_template('sleeptimer.html')

@app.route('/close', methods=['POST'])
def close():
    time_input = int(request.form['hours'])*3600 + int(request.form['minutes']) # multiply minutes by 60 later
    time.sleep(time_input)

    # list_apps = []
    # try:
    print("here")
    list_apps = request.form.getlist('check') # cannot hit back on webpage or else these checkboxes will not work

    for each in list_apps:
        print(each)
        close_task(each)
    
    # hibernate mode
    # elevate() # need to elevate to administrative level to sleep
    # os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    return "Apps have been closed"

@app.route('/render_page')
def render_page():
    open_file()
    return Response(open_file(),mimetype='multipart/x-mixed-replace; boundary=frame') #call open_file here
    
if __name__ == '__main__':
    app.run(host='localhost', debug=True, threaded=True)

# closing all applications, could add shut down
# tasks = subprocess.check_output("tasklist").decode("utf-8")
# list_tasks = (tasks.split('\n'))
# # print("before: ", len(list_tasks) - 4)
# chrome_pid = []
# i = 4
# while i < len(list_tasks): #while it has not reached the end
#     task = list_tasks[i].split()
#     if task[0] == "chrome.exe":
#         chrome_pid.append(int(task[1]))
#         continue
#     try:
#         pid = int(task[1])
#     except:
#         pass
#     # print(pid)
#     # os.kill(pid, signal.SIGINT) # SIGTERM might be safer for closing
#     i += 1
