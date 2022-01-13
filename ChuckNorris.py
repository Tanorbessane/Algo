def encodageFor(messageBit):
    seq = ""
    count = 0
    count1 = 0
    i= 0
    for i in range(len(messageBit)):
        #print(messageBit[i])
        if (messageBit[i] == "1"):
            if(messageBit[i] == messageBit[i+1]):
                count +=1
                seq +="0 "*count
            else:
                count == 0
        else:
            if(messageBit[i] == messageBit[i+1]):
                count +=1
                seq +="00 "*count
            else:
                count = 0
    return seq
message = "C"

messageBit = ''.join(format(ord(x),'07b')for x in message)
seq= encodageFor(messageBit)
print(messageBit)
print(seq)