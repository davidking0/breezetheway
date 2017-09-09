file = open("Hackathon Data - user.csv","r")
userFile = file.read()
file.close()
file = open("Hackathon Data - trips.csv","r")
tripFile = file.read()
file.close

userAndTrip = []
users = []
trips = []
userAllLists = userFile.split("\n")
tripAllLists = tripFile.split("\n")

for i in userAllLists:
    x = i.split(",")
    users.append(x)

for i in tripAllLists:
    x = i.split(",")
    trips.append(x)

jsonList = []
jsonList.append('{"user":[')
for i in users:
    x = '{"breezecard_id":"' + str(i[0]) + '",' \
                '"first_name":"' + str(i[1]) + '",' \
                '"last_name":"' + str(i[2]) + '",' \
                '"dob":"' + str(i[3]) + '",' \
                '"date_joined":"' + str(i[4]) + '",' \
                '"username":"' + str(i[5]) + '",' \
                '"password":"' + str(i[6]) + '",' \
                '"trips": ['
    jsonList.append(x)
    for j in trips:
        if i[0] == j[1]:
            y = '{"trip_id":"' + str(j[0]) + '",' \
                '"Breezecard_id":"' + str(j[1]) + '",' \
                '"Route_Type":"' +str(j[2]) + '",' \
                '"stop_enter_name":"' + str(j[3]) + '",' \
                '"stop_enter_lat":' + str(j[4]) +',' \
                '"stop_enter_long":' + str(j[5]) + ',' \
                '"stop_exit_name":"' + str(j[6]) + '",' \
                '"stop_exit_lat":' + str(j[7]) + ',' \
                '"stop_exit_long":' + str(j[8]) + ',' \
                '"trip_date":"' + str(j[9]) + '",' \
                '"trip_mileage":' + str(j[10]) + ',' \
                '"trip_duration":' + str(j[11]) + ',' \
                '"fare":' + str(j[12]) + '},'               
            jsonList.append(y)

f = open("output.text", "w")
for item in jsonList:
    f.write(item + "\n")
f.close()

#            for x in trips:
#     if i[0] == x[1]:
#         userAndTrip.append(i + x)       
##            for z in userAndTrip:               
##                print('{"user":[' \
##                '{"breezecard_id":"' + str(z[0]) + '",' \
##                '"first_name":"' + str(z[1]) + '",' \
##                '"last_name":"' + str(z[2]) + '",' \
##                '"dob":"' + str(z[3]) + '",' \
##                '"date_joined":"' + str(z[4]) + '",' \
##                '"username":"' + str(z[5]) + '",' \
##                '"password":"' + str(z[6]) + '",' \
##                '"trips": [' \
##                '{"trip_id":"' + str(z[7]) + '",' \
##                '"Breezecard_id":"' + str(z[8]) + '",' \
##                '"stop_enter_name":"' + str(z[9]) + '",' \
##                '"stop_enter_lat":' + str(z[10]) +',' \
##                '"stop_enter_long":' + str(z[11]) + ',' \
##                '"stop_exit_name":"' + str(z[12]) + '",' \
##                '"stop_exit_lat":' + str(z[13]) + ',' \
##                '"stop_exit_long":' + str(z[14]) + ',' \
##                '"trip_date":"' + str(z[15]) + '",' \
##                '"trip_mileage":' + str(z[16]) + ',' \
##                '"trip_duration":' + str(z[17]) + ',' \
##                '"fare":' + str(z[18]) + '} ]' \
##                '} ]' \
##                '}')
