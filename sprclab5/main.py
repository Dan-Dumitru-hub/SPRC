import paho.mqtt.client as mqtt
import time

broker = "127.0.0.1"
brokerpublic="mqtt.eclipseprojects.io"

def on_log(client,userdata,level,buf):
    print("log: " + buf)


def on_connect(client,userdata, flags,rc):
    if rc == 0:
        print("Connected OK!")
    else:
        print ("Not connected!")

def on_disconnect(client,userdata,flags,rc=0):
    print("Disconnected with status code:" + str(rc))

def on_message(client,userdate, msg):
    topic = msg.topic
    mDecoded = str(msg.payload.decode("utf-8"))
    print("Topic :", topic)
    print("Msg : ", mDecoded)

client = mqtt.Client("ClientTest")

client.on_log = on_log
client.on_disconnect = on_disconnect
client.on_connect = on_connect
client.on_message = on_message

client.connect(brokerpublic)

client.loop_start()

client.subscribe("sprc/chat/DanDumitru")
client.publish("sprc/chat/DanDumitru","hello")
client.publish("sprc/chat/DanDumitru","Done Dan-Dumitru Tipa gr:343C3 nr 4")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:

    client.disconnect()
    client.loop_stop()