from django.shortcuts import render
import requests as re 

# Create your views here.
API_KEY="1bf61def91bd4a7bab660625240304"
def home(request):
    if request.method=="POST":
        place=request.POST.get("place")
        parms={"key":API_KEY,"q":place}
        response=re.request(url="http://api.weatherapi.com/v1/current.json",method="get",params=parms)
        required_data=response.json()

        if response.status_code!=200:
            error_msg=required_data["error"]["message"]
            data={"msg":error_msg,"error":True}
        else:
            time=required_data["location"]["localtime"]
            deg_celcius=required_data["current"]["temp_c"]
            icon=required_data["current"]["condition"]["icon"]
            condition=required_data["current"]["condition"]["text"]
            humidity=required_data["current"]["humidity"]
            data={"place":place,"time":time,"deg_celcius":deg_celcius,"icon":icon,"condition":condition,"humidity":humidity,"Show":True}
        
        return render(request,"index.html",context=data)
    return render(request,"index.html",{"Show":False})