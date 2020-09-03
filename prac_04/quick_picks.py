
"""Quick Pick lottery program"""

"""imports"""
import random

"""CONSTRAINTS"""
QP_MAX = 45
QP_MIN = 1
NUMBERS_PER_LINE = 6

def main():

    number_of_qp = int(input("How many quick picks? "))

    for i in range(number_of_qp):
        qp = generate_numbers(QP_MAX, QP_MIN, NUMBERS_PER_LINE)
        print(" ".join("{:2}".format(number) for number in qp))


def generate_numbers(qp_max, qp_min, numbers_per_line):
    qp = []
    for j in range(numbers_per_line):
        number = random.randint(qp_min, qp_max)
        while number in qp:
            number = random.randint(qp_min, qp_max)
        qp.append(number)
    qp.sort
    return qp




main()