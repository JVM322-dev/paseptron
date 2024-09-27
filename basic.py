import numpy as np

def action(x):
    return 0 if x<0.5 else 1
def right(house,rock,view):
    x = np.array([house,rock,view])
    vect1 = [0.3,0.3,0]
    vect2 = [0.4,-0.5,1]
    weight1 = np.array([vect1,vect2]);
    weight2 = np.array([-1,1])
    sum_hidden = np.dot(weight1,x)
    print("Значения сумм нейрона скрытого слоя-"+str(sum_hidden))
    out_hidden = np.array([action(x) for x in sum_hidden])
    print("Значения на выходах скрытого слоя-"+str(out_hidden))
    sum_end = np.dot(weight2,out_hidden)
    y=action(sum_end)
    print("результат y :"+str(y))
    return y
def ReadNumber():
    answer = input()
    return int(answer)
    
def main():
    print("наличе дома 1 или 0 :")
    house= ReadNumber()
    print("слушает рок 1 или  0 :")
    rock = ReadNumber()
    print("красивый 1 или 0 :")
    view = ReadNumber()
    result =right(house,rock,view)
    if result ==1:
        print("its ok")
    else:
        print("no ,thank")


main()   
    
