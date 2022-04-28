#!/usr/bin/env python3.8

#from email import charset
import sys 
from sys import argv, stdin
# i,port library in test the file program test exponent
import math

#gui_v =  Tk()
#gui_v.mainloop()

def Func_xcalc(adding, rawx,  conjunts, rawy):
    if adding == one_list[0]:
        print("selection ---> ", sys.argv[1] )
    else:
        print ("not")
        #sys.exit(0)
    if len(sys.argv) >= 5:
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
                def ExpM(nam=int(sys.argv[2]), nem=int(sys.argv[4])):
                    if i == var_sect[6]:
                        varA = sys.argv[3]
                        funcx_6 = math.pow(nam, nem ) 
                        print("{} result power  in: ---> {}".format(funcx_6, varA))

                sys.exit(0)
            else:
                print("now _ command error> \033[1;33m ERR0R \033[0m " )
                sys.exit(1)

                
        print('not  module in_put')
        sys.exit(0)
    else:
        print('code on loop error')
        sys.exit(1)


one_list = ['--calc' , '--add', '--rse']
# smbolos aritmeticos
var_sect = ['+', '-', '/', '*', '%' , '//' , 'up']
#def programing():
#    pass
#conjunts 
#numN = sys.argv[1]
#numv = sys.argv[2]
#numN = int(input('sentence : > ' ))
#numv = int(input('var.result : > '))
if __name__ == '__main__':
    print('hello _calculator _index_text  code programing in python test ')
    Func_xcalc(str(sys.argv[1]), int(sys.argv[2]), str(sys.argv[3]), int(sys.argv[4]))
    sys.exit(0)