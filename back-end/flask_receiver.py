from flask import Flask,request,jsonify
from flask_cors import CORS
import youtube_extract as ys
import send_mail as sm

app=Flask(__name__)
CORS(app)

@app.route("/",methods=["POST"])
def flink():
    if request.method=="POST":
        link=request.json['ylink']
        mail=request.json['umail']
        ys.uinput(link,mail)
        sm.send(mail)
        return jsonify('Success')

if __name__=='__main__':
    app.run(debug=True)