# publisher/subscriber
import time
import paho.mqtt.client as mqtt
import mycamera # 카메라 사진 보내기,온습도,초음파 등을 import함.
flagFalse
def on_connect(client, userdata, flag, rc):
        client.subscribe("facerecognition", qos0)
        client.subscribe("distance", qos0)
        client.subscribe("led", qos=0)
def on_message(client, userdata, msg) :
        #카메라 이미지 코드
        global flag
        commandmsg.payload.decode("utf-8")
        if command== "action":
                print("action msg received..")
                flagTrue
                lightmycamera.getLight()
                if light <15:
                        i1
                else:
                        i0
                mycamera.controlLED(i)
        else:
                msgint(msg.payload)
                print(msg)
                mycamera.controlLED(msg)

broker_ip"localhost"# 현재 이 컴퓨터를 브로커로 설정
clientmqtt.Client()
client.on_connecton_connect
client.on_messageon_message
client.connect(broker_ip, 1883)
client.loop_start()
while True:
        if flag==True:
                imageFileNamemycamera.takePicture() # 카메라 사진 촬영
                print(imageFileName)
                client.publish("image", imageFileName, qos=0)
                flagFalse
        time.sleep(1)
client.loop_end()
client.disconnect()
