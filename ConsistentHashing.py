import math
tabServer = [0, 2, 4,  6, 10, 12, 14, 15, 17, 19, 21, 22, 26, 28, 31] #Les serveurs grisé
taille_cercle = 32 #taille du cercle
taille_table = int(math.log(taille_cercle, 2))
for j in tabServer:
    tab = []
    for i in range(0,taille_table):
        valeur_tableau = int((math.pow(2, i) + j) % taille_cercle)
        tmp_tab_server = [abs(x-valeur_tableau) for x in tabServer]
        if valeur_tableau < tabServer[tmp_tab_server.index(min(tmp_tab_server))]:
                     tmp_tab_server.pop(tmp_tab_server.index(min(tmp_tab_server)))
        tab.append(tabServer[tmp_tab_server.index(min(tmp_tab_server))])
    print("table du serveur {} : {}".format(j,tab))
