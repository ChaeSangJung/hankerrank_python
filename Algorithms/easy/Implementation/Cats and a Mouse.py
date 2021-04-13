https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

def catAndMouse(x, y, z):    
    dis_a = abs(x-z)
    dis_b = abs(y-z)
    catch = ""

    if dis_a < dis_b:
        catch = "Cat A"
    
    elif dis_a > dis_b:
        catch = "Cat B"
    
    elif dis_a == dis_b:
        catch = "Mouse C"
    
    return catch