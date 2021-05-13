def main():
    openinput = open("triinput3.txt", "r")
    inputlines = openinput.read().splitlines()

    z=0
    while(z < len(inputlines)):
        inputlines[z] = inputlines[z].split()
        z+=1

    triarray = []
    for k in range(len(inputlines)):
        subarray =[]
        for t in range(len(inputlines[k])):
            x = removefirstdigit(inputlines[k][t])
            subarray.append(int(x))
            if ( t+1 == len(inputlines[k])):
                triarray.append(subarray)
            else:
                t+=1
        k+=1

    sum = 0
    flag = 0
    for i in range(len(triarray)):
        if len(triarray[i]) == 1:
            sum += triarray[i][flag]
            i+=1
        elif len(triarray[i]) == 2:
            if isprime(triarray[i][0]) == False and isprime(triarray[i][1]) == True :
                sum+= triarray[i][flag]
                i+=1
            elif isprime(triarray[i][0]) == True and isprime(triarray[i][1]) == False :
                flag = 1
                sum+= triarray[i][flag]
                
                i+=1
            elif isprime(triarray[i][0]) == False and isprime(triarray[i][1]) == False :
                if (triarray[i][0] >= triarray[i][1]):
                    sum+= triarray[i][flag]
                    i+=1
                else:
                    flag = 1
                    sum+= triarray[i][flag]
                    i+=1
            else:
                break
        elif len(triarray[i]) >=3:
            if flag ==0:
                if (triarray[i][flag] >= triarray[i][flag+1]) and isprime(triarray[i][flag]) == False:
                    sum+= triarray[i][flag]
                    i+=1
                elif (triarray[i][flag] <= triarray[i][flag+1]) and isprime(triarray[i][flag+1]) == False:
                    flag = 1
                    sum+= triarray[i][flag]
                    i+=1
            else:
                
                if isprime(triarray[i][flag-1]) == False and isprime(triarray[i][flag]) == True and isprime(triarray[i][flag+1]) == True:
                    sum+= triarray[i][flag-1]
                    flag = triarray[i].index(triarray[i][flag-1])
                    i+=1  
                
                
                elif isprime(triarray[i][flag-1]) == True and isprime(triarray[i][flag]) == False and isprime(triarray[i][flag+1]) == True:
                    sum+= triarray[i][flag]
                    flag = triarray[i].index(triarray[i][flag])
                    i+=1  
                
                elif isprime(triarray[i][flag-1]) == True and isprime(triarray[i][flag]) == True and isprime(triarray[i][flag+1]) == False:
                    sum+= triarray[i][flag+1]
                    flag = triarray[i].index(triarray[i][flag+1])
                    i+=1  

                elif isprime(triarray[i][flag-1]) == False and isprime(triarray[i][flag]) == False and isprime(triarray[i][flag+1]) == False:
                    if (triarray[i][flag-1] >= triarray[i][flag]) and (triarray[i][flag-1] >= triarray[i][flag+1]) :
                        sum+= triarray[i][flag-1]
                        flag = triarray[i].index(triarray[i][flag-1])
                        i+=1  
                    elif (triarray[i][flag] >= triarray[i][flag-1]) and (triarray[i][flag] >= triarray[i][flag+1]) :
                        sum+= triarray[i][flag]
                        flag = triarray[i].index(triarray[i][flag])
                        i+=1 
                    elif (triarray[i][flag+1] >= triarray[i][flag-1]) and (triarray[i][flag+1] >= triarray[i][flag]) :
                        sum+= triarray[i][flag+1]
                        flag = triarray[i].index(triarray[i][flag+1])
                        i+=1 

                elif isprime(triarray[i][flag-1]) == False and isprime(triarray[i][flag]) == False and isprime(triarray[i][flag+1]) == True:
                    if (triarray[i][flag-1] >= triarray[i][flag])  :
                        sum+= triarray[i][flag-1]
                        flag = triarray[i].index(triarray[i][flag-1])
                        i+=1  
                    elif (triarray[i][flag] >= triarray[i][flag-1])  :
                        sum+= triarray[i][flag]
                        flag = triarray[i].index(triarray[i][flag])
                        i+=1 

                elif isprime(triarray[i][flag-1]) == False and isprime(triarray[i][flag]) == True and isprime(triarray[i][flag+1]) == False:
                    if (triarray[i][flag-1] >= triarray[i][flag+1]) :
                        sum+= triarray[i][flag-1]
                        flag = triarray[i].index(triarray[i][flag-1])
                        i+=1  
                    elif (triarray[i][flag+1] >= triarray[i][flag-1]) :
                        sum+= triarray[i][flag+1]
                        flag = triarray[i].index(triarray[i][flag+1])
                        i+=1  
                elif isprime(triarray[i][flag-1]) == True and isprime(triarray[i][flag]) == False and isprime(triarray[i][flag+1]) == False:
                    if (triarray[i][flag] >= triarray[i][flag+1]) :
                        sum+= triarray[i][flag]
                        flag = triarray[i].index(triarray[i][flag])
                        i+=1  
                    elif (triarray[i][flag+1] >= triarray[i][flag]) :
                        sum+= triarray[i][flag+1]
                        flag = triarray[i].index(triarray[i][flag+1])
                        i+=1  
                else:
                    break
                    
    
    for i in range(len(triarray)):
        print(triarray[i])    
    print(sum) #8294




def removefirstdigit(number):
    strnumber = str(number)
    if strnumber[0] == "0":
        strnumber = strnumber[1:]
        number2 = int(strnumber)
        return number2
    else:
        return number

def isprime(number):
    if number > 1:
        for i in range(2,number):
            if (number % i) == 0:  #is not prime
                return False
        else:                      #is  prime
            return True
    else:
        return False

if __name__ == "__main__":
    main()