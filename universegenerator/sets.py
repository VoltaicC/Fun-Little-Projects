import time
l = []
start_time = time.time()

def powerset(xs):
    result = [[]]
    i = 0
    for x in xs:
        newsubsets = [subset + [x] for subset in result]
        result.extend(newsubsets)
    
    return result

#print("generation 1")
theset = (powerset(l))

a = str(theset)
a = a.replace("[]", "0")
a = a.replace("[", "{")
a = a.replace("]", "}")
#print(a)
time1 = time.time() - start_time


#print("generation 2")
theset = powerset(theset)
b = str(theset)
b = b.replace("[]", "0")
b = b.replace("[", "{")
b = b.replace("]", "}")
#print(b)
time2 = (time.time() - start_time) - time1

#print("generation 3")
theset = powerset(theset)
c = str(theset)
c = c.replace("[]", "0")
c = c.replace("[", "{")
c = c.replace("]", "}")
#print(c)
time3 = (time.time() - start_time) - time2

#print("generation 4")
theset = powerset(theset)
d = str(theset)
d = d.replace("[]", "0")
d = d.replace("[", "{")
d = d.replace("]", "}")
#print(d)
time4 = (time.time() - start_time) - time3


#print("generation 5")
theset = powerset(theset)
e = str(theset)
e = e.replace("[]", "0")
e = e.replace("[", "{")
e = e.replace("]", "}")
#print(e)
time5 = (time.time() - start_time) - time4
#print("generation 6")
theset = powerset(theset)
f = str(theset)
f = e.replace("[]", "0")
f = e.replace("[", "{")
f = e.replace("]", "}")
#print(f)
time6 = (time.time() - start_time) - time5
with open ("results.txt", "w") as text_file:
    print("Generation 1 took ", time1, " seconds:",  file=text_file)
    print(a,  file=text_file)
    print("Generation 2 took ", time2, " seconds:", file=text_file)
    print(b,  file=text_file)
    print("Generation 3 took ", time3, " seconds:",  file=text_file)
    print(c,  file=text_file)
    print("Generation 4 took ", time4, " seconds:", file=text_file)
    print(d,  file=text_file)
    print("Generation 5 took ", time5, " seconds:", file=text_file)
    print(e,  file=text_file)
