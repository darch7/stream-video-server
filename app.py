from flask import Flask, send_from_directory, request
import os
import sys

app = Flask(__name__, static_folder=None)

@app.route('/')
def home():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    print(f"[INFO] Visita desde IP: {ip}")
    sys.stdout.flush()
    return '''
    <h1>Video Streaming</h1>
    <video width="640" controls autoplay>
      <source src="/video" type="video/mp4">
      Tu navegador no soporta video HTML5.
    </video>
    '''

@app.route('/video')
def video():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_agent = request.headers.get('User-Agent')
    print(f"[VIDEO] IP: {ip} - User-Agent: {user_agent}")
    sys.stdout.flush()
    return send_from_directory('static', 'video.mp4')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
