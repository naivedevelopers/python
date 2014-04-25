import re
def parse(expr):
    if expr == '':
        return
    if re.compile("^[-+]?[0-9]*\.?[0-9]+$").match(expr):
        return float(expr)
    if expr.rfind('(') > -1:
        c1 = expr.rfind('(')
        c2 = expr.find(')')
        t0 = expr[:c1]
        t1 = expr[c1+1:c2]
        t2 = expr[c2+1:]
        return float(parse(t0+str(parse(t1))+t2)) 
    if expr.find('-') > -1:
        cut = expr.find('-')
        t1 = expr[:cut]
        op = expr[cut:cut+1]
        t2 = expr[cut+1:]
        return float(parse(t1) - parse(t2))
    if expr.find('+') > -1:
        cut = expr.find('+')
        t1 = expr[:cut]
        op = expr[cut:cut+1]
        t2 = expr[cut+1:]
        return float(parse(t1) + parse(t2))
    if expr.find('*') > -1:
        cut = expr.find('*')
        t1 = expr[:cut]
        op = expr[cut:cut+1]
        t2 = expr[cut+1:]
        return float(parse(t1) * parse(t2))
    if expr.find('/') > -1:
        cut = expr.find('/')
        t1 = expr[:cut]
        op = expr[cut:cut+1]
        t2 = expr[cut+1:]
        return float(parse(t1) // parse(t2))
    if expr.find('%') > -1:
        cut = expr.find('%')
        t1 = expr[:cut]
        op = expr[cut:cut+1]
        t2 = expr[cut+1:]
        return float(parse(t1) % parse(t2))
  
def helper(str):
    return parse(str.replace(" ",""))
S1 = "(6*(5+3))/2"
S2 = "6*5+3/2"

print helper(S1)
print helper(S2)
