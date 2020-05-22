import random
import copy
from binary_search_tree.btnode import BSTNode
from binary_search_tree.btree import LinkedBST


class Board:
    """ Class for board representation """

    def __init__(self):
        """ (Board) -> NoneType
        Create the new board """

        self._data = [['_']*3 for _ in range(3)]

    def check_win(self):
        """ (Board) -> str/NoneType
        Check if someone win """

        for i in range(3):
            if self._data[i][0] != '_' and all(map(
                    lambda x: x == self._data[i][0],
                    self._data[i][1:])):
                return self._data[i][0]
            if self._data[0][i] == self._data[1][i] == \
                    self._data[2][i] != '_':
                return self._data[0][i]

        if self._data[0][0] == self._data[1][1] == \
                self._data[2][2] != '_':
            return self._data[0][0]

        if self._data[0][2] == self._data[1][1] == \
                self._data[2][0] != '_':
            return self._data[0][2]

        return None

    def possible(self):
        """ (Board) -> list
        Return the list with free positions """

        return [(x, y) for x in range(3)
                for y in range(3) if self._data[x][y] == '_']

    @staticmethod
    def _nb_win(tree):
        """ (LinkedBST) -> int
        Return the number of winning """

        def recurse(temp_tree):
            """ (LinkedBST) -> int
            REcursion for getting the number of winning """
            if temp_tree.left is None:
                if temp_tree.data.check_win == 'o':
                    return 1
                elif temp_tree.data.check_win == 'x':
                    return -1
                else:
                    return 0
            else:
                return recurse(temp_tree.left) + recurse(temp_tree.right)
        return recurse(tree)

    def move_computer(self):
        """ (Board) -> NoneType
        Simulate the computer movement """
        created_tree = LinkedBST()
        created_tree.add(self)

        def recursion(temp_board, tree, move):
            """ (Board, LinkedBST, str) -> NoneType
            Recursion for simulation game binary tree """
            pos = temp_board.possible()
            if temp_board.check_win() or not pos:
                return

            if move == 'x':
                nextt = 'o'
            else:
                nextt = 'x'

            if len(pos) == 1:
                board_l = copy.deepcopy(temp_board)
                board_r = copy.deepcopy(temp_board)
                board_l[pos[0]] = nextt
                tree.left = BSTNode(board_l)
                tree.right = BSTNode(board_r)
                return

            new_move_l = random.choice(pos)
            pos.remove(new_move_l)
            new_move_r = random.choice(pos)

            board_l = copy.deepcopy(temp_board)
            board_r = copy.deepcopy(temp_board)

            board_l[new_move_l] = nextt
            board_r[new_move_r] = nextt
            tree.left = BSTNode(board_l)
            tree.right = BSTNode(board_r)

            recursion(board_l, tree.left, nextt)
            recursion(board_r, tree.right, nextt)

        recursion(self, created_tree._root, 'x')
        left = self._nb_win(created_tree._root.left)
        right = self._nb_win(created_tree._root.right)

        if left > right:
            self._data = created_tree._root.left.data._data
        else:
            self._data = created_tree._root.right.data._data

    def __setitem__(self, tpl, value):
        """ (Board, tuple, str) -> NoneType
        Set the item if the conditions are right """
        assert 0 <= tpl[0] < 3 and 0 <= tpl[1] < 3
        assert value == 'o' or value == 'x'
        self._data[tpl[0]][tpl[1]] = value

    def __getitem__(self, tpl):
        """ (Board) -> str
        Return the item in the same position if numbers are right """
        assert 0 <= tpl[0] < 3 and 0 <= tpl[1] < 3
        return self._data[tpl[0]][tpl[1]]

    def __str__(self):
        """ (Board) -> str
        Return the string representation of board """
        return '\n'.join('|'.join(self[x, y] for y in range(3)) for x in range(3))
