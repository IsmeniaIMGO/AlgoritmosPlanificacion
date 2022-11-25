def FMQ():
    temp_procesos = copy.deepcopy(procesos)
    queue_rr8 = []
    queue_rr16 = []
    queue_fcfs = []
    fmq_procesos = []
    quantum8 = 8
    quantum16 = 16
    time = 0

    # Ordenar la lista en orden ascendente por hora de llegada x: x [1] se ordena por hora de llegada
    temp_procesos.sort(key = lambda x: x[1], reverse = False)

    while(len(fmq_procesos) < len(procesos)):

        if(len(queue_rr8) == 0):
            queue_rr8.append([temp_procesos.pop(0),0])
            time = queue_rr8[0][0][1]
        
        for p in temp_procesos[::-1]:
            if (p[1] <= time):
                queue_rr8.append([temp_procesos.pop(temp_procesos.index(p))], 0)

        # Ordenar la lista en orden ascendente por hora de llegada x: x [1] se ordena por hora de llegada
        queue_rr8.sort(key = lambda x: x[0][1], reverse = True)

        for p in queue_rr8[::-1]:
            if(p[0][3] == 0):
                p[0][3] = time
            if(p[0][2] <= quantum8):
                time += p[0][2]
                p[0][2] -= p[0][2]
                p[0][4] = time
                fmq_procesos.append(queue_rr8.pop(queue_rr8.index(p)).pop(0))
            elif(p[0][2] > quantum8):
                p[0][2] -= quantum8
                time += quantum8
                p[1] += 1

            if(p[1] >= 8):
                queue_rr16.append([queue_rr8.pop(queue_rr8.index(p)).pop(0),0])

        if(len(queue_rr8) == 0):
            for p in queue_rr16[::-1]:
                if(p[0][2] <= quantum16):
                    time += p[0][2]
                    p[0][2] -= p[0][2]
                    p[0][4] = time
                    fmq_procesos.append(queue_rr16.pop(queue_rr16.index(p)).pop(0))
                elif(p[0][2] > quantum16):
                    p[0][2] -= quantum16
                    time += quantum16
                    p[1] += 1

                if(p[1] >= 8):
                    queue_fcfs.append(queue_rr16.pop(queue_rr16.index(p)).pop(0))

        if(len(queue_rr16) == 0):
            queue_fcfs.sort(key = lambda x: x[1], reverse = True)
            for p in queue_fcfs[::-1]:
                time += p[2]
                p[4] = time
                fmq_procesos.append(queue_fcfs.pop(queue_fcfs.index(p)))

    for proceso in fmq_procesos:
        for p in procesos:
            if(proceso[0] == p[0]):
                proceso[2] = p[2]