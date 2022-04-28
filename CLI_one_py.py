#!/usr/bin/env python3.8
#from ast import arg
# Author  Ron B , Sanchez Mendoza
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
var_sect = ['+', '-', '/', '*', '%' , '//' , '^', '¶' , pi, '**', '(', ')'  ]
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
        idx = 0
        #x = int(sys.argv[1])
        #y = int(sys.argv[2])
        for i in ['+', '-', '/', '*', '%' , '//' , '^', '¶' , 'pi', '**', '(', ')' ]:
            if conjunts == i:
                print('my calculator: {} {} {} '.format(rawx, sys.argv[3], rawy))
                if i == var_sect[0]:
                    funx_0 = eval('rawx + rawy')
                    print("\033[1;32m result\033[0m --->:[{}]".format(funx_0))
                    sys.exit(0)
                elif i == var_sect[1]:
                    funx_1 = eval('rawx - rawy')
                    print("\033[1;32m result\033[0m --->:[{}]".format(funx_1))
                    sys.exit(0)
                elif i == var_sect[2]:
                    funx_A = eval('rawx / rawy')
                    print("\033[1;32m result\033[0m --->:[{}]".format(int(funx_A)))
                    print("\033[1;32m result\033[0m --->:[{}]".format(float(funx_A)))
                    sys.exit(0)
                    #print('my calculator: {} {} {} '.format(rawx, sys.argv[3], rawy))
                elif i == var_sect[9]:
                    if rawx == pi:
                        fnx_C = eval('pi + rawy')
                        print("\033[1;32m result\033[0m --->:[{}]".format(fnx_C))
                        sys.exit(0)
                    else:
                        if rawx != pi:
                            print('not simbol pi operator in valor is multiplo it conjunt eval')
                            sys.exit(1)
                                       
            else:
                #if conjunts != i :
                #    print('list_permit simbols is #{} {}'.format(idx , i))
                    idx += 1
                #    sys.exit(1)
                


if __name__ == '__main__':
    
    for process in range(len(sys.argv) , 6) :
        if process == 5:
          Func_xcalc(str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]), int(sys.argv[4]))