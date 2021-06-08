import psutil
import datetime
import redis

while(1):
    print('CPU: ' + str(psutil.cpu_percent(interval=60)))
    print('Memory: ' + str(psutil.virtual_memory().percent))
    print('Disk: ' + str(psutil.disk_usage('/').percent))
    time = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())

    cpu = str(psutil.cpu_percent(interval=1))
    memory =  str(psutil.virtual_memory().percent)
    disk = str(psutil.disk_usage('/').percent)

    redisCPU = redis.Redis(host='37.152.187.31', port=8005, db=0)
    redisMemory = redis.Redis(host='37.152.187.31', port=8005, db=1)
    redisDisk = redis.Redis(host='37.152.187.31', port=8005, db=2)

    redisCPU.set(time, cpu)
    redisMemory.set(time, memory)
    redisDisk.set(time, disk)