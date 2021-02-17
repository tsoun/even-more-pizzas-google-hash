with open('input.txt', 'r') as input:
    lines = input.readlines()
    info = lines[0].split() # Read info
    pizza_cnt = int(info[0])  
    t2 = int(info[1])  #Teams of 2
    t3 = int(info[2])  #And so on...
    t4 = int(info[3])
    #works as expected
    pizza = {}
    for i in range(1, pizza_cnt + 1):        
        line = lines[i].split()
        pizza[i-1] = []
        p_ingrs = int(line[0])
        for j in range(1, p_ingrs + 1):
            pizza[i-1].append(line[j])
        #print(pizza[i-1])    
    #works as expected
    ingr2 = [] #current ingredients for teams of 2
    cnt2 = 0   #current pizza count for teams of 2 
    score2 = 0 
    ingr3 = [] #and so on...
    cnt3 = 0
    score3 = 0 
    ingr4 = []
    cnt4 = 0
    score4 = 0 
    deliveries = 0
    to2 = []   #pizzas delivered to teams of 2
    buff2 = [] #buffer
    to3 = []   #and so on...
    buff3 = []
    to4 = []
    buff4 = []
    for i in range(1, pizza_cnt + 1):
        temp2 = ingr2[:] #before the new toppings (so the pizzas can br reverted)
        temp3 = ingr3[:]
        temp4 = ingr4[:]
        for ingredient in pizza[i-1]:
            if ingredient not in ingr4 and t4 != 0:
                score4 += 10 #most probably needs tweaking
                ingr4.append(ingredient)
            if ingredient not in ingr3 and t3 != 0:
                score3 += 10
                ingr3.append(ingredient)
            if ingredient not in ingr2 and t2 != 0:
                score2 += 10
                ingr2.append(ingredient)
        if score2 > score3 and score2 > score4 and t2 != 0:
            #print("2")
            cnt2 += 1
            buff2.append(i-1)
            if cnt2 == 2:
                deliveries += 1
                t2 -= 1
                cnt2 = 0
                b2 = buff2[:]
                to2.append(b2)
                buff2.clear()
                ingr2.clear()
            ingr3 = temp3[:]
            ingr4 = temp4[:]
        elif score3 > score4 and score3 >= score2 and t3 != 0:
            #print("3")
            cnt3 += 1
            buff3.append(i-1)
            if cnt3 == 3:
                deliveries += 1
                t3 -= 1
                cnt3 = 0
                b3 = buff3[:]
                to3.append(b3)
                buff3.clear()
                ingr3.clear()
            ingr2 = temp2[:]
            ingr4 = temp4[:]
        elif score4 >= score3 and score4 >= score2 and t4 != 0:
            #print("4")
            cnt4 += 1
            buff4.append(i-1)
            if cnt4 == 4:
                deliveries += 1
                t4 -= 1
                cnt4 = 0
                b4 = buff4[:] #kolopaithon
                to4.append(b4)
                buff4.clear()
                ingr4.clear()
            ingr3 = temp3[:]
            ingr2 = temp2[:]
        #print(score2,score3,score4)
        #print(deliveries, cnt2, cnt3, cnt4)
        score2 = 0
        score3 = 0
        score4 = 0
    #works as expected (kinda)
    #still need to account for the remaining pizzas
    remainder = cnt2 + cnt3 + cnt4
    rem = []
    for i in buff2:
        rem.append(i)
    for i in buff3:
        rem.append(i)
    for i in buff4:
        rem.append(i)
    if remainder == 2:
        to2.append(rem[:])
        deliveries += 1
    if remainder == 3:
        to3.append(rem[:])
        deliveries += 1
    if remainder == 4:
        to4.append(rem[:])
        deliveries += 1
    if remainder == 5:
        to3.append(rem[0:3])
        to2.append(rem[3:5])
        deliveries += 1
    if remainder == 6:
        to3.append(rem[0:3])
        to3.append(rem[3:6])
        deliveries += 1
    

with open ('output.txt', 'w') as output:
    output.write(str(deliveries) + "\n")
    for deliv in to2:
        output.write('2 ')
        for d in deliv:
            output.write(str(d) + ' ')
        output.write("\n")
    for deliv in to3:
        output.write('3 ')
        for d in deliv:
            output.write(str(d) + ' ')
        output.write("\n")
    for deliv in to4:
        output.write('4 ')
        for d in deliv:
            output.write(str(d) + ' ')
        output.write("\n")
print(remainder)
#print(to2)
#print(to3)