import heuristics
from readInfo import teachers, audiences, subjects, specialities

if __name__ == "__main__":
    # best_appearance, num = chromosome.evolution(teachers, audiences, subjects, specialities)
    # print(f"Number of generations: {num}, best: {best_appearance.appearance}")
    heuristics.make_timetable()
    print("ok")
    for lesson in heuristics.timetable:
        print(lesson)