from flask import Flask,request
import socket
import subprocess

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def openStressCPU():
    process = subprocess.Popen(['python', 'stress_cpu.py'], stdout=subprocess.PIPE)
    #output, error = process.communicate()
    #return print(output.decode('utf-8'))
    return "called openStressCPU"
    

@app.route('/', methods = ['GET'])
def getIP():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80, debug=True)
