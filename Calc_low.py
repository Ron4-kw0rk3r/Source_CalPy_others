import sys , math, time
from sys import stdin , stdout
section = ['--incalc' ,'--test','--pow' ,'--rz','--sum', '--rest' ]

def argu_C( rawx ) :
        # print(i)
        if type(rawx) == str:
            print('select :> ', sys.argv[1]+'\n')
            print('|--------------------------------------------------------|')
            
            rawa = int(float(input('number :> ')))
            rawy = int(float(input('number :> ')))
            raiz0=math.sqrt(rawy)
            number0=eval('rawa + rawy')
            number1=eval('rawa - rawy')
            numberA=eval('rawa * rawy')
            numberB=eval('rawa / rawy')
            numberC=eval('rawa % rawy')
            numberD=eval('rawa ** rawy')
            numberE=eval('rawa * raiz0')
            print('sumando ', int(float(number0)) , 'restando' ,int(float(number1)),'mult',int(float(numberA)),'div',int(float(numberB)) ,'mod',int(float(numberC)),'pow',int(numberD),'raiz',int(numberE))
            raww = int(float(input('number :> ')))
            raws = int(float(input('number :> ')))
            raiz1=math.sqrt(raws)
            number0_1=eval('raww + raws')
            number1_1=eval('raww - raws')
            numberA_A=eval('raww * raws')
            numberB_B=eval('raww / raws')
            numberC_C=eval('raww % raws')
            numberD_D=eval('raww ** raws')
            numberE_E=eval('raww * raiz1')
            print('sumando ', int(float(number0_1)) , 'restando' ,int(float(number1_1)),'mult',int(float(numberA_A)),'div',int(float(numberB_B)) ,'mod',int(float(numberC_C)),'pow',int(numberD_D),'raiz',int(numberE_E))
            rawd = int(float(input('number :> ')))
            rawE = int(float(input('number :> ')))
            raiz2=math.sqrt(rawE)
            number00=eval('rawd + rawE')
            number11=eval('rawd - rawE')
            numberAA=eval('rawd * rawE')
            numberBB=eval('rawd / rawE')
            numberCC=eval('rawd % rawE')
            numberDD=eval('rawd ** rawE')
            numberEE=eval('rawd * raiz2')
            print('sumando ', int(float(number00)) , 'restando' ,int(float(number11)),'mult',int(float(numberAA)),'div',int(float(numberBB)) ,'mod',int(float(numberCC)),'pow',int(numberDD),'raiz',int(numberEE))
            rawF = int(float(input('number :> ')))
            rawG = int(float(input('number :> ')))
            raiz3=math.sqrt(rawG)
            number10=eval('rawF + rawG')
            number21=eval('rawF - rawG')
            number3A=eval('rawF * rawG')
            number4B=eval('rawF / rawG')
            number5C=eval('rawF % rawG')
            number6D=eval('rawF ** rawG')
            number7E=eval('rawF * raiz3')
            print('sumando ', int(float(number10)) , 'restando' ,int(float(number21)),'mult',int(float(number3A)),'div',int(float(number4B)) ,'mod',int(float(number5C)),'pow',int(number6D),'raiz',int(number7E))
            rawH = int(float(input('number :> ')))
            rawI = int(float(input('number :> ')))
            raiz4=math.sqrt(rawI)
            numberT0=eval('rawH + rawI')
            numberT1=eval('rawH - rawI')
            numberTA=eval('rawH * rawI')
            numberTB=eval('rawH / rawI')
            numberTC=eval('rawH % rawI')
            numberTD=eval('rawH ** rawI')
            numberTE=eval('rawH * raiz4')
            print('sumando ', int(float(numberT0)) , 'restando' ,int(float(numberT1)),'mult',int(float(numberTA)),'div',int(float(numberTB)) ,'mod',int(float(numberTC)),'pow',int(numberTD),'raiz',int(numberTE))
            print('|---------------------------RESULTADO-----------------------------|')
            time.sleep(0.5)
            print('SUMANDO -  RESTANDO - MULTIPLICANDO - DIVIDIENDO - MODULOS-RESTO - POTENCIA - RAIZ - DIVISION-ENTERA' )
            print('|--------------------------------------------------------||--------------------------------------------------------|')
            sumv=eval('number0 + number1 - numberA * numberB + numberC % numberD ** numberE')
            print('--> [{}] ---> [{}]   ---> [{}]   ---> [{}]      ---> [{}]  "---"  --->[{}]   "---"  --->[{}]'.format(number0, number1, numberA, numberB, numberC , numberD, numberE ))
            print('|--------------------------------------------------------||--------------------------------------------------------|')
            print('--> [{}] ---> [{}]   ---> [{}]   ---> [{}]      ---> [{}]  "---"  --->[{}]   "---"  --->[{}]'.format(number0_1, number1_1, numberA_A, numberB_B, numberC_C , numberD_D, numberE_E ))
            print('|--------------------------------------------------------||--------------------------------------------------------|')
            print('--> [{}] ---> [{}]   ---> [{}]   ---> [{}]      ---> [{}]  "---"  --->[{}]   "---"  --->[{}]'.format(number00, number11, numberAA, numberBB, numberCC , numberDD, numberEE ))
            print('|--------------------------------------------------------||--------------------------------------------------------|')
            print('--> [{}] ---> [{}]   ---> [{}]   ---> [{}]      ---> [{}]  "---"  --->[{}]   "---"  --->[{}]'.format(number10, number21, number3A, number4B, number5C , number6D, number7E ))  
            print('|--------------------------------------------------------||--------------------------------------------------------|')
            print('--> [{}] ---> [{}]   ---> [{}]   ---> [{}]      ---> [{}]  "---"  --->[{}]   "---"  --->[{}]'.format(numberT0, numberT1, numberTA, numberTB, numberTC , numberTD, numberTE ))  
            sys.exit(0)

if __name__ == '__main__':
    for xss in  range(len(sys.argv) ):
        if xss >= 1:
            #print(xss)
            if sys.argv[1] == section[0] :
                argu_C(str(sys.argv[1]))

                sys.exit(0)
    for xtab in range(len(sys.argv)):
        if xtab <= 0 :
                
            print('example 3 + 4 - 5 + 1 / 10')
            rawx = str(input('number :' ))
            if type(rawx) != str:
                print('ERROR now text : example', rawx +'\n')
                sys.exit(0)
            else:
                if type(rawx) == str:          
                    testC = eval(rawx)
                    print('Result = ', testC)
                    sys.exit(1)
                elif type(rawx) != str :
                    print('ERROR -----> ', rawx+'\n' )
                    sys.exit(1)
                # finish