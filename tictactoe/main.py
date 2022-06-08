#križić-kružić za dvoje igrača

# osnovne strukture za čuvanje stanja igre
polje = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
igrač = 'X'
zauzeti = set()
potez = 1

while potez <= 9:
	# ispis igračeg polja
	print(' |1|2|3')
	print('-'*7)
	print('1|'+polje[0][0]+'|'+polje[0][1]+'|'+polje[0][2])
	print('-'*7)
	print('2|'+polje[1][0]+'|'+polje[1][1]+'|'+polje[1][2])
	print('-'*7)
	print('3|'+polje[2][0]+'|'+polje[2][1]+'|'+polje[2][2])
  
  # unos poteza nekog igrača
	if potez % 2 == 0:
        igrač = 'O'
    else:
        igrač = 'X'
    unos = input('\n'+igrač+' unesi svoj potez u obliku x,y:').split(',')
    x,y = int(unos[0])-1,int(unos[1])-1
    if (x,y) not in zauzeti:
	#ovo provjerava je li polje u sučelju
            if x > 3:		
                print('Polje je izvan sučelja, molim unesite drugo polje.')
                continue
            elif y > 3:
                print('Polje je izvan sučelja, molim unesite drugo polje.')
                continue
            else:
                polje[x][y] = igrač
                zauzeti.add((x,y))
                potez += 1
    else:
        print('Ovo mjesto je zauzeto, unesi novu koordinatu')
        continue
	
	# provjeravanje uvjeta za pobjedu
	if len(set(polje[x])) == 1:
		potez = 11
	if len(set([polje[i][y] for i in range(3)])) == 1:
		potez = 11
	if x==y and polje[0][0]==polje[1][1]==polje[2][2]:
		potez = 11
	if (x,y) == (0,2) or (x,y) == (1,1) or (x,y) == (2,0):
		if polje[0][2]==polje[1][1]==polje[2][0]:
			potez = 11

# ispisivanje konačnog rezultata
if potez == 11:
	print(igrač+' je pobijedio!')
else:
	print('Nitko nije pobijedio')
