import psutil
from flask import Flask, render_template
import datetime
import socket
import platform

app = Flask(__name__)

@app.route("/")
def index():
    # System metrics
    cpu_metric = psutil.cpu_percent()
    mem_metric = psutil.virtual_memory().percent
    disk_metric = psutil.disk_usage('/').percent
    net_io = psutil.net_io_counters()
    uptime_seconds = datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())
    process_count = len(psutil.pids())

    # Convert bytes to MB for Network I/O
    net_sent = net_io.bytes_sent / (1024 * 1024)
    net_recv = net_io.bytes_recv / (1024 * 1024)
    
    # User-friendly system stats
    hostname = socket.gethostname()
    os_name = platform.system() + " " + platform.release()
    cpu_count = psutil.cpu_count(logical=True)
    total_memory = round(psutil.virtual_memory().total / (1024 * 1024 * 1024), 2)  # Convert bytes to GB

    message = None
    if cpu_metric > 80 or mem_metric > 80:
        message = "High CPU or Memory Detected, scale up!!!"
    
    return render_template(
        "index.html", 
        cpu_metric=cpu_metric, 
        mem_metric=mem_metric, 
        disk_metric=disk_metric,
        net_sent=net_sent,
        net_recv=net_recv,
        uptime=str(uptime_seconds).split('.')[0],  # Remove microseconds from uptime
        process_count=process_count,
        hostname=hostname,
        os_name=os_name,
        cpu_count=cpu_count,
        total_memory=total_memory,
        message=message
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
