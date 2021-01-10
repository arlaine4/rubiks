import move as m
import cube as c
import visual as visu
import utils
import hta

def	edges_placement(cube, bad_edges, good_edges_up, good_edges_down, lst_moves):
        t_p_u = [[2, 0, 1, 3, 0, 1], [2, 1, 2, 4, 0, 1], [2, 2, 1, 0, 0, 1], [2, 1, 0, 1, 0, 1]]
        #t_p_u = [[2, 0, 1, 3, 0, 1], [2, 1, 0, 4, 0, 1], [2, 2, 1, 0, 0, 1], [2, 1, 2, 1, 0, 1]] #TPU positions were wrong
        #t_p_d = [[5, 0, 1, 0, 2, 1], [5, 1, 0, 4, 2, 1], [5, 2, 1, 3, 2, 1], [5, 1, 2, 1, 2, 1]] #TPD positions were wrong
        t_p_d = [[5, 0, 1, 0, 2, 1], [5, 1, 2, 4, 2, 1], [5, 2, 1, 3, 2, 1], [5, 1, 0, 1, 2, 1]]
        value_pos_up = [[2, 3], [2, 4], [2, 0], [2, 1]]
        value_pos_down = [[5, 0], [5, 4], [5, 3], [5, 1]]
        lst_order_edges = []
        lst_order_values = []
        id_current = 0
        next_pos = []
        found = False
        #separer good edge en up et down
        #-----------------------------------------------------------#
        #                       Partie Up                           #

        #--------------------------#
        # Selection starting point #
        if len(good_edges_up) > 0:
            lst_order_edges.append(good_edges_up[0])
            lst_order_values.append([good_edges_up[0][0], cube.cube[good_edges_up[0][0]][good_edges_up[0][1]][good_edges_up[0][2]]])
        elif len(good_edges_up) == 0:
            lst_moves, cube, found = utils.check_and_get_ud_slice_edge(cube, "U", lst_moves) #call avec bad_edges ou avec good_edges_down ?
            if found is False:
                    lst_moves, cube = utils.check_and_get_edge_opposite_face(cube, "U", lst_moves)
        i = 0
        lst_order_edges[0], lst_order_values = utils.replace_tpu(lst_order_edges[0], "U")
        next_pos = utils.get_next_edge_placement_pos(lst_order_edges[0], cube, "U")
        print("next_pos after finding first edge : ", next_pos)
        # OK || lst_order_edges bien replace, besoin de mettre a jour lst_order_values
        # OK || recuperer a quelle position on doit placer l'edge suivante et la value que il doit y avoir a cet endroit la pour que ca soit dans l'ordre
        #-> trouver la piece avec cet valeur (check le cubie adjascent pour s'assurer que c'est le bon cubie
        #--> la deplacer jusqua la next_pos (check le next_pos.append(t_p_u[i])
        #---> faire ca jusqua ce que la liste lst_order_edge soit full
        #----> puis faire U ou U2 ou U' (celui qui coute le moins de coups) pour tout remettre aux VRAIES pos (ordonnees et a la bonne place parceque
        #la on est ordonnes mais pas a la bonne place)
        c.print_cube(cube)
        print("order edges : ", lst_order_edges, "order values : ", lst_order_values)
        while len(lst_order_edges) != 4:
            next_pos.clear()
            next_pos.append(t_p_u[i])
            break
	    		
        #-------------------------#
        # Mise en place des edges #
        return cube, lst_moves
        """elif len(good_edges) == 0:
            pass
            #chercher edge en ud_slice, prendre la premiere que on trouve
                #move un edge ud_slice sur la face up sur l'edge la plus proche, qui coute le moins de coups
            ##chercher une edge de up qui serait sur down
                #move un edge down sur la face up sur l'edge la plus proche, qui coute le moins de coups
            #re assigner lst_order_edges et lst_order_values
        #-------------------------#

        #deplacer une a une les edge a la suite de lst_order[i] en checkant lst_order_values[i] pour savoir
        #de quel edge de la face on part

        #on passe pas a l'edge suivante tant que la courrante n'est pas a la suite de la precedente

        #forbid F and B moves
        #append every move to lst_moves
        #ne pas faire de move de la face ou on se situe si ca nique l'ordre ni qui niquerai le placement
        #d'une edge deja dans lst_order_edges
        return cube, lst_moves"""
