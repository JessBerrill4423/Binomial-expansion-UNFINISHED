
#expanding a + b ^n

indicesString = {
    '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴',
    '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹'
}

def expression(n):
    expression = ""
    numterms = 0
    for i in range(0, n + 1):
        apower = n - i
        bpower = i

        term, numterms = termgenerator(apower, bpower, n, numterms)
        expression = expression + term
    print(expression)
def termgenerator(apower,bpower, n, numterms):

    if n == 0:
        print(1)
        return None
    else:
        for term in range(n+1):
            termtemplate = ""
            a_power = "".join(indicesString[digit] for digit in str(apower))
            b_power = "".join(indicesString[digit] for digit in str(bpower))
            if apower == 1:
                a_power = ""
            if bpower == 1:
                b_power = ""
            if apower == 0 or bpower == 0:
                if apower == 0:
                    if numterms == 0:
                        termtemplate ="b" + b_power
                    else:
                        termtemplate = " + " + "b" + b_power
                elif bpower == 0:
                    if numterms == 0:
                        termtemplate ="a" + a_power
                    else:
                        termtemplate = " + " + "a" + a_power
            else:
                if numterms == 0:
                    termtemplate ="a" + a_power + "b" + b_power
                else:
                    termtemplate = " + " + "a" + a_power + "b" + b_power
            numterms += 1
            return termtemplate, numterms




n = int(input("input power for term (a+b)"))
expression(n)
