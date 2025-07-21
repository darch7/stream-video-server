from flask import Flask, send_from_directory, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    ip = request.remote_addr
    print(f"[INFO] Visita desde IP: {ip}")
    return '''
    <h1>Video Streaming</h1>
    <video width="640" controls autoplay>
      <source src="/video" type="video/mp4">
      Tu navegador no soporta video HTML5.
    </video>
    '''

@app.route('/video')
def video():
    ip = request.remote_addr
    print(f"[VIDEO] Reproduciendo desde IP: {ip}")
    return send_from_directory('static', 'video.mp4')

# ⬇️ ESTO ES FUNDAMENTAL PARA QUE FUNCIONE EN RENDER
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Render define el puerto
    app.run(host='0.0.0.0', port=port)
