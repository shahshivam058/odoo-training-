from werkzeug.serving import run_simple 
from werkzeug.wrappers import Request,Response
import os
import json
from base64 import b64encode

keys=[]

def getfile(filename):
    if os.path.exists(filename):
        print("path exist")
        #f=open(filename,"r")
        with open(filename,'r',encoding = 'utf-8') as f:
            s=f.read()
            return s
    else:
        print("no path")


@Request.application
def application(request):
    content=""
    mime="text/html"
    if request.path == "/" or  request.path == "/index.html":
        content=getfile("index.html")
        response=Response(content,mimetype=mime)
        key=b64encode(os.urandom(4)).decode("utf-8")
        response.set_cookie("shivam",key)
        keys.append(key)
        return response
    elif request.path == "/s.html":
        content=getfile("s.html")
    elif request.path == "/new.css":
        content=getfile("new.css")
        mime="text/css"
    elif request.path =="/search.js":
        content=getfile("search.js")
        mime="text/javascript"
    elif request.path == "/mobile.json":
        if request.cookies.get("shivam") in keys:
            content=getfile("mobile.json")
            mime="application/json"
        else:
            return Response("not authanticated")
    elif request.path == "/insert_data":
        content=getfile("mobile.json")
        mime="application/json"

        if request.method=="POST":
            s=str((request.form["key"]))
            t=str(request.form["value"])
            js={"mobile":s,"price":t}
            with open("mobile.json") as i:
                data=json.load(i)
            with open("mobile.json","w") as r:
                data.append(js)
                json.dump(data,r,indent=4)
 
 
    response =Response(content,mimetype=mime)
    return response
        
if __name__ == '__main__':
    run_simple("127.0.0.1",4444,application,use_debugger=True,use_reloader=True)
