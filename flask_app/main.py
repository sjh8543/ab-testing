from flask import Flask
from flask import request
import logging
import os

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='/var/log/flask/'+os.getenv('APP_NAME')+'_app_info.log',
                    filemode='w')
info_logger = logging.getLogger('app_logger')

app = Flask(__name__)

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None: 
        raise RuntimeError( 'Not Running with Werkezeug Server' )
    func()

@app.route("/admin")
def admin():
    info_logger.info("admin URL")
    return "It's admin URL"

@app.route("/collecting")
def collecting():
    info_logger.info("collecting URL")
    return "It's collecting URL"

@app.route("/reporting")
def reporting():
    info_logger.info("reporting URL")
    return "It's reporting URL"

@app.route("/routing")
def routing():
    info_logger.info("routing URL")
    return "It's routing URL"

@app.route('/shutdown',methods=['POST'])
def shutdown():
    """
     API for gracefully shutdown flask application.
     Flask application can be shut down when every requests requested to flask apllication are complete.
     It will help application rollout process. 
    """
    shutdown_server()
    return 'Server shutting down.....'

if __name__ == "__main__":
    info_logger.info("engine application start!")
    app.run()
