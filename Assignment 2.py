RNA = "AAUGCUAAU"
def frequency_rna(RNA):
    list = []
    test = ""
    num = 0
    AAU = 0
    GCU = 0
    for word in RNA:
        test+=word
        num+=1
        if num == 3:
            list.append(test)
            test=""
            num = 0
    print (list)
    for content in list:
        if content == "AAU":
            AAU = AAU+1
        if content == "GCU":
            GCU = GCU+ 1
    
    print("AAU:"+ str(AAU))
    print("GCU:"+ str(GCU))
frequency_rna(RNA)