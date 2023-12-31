from flask import Flask, send_from_directory, render_template ,request, url_for, redirect, send_file, make_response
import random
from main import generate_data_address
from main import generate_data_coordinate

app = Flask(__name__)

'''
# Path for our main Svelte page
@app.route("/") #www.abc.com
def base():
    return send_from_directory('client/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)
    
'''

@app.route("/",methods=['GET','POST']) 
def base():
    return render_template("index.html")
    

@app.route("/search",methods=['GET','POST']) 
def search():
    
    if(request.args.get('address')):
        generate_data_address(request.args.get('address')) #生成json檔
    elif(request.args.get('lat') and request.args.get('lon')):
        generate_data_coordinate(request.args.get('lat'),request.args.get('lon')) #生成json檔
        
    return render_template("data.html")

#測試用網址(不會生成json)
@app.route("/test",methods=['GET','POST']) 
def test():
    
    return render_template("data.html")
    

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5001)
    