cities = ['Seoul', 'Pusan', 'Incheon', 'Daegu', 'Gwangju']
population = ['10,312,545', '3,567,910', '2,758,296', '2,511,676', '1,454,636']
updown = ['+91,375', '+5,868', '+64,888', '+17,230', '+29,774']

for i in range(len(cities)):
    print("%15s" % cities[i], "%15s" % population[i], "%15s" % updown[i], sep="")

