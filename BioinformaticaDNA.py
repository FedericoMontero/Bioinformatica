def complentoinverso(dna):
    dnainverso=[]
    for i in reversed(dna):
        if i=="A":
            dnainverso.append("T")
        # Aca estan al mismo nivel
        elif i =="G":
            dnainverso.append("C")
        elif i =="C":
            dnainverso.append("G")
        elif i =="T":
             dnainverso.append("A")
    # En P3 ahora hay que escribir asi:
    print(str.join("", (x for x in dnainverso)))
complentoinverso("AAACCCGGT")
