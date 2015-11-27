def getValue(key,code):
  keyDict={}
  for val,char in enumerate(key, start=1):
    keyDict[char]=val%10
    cost=""
    for char in code:
      if char in keyDict:
        cost += str(keyDict[char])
  return int(cost)

if __name__ == "__main__":
  print getValue("TRADINGFEW","LGXWEV")
