participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]

hashDict = {} 
sumHash = 0

for part in participant: 
    hashDict[hash(part)] = part
    print(hashDict)
    sumHash += hash(part) 

for part in participant: 
    hashDict[hash(part)] = part 
    sumHash += hash(part) 

print(hashDict.keys())
print(hashDict.values())
print(hashDict.get("josipa"))
print(hash("filipa"))
# for comp in completion: 
#     sumHash -= hash(comp) 

# print(hashDict[sumHash])

