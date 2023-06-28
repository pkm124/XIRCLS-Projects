from django.shortcuts import render
import requests
import mysql.connector
from urllib.request import urlopen


mydb = mysql.connector.connect(host="localhost",user="root",password="1234",database="digital_footprinting" )
mycursor = mydb.cursor()


def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def index(request):
    context = {}
    x_forw_for = request.META.get('HTTP_X_FORMWARDED_FOR')
    if x_forw_for is not None:
        ip = x_forw_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print("IP ADDRESS OF USER : ", ip)
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name"),
        "latitude": response.get("latitude") ,
        "longitude": response.get("longitude")
    }
    print(location_data)
    sql = "INSERT INTO requests (ipaddress) VALUES (%s)"
    val = (str(ip_address), )
    mycursor.execute(sql, val)
    mydb.commit()

    print(mycursor.rowcount, "record inserted.")



    mycursor.execute("SELECT DISTINCT ipaddress FROM requests")
    myresult = mycursor.fetchall()
    print(len(myresult))
    for x in myresult:
        print(x)
    url = "http://127.0.0.1:8000/index"
    
    

    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def pricing(request):
    var = request.POST['duration']
    print(var)
    return render(request, 'pricing.html')

def features(request):
    return render(request, 'features.html')