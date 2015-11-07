import serial, time, io
import redis
from pusher import Pusher

ser = serial.Serial('/dev/ttyUSB0', 9600)

# r = redis.StrictRedis(host='localhost', port=6379, db=0)
# p = r.pubsub()
pusher = Pusher(
    app_id=u'4',
    key=u'765ec374ae0a69f4ce44',
    secret=u'your-pusher-secret',
    host=u'localhost',
    port=4567,
    ssl=False,
)

while 1:
    serial_line = ser.readline()
    movement = serial_line.decode().strip('\r\n')
    print(movement)
    if movement:
        # r.publish('movement', '1')
        try:
            pusher.trigger(u'movement', u'movement-detected', {})
        except:
          pass

ser.close()
