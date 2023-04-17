import sys

# Add Your functions here

def possibleBest(h, m, price, incr, keep):
    rtrn = (incr[h-1]/100 * price[h-1]) + keep[h-1][m-price[h-1]][0]
    cost_rtrn = price[h-1] + keep[h-1][m-price[h-1]][1]
    rtrn = round(rtrn, 2)
    return (rtrn, cost_rtrn)

def max_profit(money, num_h, price, incr):
    # create an array of tuples to keep optimal solutions
    # each tuple has values such that tuple[0] = the return on investment
    # and tuple[1] = the total initial cost of that investment (in millions of dollars)
    keep = [[(0,0) for x in range(money+1)] for z in range(num_h+1)]
    best_return  = 0

    for h in range(num_h+1):
        for m in range(money+1):

            if h == 0 or m ==0:
                pass

            elif price[h-1] <= m:
                prev_best = (keep[h-1][m])
                # possible best is a tuple with possible_best[0] equal to the 
                possible_best = possibleBest(h, m, price, incr, keep)
                # possible_best = ( ( (incr[h-1]/100 * price[h-1]) + keep[h-1][m-price[h-1]][0] ), ( price[h-1] + keep[h-1][m-price[h-1]][1] ) )
                # possible_best = (round(possible_best[0], 2), possible_best[1])

                if possible_best[0] > prev_best[0]:
                    keep[h][m] = possible_best
                else:
                    keep[h][m] = prev_best

            else:
                keep[h][m] = keep[h-1][m]



    for i in keep:
        print(i)
    print()


                



# You are allowed to change the main function. 

# Do not change the template file name. 

def main():

    # The first line is the amount of investment in million USD which is an integer number.
    line = sys.stdin.readline()
    line = line.strip()
    money = int(line)

# The second line includes an integer number which is the number of houses listed for sale.
    line = sys.stdin.readline()
    line = line.strip()
    num_houses = int(line)

    # The third line is a list of house prices in million dollar which is a list of \textit{integer numbers} (Consider that house prices can be an integer number in million dollar only).
    line = sys.stdin.readline()
    line = line.strip()
    prices = line.split(",")
    for i in range(0, len(prices)):
        prices[i] = int(prices[i])
    
    # read the number of vertices
    line = sys.stdin.readline()
    line = line.strip()
    increase = line.split(",")
    for i in range(0, len(increase)):
        increase[i] = float(increase[i])



# Add your implementation here .... 
    result =  max_profit(money, num_houses, prices, increase)

# Add your functions and call them to generate the result. 

    print(result)

main()
