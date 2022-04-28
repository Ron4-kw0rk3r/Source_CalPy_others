#!/usr/bin/env python3.8


#from ast import arg
import sys 
from sys import argv, stdin
# i,port library in test the file program test exponent
import math
from math import pi
# rom tokenize import Triple
#from tkinter import E
#gui_v =  Tk()
#gui_v.mainloop()
def funx_banner():
    ban_func ="""
           ##############################################################################
           #.#      C00000    @@@@@      LL      C0000  UU  UU   PPPPPPP  YYY    YYY  #.#
           #.#     C0       @@@  @@@    LL      C0     UU  UU    PP    PP  YYY  YYY   #.#
           #.#    C0       @@      @@  LL      C0     UU  UU     PPPPPPP     YYYY     #.3
           #.#   C0       @@  @@@ @@@ LL      C0     UU  UU      PPP          YY      #.#
           #.#  C00000   @@     @@@@@ LLLLLLL C00000 UUUUU       PPP          YY      #.#
           ##############################################################################
        """
    print(ban_func +'\n')
    print('\033[1;34m calculator _CLI command \033[1;31m [code] \033[0m programing in \033[1;33m python\033[0m testing release...')
pi=math.pi
one_list = ['--calc' , '--add', '--raice', '-r' , '--help' , '-h', '-log', '-pi', '--version' , '-V' ]
# smbolos aritmeticos
var_sect = ['+', '-', '/', '*', '%' , '//' , '^', '¶' , pi]
verS = '0.1.11' 
# how simbol  raice ¶
# how simbol power ^


def Helpme():
    run= """
        -h || --help  --> imprime la descripcion de los comandos (ayuda)
        --calc    --->   [ valor operador valor ... operador valor ] (cantidad maxima de argumentos 14 )
        --add     ----> [añade un valor al cargar ]
        --raice || -r ----> valor valor ... (max 10 argumentos  ) 
        --log     ----> ( valor valor ... realiza el calculo de lagoritmos max 10 argumentos )
        --pi      ---->  (imprime el valor de pi (tampien funciona como operador ))
        --version ----> imprime la version del programa
    """
    
    print(run)

def Func_xcalc(adding, rawx,  conjunts, rawy):
    if adding == one_list[0]:
        print("selection ---> ", sys.argv[1])
    #if len(sys.argv) >= 5:
        #x = int(sys.argv[1])
        #y = int(sys.argv[2])
        for i in conjunts:
            if i == var_sect[0]:
                print("my calculator : ", rawx , sys.argv[3],  rawy )
                funcx_0 = eval( 'rawx + rawy '+'\n' )
                print("\033[1;32m result\033[0m --->: " , funcx_0)
                sys.exit(0)
            elif i == var_sect[1]:
                print("my calculator : ", rawx , sys.argv[3],  rawy )                
                funcx_1 = eval('rawx - rawy'+'\n')
                print('result :', funcx_1)
                sys.exit(0)
            elif i == var_sect[2]:
                print("my calculator : ", rawx , sys.argv[3],  rawy )                
                funcx_2 = eval('rawx / rawy'+'\n')
                print('result :',float(funcx_2))
                sys.exit(0)
            elif i == var_sect[3]:
                print("my calculator : ", rawx , sys.argv[3],  rawy )                
                funcx_3 = eval('rawx * rawy'+'\n')
                print('result :', funcx_3)
                sys.exit(0)
            elif i == var_sect[4]:
                print("my calculator : ", rawx , sys.argv[3],  rawy )                
                funcx_4 = eval('rawx % rawy' +'\n')
                print('result :',funcx_4)
                sys.exit(0)
            elif i == var_sect[5]:
                print("my calculator : ", rawx , sys.argv[3],  rawy )                
                funcx_5 = eval(float('rawx // rawy'+'\n'))
                print('result :', funcx_5)
                sys.exit(0)
            elif i == var_sect[6]:
                def ExpM( nam , nem ):
                    funcx_6 = math.pow(nam , nem ) 
                    print('my calculator :> ', )
                    print("\033[1;32m result power  in: ---> {}".format(funcx_6)) 
                    # section formating code in test  > programing  power in real number 
                ExpM(int(sys.argv[2]), int(sys.argv[4]))
                sys.exit(0)
            elif i == var_sect[7]:
                def ExpR(raice0  , raice1 ):
                    Factx_R = math.sqrt( raice0 ) 
                    # Factx_R = eval('raice0 * ( raice0 * raice1 )')
                    # print("\033[1;34m Result ---> {} ".format(Factx_R) )
                ExpR(int(sys.argv[2]), int(sys.argv[4]))
                sys.exit(0)
            else:
                print("now _ command error> \033[1;33m ERR0R \033[0m " )
                sys.exit(1)
    else:
        print ("not")
        sys.exit(0)
            
    #print('not  module in_put')
    #sys.exit(0)
    #else:
    #    print('code on loop error')
    #    sys.exit(1)

def Funcx_fourdom (adding , rawx, conjunts ,  rawy , subconjunts,   rawc ):
    if  adding == one_list[0]:
        print("comprovating' ---> ", sys.argv[1] )
         
        for xt in conjunts:
            for z in subconjunts:
                if xt == var_sect[0]:

                    if z == var_sect[0] :
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_0 =eval('rawx + rawy +  rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_0)
                        sys.exit(0)
                    elif var_sect[1] == z :
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_1 =eval('rawx + rawy - rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_1)
                        sys.exit(0)
                    elif z == var_sect[2]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_2 =eval('rawx + rawy  / rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_2)
                        sys.exit(0)
                    elif z == var_sect[3]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_3 =eval('rawx + rawy  * rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_3)
                        sys.exit(0)
                    elif z == var_sect[4]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_4 =eval('rawx + rawy  % rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_4)
                        sys.exit(0)
                    elif z == var_sect[5]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_5 =eval('rawx + rawy  // rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_5)
                        sys.exit(0)
                    elif z == var_sect[6]:
                        def ExpMwob( nam , nem ):
                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                            powcx_0 = math.pow(nam , nem ) 
                            funcx_6 = eval('powcx_0 + rawc'+'\n')
                            print("\033[1;32m result\033[1;31m power \033[0m in: ---> {}".format(funcx_6)) 
                            sys.exit(0)
                            # section formating code in test  > programing  power in real number 
                        ExpMwob(int(sys.argv[4]), int(sys.argv[6]))
                        # sys.exit(0)
                    elif z == var_sect[7]:
                        def ExpR(raice0):
                            Factx_R = math.sqrt( raice0 )
                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                            producT = eval('rawx + rawy * Factx_R'+'\n')
                            print("\033[1;32m result\033[0m --->: ", producT)
                            sys.exit(0)
                        ExpR(int(sys.argv[6]))
                            
                            # funcx_7 =eval('rawx + rawy  ¶ rawc '+'\n' )
                                # Factx_R = eval('raice0 * ( raice0 * raice1 )')
                                # print("\033[1;34m Result ---> {} ".format(Factx_R) )
                        #sys.exit(0)
                    else:
                        #     print("now _ command error> \033[1;33m ERR0R \033[0m " )
                        sys.exit(1)
                if xt == var_sect[1]:
                    if z == var_sect[0]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcxA_0 =eval('rawx - rawy +  rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcxA_0)
                        sys.exit(0)
                    elif z == var_sect[1]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_1 =eval('rawx - rawy - rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_1)
                        sys.exit(0)
                    elif z == var_sect[2]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_2 =eval('rawx - rawy  / rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_2)
                        sys.exit(0)
                    elif z == var_sect[3]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_3 =eval('rawx - rawy  * rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_3)
                        sys.exit(0)
                    elif z == var_sect[4]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_4 =eval('rawx - rawy  % rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_4)
                        sys.exit(0)
                    elif z == var_sect[5]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_5 =eval('rawx - rawy  // rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_5)
                        sys.exit(0)
                    elif z == var_sect[6]:
                        def ExpMwob( nam , nem ):
                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                            powcx_1 = math.pow(nam , nem ) 
                            funcx_5 = eval('rawx - powcx_1 '+'\n')
                            # section formating code in test  > programing  power in real number 
                            print("\033[1;32m result\033[1;31m power \033[0m in: ---> {}".format(funcx_5)) 
                            sys.exit(0)
                        ExpMwob(int(sys.argv[4]), int(sys.argv[6]))
                        # print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        # funcx_6 =eval('rawx - rawy  ^ rawc '+'\n' )
                        # print("\033[1;32m result\033[0m --->: " , funcx_6)
                        # sys.exit(0)
                        # print("my calculator : ", rawx , xt,  rawy , z, rawc )
                    elif z == var_sect[7]:
                        def ExpowR(raice1):
                            Factx1_R = math.sqrt( raice1 )
                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                            producT0 = eval('rawx - rawy * Factx_R'+'\n')
                            print("\033[1;32m result\033[0m --->: ", producT0)
                            sys.exit(0)
                        ExpR(int(sys.argv[6]))
                        #funcx_7 =eval('rawx - rawy  ¶ rawc '+'\n' )
                        #print("\033[1;32m result\033[0m --->: " , funcx_7)
                        #sys.exit(0)
                    else:
                        sys.exit(1)
                        
                elif xt == var_sect[0]:
                    if z == var_sect[0]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_0 =eval('rawx / rawy +  rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_0)
                        sys.exit(0)
                    elif z == var_sect[1]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_1 =eval('rawx / rawy - rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_1)
                        sys.exit(0)
                    elif z == var_sect[2]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_2 =eval('rawx / rawy  / rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_2)
                        sys.exit(0)
                    elif z == var_sect[3]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_3 =eval('rawx / rawy  * rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_3)
                        sys.exit(0)
                    elif z == var_sect[4]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_4 =eval('rawx / rawy  % rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_4)
                        sys.exit(0)
                    elif z == var_sect[5]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_5 =eval('rawx / rawy  // rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_5)
                        sys.exit(0)
                    elif z == var_sect[6]:
                        def ExpMwob0( nam , nem ):
                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                            powcx_1 = math.pow(nam , nem ) 
                            funccx_ = eval('rawx / powcx_1 '+'\n')
                            # section formating code in test  > programing  power in real number 
                            print("\033[1;32m result\033[1;31m power \033[0m in: ---> {}".format(funccx_)) 
                            sys.exit(0)
                        ExpMwob(int(sys.argv[4]), int(sys.argv[6]))
                        #print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        #funcx_6 =eval('rawx / rawy  ^ rawc '+'\n' )
                        #print("\033[1;32m result\033[0m --->: " , funcx_6)
                        # sys.exit(0)
                    elif z == var_sect[7]:
                        def ExpowR1(raice1):
                            Factx_R2 = math.sqrt( raice1 )
                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                            producT1 = eval('rawx / rawy * Factx_R2'+'\n')
                            print("\033[1;32m result\033[0m --->: ", producT1)
                            sys.exit(0)
                        ExpowR1(int(sys.argv[6]))
                    else:
                        sys.exit(1)
                elif xt == var_sect[3]:
                    if z == var_sect[0]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_0 =eval('rawx * rawy +  rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_0)
                        sys.exit(0)
                    elif z == var_sect[1]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_1 =eval('rawx * rawy - rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_1)
                        sys.exit(0)
                    elif z == var_sect[2]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_2 =eval('rawx * rawy  / rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_2)
                        sys.exit(0)
                    elif z == var_sect[3]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_3 =eval('rawx * rawy  * rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_3)
                        sys.exit(0)
                    elif z == var_sect[4]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_4 =eval('rawx * rawy  % rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_4)
                        sys.exit(0)
                    elif z == var_sect[5]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_5 =eval('rawx * rawy  // rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_5)
                        sys.exit(0)
                    elif z == var_sect[6]:
                        def ExpMwob_0( nam , nem ):
                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                            powcx_1 = math.pow(nam , nem ) 
                            funccx_A = eval('rawx * powcx_1 '+'\n')
                            # section formating code in test  > programing  power in real number 
                            print("\033[1;32m result\033[1;31m power \033[0m in: ---> {}".format(funccx_A)) 
                            sys.exit(0)
                        ExpMwob_0(int(sys.argv[4]), int(sys.argv[6]))
                    elif z == var_sect[7]:
                        def ExpowR2(raice2):
                            Factx_R2 = math.sqrt( raice2 )
                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                            producT2 = eval('rawx * rawy * Factx_R2'+'\n')
                            print("\033[1;32m result\033[0m --->: ", producT2)
                            sys.exit(0)
                        ExpowR2(int(sys.argv[6]))
                        # print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        # funcx_7 =eval('rawx * rawy  ¶ rawc '+'\n' )
                        # print("\033[1;32m result\033[0m --->: " , funcx_7)
                        # sys.exit(0)
                    else:
                        sys.exit(1)
                elif xt == var_sect[4]:
                    if z == var_sect[0]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_0 =eval('rawx % rawy +  rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_0)
                        sys.exit(0)
                    elif z == var_sect[1]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_1 =eval('rawx % rawy - rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_1)
                        sys.exit(0)
                    elif z == var_sect[2]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_2 =eval('rawx % rawy  / rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_2)
                        sys.exit(0)
                    elif z == var_sect[3]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_3 =eval('rawx % rawy  * rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_3)
                        sys.exit(0)
                    elif z == var_sect[4]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_4 =eval('rawx % rawy  % rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_4)
                        sys.exit(0)
                    elif z == var_sect[5]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_5 =eval('rawx % rawy  // rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_5)
                        sys.exit(0)
                    elif z == var_sect[6]:
                        def ExpMwob_0( nam , nem ):
                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                            powcxx_1 = math.pow(nam , nem ) 
                            funccx_B = eval('rawx % powcxx_1 '+'\n')
                            # section formating code in test  > programing  power in real number 
                            print("\033[1;32m result\033[1;31m power \033[0m in: ---> {}".format(funccx_B)) 
                            sys.exit(0)
                        ExpMwob_0(int(sys.argv[4]), int(sys.argv[6]))
                    elif z == var_sect[7]:
                        def ExpowR3(raice2):
                            Factx_R3 = math.sqrt( raice2 )
                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                            producT3 = eval('rawx % rawy * Factx_R3'+'\n')
                            print("\033[1;32m result\033[0m --->: ", producT3)
                            sys.exit(0)
                        ExpowR3(int(sys.argv[6]))
                        #print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        # funcx_7 =eval('rawx % rawy  ¶ rawc '+'\n' )
                        # print("\033[1;32m result\033[0m --->: " , funcx_7)
                        # sys.exit(0)
                    else:
                        sys.exit(1)
                elif xt == var_sect[5]:
                    if z == var_sect[0]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_0 =eval('rawx // rawy +  rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_0)
                        sys.exit(0)
                    elif z == var_sect[1]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_1 =eval('rawx // rawy - rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_1)
                        sys.exit(0)
                    elif z == var_sect[2]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_2 =eval('rawx // rawy  / rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_2)
                        sys.exit(0)
                    elif z == var_sect[3]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_3 =eval('rawx // rawy  * rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_3)
                        sys.exit(0)
                    elif z == var_sect[4]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_4 =eval('rawx // rawy  % rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_4)
                        sys.exit(0)
                    elif z == var_sect[5]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_5 =eval('rawx // rawy  // rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_5)
                        sys.exit(0)
                    elif z == var_sect[6]:
                        def ExpMwob_1( nam , nem ):
                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                            powcxx_1 = math.pow(nam , nem ) 
                            funccx_B = eval('rawx // powcxx_1 '+'\n')
                            # section formating code in test  > programing  power in real number 
                            print("\033[1;32m result\033[1;31m power \033[0m in: ---> {}".format(funccx_B)) 
                            sys.exit(0)
                        ExpMwob_1(int(sys.argv[4]), int(sys.argv[6]))
                    elif z == var_sect[7]:
                        def ExpowR4(raice4):
                            Factx_R4 = math.sqrt( raice4 )
                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                            producT4 = eval('rawx // rawy * Factx_R2'+'\n')
                            print("\033[1;32m result\033[0m --->: ", producT4)
                            sys.exit(0)
                        ExpowR4(int(sys.argv[6]))
                    else:
                        sys.exit(1)
                elif xt == var_sect[6]:
                    if z == var_sect[0]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_0 =eval('rawx ** rawy +  rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_0)
                        sys.exit(0)
                    elif z == var_sect[1]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_1 =eval('rawx ** rawy - rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_1)
                        sys.exit(0)
                    elif z == var_sect[2]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_2 =eval('rawx ** rawy  / rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_2)
                        sys.exit(0)
                    elif z == var_sect[3]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_3 =eval('rawx ** rawy  * rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_3)
                        sys.exit(0)
                    elif z == var_sect[4]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_4 =eval('rawx ** rawy  % rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_4)
                        sys.exit(0)
                    elif z == var_sect[5]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_5 =eval('rawx ** rawy  // rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_5)
                        sys.exit(0)
                    elif z == var_sect[6]:
                        def ExpMwob_2( nam , nem ):
                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                            powcxx_1 = math.pow(nam , nem ) 
                            def Exponew_0( rats , pow ):
                                funccx_C = eval('rats ** pow '+'\n')
                                print("\033[1;32m result\033[1;31m power \033[0m in: ---> {}".format(funccx_C)) 
                                # section formating code in test  > programing  power in real number 
                                sys.exit(0)
                            Exponew_0(int(sys.argv[2]), powcxx_1)        
                        ExpMwob_2(int(sys.argv[4]), int(sys.argv[6]))
                    elif z == var_sect[7]:
                        def ExpowR5( raice5 ):
                            Factx_R4 = math.sqrt( raice5 )
                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                            produccT5 = eval('rawx ** rawy * Factx_R4'+'\n')
                            print("\033[1;32m result\033[0m --->: ", produccT5)
                            sys.exit(0)
                        ExpowR4(int(sys.argv[6]))
                        # print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        # funcx_7 =eval('rawx ^ rawy  ¶ rawc '+'\n' )
                        # print("\033[1;32m result\033[0m --->: " , funcx_7)
                        # sys.exit(0)
                    else:
                        sys.exit(1)
                elif xt == var_sect[7]:
                    if z == var_sect[0]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funccxx_0 = math.sqrt( rawy )  
                        func_1 = eval('rawx * funccxx_0 +  rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , func_1)
                        sys.exit(0)
                    elif z == var_sect[1]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funccxx_1 = math.sqrt( rawy )
                        funcc_2 = eval('rawx * funccxx_1 - rawc '+'\n' ) 
                        print("\033[1;32m result\033[0m --->: " , funcc_2 )
                        sys.exit(0)
                            
                    elif z == var_sect[2]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funccxx_2 = math.sqrt( rawy )
                        funcc_3 =eval('rawx * funccxx_2  / rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcc_3)
                        sys.exit(0)
                    elif z == var_sect[3]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funccxx_3 = math.sqrt( rawy )
                        funcc_4 =eval('rawx * funccxx_3 * rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcc_4)
                        sys.exit(0)
                    elif z == var_sect[4]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funccxx_4 = math.sqrt( rawy )
                        funcc_5 =eval('rawx * funccxx_4  % rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcc_5 )
                        sys.exit(0)
                    elif z == var_sect[5]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funccxx_5 = math.sqrt( rawy )
                        funcc_6 =eval('rawx * funccxx_6  // rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcc_6 )
                        sys.exit(0)
                    elif z == var_sect[6]:
                        def ExpMwob_4( nam , nem ):
                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                            powcxx_2 = math.pow(nam , nem )
                            funccxx_7 = math.sqrt(powcxx_2) 
                            funccxx_D = eval('rawx * funccxx_7 '+'\n')
                            print("\033[1;32m result\033[1;31m power \033[0m in: ---> {}".format(funccxx_D)) 
                            # section formating code in test  > programing  power in real number 
                            sys.exit(0)
                        ExpMwob_4(int(sys.argv[4]), int(sys.argv[6]))
                            
                        #print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        # funccxx_6 = math.sqrt( rawy )
                        # funcc_6 =eval('rawx * funccxx_6  ** rawc '+'\n' )
                        # print("\033[1;32m result\033[0m --->: " , funcc_6)
                        # sys.exit(0)
                    elif z == var_sect[7]:
                        def ExpowR6( raiceA , raice6 ):
                            Factx_R5 = math.sqrt( raice6 )
                            Factxx_RA = math.sqrt( raiceA ) 
                            test_v = Factx_R5 + Factxx_RA
                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                            produccT5 = eval('rawx * test_v '+'\n')
                            print("\033[1;32m result\033[0m --->: ", produccT5)
                            sys.exit(0)
                        ExpowR6(int(sys.argv[4]), int(sys.argv[6]))
                        #print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        #funcx_7 =eval('rawx ¶ rawy  ¶ rawc '+'\n' )
                        #print("\033[1;32m result\033[0m --->: " , funcx_7)
                        #sys.exit(0)
                    else:
                        sys.exit(1)
                        
                # all operators se__ _now __ ________
        #    sys.exit(1)
    # stderr('hellow')        
# new_ line --------------------------------------------------------------
# ------------------------------------------------------------------------------
def Funcx_fivedom(adding , rawx, conjunts ,  rawy , subconjunts,   rawc , treconjunts ,rawv ):
    for xt in conjunts:
        for z in subconjunts:
            for tryx in treconjunts:
                if xt == var_sect[0]:
                    if z == var_sect[0] :
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_0 =eval('rawx + rawy +  rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_0)
                        sys.exit(0)
                    elif var_sect[1] == z :
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_1 =eval('rawx + rawy - rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_1)
                        sys.exit(0)
                    elif z == var_sect[2]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_2 =eval('rawx + rawy  / rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_2)
                        sys.exit(0)
                    elif z == var_sect[3]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_3 =eval('rawx + rawy  * rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_3)
                        sys.exit(0)
                    elif z == var_sect[4]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_4 =eval('rawx + rawy  % rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_4)
                        sys.exit(0)
                    elif z == var_sect[5]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_5 =eval('rawx + rawy  // rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_5)
                        sys.exit(0)
                    elif z == var_sect[6]:
                        def ExpMwob( nam , nem ):
                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                            powcx_0 = math.pow(nam , nem ) 
                            funcx_6 = eval('powcx_0 + rawc'+'\n')
                            print("\033[1;32m result\033[1;31m power \033[0m in: ---> {}".format(funcx_6)) 
                            sys.exit(0)
                            # section formating code in test  > programing  power in real number 
                        ExpMwob(int(sys.argv[4]), int(sys.argv[6]))
                        # sys.exit(0)
                    elif z == var_sect[7]:
                        def ExpR(raice0):
                            Factx_R = math.sqrt( raice0 )
                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                            producT = eval('rawx + rawy * Factx_R'+'\n')
                            print("\033[1;32m result\033[0m --->: ", producT)
                            sys.exit(0)
                        ExpR(int(sys.argv[6]))
                            
                            # funcx_7 =eval('rawx + rawy  ¶ rawc '+'\n' )
                                # Factx_R = eval('raice0 * ( raice0 * raice1 )')
                                # print("\033[1;34m Result ---> {} ".format(Factx_R) )
                        #sys.exit(0)
                    else:
                        #     print("now _ command error> \033[1;33m ERR0R \033[0m " )
                        sys.exit(1)
                if xt == var_sect[1]:
                    if z == var_sect[0]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcxA_0 =eval('rawx - rawy +  rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcxA_0)
                        sys.exit(0)
                    elif z == var_sect[1]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_1 =eval('rawx - rawy - rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_1)
                        sys.exit(0)
                    elif z == var_sect[2]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_2 =eval('rawx - rawy  / rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_2)
                        sys.exit(0)
                    elif z == var_sect[3]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_3 =eval('rawx - rawy  * rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_3)
                        sys.exit(0)
                    elif z == var_sect[4]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_4 =eval('rawx - rawy  % rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_4)
                        sys.exit(0)
                    elif z == var_sect[5]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_5 =eval('rawx - rawy  // rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_5)
                        sys.exit(0)
                    elif z == var_sect[6]:
                        def ExpMwob( nam , nem ):
                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                            powcx_1 = math.pow(nam , nem ) 
                            funcx_5 = eval('rawx - powcx_1 '+'\n')
                            # section formating code in test  > programing  power in real number 
                            print("\033[1;32m result\033[1;31m power \033[0m in: ---> {}".format(funcx_5)) 
                            sys.exit(0)
                        ExpMwob(int(sys.argv[4]), int(sys.argv[6]))
                        # print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        # funcx_6 =eval('rawx - rawy  ^ rawc '+'\n' )
                        # print("\033[1;32m result\033[0m --->: " , funcx_6)
                        # sys.exit(0)
                        # print("my calculator : ", rawx , xt,  rawy , z, rawc )
                    elif z == var_sect[7]:
                        def ExpowR(raice1):
                            Factx1_R = math.sqrt( raice1 )
                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                            producT0 = eval('rawx - rawy * Factx_R'+'\n')
                            print("\033[1;32m result\033[0m --->: ", producT0)
                            sys.exit(0)
                        ExpR(int(sys.argv[6]))
                        #funcx_7 =eval('rawx - rawy  ¶ rawc '+'\n' )
                        #print("\033[1;32m result\033[0m --->: " , funcx_7)
                        #sys.exit(0)
                    else:
                        sys.exit(1)
                        
                elif xt == var_sect[0]:
                    if z == var_sect[0]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_0 =eval('rawx / rawy +  rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_0)
                        sys.exit(0)
                    elif z == var_sect[1]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_1 =eval('rawx / rawy - rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_1)
                        sys.exit(0)
                    elif z == var_sect[2]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_2 =eval('rawx / rawy  / rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_2)
                        sys.exit(0)
                    elif z == var_sect[3]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_3 =eval('rawx / rawy  * rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_3)
                        sys.exit(0)
                    elif z == var_sect[4]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_4 =eval('rawx / rawy  % rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_4)
                        sys.exit(0)
                    elif z == var_sect[5]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_5 =eval('rawx / rawy  // rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_5)
                        sys.exit(0)
                    elif z == var_sect[6]:
                        def ExpMwob0( nam , nem ):
                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                            powcx_1 = math.pow(nam , nem ) 
                            funccx_ = eval('rawx / powcx_1 '+'\n')
                            # section formating code in test  > programing  power in real number 
                            print("\033[1;32m result\033[1;31m power \033[0m in: ---> {}".format(funccx_)) 
                            sys.exit(0)
                        ExpMwob(int(sys.argv[4]), int(sys.argv[6]))
                        #print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        #funcx_6 =eval('rawx / rawy  ^ rawc '+'\n' )
                        #print("\033[1;32m result\033[0m --->: " , funcx_6)
                        # sys.exit(0)
                    elif z == var_sect[7]:
                        def ExpowR1(raice1):
                            Factx_R2 = math.sqrt( raice1 )
                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                            producT1 = eval('rawx / rawy * Factx_R2'+'\n')
                            print("\033[1;32m result\033[0m --->: ", producT1)
                            sys.exit(0)
                        ExpowR1(int(sys.argv[6]))
                    else:
                        sys.exit(1)
                elif xt == var_sect[3]:
                    if z == var_sect[0]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_0 =eval('rawx * rawy +  rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_0)
                        sys.exit(0)
                    elif z == var_sect[1]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_1 =eval('rawx * rawy - rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_1)
                        sys.exit(0)
                    elif z == var_sect[2]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_2 =eval('rawx * rawy  / rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_2)
                        sys.exit(0)
                    elif z == var_sect[3]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_3 =eval('rawx * rawy  * rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_3)
                        sys.exit(0)
                    elif z == var_sect[4]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_4 =eval('rawx * rawy  % rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_4)
                        sys.exit(0)
                    elif z == var_sect[5]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_5 =eval('rawx * rawy  // rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_5)
                        sys.exit(0)
                    elif z == var_sect[6]:
                        def ExpMwob_0( nam , nem ):
                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                            powcx_1 = math.pow(nam , nem ) 
                            funccx_A = eval('rawx * powcx_1 '+'\n')
                            # section formating code in test  > programing  power in real number 
                            print("\033[1;32m result\033[1;31m power \033[0m in: ---> {}".format(funccx_A)) 
                            sys.exit(0)
                        ExpMwob_0(int(sys.argv[4]), int(sys.argv[6]))
                    elif z == var_sect[7]:
                        def ExpowR2(raice2):
                            Factx_R2 = math.sqrt( raice2 )
                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                            producT2 = eval('rawx * rawy * Factx_R2'+'\n')
                            print("\033[1;32m result\033[0m --->: ", producT2)
                            sys.exit(0)
                        ExpowR2(int(sys.argv[6]))
                        # print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        # funcx_7 =eval('rawx * rawy  ¶ rawc '+'\n' )
                        # print("\033[1;32m result\033[0m --->: " , funcx_7)
                        # sys.exit(0)
                    else:
                        sys.exit(1)
                elif xt == var_sect[4]:
                    if z == var_sect[0]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_0 =eval('rawx % rawy +  rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_0)
                        sys.exit(0)
                    elif z == var_sect[1]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_1 =eval('rawx % rawy - rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_1)
                        sys.exit(0)
                    elif z == var_sect[2]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_2 =eval('rawx % rawy  / rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_2)
                        sys.exit(0)
                    elif z == var_sect[3]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_3 =eval('rawx % rawy  * rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_3)
                        sys.exit(0)
                    elif z == var_sect[4]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_4 =eval('rawx % rawy  % rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_4)
                        sys.exit(0)
                    elif z == var_sect[5]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_5 =eval('rawx % rawy  // rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_5)
                        sys.exit(0)
                    elif z == var_sect[6]:
                        def ExpMwob_0( nam , nem ):
                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                            powcxx_1 = math.pow(nam , nem ) 
                            funccx_B = eval('rawx % powcxx_1 '+'\n')
                            # section formating code in test  > programing  power in real number 
                            print("\033[1;32m result\033[1;31m power \033[0m in: ---> {}".format(funccx_B)) 
                            sys.exit(0)
                        ExpMwob_0(int(sys.argv[4]), int(sys.argv[6]))
                    elif z == var_sect[7]:
                        def ExpowR3(raice2):
                            Factx_R3 = math.sqrt( raice2 )
                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                            producT3 = eval('rawx % rawy * Factx_R3'+'\n')
                            print("\033[1;32m result\033[0m --->: ", producT3)
                            sys.exit(0)
                        ExpowR3(int(sys.argv[6]))
                        #print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        # funcx_7 =eval('rawx % rawy  ¶ rawc '+'\n' )
                        # print("\033[1;32m result\033[0m --->: " , funcx_7)
                        # sys.exit(0)
                    else:
                        sys.exit(1)
                elif xt == var_sect[5]:
                    if z == var_sect[0]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_0 =eval('rawx // rawy +  rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_0)
                        sys.exit(0)
                    elif z == var_sect[1]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_1 =eval('rawx // rawy - rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_1)
                        sys.exit(0)
                    elif z == var_sect[2]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_2 =eval('rawx // rawy  / rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_2)
                        sys.exit(0)
                    elif z == var_sect[3]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_3 =eval('rawx // rawy  * rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_3)
                        sys.exit(0)
                    elif z == var_sect[4]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_4 =eval('rawx // rawy  % rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_4)
                        sys.exit(0)
                    elif z == var_sect[5]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_5 =eval('rawx // rawy  // rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_5)
                        sys.exit(0)
                    elif z == var_sect[6]:
                        def ExpMwob_1( nam , nem ):
                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                            powcxx_1 = math.pow(nam , nem ) 
                            funccx_B = eval('rawx // powcxx_1 '+'\n')
                            # section formating code in test  > programing  power in real number 
                            print("\033[1;32m result\033[1;31m power \033[0m in: ---> {}".format(funccx_B)) 
                            sys.exit(0)
                        ExpMwob_1(int(sys.argv[4]), int(sys.argv[6]))
                    elif z == var_sect[7]:
                        def ExpowR4(raice4):
                            Factx_R4 = math.sqrt( raice4 )
                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                            producT4 = eval('rawx // rawy * Factx_R2'+'\n')
                            print("\033[1;32m result\033[0m --->: ", producT4)
                            sys.exit(0)
                        ExpowR4(int(sys.argv[6]))
                    else:
                        sys.exit(1)
                elif xt == var_sect[6]:
                    if z == var_sect[0]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_0 =eval('rawx ** rawy +  rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_0)
                        sys.exit(0)
                    elif z == var_sect[1]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_1 =eval('rawx ** rawy - rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_1)
                        sys.exit(0)
                    elif z == var_sect[2]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_2 =eval('rawx ** rawy  / rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_2)
                        sys.exit(0)
                    elif z == var_sect[3]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_3 =eval('rawx ** rawy  * rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_3)
                        sys.exit(0)
                    elif z == var_sect[4]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_4 =eval('rawx ** rawy  % rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_4)
                        sys.exit(0)
                    elif z == var_sect[5]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funcx_5 =eval('rawx ** rawy  // rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcx_5)
                        sys.exit(0)
                    elif z == var_sect[6]:
                        def ExpMwob_2( nam , nem ):
                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                            powcxx_1 = math.pow(nam , nem ) 
                            def Exponew_0( rats , pow ):
                                funccx_C = eval('rats ** pow '+'\n')
                                print("\033[1;32m result\033[1;31m power \033[0m in: ---> {}".format(funccx_C)) 
                                # section formating code in test  > programing  power in real number 
                                sys.exit(0)
                            Exponew_0(int(sys.argv[2]), powcxx_1)        
                        ExpMwob_2(int(sys.argv[4]), int(sys.argv[6]))
                    elif z == var_sect[7]:
                        def ExpowR5( raice5 ):
                            Factx_R4 = math.sqrt( raice5 )
                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                            produccT5 = eval('rawx ** rawy * Factx_R4'+'\n')
                            print("\033[1;32m result\033[0m --->: ", produccT5)
                            sys.exit(0)
                        ExpowR4(int(sys.argv[6]))
                        # print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        # funcx_7 =eval('rawx ^ rawy  ¶ rawc '+'\n' )
                        # print("\033[1;32m result\033[0m --->: " , funcx_7)
                        # sys.exit(0)
                    else:
                        sys.exit(1)
                elif xt == var_sect[7]:
                    if z == var_sect[0]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funccxx_0 = math.sqrt( rawy )  
                        func_1 = eval('rawx * funccxx_0 +  rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , func_1)
                        sys.exit(0)
                    elif z == var_sect[1]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funccxx_1 = math.sqrt( rawy )
                        funcc_2 = eval('rawx * funccxx_1 - rawc '+'\n' ) 
                        print("\033[1;32m result\033[0m --->: " , funcc_2 )
                        sys.exit(0)
                            
                    elif z == var_sect[2]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funccxx_2 = math.sqrt( rawy )
                        funcc_3 =eval('rawx * funccxx_2  / rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcc_3)
                        sys.exit(0)
                    elif z == var_sect[3]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funccxx_3 = math.sqrt( rawy )
                        funcc_4 =eval('rawx * funccxx_3 * rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcc_4)
                        sys.exit(0)
                    elif z == var_sect[4]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funccxx_4 = math.sqrt( rawy )
                        funcc_5 =eval('rawx * funccxx_4  % rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcc_5 )
                        sys.exit(0)
                    elif z == var_sect[5]:
                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        funccxx_5 = math.sqrt( rawy )
                        funcc_6 =eval('rawx * funccxx_6  // rawc '+'\n' )
                        print("\033[1;32m result\033[0m --->: " , funcc_6 )
                        sys.exit(0)
                    elif z == var_sect[6]:
                        def ExpMwob_4( nam , nem ):
                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                            powcxx_2 = math.pow(nam , nem )
                            funccxx_7 = math.sqrt(powcxx_2) 
                            funccxx_D = eval('rawx * funccxx_7 '+'\n')
                            print("\033[1;32m result\033[1;31m power \033[0m in: ---> {}".format(funccxx_D)) 
                            # section formating code in test  > programing  power in real number 
                            sys.exit(0)
                        ExpMwob_4(int(sys.argv[4]), int(sys.argv[6]))
                            
                        #print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        # funccxx_6 = math.sqrt( rawy )
                        # funcc_6 =eval('rawx * funccxx_6  ** rawc '+'\n' )
                        # print("\033[1;32m result\033[0m --->: " , funcc_6)
                        # sys.exit(0)
                    elif z == var_sect[7]:
                        def ExpowR6( raiceA , raice6 ):
                            Factx_R5 = math.sqrt( raice6 )
                            Factxx_RA = math.sqrt( raiceA ) 
                            test_v = Factx_R5 + Factxx_RA
                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                            produccT5 = eval('rawx * test_v '+'\n')
                            print("\033[1;32m result\033[0m --->: ", produccT5)
                            sys.exit(0)
                        ExpowR6(int(sys.argv[4]), int(sys.argv[6]))
                        #print("my calculator : ", rawx , xt,  rawy , z, rawc )
                        #funcx_7 =eval('rawx ¶ rawy  ¶ rawc '+'\n' )
                        #print("\033[1;32m result\033[0m --->: " , funcx_7)
                        #sys.exit(0)
                    else:
                        sys.exit(1)
    #elif i == var_sect[6]:
    
# new_ line *-----------------------------------------------------*
# ----------------------------------------------------------------------------
def Funcx_sixdom(adding , rawx, conjunts ,  rawy , subconjunts,   rawc , treconjuts , rawb ,fourconjunts,  raws ):
    for xt in conjunts:
        for z in subconjunts:
            for tryx in treconjuts:
                for fourx in fourconjunts:
                    if xt == var_sect[0]:
                        if z == var_sect[0] :
                            if tryx == var_sect[0]:
                                if fourconjunts == var_sect[0]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funcx_0 =eval('rawx + rawy +  rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcx_0)
                                    sys.exit(0)
                                elif var_sect[1] == z :
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funcx_1 =eval('rawx + rawy - rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcx_1)
                                    sys.exit(0)
                                elif z == var_sect[2]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funcx_2 =eval('rawx + rawy  / rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcx_2)
                                    sys.exit(0)
                                elif z == var_sect[3]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funcx_3 =eval('rawx + rawy  * rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcx_3)
                                    sys.exit(0)
                                elif z == var_sect[4]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funcx_4 =eval('rawx + rawy  % rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcx_4)
                                    sys.exit(0)
                                elif z == var_sect[5]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funcx_5 =eval('rawx + rawy  // rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcx_5)
                                    sys.exit(0)
                                elif z == var_sect[6]:
                                    def ExpMwob( nam , nem ):
                                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                        powcx_0 = math.pow(nam , nem ) 
                                        funcx_6 = eval('powcx_0 + rawc'+'\n')
                                        print("\033[1;32m result\033[1;31m power \033[0m in: ---> {}".format(funcx_6)) 
                                        sys.exit(0)
                                        # section formating code in test  > programing  power in real number 
                                    ExpMwob(int(sys.argv[4]), int(sys.argv[6]))
                                    # sys.exit(0)
                                elif z == var_sect[7]:
                                    def ExpR(raice0):
                                        Factx_R = math.sqrt( raice0 )
                                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                        producT = eval('rawx + rawy * Factx_R'+'\n')
                                        print("\033[1;32m result\033[0m --->: ", producT)
                                        sys.exit(0)
                                    ExpR(int(sys.argv[6]))
                                        
                                        # funcx_7 =eval('rawx + rawy  ¶ rawc '+'\n' )
                                            # Factx_R = eval('raice0 * ( raice0 * raice1 )')
                                            # print("\033[1;34m Result ---> {} ".format(Factx_R) )
                                    #sys.exit(0)
                                else:
                                    #     print("now _ command error> \033[1;33m ERR0R \033[0m " )
                                    sys.exit(1)
                            if xt == var_sect[1]:
                                if z == var_sect[0]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funcxA_0 =eval('rawx - rawy +  rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcxA_0)
                                    sys.exit(0)
                                elif z == var_sect[1]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funcx_1 =eval('rawx - rawy - rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcx_1)
                                    sys.exit(0)
                                elif z == var_sect[2]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funcx_2 =eval('rawx - rawy  / rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcx_2)
                                    sys.exit(0)
                                elif z == var_sect[3]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funcx_3 =eval('rawx - rawy  * rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcx_3)
                                    sys.exit(0)
                                elif z == var_sect[4]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funcx_4 =eval('rawx - rawy  % rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcx_4)
                                    sys.exit(0)
                                elif z == var_sect[5]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funcx_5 =eval('rawx - rawy  // rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcx_5)
                                    sys.exit(0)
                                elif z == var_sect[6]:
                                    def ExpMwob( nam , nem ):
                                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                        powcx_1 = math.pow(nam , nem ) 
                                        funcx_5 = eval('rawx - powcx_1 '+'\n')
                                        # section formating code in test  > programing  power in real number 
                                        print("\033[1;32m result\033[1;31m power \033[0m in: ---> {}".format(funcx_5)) 
                                        sys.exit(0)
                                    ExpMwob(int(sys.argv[4]), int(sys.argv[6]))
                                    # print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    # funcx_6 =eval('rawx - rawy  ^ rawc '+'\n' )
                                    # print("\033[1;32m result\033[0m --->: " , funcx_6)
                                    # sys.exit(0)
                                    # print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                elif z == var_sect[7]:
                                    def ExpowR(raice1):
                                        Factx1_R = math.sqrt( raice1 )
                                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                        producT0 = eval('rawx - rawy * Factx_R'+'\n')
                                        print("\033[1;32m result\033[0m --->: ", producT0)
                                        sys.exit(0)
                                    ExpR(int(sys.argv[6]))
                                    #funcx_7 =eval('rawx - rawy  ¶ rawc '+'\n' )
                                    #print("\033[1;32m result\033[0m --->: " , funcx_7)
                                    #sys.exit(0)
                                else:
                                    sys.exit(1)
                                    
                            elif xt == var_sect[0]:
                                if z == var_sect[0]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funcx_0 =eval('rawx / rawy +  rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcx_0)
                                    sys.exit(0)
                                elif z == var_sect[1]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funcx_1 =eval('rawx / rawy - rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcx_1)
                                    sys.exit(0)
                                elif z == var_sect[2]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funcx_2 =eval('rawx / rawy  / rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcx_2)
                                    sys.exit(0)
                                elif z == var_sect[3]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funcx_3 =eval('rawx / rawy  * rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcx_3)
                                    sys.exit(0)
                                elif z == var_sect[4]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funcx_4 =eval('rawx / rawy  % rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcx_4)
                                    sys.exit(0)
                                elif z == var_sect[5]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funcx_5 =eval('rawx / rawy  // rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcx_5)
                                    sys.exit(0)
                                elif z == var_sect[6]:
                                    def ExpMwob0( nam , nem ):
                                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                        powcx_1 = math.pow(nam , nem ) 
                                        funccx_ = eval('rawx / powcx_1 '+'\n')
                                        # section formating code in test  > programing  power in real number 
                                        print("\033[1;32m result\033[1;31m power \033[0m in: ---> {}".format(funccx_)) 
                                        sys.exit(0)
                                    ExpMwob(int(sys.argv[4]), int(sys.argv[6]))
                                    #print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    #funcx_6 =eval('rawx / rawy  ^ rawc '+'\n' )
                                    #print("\033[1;32m result\033[0m --->: " , funcx_6)
                                    # sys.exit(0)
                                elif z == var_sect[7]:
                                    def ExpowR1(raice1):
                                        Factx_R2 = math.sqrt( raice1 )
                                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                        producT1 = eval('rawx / rawy * Factx_R2'+'\n')
                                        print("\033[1;32m result\033[0m --->: ", producT1)
                                        sys.exit(0)
                                    ExpowR1(int(sys.argv[6]))
                                else:
                                    sys.exit(1)
                            elif xt == var_sect[3]:
                                if z == var_sect[0]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funcx_0 =eval('rawx * rawy +  rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcx_0)
                                    sys.exit(0)
                                elif z == var_sect[1]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funcx_1 =eval('rawx * rawy - rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcx_1)
                                    sys.exit(0)
                                elif z == var_sect[2]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funcx_2 =eval('rawx * rawy  / rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcx_2)
                                    sys.exit(0)
                                elif z == var_sect[3]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funcx_3 =eval('rawx * rawy  * rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcx_3)
                                    sys.exit(0)
                                elif z == var_sect[4]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funcx_4 =eval('rawx * rawy  % rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcx_4)
                                    sys.exit(0)
                                elif z == var_sect[5]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funcx_5 =eval('rawx * rawy  // rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcx_5)
                                    sys.exit(0)
                                elif z == var_sect[6]:
                                    def ExpMwob_0( nam , nem ):
                                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                        powcx_1 = math.pow(nam , nem ) 
                                        funccx_A = eval('rawx * powcx_1 '+'\n')
                                        # section formating code in test  > programing  power in real number 
                                        print("\033[1;32m result\033[1;31m power \033[0m in: ---> {}".format(funccx_A)) 
                                        sys.exit(0)
                                    ExpMwob_0(int(sys.argv[4]), int(sys.argv[6]))
                                elif z == var_sect[7]:
                                    def ExpowR2(raice2):
                                        Factx_R2 = math.sqrt( raice2 )
                                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                        producT2 = eval('rawx * rawy * Factx_R2'+'\n')
                                        print("\033[1;32m result\033[0m --->: ", producT2)
                                        sys.exit(0)
                                    ExpowR2(int(sys.argv[6]))
                                    # print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    # funcx_7 =eval('rawx * rawy  ¶ rawc '+'\n' )
                                    # print("\033[1;32m result\033[0m --->: " , funcx_7)
                                    # sys.exit(0)
                                else:
                                    sys.exit(1)
                            elif xt == var_sect[4]:
                                if z == var_sect[0]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funcx_0 =eval('rawx % rawy +  rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcx_0)
                                    sys.exit(0)
                                elif z == var_sect[1]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funcx_1 =eval('rawx % rawy - rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcx_1)
                                    sys.exit(0)
                                elif z == var_sect[2]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funcx_2 =eval('rawx % rawy  / rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcx_2)
                                    sys.exit(0)
                                elif z == var_sect[3]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funcx_3 =eval('rawx % rawy  * rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcx_3)
                                    sys.exit(0)
                                elif z == var_sect[4]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funcx_4 =eval('rawx % rawy  % rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcx_4)
                                    sys.exit(0)
                                elif z == var_sect[5]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funcx_5 =eval('rawx % rawy  // rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcx_5)
                                    sys.exit(0)
                                elif z == var_sect[6]:
                                    def ExpMwob_0( nam , nem ):
                                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                        powcxx_1 = math.pow(nam , nem ) 
                                        funccx_B = eval('rawx % powcxx_1 '+'\n')
                                        # section formating code in test  > programing  power in real number 
                                        print("\033[1;32m result\033[1;31m power \033[0m in: ---> {}".format(funccx_B)) 
                                        sys.exit(0)
                                    ExpMwob_0(int(sys.argv[4]), int(sys.argv[6]))
                                elif z == var_sect[7]:
                                    def ExpowR3(raice2):
                                        Factx_R3 = math.sqrt( raice2 )
                                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                        producT3 = eval('rawx % rawy * Factx_R3'+'\n')
                                        print("\033[1;32m result\033[0m --->: ", producT3)
                                        sys.exit(0)
                                    ExpowR3(int(sys.argv[6]))
                                    #print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    # funcx_7 =eval('rawx % rawy  ¶ rawc '+'\n' )
                                    # print("\033[1;32m result\033[0m --->: " , funcx_7)
                                    # sys.exit(0)
                                else:
                                    sys.exit(1)
                            elif xt == var_sect[5]:
                                if z == var_sect[0]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funcx_0 =eval('rawx // rawy +  rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcx_0)
                                    sys.exit(0)
                                elif z == var_sect[1]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funcx_1 =eval('rawx // rawy - rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcx_1)
                                    sys.exit(0)
                                elif z == var_sect[2]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funcx_2 =eval('rawx // rawy  / rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcx_2)
                                    sys.exit(0)
                                elif z == var_sect[3]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funcx_3 =eval('rawx // rawy  * rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcx_3)
                                    sys.exit(0)
                                elif z == var_sect[4]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funcx_4 =eval('rawx // rawy  % rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcx_4)
                                    sys.exit(0)
                                elif z == var_sect[5]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funcx_5 =eval('rawx // rawy  // rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcx_5)
                                    sys.exit(0)
                                elif z == var_sect[6]:
                                    def ExpMwob_1( nam , nem ):
                                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                        powcxx_1 = math.pow(nam , nem ) 
                                        funccx_B = eval('rawx // powcxx_1 '+'\n')
                                        # section formating code in test  > programing  power in real number 
                                        print("\033[1;32m result\033[1;31m power \033[0m in: ---> {}".format(funccx_B)) 
                                        sys.exit(0)
                                    ExpMwob_1(int(sys.argv[4]), int(sys.argv[6]))
                                elif z == var_sect[7]:
                                    def ExpowR4(raice4):
                                        Factx_R4 = math.sqrt( raice4 )
                                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                        producT4 = eval('rawx // rawy * Factx_R2'+'\n')
                                        print("\033[1;32m result\033[0m --->: ", producT4)
                                        sys.exit(0)
                                    ExpowR4(int(sys.argv[6]))
                                else:
                                    sys.exit(1)
                            elif xt == var_sect[6]:
                                if z == var_sect[0]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funcx_0 =eval('rawx ** rawy +  rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcx_0)
                                    sys.exit(0)
                                elif z == var_sect[1]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funcx_1 =eval('rawx ** rawy - rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcx_1)
                                    sys.exit(0)
                                elif z == var_sect[2]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funcx_2 =eval('rawx ** rawy  / rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcx_2)
                                    sys.exit(0)
                                elif z == var_sect[3]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funcx_3 =eval('rawx ** rawy  * rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcx_3)
                                    sys.exit(0)
                                elif z == var_sect[4]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funcx_4 =eval('rawx ** rawy  % rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcx_4)
                                    sys.exit(0)
                                elif z == var_sect[5]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funcx_5 =eval('rawx ** rawy  // rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcx_5)
                                    sys.exit(0)
                                elif z == var_sect[6]:
                                    def ExpMwob_2( nam , nem ):
                                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                        powcxx_1 = math.pow(nam , nem ) 
                                        def Exponew_0( rats , pow ):
                                            funccx_C = eval('rats ** pow '+'\n')
                                            print("\033[1;32m result\033[1;31m power \033[0m in: ---> {}".format(funccx_C)) 
                                            # section formating code in test  > programing  power in real number 
                                            sys.exit(0)
                                        Exponew_0(int(sys.argv[2]), powcxx_1)        
                                    ExpMwob_2(int(sys.argv[4]), int(sys.argv[6]))
                                elif z == var_sect[7]:
                                    def ExpowR5( raice5 ):
                                        Factx_R4 = math.sqrt( raice5 )
                                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                        produccT5 = eval('rawx ** rawy * Factx_R4'+'\n')
                                        print("\033[1;32m result\033[0m --->: ", produccT5)
                                        sys.exit(0)
                                    ExpowR4(int(sys.argv[6]))
                                    # print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    # funcx_7 =eval('rawx ^ rawy  ¶ rawc '+'\n' )
                                    # print("\033[1;32m result\033[0m --->: " , funcx_7)
                                    # sys.exit(0)
                                else:
                                    sys.exit(1)
                            elif xt == var_sect[7]:
                                if z == var_sect[0]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funccxx_0 = math.sqrt( rawy )  
                                    func_1 = eval('rawx * funccxx_0 +  rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , func_1)
                                    sys.exit(0)
                                elif z == var_sect[1]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funccxx_1 = math.sqrt( rawy )
                                    funcc_2 = eval('rawx * funccxx_1 - rawc '+'\n' ) 
                                    print("\033[1;32m result\033[0m --->: " , funcc_2 )
                                    sys.exit(0)
                                        
                                elif z == var_sect[2]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funccxx_2 = math.sqrt( rawy )
                                    funcc_3 =eval('rawx * funccxx_2  / rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcc_3)
                                    sys.exit(0)
                                elif z == var_sect[3]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funccxx_3 = math.sqrt( rawy )
                                    funcc_4 =eval('rawx * funccxx_3 * rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcc_4)
                                    sys.exit(0)
                                elif z == var_sect[4]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funccxx_4 = math.sqrt( rawy )
                                    funcc_5 =eval('rawx * funccxx_4  % rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcc_5 )
                                    sys.exit(0)
                                elif z == var_sect[5]:
                                    print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    funccxx_5 = math.sqrt( rawy )
                                    funcc_6 =eval('rawx * funccxx_6  // rawc '+'\n' )
                                    print("\033[1;32m result\033[0m --->: " , funcc_6 )
                                    sys.exit(0)
                                elif z == var_sect[6]:
                                    def ExpMwob_4( nam , nem ):
                                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                        powcxx_2 = math.pow(nam , nem )
                                        funccxx_7 = math.sqrt(powcxx_2) 
                                        funccxx_D = eval('rawx * funccxx_7 '+'\n')
                                        print("\033[1;32m result\033[1;31m power \033[0m in: ---> {}".format(funccxx_D)) 
                                        # section formating code in test  > programing  power in real number 
                                        sys.exit(0)
                                    ExpMwob_4(int(sys.argv[4]), int(sys.argv[6]))
                                        
                                    #print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    # funccxx_6 = math.sqrt( rawy )
                                    # funcc_6 =eval('rawx * funccxx_6  ** rawc '+'\n' )
                                    # print("\033[1;32m result\033[0m --->: " , funcc_6)
                                    # sys.exit(0)
                                elif z == var_sect[7]:
                                    def ExpowR6( raiceA , raice6 ):
                                        Factx_R5 = math.sqrt( raice6 )
                                        Factxx_RA = math.sqrt( raiceA ) 
                                        test_v = Factx_R5 + Factxx_RA
                                        print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                        produccT5 = eval('rawx * test_v '+'\n')
                                        print("\033[1;32m result\033[0m --->: ", produccT5)
                                        sys.exit(0)
                                    ExpowR6(int(sys.argv[4]), int(sys.argv[6]))
                                    #print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                    #funcx_7 =eval('rawx ¶ rawy  ¶ rawc '+'\n' )
                                    #print("\033[1;32m result\033[0m --->: " , funcx_7)
                                    #sys.exit(0)
                                else:
                                    sys.exit(1)
# code __fuck_line ------------------------------------
#  ---------------------------------------------------------------
# error
def Funcx_sevendom(adding , rawx, conjunts ,  rawy , subconjunts,   rawc , treconjunts, rawd, fourconjunts, rawe , fiveconjunts, rawf, six, rawg ):
    for xt in conjunts:
        for z in subconjunts:
            for tryx in treconjunts:
                for forA in fourconjunts:
                    for fivA in fiveconjunts:
                        if xt == var_sect[0]:
                            if z == var_sect[0] :
                                if tryx == var_sect[0]:
                                    if forA == var_sect[0]:
                                        if fivA == var_sect[0]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funcx_0 =eval('rawx + rawy +  rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcx_0)
                                            sys.exit(0)
                                        elif var_sect[1] == z :
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funcx_1 =eval('rawx + rawy - rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcx_1)
                                            sys.exit(0)
                                        elif z == var_sect[2]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funcx_2 =eval('rawx + rawy  / rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcx_2)
                                            sys.exit(0)
                                        elif z == var_sect[3]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funcx_3 =eval('rawx + rawy  * rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcx_3)
                                            sys.exit(0)
                                        elif z == var_sect[4]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funcx_4 =eval('rawx + rawy  % rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcx_4)
                                            sys.exit(0)
                                        elif z == var_sect[5]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funcx_5 =eval('rawx + rawy  // rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcx_5)
                                            sys.exit(0)
                                        elif z == var_sect[6]:
                                            def ExpMwob( nam , nem ):
                                                print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                powcx_0 = math.pow(nam , nem ) 
                                                funcx_6 = eval('powcx_0 + rawc'+'\n')
                                                print("\033[1;32m result\033[1;31m power \033[0m in: ---> {}".format(funcx_6)) 
                                                sys.exit(0)
                                                # section formating code in test  > programing  power in real number 
                                            ExpMwob(int(sys.argv[4]), int(sys.argv[6]))
                                            # sys.exit(0)
                                        elif z == var_sect[7]:
                                            def ExpR(raice0):
                                                Factx_R = math.sqrt( raice0 )
                                                print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                producT = eval('rawx + rawy * Factx_R'+'\n')
                                                print("\033[1;32m result\033[0m --->: ", producT)
                                                sys.exit(0)
                                            ExpR(int(sys.argv[6]))
                                                
                                                # funcx_7 =eval('rawx + rawy  ¶ rawc '+'\n' )
                                                    # Factx_R = eval('raice0 * ( raice0 * raice1 )')
                                                    # print("\033[1;34m Result ---> {} ".format(Factx_R) )
                                            #sys.exit(0)
                                        else:
                                            #     print("now _ command error> \033[1;33m ERR0R \033[0m " )
                                            sys.exit(1)
                                    if xt == var_sect[1]:
                                        if z == var_sect[0]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funcxA_0 =eval('rawx - rawy +  rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcxA_0)
                                            sys.exit(0)
                                        elif z == var_sect[1]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funcx_1 =eval('rawx - rawy - rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcx_1)
                                            sys.exit(0)
                                        elif z == var_sect[2]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funcx_2 =eval('rawx - rawy  / rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcx_2)
                                            sys.exit(0)
                                        elif z == var_sect[3]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funcx_3 =eval('rawx - rawy  * rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcx_3)
                                            sys.exit(0)
                                        elif z == var_sect[4]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funcx_4 =eval('rawx - rawy  % rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcx_4)
                                            sys.exit(0)
                                        elif z == var_sect[5]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funcx_5 =eval('rawx - rawy  // rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcx_5)
                                            sys.exit(0)
                                        elif z == var_sect[6]:
                                            def ExpMwob( nam , nem ):
                                                print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                powcx_1 = math.pow(nam , nem ) 
                                                funcx_5 = eval('rawx - powcx_1 '+'\n')
                                                # section formating code in test  > programing  power in real number 
                                                print("\033[1;32m result\033[1;31m power \033[0m in: ---> {}".format(funcx_5)) 
                                                sys.exit(0)
                                            ExpMwob(int(sys.argv[4]), int(sys.argv[6]))
                                            # print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            # funcx_6 =eval('rawx - rawy  ^ rawc '+'\n' )
                                            # print("\033[1;32m result\033[0m --->: " , funcx_6)
                                            # sys.exit(0)
                                            # print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                        elif z == var_sect[7]:
                                            def ExpowR(raice1):
                                                Factx1_R = math.sqrt( raice1 )
                                                print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                producT0 = eval('rawx - rawy * Factx_R'+'\n')
                                                print("\033[1;32m result\033[0m --->: ", producT0)
                                                sys.exit(0)
                                            ExpR(int(sys.argv[6]))
                                            #funcx_7 =eval('rawx - rawy  ¶ rawc '+'\n' )
                                            #print("\033[1;32m result\033[0m --->: " , funcx_7)
                                            #sys.exit(0)
                                        else:
                                            sys.exit(1)
                                            
                                    elif xt == var_sect[0]:
                                        if z == var_sect[0]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funcx_0 =eval('rawx / rawy +  rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcx_0)
                                            sys.exit(0)
                                        elif z == var_sect[1]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funcx_1 =eval('rawx / rawy - rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcx_1)
                                            sys.exit(0)
                                        elif z == var_sect[2]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funcx_2 =eval('rawx / rawy  / rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcx_2)
                                            sys.exit(0)
                                        elif z == var_sect[3]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funcx_3 =eval('rawx / rawy  * rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcx_3)
                                            sys.exit(0)
                                        elif z == var_sect[4]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funcx_4 =eval('rawx / rawy  % rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcx_4)
                                            sys.exit(0)
                                        elif z == var_sect[5]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funcx_5 =eval('rawx / rawy  // rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcx_5)
                                            sys.exit(0)
                                        elif z == var_sect[6]:
                                            def ExpMwob0( nam , nem ):
                                                print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                powcx_1 = math.pow(nam , nem ) 
                                                funccx_ = eval('rawx / powcx_1 '+'\n')
                                                # section formating code in test  > programing  power in real number 
                                                print("\033[1;32m result\033[1;31m power \033[0m in: ---> {}".format(funccx_)) 
                                                sys.exit(0)
                                            ExpMwob(int(sys.argv[4]), int(sys.argv[6]))
                                            #print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            #funcx_6 =eval('rawx / rawy  ^ rawc '+'\n' )
                                            #print("\033[1;32m result\033[0m --->: " , funcx_6)
                                            # sys.exit(0)
                                        elif z == var_sect[7]:
                                            def ExpowR1(raice1):
                                                Factx_R2 = math.sqrt( raice1 )
                                                print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                producT1 = eval('rawx / rawy * Factx_R2'+'\n')
                                                print("\033[1;32m result\033[0m --->: ", producT1)
                                                sys.exit(0)
                                            ExpowR1(int(sys.argv[6]))
                                        else:
                                            sys.exit(1)
                                    elif xt == var_sect[3]:
                                        if z == var_sect[0]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funcx_0 =eval('rawx * rawy +  rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcx_0)
                                            sys.exit(0)
                                        elif z == var_sect[1]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funcx_1 =eval('rawx * rawy - rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcx_1)
                                            sys.exit(0)
                                        elif z == var_sect[2]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funcx_2 =eval('rawx * rawy  / rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcx_2)
                                            sys.exit(0)
                                        elif z == var_sect[3]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funcx_3 =eval('rawx * rawy  * rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcx_3)
                                            sys.exit(0)
                                        elif z == var_sect[4]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funcx_4 =eval('rawx * rawy  % rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcx_4)
                                            sys.exit(0)
                                        elif z == var_sect[5]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funcx_5 =eval('rawx * rawy  // rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcx_5)
                                            sys.exit(0)
                                        elif z == var_sect[6]:
                                            def ExpMwob_0( nam , nem ):
                                                print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                powcx_1 = math.pow(nam , nem ) 
                                                funccx_A = eval('rawx * powcx_1 '+'\n')
                                                # section formating code in test  > programing  power in real number 
                                                print("\033[1;32m result\033[1;31m power \033[0m in: ---> {}".format(funccx_A)) 
                                                sys.exit(0)
                                            ExpMwob_0(int(sys.argv[4]), int(sys.argv[6]))
                                        elif z == var_sect[7]:
                                            def ExpowR2(raice2):
                                                Factx_R2 = math.sqrt( raice2 )
                                                print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                producT2 = eval('rawx * rawy * Factx_R2'+'\n')
                                                print("\033[1;32m result\033[0m --->: ", producT2)
                                                sys.exit(0)
                                            ExpowR2(int(sys.argv[6]))
                                            # print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            # funcx_7 =eval('rawx * rawy  ¶ rawc '+'\n' )
                                            # print("\033[1;32m result\033[0m --->: " , funcx_7)
                                            # sys.exit(0)
                                        else:
                                            sys.exit(1)
                                    elif xt == var_sect[4]:
                                        if z == var_sect[0]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funcx_0 =eval('rawx % rawy +  rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcx_0)
                                            sys.exit(0)
                                        elif z == var_sect[1]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funcx_1 =eval('rawx % rawy - rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcx_1)
                                            sys.exit(0)
                                        elif z == var_sect[2]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funcx_2 =eval('rawx % rawy  / rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcx_2)
                                            sys.exit(0)
                                        elif z == var_sect[3]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funcx_3 =eval('rawx % rawy  * rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcx_3)
                                            sys.exit(0)
                                        elif z == var_sect[4]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funcx_4 =eval('rawx % rawy  % rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcx_4)
                                            sys.exit(0)
                                        elif z == var_sect[5]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funcx_5 =eval('rawx % rawy  // rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcx_5)
                                            sys.exit(0)
                                        elif z == var_sect[6]:
                                            def ExpMwob_0( nam , nem ):
                                                print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                powcxx_1 = math.pow(nam , nem ) 
                                                funccx_B = eval('rawx % powcxx_1 '+'\n')
                                                # section formating code in test  > programing  power in real number 
                                                print("\033[1;32m result\033[1;31m power \033[0m in: ---> {}".format(funccx_B)) 
                                                sys.exit(0)
                                            ExpMwob_0(int(sys.argv[4]), int(sys.argv[6]))
                                        elif z == var_sect[7]:
                                            def ExpowR3(raice2):
                                                Factx_R3 = math.sqrt( raice2 )
                                                print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                producT3 = eval('rawx % rawy * Factx_R3'+'\n')
                                                print("\033[1;32m result\033[0m --->: ", producT3)
                                                sys.exit(0)
                                            ExpowR3(int(sys.argv[6]))
                                            #print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            # funcx_7 =eval('rawx % rawy  ¶ rawc '+'\n' )
                                            # print("\033[1;32m result\033[0m --->: " , funcx_7)
                                            # sys.exit(0)
                                        else:
                                            sys.exit(1)
                                    elif xt == var_sect[5]:
                                        if z == var_sect[0]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funcx_0 =eval('rawx // rawy +  rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcx_0)
                                            sys.exit(0)
                                        elif z == var_sect[1]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funcx_1 =eval('rawx // rawy - rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcx_1)
                                            sys.exit(0)
                                        elif z == var_sect[2]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funcx_2 =eval('rawx // rawy  / rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcx_2)
                                            sys.exit(0)
                                        elif z == var_sect[3]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funcx_3 =eval('rawx // rawy  * rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcx_3)
                                            sys.exit(0)
                                        elif z == var_sect[4]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funcx_4 =eval('rawx // rawy  % rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcx_4)
                                            sys.exit(0)
                                        elif z == var_sect[5]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funcx_5 =eval('rawx // rawy  // rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcx_5)
                                            sys.exit(0)
                                        elif z == var_sect[6]:
                                            def ExpMwob_1( nam , nem ):
                                                print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                powcxx_1 = math.pow(nam , nem ) 
                                                funccx_B = eval('rawx // powcxx_1 '+'\n')
                                                # section formating code in test  > programing  power in real number 
                                                print("\033[1;32m result\033[1;31m power \033[0m in: ---> {}".format(funccx_B)) 
                                                sys.exit(0)
                                            ExpMwob_1(int(sys.argv[4]), int(sys.argv[6]))
                                        elif z == var_sect[7]:
                                            def ExpowR4(raice4):
                                                Factx_R4 = math.sqrt( raice4 )
                                                print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                producT4 = eval('rawx // rawy * Factx_R2'+'\n')
                                                print("\033[1;32m result\033[0m --->: ", producT4)
                                                sys.exit(0)
                                            ExpowR4(int(sys.argv[6]))
                                        else:
                                            sys.exit(1)
                                    elif xt == var_sect[6]:
                                        if z == var_sect[0]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funcx_0 =eval('rawx ** rawy +  rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcx_0)
                                            sys.exit(0)
                                        elif z == var_sect[1]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funcx_1 =eval('rawx ** rawy - rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcx_1)
                                            sys.exit(0)
                                        elif z == var_sect[2]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funcx_2 =eval('rawx ** rawy  / rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcx_2)
                                            sys.exit(0)
                                        elif z == var_sect[3]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funcx_3 =eval('rawx ** rawy  * rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcx_3)
                                            sys.exit(0)
                                        elif z == var_sect[4]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funcx_4 =eval('rawx ** rawy  % rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcx_4)
                                            sys.exit(0)
                                        elif z == var_sect[5]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funcx_5 =eval('rawx ** rawy  // rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcx_5)
                                            sys.exit(0)
                                        elif z == var_sect[6]:
                                            def ExpMwob_2( nam , nem ):
                                                print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                powcxx_1 = math.pow(nam , nem ) 
                                                def Exponew_0( rats , pow ):
                                                    funccx_C = eval('rats ** pow '+'\n')
                                                    print("\033[1;32m result\033[1;31m power \033[0m in: ---> {}".format(funccx_C)) 
                                                    # section formating code in test  > programing  power in real number 
                                                    sys.exit(0)
                                                Exponew_0(int(sys.argv[2]), powcxx_1)        
                                            ExpMwob_2(int(sys.argv[4]), int(sys.argv[6]))
                                        elif z == var_sect[7]:
                                            def ExpowR5( raice5 ):
                                                Factx_R4 = math.sqrt( raice5 )
                                                print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                produccT5 = eval('rawx ** rawy * Factx_R4'+'\n')
                                                print("\033[1;32m result\033[0m --->: ", produccT5)
                                                sys.exit(0)
                                            ExpowR4(int(sys.argv[6]))
                                            # print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            # funcx_7 =eval('rawx ^ rawy  ¶ rawc '+'\n' )
                                            # print("\033[1;32m result\033[0m --->: " , funcx_7)
                                            # sys.exit(0)
                                        else:
                                            sys.exit(1)
                                    elif xt == var_sect[7]:
                                        if z == var_sect[0]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funccxx_0 = math.sqrt( rawy )  
                                            func_1 = eval('rawx * funccxx_0 +  rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , func_1)
                                            sys.exit(0)
                                        elif z == var_sect[1]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funccxx_1 = math.sqrt( rawy )
                                            funcc_2 = eval('rawx * funccxx_1 - rawc '+'\n' ) 
                                            print("\033[1;32m result\033[0m --->: " , funcc_2 )
                                            sys.exit(0)
                                                
                                        elif z == var_sect[2]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funccxx_2 = math.sqrt( rawy )
                                            funcc_3 =eval('rawx * funccxx_2  / rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcc_3)
                                            sys.exit(0)
                                        elif z == var_sect[3]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funccxx_3 = math.sqrt( rawy )
                                            funcc_4 =eval('rawx * funccxx_3 * rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcc_4)
                                            sys.exit(0)
                                        elif z == var_sect[4]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funccxx_4 = math.sqrt( rawy )
                                            funcc_5 =eval('rawx * funccxx_4  % rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcc_5 )
                                            sys.exit(0)
                                        elif z == var_sect[5]:
                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            funccxx_5 = math.sqrt( rawy )
                                            funcc_6 =eval('rawx * funccxx_6  // rawc '+'\n' )
                                            print("\033[1;32m result\033[0m --->: " , funcc_6 )
                                            sys.exit(0)
                                        elif z == var_sect[6]:
                                            def ExpMwob_4( nam , nem ):
                                                print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                powcxx_2 = math.pow(nam , nem )
                                                funccxx_7 = math.sqrt(powcxx_2) 
                                                funccxx_D = eval('rawx * funccxx_7 '+'\n')
                                                print("\033[1;32m result\033[1;31m power \033[0m in: ---> {}".format(funccxx_D)) 
                                                # section formating code in test  > programing  power in real number 
                                                sys.exit(0)
                                            ExpMwob_4(int(sys.argv[4]), int(sys.argv[6]))
                                                
                                            #print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            # funccxx_6 = math.sqrt( rawy )
                                            # funcc_6 =eval('rawx * funccxx_6  ** rawc '+'\n' )
                                            # print("\033[1;32m result\033[0m --->: " , funcc_6)
                                            # sys.exit(0)
                                        elif z == var_sect[7]:
                                            def ExpowR6( raiceA , raice6 ):
                                                Factx_R5 = math.sqrt( raice6 )
                                                Factxx_RA = math.sqrt( raiceA ) 
                                                test_v = Factx_R5 + Factxx_RA
                                                print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                produccT5 = eval('rawx * test_v '+'\n')
                                                print("\033[1;32m result\033[0m --->: ", produccT5)
                                                sys.exit(0)
                                            ExpowR6(int(sys.argv[4]), int(sys.argv[6]))
                                            #print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                            #funcx_7 =eval('rawx ¶ rawy  ¶ rawc '+'\n' )
                                            #print("\033[1;32m result\033[0m --->: " , funcx_7)
                                            #sys.exit(0)
                                        else:
                                            sys.exit(1)
  
# :: @Command ------------------------------------------------
# ;; code separation --------------------------------------------- 
def Funcx_eightdom(adding , rawx, conjunts ,  rawy , subconjunts,   rawc , treconjunts, rawd, foronjunts, rawe , fivconjunts, rawf, six_C, rawg , sevjunts, rawh  ):
    for xt in conjunts:
        for z in subconjunts:
            for tryx in treconjunts:
                for forA in foronjunts:
                    for fiv_A  in fivconjunts:
                        for six_A in six_C:
                            for seven in sevjunts:
                                if xt == var_sect[0] :
                                    if z == var_sect[0]:
                                        if tryx == var_sect[0]:
                                            if forA == var_sect[0]:
                                                if fiv_A == var_sect[0]:
                                                    if six_A == var_sect[0]:
                                                        if seven == var_sect[0]:
                                                    
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funcx_0 =eval('rawx + rawy +  rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcx_0)
                                                            sys.exit(0)
                                                        elif var_sect[1] == z :
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funcx_1 =eval('rawx + rawy - rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcx_1)
                                                            sys.exit(0)
                                                        elif z == var_sect[2]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funcx_2 =eval('rawx + rawy  / rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcx_2)
                                                            sys.exit(0)
                                                        elif z == var_sect[3]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funcx_3 =eval('rawx + rawy  * rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcx_3)
                                                            sys.exit(0)
                                                        elif z == var_sect[4]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funcx_4 =eval('rawx + rawy  % rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcx_4)
                                                            sys.exit(0)
                                                        elif z == var_sect[5]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funcx_5 =eval('rawx + rawy  // rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcx_5)
                                                            sys.exit(0)
                                                        elif z == var_sect[6]:
                                                            def ExpMwob( nam , nem ):
                                                                print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                                powcx_0 = math.pow(nam , nem ) 
                                                                funcx_6 = eval('powcx_0 + rawc'+'\n')
                                                                print("\033[1;32m result\033[1;31m power \033[0m in: ---> {}".format(funcx_6)) 
                                                                sys.exit(0)
                                                                # section formating code in test  > programing  power in real number 
                                                            ExpMwob(int(sys.argv[4]), int(sys.argv[6]))
                                                            # sys.exit(0)
                                                        elif z == var_sect[7]:
                                                            def ExpR(raice0):
                                                                Factx_R = math.sqrt( raice0 )
                                                                print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                                producT = eval('rawx + rawy * Factx_R'+'\n')
                                                                print("\033[1;32m result\033[0m --->: ", producT)
                                                                sys.exit(0)
                                                            ExpR(int(sys.argv[6]))
                                                                
                                                                # funcx_7 =eval('rawx + rawy  ¶ rawc '+'\n' )
                                                                    # Factx_R = eval('raice0 * ( raice0 * raice1 )')
                                                                    # print("\033[1;34m Result ---> {} ".format(Factx_R) )
                                                            #sys.exit(0)
                                                        else:
                                                            #     print("now _ command error> \033[1;33m ERR0R \033[0m " )
                                                            sys.exit(1)
                                                    if xt == var_sect[1]:
                                                        if z == var_sect[0]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funcxA_0 =eval('rawx - rawy +  rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcxA_0)
                                                            sys.exit(0)
                                                        elif z == var_sect[1]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funcx_1 =eval('rawx - rawy - rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcx_1)
                                                            sys.exit(0)
                                                        elif z == var_sect[2]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funcx_2 =eval('rawx - rawy  / rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcx_2)
                                                            sys.exit(0)
                                                        elif z == var_sect[3]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funcx_3 =eval('rawx - rawy  * rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcx_3)
                                                            sys.exit(0)
                                                        elif z == var_sect[4]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funcx_4 =eval('rawx - rawy  % rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcx_4)
                                                            sys.exit(0)
                                                        elif z == var_sect[5]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funcx_5 =eval('rawx - rawy  // rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcx_5)
                                                            sys.exit(0)
                                                        elif z == var_sect[6]:
                                                            def ExpMwob( nam , nem ):
                                                                print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                                powcx_1 = math.pow(nam , nem ) 
                                                                funcx_5 = eval('rawx - powcx_1 '+'\n')
                                                                # section formating code in test  > programing  power in real number 
                                                                print("\033[1;32m result\033[1;31m power \033[0m in: ---> {}".format(funcx_5)) 
                                                                sys.exit(0)
                                                            ExpMwob(int(sys.argv[4]), int(sys.argv[6]))
                                                            # print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            # funcx_6 =eval('rawx - rawy  ^ rawc '+'\n' )
                                                            # print("\033[1;32m result\033[0m --->: " , funcx_6)
                                                            # sys.exit(0)
                                                            # print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                        elif z == var_sect[7]:
                                                            def ExpowR(raice1):
                                                                Factx1_R = math.sqrt( raice1 )
                                                                print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                                producT0 = eval('rawx - rawy * Factx_R'+'\n')
                                                                print("\033[1;32m result\033[0m --->: ", producT0)
                                                                sys.exit(0)
                                                            ExpR(int(sys.argv[6]))
                                                            #funcx_7 =eval('rawx - rawy  ¶ rawc '+'\n' )
                                                            #print("\033[1;32m result\033[0m --->: " , funcx_7)
                                                            #sys.exit(0)
                                                        else:
                                                            sys.exit(1)
                                                            
                                                    elif xt == var_sect[0]:
                                                        if z == var_sect[0]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funcx_0 =eval('rawx / rawy +  rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcx_0)
                                                            sys.exit(0)
                                                        elif z == var_sect[1]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funcx_1 =eval('rawx / rawy - rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcx_1)
                                                            sys.exit(0)
                                                        elif z == var_sect[2]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funcx_2 =eval('rawx / rawy  / rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcx_2)
                                                            sys.exit(0)
                                                        elif z == var_sect[3]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funcx_3 =eval('rawx / rawy  * rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcx_3)
                                                            sys.exit(0)
                                                        elif z == var_sect[4]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funcx_4 =eval('rawx / rawy  % rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcx_4)
                                                            sys.exit(0)
                                                        elif z == var_sect[5]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funcx_5 =eval('rawx / rawy  // rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcx_5)
                                                            sys.exit(0)
                                                        elif z == var_sect[6]:
                                                            def ExpMwob0( nam , nem ):
                                                                print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                                powcx_1 = math.pow(nam , nem ) 
                                                                funccx_ = eval('rawx / powcx_1 '+'\n')
                                                                # section formating code in test  > programing  power in real number 
                                                                print("\033[1;32m result\033[1;31m power \033[0m in: ---> {}".format(funccx_)) 
                                                                sys.exit(0)
                                                            ExpMwob(int(sys.argv[4]), int(sys.argv[6]))
                                                            #print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            #funcx_6 =eval('rawx / rawy  ^ rawc '+'\n' )
                                                            #print("\033[1;32m result\033[0m --->: " , funcx_6)
                                                            # sys.exit(0)
                                                        elif z == var_sect[7]:
                                                            def ExpowR1(raice1):
                                                                Factx_R2 = math.sqrt( raice1 )
                                                                print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                                producT1 = eval('rawx / rawy * Factx_R2'+'\n')
                                                                print("\033[1;32m result\033[0m --->: ", producT1)
                                                                sys.exit(0)
                                                            ExpowR1(int(sys.argv[6]))
                                                        else:
                                                            sys.exit(1)
                                                    elif xt == var_sect[3]:
                                                        if z == var_sect[0]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funcx_0 =eval('rawx * rawy +  rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcx_0)
                                                            sys.exit(0)
                                                        elif z == var_sect[1]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funcx_1 =eval('rawx * rawy - rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcx_1)
                                                            sys.exit(0)
                                                        elif z == var_sect[2]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funcx_2 =eval('rawx * rawy  / rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcx_2)
                                                            sys.exit(0)
                                                        elif z == var_sect[3]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funcx_3 =eval('rawx * rawy  * rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcx_3)
                                                            sys.exit(0)
                                                        elif z == var_sect[4]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funcx_4 =eval('rawx * rawy  % rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcx_4)
                                                            sys.exit(0)
                                                        elif z == var_sect[5]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funcx_5 =eval('rawx * rawy  // rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcx_5)
                                                            sys.exit(0)
                                                        elif z == var_sect[6]:
                                                            def ExpMwob_0( nam , nem ):
                                                                print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                                powcx_1 = math.pow(nam , nem ) 
                                                                funccx_A = eval('rawx * powcx_1 '+'\n')
                                                                # section formating code in test  > programing  power in real number 
                                                                print("\033[1;32m result\033[1;31m power \033[0m in: ---> {}".format(funccx_A)) 
                                                                sys.exit(0)
                                                            ExpMwob_0(int(sys.argv[4]), int(sys.argv[6]))
                                                        elif z == var_sect[7]:
                                                            def ExpowR2(raice2):
                                                                Factx_R2 = math.sqrt( raice2 )
                                                                print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                                producT2 = eval('rawx * rawy * Factx_R2'+'\n')
                                                                print("\033[1;32m result\033[0m --->: ", producT2)
                                                                sys.exit(0)
                                                            ExpowR2(int(sys.argv[6]))
                                                            # print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            # funcx_7 =eval('rawx * rawy  ¶ rawc '+'\n' )
                                                            # print("\033[1;32m result\033[0m --->: " , funcx_7)
                                                            # sys.exit(0)
                                                        else:
                                                            sys.exit(1)
                                                    elif xt == var_sect[4]:
                                                        if z == var_sect[0]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funcx_0 =eval('rawx % rawy +  rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcx_0)
                                                            sys.exit(0)
                                                        elif z == var_sect[1]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funcx_1 =eval('rawx % rawy - rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcx_1)
                                                            sys.exit(0)
                                                        elif z == var_sect[2]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funcx_2 =eval('rawx % rawy  / rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcx_2)
                                                            sys.exit(0)
                                                        elif z == var_sect[3]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funcx_3 =eval('rawx % rawy  * rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcx_3)
                                                            sys.exit(0)
                                                        elif z == var_sect[4]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funcx_4 =eval('rawx % rawy  % rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcx_4)
                                                            sys.exit(0)
                                                        elif z == var_sect[5]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funcx_5 =eval('rawx % rawy  // rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcx_5)
                                                            sys.exit(0)
                                                        elif z == var_sect[6]:
                                                            def ExpMwob_0( nam , nem ):
                                                                print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                                powcxx_1 = math.pow(nam , nem ) 
                                                                funccx_B = eval('rawx % powcxx_1 '+'\n')
                                                                # section formating code in test  > programing  power in real number 
                                                                print("\033[1;32m result\033[1;31m power \033[0m in: ---> {}".format(funccx_B)) 
                                                                sys.exit(0)
                                                            ExpMwob_0(int(sys.argv[4]), int(sys.argv[6]))
                                                        elif z == var_sect[7]:
                                                            def ExpowR3(raice2):
                                                                Factx_R3 = math.sqrt( raice2 )
                                                                print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                                producT3 = eval('rawx % rawy * Factx_R3'+'\n')
                                                                print("\033[1;32m result\033[0m --->: ", producT3)
                                                                sys.exit(0)
                                                            ExpowR3(int(sys.argv[6]))
                                                            #print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            # funcx_7 =eval('rawx % rawy  ¶ rawc '+'\n' )
                                                            # print("\033[1;32m result\033[0m --->: " , funcx_7)
                                                            # sys.exit(0)
                                                        else:
                                                            sys.exit(1)
                                                    elif xt == var_sect[5]:
                                                        if z == var_sect[0]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funcx_0 =eval('rawx // rawy +  rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcx_0)
                                                            sys.exit(0)
                                                        elif z == var_sect[1]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funcx_1 =eval('rawx // rawy - rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcx_1)
                                                            sys.exit(0)
                                                        elif z == var_sect[2]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funcx_2 =eval('rawx // rawy  / rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcx_2)
                                                            sys.exit(0)
                                                        elif z == var_sect[3]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funcx_3 =eval('rawx // rawy  * rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcx_3)
                                                            sys.exit(0)
                                                        elif z == var_sect[4]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funcx_4 =eval('rawx // rawy  % rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcx_4)
                                                            sys.exit(0)
                                                        elif z == var_sect[5]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funcx_5 =eval('rawx // rawy  // rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcx_5)
                                                            sys.exit(0)
                                                        elif z == var_sect[6]:
                                                            def ExpMwob_1( nam , nem ):
                                                                print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                                powcxx_1 = math.pow(nam , nem ) 
                                                                funccx_B = eval('rawx // powcxx_1 '+'\n')
                                                                # section formating code in test  > programing  power in real number 
                                                                print("\033[1;32m result\033[1;31m power \033[0m in: ---> {}".format(funccx_B)) 
                                                                sys.exit(0)
                                                            ExpMwob_1(int(sys.argv[4]), int(sys.argv[6]))
                                                        elif z == var_sect[7]:
                                                            def ExpowR4(raice4):
                                                                Factx_R4 = math.sqrt( raice4 )
                                                                print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                                producT4 = eval('rawx // rawy * Factx_R2'+'\n')
                                                                print("\033[1;32m result\033[0m --->: ", producT4)
                                                                sys.exit(0)
                                                            ExpowR4(int(sys.argv[6]))
                                                        else:
                                                            sys.exit(1)
                                                    elif xt == var_sect[6]:
                                                        if z == var_sect[0]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funcx_0 =eval('rawx ** rawy +  rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcx_0)
                                                            sys.exit(0)
                                                        elif z == var_sect[1]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funcx_1 =eval('rawx ** rawy - rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcx_1)
                                                            sys.exit(0)
                                                        elif z == var_sect[2]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funcx_2 =eval('rawx ** rawy  / rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcx_2)
                                                            sys.exit(0)
                                                        elif z == var_sect[3]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funcx_3 =eval('rawx ** rawy  * rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcx_3)
                                                            sys.exit(0)
                                                        elif z == var_sect[4]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funcx_4 =eval('rawx ** rawy  % rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcx_4)
                                                            sys.exit(0)
                                                        elif z == var_sect[5]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funcx_5 =eval('rawx ** rawy  // rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcx_5)
                                                            sys.exit(0)
                                                        elif z == var_sect[6]:
                                                            def ExpMwob_2( nam , nem ):
                                                                print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                                powcxx_1 = math.pow(nam , nem ) 
                                                                def Exponew_0( rats , pow ):
                                                                    funccx_C = eval('rats ** pow '+'\n')
                                                                    print("\033[1;32m result\033[1;31m power \033[0m in: ---> {}".format(funccx_C)) 
                                                                    # section formating code in test  > programing  power in real number 
                                                                    sys.exit(0)
                                                                Exponew_0(int(sys.argv[2]), powcxx_1)        
                                                            ExpMwob_2(int(sys.argv[4]), int(sys.argv[6]))
                                                        elif z == var_sect[7]:
                                                            def ExpowR5( raice5 ):
                                                                Factx_R4 = math.sqrt( raice5 )
                                                                print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                                produccT5 = eval('rawx ** rawy * Factx_R4'+'\n')
                                                                print("\033[1;32m result\033[0m --->: ", produccT5)
                                                                sys.exit(0)
                                                            ExpowR4(int(sys.argv[6]))
                                                            # print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            # funcx_7 =eval('rawx ^ rawy  ¶ rawc '+'\n' )
                                                            # print("\033[1;32m result\033[0m --->: " , funcx_7)
                                                            # sys.exit(0)
                                                        else:
                                                            sys.exit(1)
                                                    elif xt == var_sect[7]:
                                                        if z == var_sect[0]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funccxx_0 = math.sqrt( rawy )  
                                                            func_1 = eval('rawx * funccxx_0 +  rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , func_1)
                                                            sys.exit(0)
                                                        elif z == var_sect[1]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funccxx_1 = math.sqrt( rawy )
                                                            funcc_2 = eval('rawx * funccxx_1 - rawc '+'\n' ) 
                                                            print("\033[1;32m result\033[0m --->: " , funcc_2 )
                                                            sys.exit(0)
                                                                
                                                        elif z == var_sect[2]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funccxx_2 = math.sqrt( rawy )
                                                            funcc_3 =eval('rawx * funccxx_2  / rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcc_3)
                                                            sys.exit(0)
                                                        elif z == var_sect[3]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funccxx_3 = math.sqrt( rawy )
                                                            funcc_4 =eval('rawx * funccxx_3 * rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcc_4)
                                                            sys.exit(0)
                                                        elif z == var_sect[4]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funccxx_4 = math.sqrt( rawy )
                                                            funcc_5 =eval('rawx * funccxx_4  % rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcc_5 )
                                                            sys.exit(0)
                                                        elif z == var_sect[5]:
                                                            print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            funccxx_5 = math.sqrt( rawy )
                                                            funcc_6 =eval('rawx * funccxx_6  // rawc '+'\n' )
                                                            print("\033[1;32m result\033[0m --->: " , funcc_6 )
                                                            sys.exit(0)
                                                        elif z == var_sect[6]:
                                                            def ExpMwob_4( nam , nem ):
                                                                print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                                powcxx_2 = math.pow(nam , nem )
                                                                funccxx_7 = math.sqrt(powcxx_2) 
                                                                funccxx_D = eval('rawx * funccxx_7 '+'\n')
                                                                print("\033[1;32m result\033[1;31m power \033[0m in: ---> {}".format(funccxx_D)) 
                                                                # section formating code in test  > programing  power in real number 
                                                                sys.exit(0)
                                                            ExpMwob_4(int(sys.argv[4]), int(sys.argv[6]))
                                                                
                                                            #print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            # funccxx_6 = math.sqrt( rawy )
                                                            # funcc_6 =eval('rawx * funccxx_6  ** rawc '+'\n' )
                                                            # print("\033[1;32m result\033[0m --->: " , funcc_6)
                                                            # sys.exit(0)
                                                        elif z == var_sect[7]:
                                                            def ExpowR6( raiceA , raice6 ):
                                                                Factx_R5 = math.sqrt( raice6 )
                                                                Factxx_RA = math.sqrt( raiceA ) 
                                                                test_v = Factx_R5 + Factxx_RA
                                                                print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                                produccT5 = eval('rawx * test_v '+'\n')
                                                                print("\033[1;32m result\033[0m --->: ", produccT5)
                                                                sys.exit(0)
                                                            ExpowR6(int(sys.argv[4]), int(sys.argv[6]))
                                                            #print("my calculator : ", rawx , xt,  rawy , z, rawc )
                                                            #funcx_7 =eval('rawx ¶ rawy  ¶ rawc '+'\n' )
                                                            #print("\033[1;32m result\033[0m --->: " , funcx_7)
                                                            #sys.exit(0)
                                                        else:
                                                            sys.exit(1)
                                    #elif i == var_sect[6]:
# new_ line | ---------------------------------------------------------------
# ------------------------------------------------------------------------------ ! fuck line 



# var seeting cofig equal simbol no commander 
# var creator program in test _ code _ raize
# var creator program in test _ code _ log
# var _creator program in test _code _ py 
#def programing():
#    pass
#conjunts 
#numN = sys.argv[1]
#numv = sys.argv[2]
#numN = int(input('sentence : > ' ))
#numv = int(input('var.result : > '))



if __name__ == '__main__':
    funx_banner()
    
    if sys.argv[1] == one_list[4] or sys.argv[1] == one_list[5]:
        Helpme()
        sys.exit(0)
    elif sys.argv[1] == one_list[8] or sys.argv[1] == one_list[9]  :
        print('last ------> ''[', verS ,']')
        sys.exit(0)
        
    elif sys.argv[1] == one_list[2] or  sys.argv[1] == one_list[3]:
        
        print('example test raice ')
        for Sys in range(0, 11):
            # print( Sys )
            if int(len(sys.argv)) == 12:
                # print('code [', Sys ,' ] in testing characters in arguments', sys.argv[2:10]  ) 
                if Sys == 0:
                    operati0n = math.sqrt(int(sys.argv[2]))
                    if type(operati0n) == float:
                        #print('number float' )
                        print('list [{}] raice type float  ----> {} → [{}]'.format(Sys, sys.argv[2],  operati0n  ) )
                    else:
                        print('list [{}] raice ----> {} → {} '.format(Sys, sys.argv[2],  operati0n  ) )
                elif Sys == 2 :
                    operation1 = math.sqrt(int(sys.argv[3]))
                    if type(operation1) == float:                
                        print('list [{}] raice type float ----> {} → [{}] '.format(Sys, sys.argv[3],  operation1  ) )
                    else:
                        print('list [{}] raice ----> {} → {} '.format(Sys, sys.argv[3],  operation1  ) )
                elif Sys == 3:
                    operation2 = math.sqrt(int(sys.argv[4]))
                    if type(operation2) == float:      
                        print('list [{}] raice type float ----> {} → {} '.format(Sys, sys.argv[4],  operation2  ) )
                    else:
                        print('list [{}] raice ----> {} → {} '.format(Sys, sys.argv[4],  operation2  ) )
                elif Sys == 4:
                    operation3 = math.sqrt(int(sys.argv[5]))
                    if type(operation3) == float:
                        print('list [{}] raice type float ----> {} → [{}] '.format(Sys, sys.argv[5],  operation3  ) )
                    else:
                        print('list [{}] raice ----> {} → {} '.format(Sys, sys.argv[5],  operation3 ))
                elif Sys == 5:
                    operation4 = math.sqrt(int(sys.argv[6]))
                    if type(operation4) == float:
                        print('list [{}] raice type float ----> {} → [{}] '.format(Sys, sys.argv[6],  operation4  ) )
                    else:
                        print('list [{}] raice ----> {} → {} '.format(Sys, sys.argv[6],  operation4  ) )
                elif Sys == 6:
                    operation5 = math.sqrt(int(sys.argv[7]))
                    if type(operation5) == float:
                        print('list [{}] raice type float ----> {} → [{}] '.format(Sys, sys.argv[7],  operation5  ) )
                    else:
                        print('list [{}] raice ----> {} → {} '.format(Sys, sys.argv[7],  operation5))
                        
                elif Sys == 7:
                    operation6 = math.sqrt(int(sys.argv[8]))
                    if type(operation6) == float:
                        print('list [{}] raice type float ----> {} → [{}] '.format(Sys, sys.argv[8],  operation6  ) )
                    else:
                        print('list [{}] raice ----> {} → {} '.format(Sys, sys.argv[8],  operation6 ))
                    
                elif Sys == 8:
                    operation7 = math.sqrt(int(sys.argv[9]))
                    rrest = eval('operation7 * 1 ')
                    if type(rrest) == float:
                        print('list [{}] raice type float ----> {} → [{}] '.format(Sys, sys.argv[9],  rrest  ) )
                        #sys.exit(0)
                    else:
                        print('list [{}] raice ----> {} → {} '.format(Sys, sys.argv[9],  rrest  ))
                    
                elif Sys == 9:
                    operation8 = math.sqrt(int(sys.argv[10]))
                    if type(operation8) == float:
                        print('list [{}] raice type float ----> {} → [{}] '.format(Sys, sys.argv[10],  operation8  ) )
                    else:
                        print('list [{}] raice ----> {} → {} '.format(Sys, sys.argv[10],  operation8  ) )
                        
                elif Sys == 10:
                    operation9 = math.sqrt(int(sys.argv[11]))
                    if type(operation9) == float:
                        print('list [{}] raice  type float ----> {} → [{}] '.format(Sys, sys.argv[11],  operation9  ) )
                    else:
                        print('list [{}] raice ----> {} → {} '.format(Sys, sys.argv[11],  operation9 ))
                    sys.exit(0)
            
            else:
                print('execed limetation in range arguments  max <= 10')

                sys.exit(1)
        #sys.exit(0)
        
        #sys.exit(0)
# how -**-*-*-------------------*-*-*-*-*--***********************************
        
    for process in range(len(sys.argv) , 15) :
        if process == 5:
          Func_xcalc(str(sys.argv[1]), int(sys.argv[2]), str(sys.argv[3]), int(sys.argv[4]))
          #sys.exit(0)
        elif process >= 6:
            #print('hello friend')
            Funcx_fourdom(str(sys.argv[1]), int(sys.argv[2]), str(sys.argv[3]), int(sys.argv[4]), str(sys.argv[5]), int(sys.argv[6]))
        elif process >= 11:
            Funcx_fivedom(str(sys.argv[1]), int(sys.argv[2]), str(sys.argv[3]), int(sys.argv[4]), str(sys.argv[5]), int(sys.argv[6]), str(sys.argv[7]), int(sys.argv[8]))
        elif process >= 13:
            Funcx_sixdom(str(sys.argv[1]), int(sys.argv[2]) , str(sys.argv[3]), int(sys.argv[4]), str(sys.argv[5]), int(sys.argv[6]), str(sys.argv[7]), int(sys.argv[8]), str(sys.argv[9]), int(sys.argv[10]))
        elif process >= 15:
            Funcx_sevendom(str(sys.argv[1]), int(sys.argv[2]), str(sys.argv[3]), int(sys.argv[4]), str(sys.argv[5]), int(sys.argv[6]), str(sys.argv[7]), int(sys.argv[8]), str(sys.argv[9]), int(sys.argv[10]) , str(sys.argv[11]) , int(sys.argv[12]) )                        
        elif process >= 17:
            Funcx_eightdom(str(sys.argv[1]), int(sys.argv[2]), str(sys.argv[3]), int(sys.argv[4]), str(sys.argv[5]), int(sys.argv[6]), str(sys.argv[7]), int(sys.argv[8]),str(sys.argv[9]), int(sys.argv[10]),str(sys.argv[11]), int(sys.argv[12]),str(sys.argv[13]), int(sys.argv[14]))
        
        else:
            print("\033[1;31m ----> argument_now asigned  " )
            print(" < ERROR > \033[0m")
            sys.exit(1)
    
    
    sys.exit(0)