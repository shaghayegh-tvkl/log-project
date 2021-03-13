import sys
import gzip
import time

start = time.time()
# print("hello")

api = ["GET", "POST", "PUT", "DELETE", "PATCH"]
try:
    successful_responses = 0
    client_errors = 0
    server_errors = 0

    for i in range(int(sys.argv[1]), int(sys.argv[2])):
        with gzip.open('./logs/haproxy_latest.' + str(i) + '.log.gz','rt') as file:
            for line in file:
                if any(x in line for x in api):
                    # print(line)
                    status = line.split(' ')[10]
                    # print(status)
                    if(status.startswith("2")):
                        successful_responses += 1
                    if(status.startswith("4")):
                        client_errors += 1
                        # print(status)
                    if(status.startswith("5")):
                        server_errors += 1
                        # print(status)

    print("Start Date: " + str(sys.argv[1]) + " - End Date:  "+ str(sys.argv[1]) + ":  2xx: "+ str(successful_responses) + " **  4xx: " + str(client_errors) + " **  5xx: " + str(server_errors))
                
except Exception as e:
    print("An exception occurred: ", e) 

end = time.time()
# print(end - start)