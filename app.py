import mycamera
fromflask importFlask, render_template, request
app= Flask(__name__)
@app.route('/')
def index():
        #image.html 파일을 mqttio.js 파일에 로딩한다.
        tempmycamera.getTemperature()
        humimycamera.getTemperature()
        lightmycamera.getLight() 
        distancemycamera.measureDistance()
        print("test %d %d"%(temp, humi))
        print("test %d"%(distance))
        print("test %d"%(light))
        returnrender_template('image.html', temp=temp, humi=humi, distance=distance, light=light)

if __name__== "__main__":
        app.run(host='0.0.0.0', port=8080)
