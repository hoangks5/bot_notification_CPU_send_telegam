import requests
import socket
import psutil
import datetime
import os
def telegram(text):
    url = 'https://api.telegram.org/bot1920849778:AAE4xOcQn1gIbctUOwQbQpw9Iy9hQ10rv90/sendMessage?chat_id=-570885952&text=' +str(text)
    requests.get(url)
my_ip = requests.get('https://api.ipify.org').text
def check():
    load_cpu = 0
    for i in range(2880):
        load_cpu = load_cpu + psutil.cpu_percent(interval=5)
    return load_cpu
def send_noti():
    cpu_tb = round(check()/2880)
    if cpu_tb > 85:
        text = 'Máy chủ IP: '+my_ip +'\nTime: '+str(datetime.datetime.now())[:18] +'\nCPU Trung bình: '+str(cpu_tb)+'%'+'\nStatus: Restar'
        telegram(text)
        os.system("shutdown /r /t 1")
    text = 'Máy chủ IP: '+my_ip +'\nTime: '+str(datetime.datetime.now())[:18] +'\nCPU Trung bình: '+str(cpu_tb)+'%'+'\nStatus: Running'
    telegram(text)
def batdau():
    text = 'Đã kích hoạt thông báo CPU cho máy chủ: '+my_ip
    telegram(text)
def main():
    batdau()
    try:
        while True:
            send_noti()
    except:
        return main
if __name__ == '__main__':
    main()
