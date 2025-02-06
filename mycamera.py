import os; import io; import time
importpicamera; importcv2
importRPi.GPIO as GPIO
importnumpy as np; from PIL import Image
fromadafruit_htu21d importHTU21D
importAdafruit_MCP3008
importbusio
# 전역 변수 선언 및 초기화
trig20
echo16
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.output(trig, False)
mcpAdafruit_MCP3008.MCP3008(clk=11, cs=8, miso=9, mosi=10)
led6 #핀 번호 6, 빵판으로는 하단 16번
GPIO.setup(led, GPIO.OUT) #gpio 6번 핀을 출력 선으로 지정
#온습도 측정을 위한 코드
sda2 #GPIO핀번호
scl3 #GPIO핀번호
i2cbusio.I2C(scl, sda)
sensor= HTU21D(i2c)  #HTU21D장치를제어하는객체리턴
def getTemperature():
    return float(sensor.temperature)
def getHumidity():
    return float(sensor.relative_humidity)
def getLight():
        return int(mcp.read_adc(0))
def controlLED(onOff): #led번호의 핀에 onOff(0,1) 값 출력하는 함수
        GPIO.output(led, onOff)
#초음파 측정을 위한 코드 
def measureDistance():
        global trig, echo
        GPIO.output(trig, True) # 신호 1 발생
        GPIO.output(trig, False) # 신호 0 발생(falling 에지)
        while(GPIO.input(echo) == 0):
                pass
        pulse_starttime.time() # 신호 1. 초음파 발생이 시작되었음을 알림
        while(GPIO.input(echo) == 1):
                pass
        pulse_endtime.time() # 신호 0. 초음파 수신 완료를 알림
        pulse_durationpulse_endpulse_start
        return 340*100/2*pulse_duration
#카메라 측정을 위한 코드        
fileName""
streamio.BytesIO()
cameracv2.VideoCapture(0, cv2.CAP_V4L)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
camera.set(cv2.CAP_PROP_BUFFERSIZE, 1)
bufferSizeint(camera.get(cv2.CAP_PROP_BUFFERSIZE))
print(bufferSize)
time.sleep(1)
#실시간사진을찍어주는함수
def takePicture() :
        global fileName, stream, camera
        if len(fileName) != 0:
                os.remove(fileName)
        stream.seek(0)
        stream.truncate()
        
        for i in range(bufferSize+1):
                ret, framecamera.read()
        Image.fromarray(frame).save(stream, format='JPEG')
        stream.seek(0)
        datanp.frombuffer(stream.getvalue(), dtype=np.uint8)
        imagecv2.imdecode(data, 1)
        takeTimetime.time()
        fileName"./static/%d.jpg"% (takeTime10)
        cv2.imwrite(fileName, image)
        return fileName
#웹페이지에는영향이없는부분
if __name__== '__main__':  
        count0
        while(True):
                nametakePicture()
                print("fname= %s"name)
                count+= 1
                if(count== 5):
                      break
