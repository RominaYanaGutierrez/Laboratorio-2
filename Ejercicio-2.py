n = 5
#Formacion de figura
for i in range(n*2 - 1):
    if i < n:
        fig_asteriscos = i + 1
    else:
        fig_asteriscos = n*2 - i - 1

    for j in range(fig_asteriscos):
        print("*", end=" ")
    print()
