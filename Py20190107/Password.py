str = "The waterbottle is blue."
str_list = list(str)
str_list

for a in range(24):
    str_list[a] = ord(str_list[a])+5
    #print str_list

    str_list[a] = chr(str_list[a])
    #print str_list

str_convert = "".join(str_list)
print str_convert

print "The added number is 5, solve the password."

    
