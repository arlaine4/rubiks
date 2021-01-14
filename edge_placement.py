import move as m
import cube as c
import visual as visu
import utils
import hta

def     edges_placement(cube, bad_edges, good_edges_up, good_edges_down, lst_moves):
        t_p_u = [[2, 0, 1, 3, 0, 1], [2, 1, 2, 1, 0, 1], [2, 2, 1, 0, 0, 1], [2, 1, 0, 4, 0, 1]]
        t_p_d = [[5, 0, 1, 0, 2, 1], [5, 1, 2, 1, 2, 1], [5, 2, 1, 3, 2, 1], [5, 1, 0, 4, 2, 1]]
        dic_pos_u = {"201" : [2, 3], "212" : [2, 1], "221" : [2, 0], "210" : [2, 4]}
        dic_pos_d = {"501" : [5, 0], "512" : [5, 1], "521" : [5, 3], "510" : [5, 4]}
        value_pos_up = [[2, 3], [2, 1], [2, 0], [2, 4]]
        value_pos_down = [[5, 0], [5, 1], [5, 3], [5, 4]]
        bad_edges_values = []
        lst_order_edges = []
        lst_order_values = []
        next_pos = []
        found = False
        #-------------------------#
        #           Up            #
        print("\n\n-------------------------------- UP edge_placement ---------------------------------------\n\n")
        good_edges_up.reverse()
        if len(good_edges_up) > 0:
            for i in range(len(good_edges_up)):
                lst_order_edges.append(good_edges_up[i])
                lst_order_values.append([good_edges_up[i][0], cube.cube[good_edges_up[i][0]][good_edges_up[i][1]][good_edges_up[i][2]]])
                lst_order_edges[i], lst_order_values[i] = utils.replace_tpu(lst_order_edges[i], lst_order_values[i], "U")
        elif len(good_edges_up) == 0:
            lst_moves, cube, found = utils.check_and_get_ud_slice_edge(cube, "U", lst_moves)
            if found is False:
                lst_moves, cube = utils.check_and_get_edge_oppisite_face(cube, "U", lst_moves)

        #print("lst_order_edges : {}\nlst_order_values : {}".format(lst_order_edges, lst_order_values))
        next_pos = utils.get_next_edge_placement_pos(lst_order_edges[len(lst_order_edges) - 1], cube, "U")
        #print("next_pos : {}".format(next_pos))

        for edge in bad_edges:
            new_pos = edge
            bad_edges_value = utils.append_bad_edges_values(new_pos, cube)
            bad_edges_values.append([cube.cube[new_pos[0]][new_pos[1]][new_pos[2]], bad_edges_value])

        i = len(lst_order_edges) - 1
        while i < 4:
            tmp_value = None
            tmp_edge = None
            if i == 3:
                break
            s = str(lst_order_edges[i][0]) + str(lst_order_edges[i][1]) + str(lst_order_edges[i][2])
            cube, lst_moves, tmp_edge, tmp_value= utils.find_and_move_next_edge_placement(cube, lst_order_values[i], dic_pos_u[s], \
                bad_edges, bad_edges_values, next_pos, "U", lst_moves, lst_order_edges)
            if tmp_edge in lst_order_edges and tmp_value in lst_order_values:
                break
            lst_order_edges.append(tmp_edge) ; lst_order_values.append(tmp_value)
            next_pos = utils.get_next_edge_placement_pos(lst_order_edges[len(lst_order_edges) - 1], cube, "U")
            c.print_cube(cube)
            i += 1

        #-------------------------#
        #           Down          #
        print("\n\n-------------------------------- DOWN edge_placement ---------------------------------------\n\n")
        lst_order_edges.clear() ; lst_order_values.clear()
        print(good_edges_down)
        if len(good_edges_down) > 0:
            for i in range(len(good_edges_down)):
                lst_order_edges.append(good_edges_down[i])
                lst_order_values.append([good_edges_down[i][0], cube.cube[good_edges_down[i][0]][good_edges_down[i][1]][good_edges_down[i][2]]])
                lst_order_edges[i], lst_order_values[i] = utils.replace_tpu(lst_order_edges[i], lst_order_values[i], "D")
                print(lst_order_edges, lst_order_values)
        elif len(good_edges_down) == 0:
            lst_moves, cube, found = utils.check_and_get_ud_slice_edge(cube, "D", lst_moves)
            if found is False:
                lst_moves, cube = utils.check_and_get_edge_oppisite_face(cube, "D", lst_moves)

        print("lst_order_edges : {}\nlst_order_values : {}".format(lst_order_edges, lst_order_values))
        next_pos = utils.get_next_edge_placement_pos(lst_order_edges[len(lst_order_edges) - 1], cube, "D")
        print("next_pos : {}".format(next_pos))

        for edge in bad_edges:
            new_pos = edge
            bad_edges_value = utils.append_bad_edges_values(new_pos, cube)
            bad_edges_values.append([cube.cube[new_pos[0]][new_pos[1]][new_pos[2]], bad_edges_value])

        i = len(lst_order_edges) - 1
        while i < 4:
            tmp_value = None
            tmp_edge = None
            s = str(lst_order_edges[i][0]) + str(lst_order_edges[i][1]) + str(lst_order_edges[i][2])
            cube, lst_moves, tmp_edge, tmp_value = utils.find_and_move_next_edge_placement(cube, lst_order_values[i], dic_pos_d[s], \
                    bad_edges, bad_edges_values, next_pos, "U", lst_moves, lst_order_edges)
            if tmp_edge in lst_order_edges and tmp_value in lst_order_values:
                break
            lst_order_edges.append(tmp_edge) ; lst_order_values.append(tmp_value)
            next_pos = utils.get_next_edge_placement_pos(lst_order_edges[len(lst_order_edges) - 1], cube, "D")
            print("lst_order_edges : {}\nlst_order_values : {}".format(lst_order_edges, lst_order_values))
            print("next_pos : {}".format(next_pos))
        return cube, lst_moves
