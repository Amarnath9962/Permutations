
data = input("please enter the String : ")
print("The general string",data)
result = []

def Permu_1(data,i,length):
    if i == length:
        result.append("".join(data))
    else:
        for j in range(i,length):
            data[i],data[j] = data[j],data[i]
            Permu_1(data,i+1,length)
            data[i],data[j]=data[j],data[i]

Permu_1(list(data),0,len(data))
print(result)