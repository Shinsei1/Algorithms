

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b


#idee principale: nombre d op = nombre de nombres - 1 

def priorite_mul_div(expr):#je remet en ordre le tableau et extrait des nombres et les op dns le bon sens
    copy_str_expr = expr 
    op_expr = [x for x in expr if x in "/*-+"]
    #a faire dns une boucle mais je laisse en clair:
    expr =expr.replace("*"," ")
    expr =expr.replace("/"," ")
    expr =expr.replace("-"," ")
    expr =expr.replace("+"," ")
    expr = expr.split(" ")
    alterner = []
    for x in range(len(expr)):
        alterner.append(expr[x])
        if x  < len(op_expr):
            alterner.append(op_expr[x])
    alterner_int = []
    for y in alterner:
        try:
            alterner_int.append(int(y))
        except Exception as e:
            alterner_int.append(y)
    
    #au lieu de chercher l ordre, faire juste traiter mult et div avant somme et soustr
    #traiter de gauche a droite
    
    i = 0
    while i < len(alterner_int):
        if alterner_int[i] == "*":
            result = mul(alterner_int[i - 1], alterner_int[i + 1])
            alterner_int.pop(i+1)  
            alterner_int.pop(i-1)  
            alterner_int[i-1] = result
        elif alterner_int[i] == "/":
            result = div(alterner_int[i - 1], alterner_int[i + 1])
            alterner_int.pop(i+1)  
            alterner_int.pop(i-1)  
            alterner_int[i-1] = result
        else:
            i += 1
    i = 0 
    while i < len(alterner_int):
        if alterner_int[i] == "+":
            result = add(alterner_int[i - 1], alterner_int[i + 1])
            alterner_int.pop(i+1)  
            alterner_int.pop(i-1)  
            alterner_int[i-1] = result           
        elif alterner_int[i] == "-":
            result = sub(alterner_int[i - 1], alterner_int[i + 1])
            alterner_int.pop(i+1)  
            alterner_int.pop(i-1)  
            alterner_int[i-1] = result         
        else:
            i += 1
        
    alterner_int = [int(x) for x in alterner_int]

    return f"Résultat de {copy_str_expr} = {int("".join([str(x) for x in alterner_int]))}"
            

print(priorite_mul_div("3*18+2+7/4*9-8*100+2+5+8-985*8/4*55"))

# → [54, '+', 2, '+', 15, '-', 800]
print(priorite_mul_div("10+3"))
print(priorite_mul_div("10+3*5-6/2"))
# → [10, '+', 15, '-', 3]

print(priorite_mul_div("100/10+5*2-1"))
# → [10, '+', 10, '-', 1]

print(priorite_mul_div("8+6/3+2*4"))
# → [8, '+', 2, '+', 8]

print(priorite_mul_div("50-10*2+30/5"))
# → [50, '-', 20, '+', 6]

print(priorite_mul_div("7*3+9/3+6"))
# → [21, '+', 3, '+', 6]

print(priorite_mul_div("1+2+3*4*5"))
# → [1, '+', 2, '+', 60]

print(priorite_mul_div("100/2/5+7"))
# → [10, '+', 7]

print(priorite_mul_div("4*5-6*2+1"))
# → [20, '-', 12, '+', 1]

print(priorite_mul_div("9+8/4*3-2"))
# → [9, '+', 6, '-', 2]