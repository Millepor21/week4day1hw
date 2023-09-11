# time: O(N) space: O(N)
import random

def create_show(fireworks, show_time):# time: O(1) space: O(N) + O(1) => O(N)
    fireworks.sort()# time: O(1) space: O(1)
    show = []# time: O(1) space: O(N)
    remaining_time = show_time# time: O(1) space: O(1)
    while remaining_time > 0 and fireworks:# time: O(N) space: O(1)
           # Select a random firework
           firework = random.choice(fireworks)# time: O(1) space: O(1)
           if firework <= remaining_time:# time: O(1) space: O(1)
               # Add the firework to the show

               show.append(firework)# time: O(1) space: O(1)

               remaining_time -= firework# time: O(1) space: O(1)
           else:# time: O(1) space: O(1)
              # This firework is too long, remove it from consideration
              fireworks.remove(firework)# time: O(1) space: O(1)
    return show# time: O(1) space: O(1)