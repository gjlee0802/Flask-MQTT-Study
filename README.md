# MQTT-Study
학습 자료:   
http://www.steves-internet-guide.com/mqtt-python-beginners-course/   
...   
## Introduction to the Paho Python MQTT Client
### 설치
~~~
$ pip install paho-mqtt
~~~
### Main Client Methods   
- connect() and disconnect()   
- subscribe() and unsubscribe()   
- publish()   
### Client 객체
Client 생성자는 다음과 같이 4개의 파라미터를 받는다. **client_id는 Unique해야하며 필수이다.**
~~~
Client(client_id=””, clean_session=True, userdata=None, protocol=MQTTv311, transport=”tcp”)
~~~
인스턴스를 생성하기 위해 다음과 같이 작성한다.   
~~~
client = mqtt.Client(client_name)
~~~
### Broker나 Server에 연결   
브로커에 연결하는 과정이 필요하다.   
이를 위해 connect method를 이용한다. broker name/IP address만 넘겨주어도 된다.   
~~~
connect(host, port=1883, keepalive=60, bind_address="")
~~~
다음과 같이 작성한다.   
~~~
client.connect(host_name)
~~~
클라이언트 연결 동작은 다음을 참고   
http://www.steves-internet-guide.com/client-connections-python-mqtt/   

### 메시지 발행(Publishing)   
연결했다면 이제 메시지를 발행할 수 있다. topic과 payload만 신경써서 전달해주면 된다.   
~~~
publish(topic, payload=None, qos=0, retain=False)
~~~
payload는 발행하고자 하는 메시지이다. 다음과 같이 작성한다.   
~~~
client.publish("house/light","ON")
~~~

### 예제 코드   
"OFF" 메시지를 "house/main-light" 토픽으로 발행하는 코드이다.   
~~~
import paho.mqtt.client as mqtt #import the client1
broker_address="192.168.1.184" 
#broker_address="iot.eclipse.org" #use external broker
client = mqtt.Client("P1") #create new instance
client.connect(broker_address) #connect to broker
client.publish("house/main-light","OFF")#publish
~~~

### 토픽 구독   
subscribe method를 이용한다.   
~~~
subscribe(topic, qos=0)
~~~

