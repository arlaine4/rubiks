import move as m
import cube as c
import visual as visu
import utils
import hta

def	edges_placement(cube, bad_edges, good_edges_up, good_edges_down, lst_moves):
        t_p_u = [[2, 0, 1, 3, 0, 1], [2, 1, 2, 1, 0, 1], [2, 2, 1, 0, 0, 1], [2, 1, 0, 4, 0, 1]]
        t_p_d = [[5, 0, 1, 0, 2, 1], [5, 1, 2, 1, 2, 1], [5, 2, 1, 3, 2, 1], [5, 1, 0, 4, 2, 1]]
        value_pos_up = [[2, 3], [2, 1], [2, 0], [2, 4]]
        value_pos_down = [[5, 0], [5, 1], [5, 3], [5, 4]]
        bad_edges_values = []
        lst_order_edges = []
        lst_order_values = []
        next_pos = []
        found = False
        #-----------------------------------------------------------#
        #                       Partie Up                           #

        #--------------------------#
        # Selection starting point #
        i = 0
        if len(good_edges_up) > 0:
            if i < len(good_edges_up):
                while i < len(good_edges_up) - 1:
                    i += 1
            lst_order_edges.append(good_edges_up[i])
            lst_order_values.append([good_edges_up[i][0], cube.cube[good_edges_up[i][0]][good_edges_up[i][1]][good_edges_up[i][2]]])

        elif len(good_edges_up) == 0:
            lst_moves, cube, found = utils.check_and_get_ud_slice_edge(cube, "U", lst_moves) #call avec bad_edges ou avec good_edges_down ?
            if found is False:
                    lst_moves, cube = utils.check_and_get_edge_opposite_face(cube, "U", lst_moves)
        #                          #
        #--------------------------#
        

        lst_order_edges[0], lst_order_values[0] = utils.replace_tpu(lst_order_edges[0], "U") #update lst_order_values
        next_pos = utils.get_next_edge_placement_pos(lst_order_edges[0], cube, "U") #recuperation position ideale pour next edge
        lst_order_edges.append([]) ; lst_order_values.append([])

        for edge in bad_edges: #recuperation values sur les bad_edges pour check de la bonne edge a moove sur la next_pos
            new_pos = edge
            bad_edges_value = utils.append_bad_edges_values(new_pos, cube)
            bad_edges_values.append([cube.cube[new_pos[0]][new_pos[1]][new_pos[2]], bad_edges_value])
    
        #ajuster lst_order_values du nombre de case decalees
        print("bonsoir ",lst_order_edges, next_pos)
        cube, lst_order_edges[1], lst_order_values[1] = utils.find_and_move_next_edge_placement(cube, lst_order_edges[0], lst_order_values[0],\
                bad_edges, bad_edges_values, next_pos, "U", lst_moves)

        # OK || lst_order_edges bien replace, besoin de mettre a jour lst_order_values
        # OK || recuperer a quelle position on doit placer l'edge suivante et la value que il doit y avoir a cet endroit la pour que ca soit dans l'ordre
        #-> trouver la piece avec cet valeur (check le cubie adjascent pour s'assurer que c'est le bon cubie
        #--> la deplacer jusqua la next_pos (check le next_pos.append(t_p_u[i])
        #---> faire ca jusqua ce que la liste lst_order_edge soit full
        #----> puis faire U ou U2 ou U' (celui qui coute le moins de coups) pour tout remettre aux VRAIES pos (ordonnees et a la bonne place parceque
        #la on est ordonnes mais pas a la bonne place)
        c.print_cube(cube)
        print("order edges : ", lst_order_edges, "order values : ", lst_order_values)
        #while len(lst_order_edges) != 4:
            #next_pos.clear()
            #next_pos.append(t_p_u[i])
            #break
        return cube, lst_moves
