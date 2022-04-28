import sys 
def one(x):
    #raw_entra = int(input('Ingresa un numero >-->:'))
    enum , calc  = 0 , 0
    # new_ formule
    onelist = [] 
    co_key = 0
    co_2 = 0
    enum = 0
    calc = 0
    for  zamp in range(1, x+1 ,1):
        pass
        #if w%2 == 0:
        # print(zamp , end = ' ,')
           
    for  w in range(1, x+1, 1):
        if w % 2 == 0:
        # if zamp %2:
            
            print('\t''#[{}] el valor es par es 0 \033[1;33m [{}]\033[0m'.format(enum, w))
            co_key += w 
            onelist.append([w])
            enum += 1
            ################################ PASO LIBRE ##############################################
        elif w != 1:
            print(' #[{}] el valor es impar 1 \033[1;31m [{}]\033[0m '.format( calc , w), end= ",")
            co_2 += w
            calc +=1


    print('variable_par  ', co_key)
    print('var_IMPAR_ES', co_2)
    print(onelist)
if __name__ == '__main__':
    one(int(sys.argv[1]))
