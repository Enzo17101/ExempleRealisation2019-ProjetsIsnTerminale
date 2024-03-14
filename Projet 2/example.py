
hanoi = [[1,2,3,4]
        ,[],
         []]
hanoi[1].insert(0,hanoi[0].pop(0))
hanoi[2].insert(0,hanoi[0].pop(0))
hanoi[2].insert(0,hanoi[1].pop(0))
hanoi[1].insert(0,hanoi[0].pop(0))
hanoi[0].insert(0,hanoi[2].pop(0))
hanoi[1].insert(0,hanoi[2].pop(0))
hanoi[1].insert(0,hanoi[0].pop(0))
hanoi[2].insert(0,hanoi[0].pop(0))
hanoi[0].insert(0,hanoi[1].pop(0))
hanoi[2].insert(0,hanoi[1].pop(0))
hanoi[1].insert(0,hanoi[0].pop(0))
hanoi[0].insert(0,hanoi[2].pop(0))
hanoi[0].insert(0,hanoi[1].pop(0))
hanoi[2].insert(0,hanoi[1].pop(0))
hanoi[1].insert(0,hanoi[0].pop(0))
hanoi[2].insert(0,hanoi[0].pop(0))
hanoi[2].insert(0,hanoi[1].pop(0))

if hanoi == [[],[],[1,2,3,4]] :
    print("Terminé")
    hanoi = [["x","x","x","x"],["x","x","x","x"],[1,2,3,4]]
print(f"{hanoi[0][0]}   {hanoi[1][0]}   {hanoi[2][0]}\n{hanoi[0][1]}   {hanoi[1][1]}   {hanoi[2][1]}\n{hanoi[0][2]}   {hanoi[1][2]}   {hanoi[2][2]}\n{hanoi[0][3]}   {hanoi[1][3]}   {hanoi[2][3]}" )
