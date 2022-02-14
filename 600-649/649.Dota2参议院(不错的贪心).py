'''
这题分析的不够准确，但是很快就明白了，是一个贪心算法去“杀敌人”，但是我的贪心逻辑
有瑕疵。我是仅仅让每个人确保能击杀一个敌人即可，在后面的人可能杀到他前面执行过命令
的敌人，但是官方题解的贪心，如果该位置没死，就杀他后面的敌人。这样不仅可以保证杀到
人，还能救下一个“队友”，这是我的理解。换种说法就是杀前面存在的敌人不如杀后面存在的
敌人，事已至此，向后发展看的话，杀后面的敌人可以减少伤亡，但是杀前面已经执行指令的
敌人是没有这个效果。 很遗憾，又是差一点。 其实当写的时候就感觉算法有问题，但是又没
去探究。 我为这题付出的时间确实不够。 --下午摸鱼，记录。
'''
from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant = deque()
        dire = deque()

        for i, ch in enumerate(senate):
            if ch == "R":
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            if radiant[0] < dire[0]:
                radiant.append(radiant[0] + n)
            else:
                dire.append(dire[0] + n)
            radiant.popleft()
            dire.popleft()

        return "Radiant" if radiant else "Dire"



test = ['RDD', "DDRRR", "DRRDRDRDRDDRDRDR"]
for i in test[1:]:
    print(i, '-->', Solution().predictPartyVictory(i))