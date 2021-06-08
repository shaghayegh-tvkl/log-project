# import redis
import plotly.graph_objects as go

# redisCPU = redis.Redis(host='37.152.187.31', port=8005, db=0, charset="utf-8", decode_responses=True)
# redisMemory = redis.Redis(host='37.152.187.31', port=8005, db=1, charset="utf-8", decode_responses=True)
# redisDisk = redis.Redis(host='37.152.187.31', port=8005, db=2, charset="utf-8", decode_responses=True)

# cpuKeys = sorted(redisCPU.keys())
# cpuValues = []

# for x in cpuKeys:
#    cpuValues.append(str(redisCPU.get(x)))

# memoryKeys = sorted(redisMemory.keys())
# memoryValues = []

# for x in memoryKeys:
#     memoryValues.append(str(redisMemory.get(x)))
#     print(memoryValues)

# diskKeys = sorted(redisDisk.keys())
# diskValues = []

# for x in diskKeys:
#    diskValues.append(str(redisDisk.get(x)))


fig = go.Figure()

fig.add_trace(go.Scatter(x=cpuKeys, y=cpuValues,
                    mode='lines',
                    name='lines', line=dict(color='royalblue', width=4)))

fig.add_trace(go.Scatter(x=memoryKeys, y=memoryValues,
                    mode='lines',
                    name='lines', line=dict(color='firebrick', width=4)))

fig.add_trace(go.Scatter(x=diskKeys, y=diskValues,
                    mode='lines',
                    name='lines'))



fig.show()