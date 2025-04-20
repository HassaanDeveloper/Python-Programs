def average(a:float, b:float):
    """
    Returns the number which is half way between a and b
    """
    sum = a + b
    return sum / 2

def main():
    avg_1 = average(0, 10)
    avg_2 = average(8, 10)
    final = average(avg_1, avg_2)

    print("average1: ", avg_1)
    print("average2: ", avg_2)
    print("final average: ", final)