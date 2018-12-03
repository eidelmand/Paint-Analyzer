import Analyzer

testList = [(102,0,0), (102,51,0), (102,102,0), (51,102,0), (0,102,0), (0,102,51), (0,102,102,),(0,51,102),(0,0,102), (51,0,102), (102,0,102),
            (102,0,51), (32,32,32), (204,0,0),(204,102,0),(204,204,0),(102,204,0),(0,204,0),(0,204,102),(0,204,204),(0,102,204),(0,0,204),(102,0,204),
            (204,0,204),(204,0,102),(96,96,96), (225, 250, 225), (225, 250, 20), (205, 50, 225), (35, 250, 225), (225, 50, 25), (25, 250, 25), (25, 50, 225), (175, 200, 225),
            (150, 175, 200), (175, 100, 150), (125, 75, 50), (25, 50, 0), (0,0,0)]
print("Test")
result = Analyzer.main("test.jpg", 15, testList)
print("results")
for p in result : print p #if this prints out 5 different paints, its operating correctly

paint1 = (200, 200, 200) #baseline
paint2 = (205, 200, 210) #15 above
print(Analyzer.compareColor(paint1,paint2)) #if 15, it's comparing properly

Analyzer.repaint("test.jpg", result)
