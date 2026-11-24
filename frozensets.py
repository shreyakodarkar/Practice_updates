# students = {"name": "shreya", "age": 23}
# print(students)

# students = dict(name="shreya", age=23)
# print(students)

# keys = ["a", "b","c",]
# vals = [1,2,3]
# result = dict(zip(keys,vals))
# print (result)

# a = [("x",10),("y",10)]
# result = dict(a)
# print(result)

# print (dict.fromkeys(["a","b","c"],0))

# a = dict()
# print(a)
# a ={}
# print(a)

# d = {"a":1,"b":2,"c":3}
# d["b"]=4
# print(d)
# print(d.get("z",0))
# print(d.keys()) 
# print (list(d.items()))
# print (len(d))

# a["d"] = 4
# print (a)
# a.update({"a":100})
# print(a)
# a.update(e=5,f=6)
# print(a)
# a.pop("a")
# print(a)
# print(a.clear())

# a.setdefault("g",7)
# print(a)

# marks = {"a":80,"b":50,"c":70}
# total = sum(marks.values())
# average = total/len(marks)
# print(total)
# print(average)

# highest = max(marks.values())
# print(highest)

# minimum = min(marks.values())
# print(minimum)

# a = max(marks,key=marks.get)
# print(a)
# a = sorted(marks)
# b = dict(sorted(marks.items()))
# print(b)
# print (sorted(marks.values()))
# print (list(reversed(marks)))

# d1 = {"a":1,"b":2}
# d2 = {"b":20,"c":30}
# print (d1|d2)
# d1|=d2
# print (d1,d2)

# merged = {**d1,**d2}
# print(merged)

# print("a"in d1)
# print ("z" in d1)

# print ({"a":1,"b":2}=={"b":2,"a":1})
# d1 = d2
# print(d1)
# d2 = {"d":56, "e":98}
# print (d1)
# d3 = d1.copy()
# print (d1)
# d3["c"]=3
# print(d3)

# d = {"x":[1,2]}
# c = d.copy()
# c["x"].append(3)
# print (c)