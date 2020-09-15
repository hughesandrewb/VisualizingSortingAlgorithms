import matplotlib.pyplot as plt
import matplotlib.animation as animation
import CreateRandomList

LIST_LENGTH = 25  # Length of random list to sort

A = CreateRandomList.CreateRandomList(LIST_LENGTH).randomList


def bubbleSort(A):
    swapped = True
    for i in range(len(A) - 1):
        if not swapped:
            break
        swapped = False
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                swapped = True
            yield A


fig, ax = plt.subplots()
ax.set_title('Bubble Sort')
bar_rects = ax.bar(range(len(A)), A, align="edge")
text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
iteration = [0]


def update_fig(A, rects, iteration):
    for rect, val in zip(rects, A):
        rect.set_height(val)
    iteration[0] += 1
    text.set_text("# of operations: {}".format(iteration[0]))


anim = animation.FuncAnimation(fig, func=update_fig,
                               fargs=(bar_rects, iteration), frames=bubbleSort(A), interval=100,
                               repeat=False)
anim.save("BubbleSortAnim.gif")
plt.show()
