import game_manager, game_rules, unittest
from player import makePlayer
from multiprocessing.pool import ThreadPool

def run_test(gm):
    gm.play()
    game_rules.printBoard(gm.board)
    # print(gm.GetWinner(), "WINS")
    return gm.board

class GameTest(unittest.TestCase):

    def makeGame(self, size, player1, player2, depth, script=None):

        gm = game_manager.GameManager(
              size
            , size
            , makePlayer(player1, 'x', depth)
            , makePlayer(player2, 'o', depth)
            , script
            , True)
        return gm

    def test1(self):
        p1 = 'm'
        p2 = 'd'
        depth = 2
        gm = self.makeGame(4, p1, p2, depth)
        # gm.play()
        pool = ThreadPool(processes=1)
        async_result = pool.apply_async(run_test, [gm])
        result = None
        try:
            returned_value = async_result.get(300)
            self.assertEqual(gm.board,
                             [['x', ' ', ' ', 'o'], [' ', 'x', ' ', 'x'], [' ', 'o', ' ', 'o'], ['o', 'x', 'o', 'x']])
        except Exception as e:
            self.fail('Timed out: {}'.format(e))

    # def test1s(self):
    #     # Identical to test1 but totally run by the game1.log script
    #     # Minimax player never gets called.
    #     #Truncate game1.log to script the early game play and Minimax for rest
    #     p1 = 'm'
    #     p2 = 'd'
    #     depth = 2
    #     gm = self.makeGame(4, p1, p2, depth, 'game1.log')

    #     pool = ThreadPool(processes=1)
    #     async_result = pool.apply_async(run_test, [gm])
    #     result = None
    #     try:
    #         returned_value = async_result.get(300)
    #         self.assertEqual(gm.board,
    #                          [['x', ' ', ' ', 'o'], [' ', 'x', ' ', 'x'], [' ', 'o', ' ', 'o'], ['o', 'x', 'o', 'x']])
    #     except Exception as e:
    #         self.fail('Timed out: {}'.format(e))

    # def test2(self):
    #     p1 = 'm'
    #     p2 = 'd'
    #     depth = 5
    #     gm = self.makeGame(4, p1, p2, depth)

    #     pool = ThreadPool(processes=1)
    #     async_result = pool.apply_async(run_test, [gm])
    #     result = None
    #     try:
    #         returned_value = async_result.get(300)
    #         self.assertEqual(gm.board,
    #                          [['x', ' ', ' ', 'o'], [' ', 'x', ' ', 'x'], [' ', 'o', ' ', 'o'], ['o', 'x', 'o', 'x']])
    #     except Exception as e:
    #         self.fail('Timed out: {}'.format(e))

    # def test3u_depth0(self):
    #     p1 = 'd'
    #     p2 = 'm'
    #     depth = 4
    #     gm = self.makeGame(6, p1, p2, depth)

    #     board = [['x', ' ', 'x', 'o', 'x', 'o'], [' ', 'x', 'o', 'x', 'o', 'x'], [' ', 'o', 'x', 'o', 'x', 'o'], ['o', 'x', 'o', 'x', 'o', 'x'], ['x', 'o', 'x', 'o', 'x', 'o'], ['o', 'x', 'o', 'x', 'o', 'x']]
    #     depth = 4  # I am counting down from 4 to 0, so this is actually depth 0.  You can count up if you prefer
    #     symbol = 'o'  # If you function signature does not include symbol, just remove this in the fxn call below
    #     # walk through the execution of this function
    #     # it should find 3 possible moves.
    #     # values for those moves are -5, -5, -5
    #     v = gm.p2.maxValue(board, depth)  # change the name/arguments/return to fit your method signature
    #     self.assertEqual(v, -5)

    # def test3u_depth2(self):
    #     p1 = 'd'
    #     p2 = 'm'
    #     depth = 4
    #     gm = self.makeGame(6, p1, p2, depth)

    #     board = [[' ', ' ', 'x', ' ', 'x', 'o'], [' ', 'x', 'o', 'x', 'o', 'x'], [' ', 'o', 'x', 'o', 'x', 'o'], ['o', 'x', 'o', 'x', 'o', 'x'], ['x', 'o', 'x', 'o', 'x', 'o'], ['o', 'x', 'o', 'x', 'o', 'x']]
    #     depth = 2  
    #     symbol = 'o'  # If you function signature does not include symbol, just remove this in the fxn call below
    #     # walk through the execution of this function
    #     # it should find 5 possible moves.
    #     # values for those moves are -6, -5, -4, -4, -4
    #     v = gm.p2.maxValue(board, depth,symbol)  # change the name/arguments/return to fit your method signature
    #     self.assertEqual(v, -4)

    # def test3(self):
    #     p1 = 'd'
    #     p2 = 'm'
    #     depth = 4
    #     gm = self.makeGame(6, p1, p2, depth)

    #     pool = ThreadPool(processes=1)
    #     async_result = pool.apply_async(run_test, [gm])
    #     result = None
    #     try:
    #         returned_value = async_result.get(300)
    #         self.assertEqual(gm.board, [[' ', 'o', ' ', 'o', ' ', 'o'], [' ', ' ', ' ', ' ', ' ', ' '],
    #                                     [' ', ' ', ' ', ' ', 'x', ' '], ['o', ' ', ' ', 'x', 'o', 'x'],
    #                                     [' ', ' ', 'x', ' ', 'x', 'o'], ['o', 'x', 'o', 'x', 'o', 'x']])
    #     except Exception as e:
    #         self.fail('Timed out: {}'.format(e))


    # def test4(self):
    #     # Uses script to have alternative start moves
    #     p1 = 'm'
    #     p2 = 'd'
    #     depth = 6
    #     gm = self.makeGame(4, p1, p2, depth, 'game4.log')

    #     pool = ThreadPool(processes=1)
    #     async_result = pool.apply_async(run_test, [gm])
    #     result = None
    #     try:
    #         returned_value = async_result.get(300)
    #         self.assertEqual(gm.board,
    #                          [['x', ' ', ' ', 'o'], ['o', ' ', ' ', 'x'], ['x', 'o', 'x', 'o'], ['o', ' ', ' ', 'x']])
    #     except Exception as e:
    #         self.fail('Timed out: {}'.format(e))


    # def test5(self):
    #     p1 = 'd'
    #     p2 = 'a'
    #     depth = 4
    #     gm = self.makeGame(6, p1, p2, depth)
    #     gm.play()
    #     pool = ThreadPool(processes=1)
    #     async_result = pool.apply_async(run_test, [gm])
    #     result = None
    #     try:
    #         returned_value = async_result.get(300)
    #         self.assertEqual(gm.board, [[' ', 'o', ' ', 'o', ' ', 'o'], [' ', ' ', ' ', ' ', ' ', ' '],
    #                                     [' ', ' ', ' ', ' ', 'x', ' '], ['o', ' ', ' ', 'x', 'o', 'x'],
    #                                     [' ', ' ', 'x', ' ', 'x', 'o'], ['o', 'x', 'o', 'x', 'o', 'x']])
    #     except Exception as e:
    #         self.fail('Timed out: {}'.format(e))


    # def test6(self):
    #     p1 = 'a'
    #     p2 = 'd'
    #     depth = 6
    #     gm = self.makeGame(8, p1, p2, depth)

    #     pool = ThreadPool(processes=1)
    #     async_result = pool.apply_async(run_test, [gm])
    #     result = None
    #     try:
    #         returned_value = async_result.get(300)
    #         self.assertEqual(gm.board,
    #                          [['x', ' ', 'x', ' ', 'x', ' ', ' ', 'o'], [' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x'],
    #                           [' ', ' ', 'x', ' ', 'x', ' ', ' ', 'o'], ['o', ' ', ' ', ' ', ' ', 'x', ' ', 'x'],
    #                           [' ', 'o', ' ', 'o', ' ', ' ', ' ', 'o'], ['o', ' ', 'o', ' ', ' ', ' ', 'o', 'x'],
    #                           ['x', ' ', ' ', 'o', ' ', 'o', 'x', 'o'], ['o', 'x', 'o', 'x', 'o', 'x', 'o', 'x']])
    #     except Exception as e:
    #         self.fail('Timed out: {}'.format(e))


    # def test6s(self):
    #     # Identical to test6 but completely script driven
    #     p1 = 'a'
    #     p2 = 'd'
    #     depth = 6
    #     gm = self.makeGame(8, p1, p2, depth, 'game6.log')

    #     pool = ThreadPool(processes=1)
    #     async_result = pool.apply_async(run_test, [gm])
    #     result = None
    #     try:
    #         returned_value = async_result.get(300)
    #         self.assertEqual(gm.board,
    #                          [['x', ' ', 'x', ' ', 'x', ' ', ' ', 'o'], [' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x'],
    #                           [' ', ' ', 'x', ' ', 'x', ' ', ' ', 'o'], ['o', ' ', ' ', ' ', ' ', 'x', ' ', 'x'],
    #                           [' ', 'o', ' ', 'o', ' ', ' ', ' ', 'o'], ['o', ' ', 'o', ' ', ' ', ' ', 'o', 'x'],
    #                           ['x', ' ', ' ', 'o', ' ', 'o', 'x', 'o'], ['o', 'x', 'o', 'x', 'o', 'x', 'o', 'x']])
    #     except Exception as e:
    #         self.fail('Timed out: {}'.format(e))

    # def myTest1(self):
    #     #TESTING TO SEE THAT X COMPLETES THE DOUBLE JUMP FROM TOP RIGHT TO BOTTOM RIGHT RATHER THAN A SINGLE JUMP TO MAKE SURE HEURISTIC IS CORRECT
    #     #But I am getting an error witht he code reading the file
    #     p1 = 'm'
    #     p2 = 'd'
    #     depth = 2
    #     gm = self.makeGame(5, p1, p2, depth, 'test1.log')

    #     pool = ThreadPool(processes=1)
    #     async_result = pool.apply_async(run_test, [gm])
    #     result = None
    #     try:
    #         returned_value = async_result.get(300)
    #         #final game board is not correct could not see the final state beacause log file did not work
    #         self.assertEqual(gm.board,
    #                          [['x', ' ', ' ', 'o', 'x'], [' ', 'x', ' ', 'x','o'], [' ', 'o', ' ', 'o','x'], ['o', 'x', 'o', 'x','o'], ['o', 'x', 'o', 'x','o']])
    #     except Exception as e:
    #         self.fail('Timed out: {}'.format(e))

    # def myTest2(self):
    #     #TESTING TO AB MAKES THE SAME MOVE AS MINI
    #     #But I am getting an error witht he code reading the file
    #     p1 = 'm'
    #     p2 = 'd'
    #     depth = 2
    #     gm = self.makeGame(5, p1, p2, depth, 'test1.log')

    #     pool = ThreadPool(processes=1)
    #     async_result = pool.apply_async(run_test, [gm])
    #     result = None
    #     try:
    #         returned_value = async_result.get(300)
    #         #final game board is not correct could not see the final state beacause log file did not work
    #         self.assertEqual(gm.board,
    #                          [['x', ' ', ' ', 'o', 'x'], [' ', 'x', ' ', 'x','o'], [' ', 'o', ' ', 'o','x'], ['o', 'x', 'o', 'x','o'], ['o', 'x', 'o', 'x','o']])
    #     except Exception as e:
    #         self.fail('Timed out: {}'.format(e))



if __name__== "__main__":
    unittest.main()