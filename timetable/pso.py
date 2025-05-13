# import random
# import matplotlib.pyplot as plt 
# from tabulate import tabulate 

# # Параметры
# NUM_PARTICLES = 50
# MAX_ITERATIONS = 100
# DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# PERIODS_PER_DAY = 3
# GROUPS = ["Group 1", "Group 2", "Group 3", "Group 4"]
# COURSES = {"DSA": 3, "ENG": 5, "IAI": 2, "APY": 2, "GEO": 1, "HIS": 1, "MNS": 1}
# CONFLICT_PAIRS = [("DSA", "ENG"), ("DSA", "IAI"), ("APY", "ENG"), ("HIS", "GEO")]
# #  Определение класса
# class Particle:
#     def __init__(self):
#         self.schedule = self.generate_random_schedule()
#         self.best_schedule = self.schedule.copy()
#         self.best_value = float('-inf')
#         self.velocity = {}
# # 1 Метод 
#     def generate_random_schedule(self) -> dict:
#         schedule = {}
#         available_courses = {group: random.sample(list(COURSES.keys()), len(COURSES)) for group in GROUPS}

#         for group in GROUPS:
#             course_index = 0
#             for day in DAYS:
#                 for period in range(PERIODS_PER_DAY):
#                     course = available_courses[group][course_index % len(available_courses[group])]
#                     schedule[(day, period, group)] = course
#                     course_index += 1

#         return schedule
# # 2. Метод
#     def update_velocity(self, global_best_schedule) -> None:
#         for key in self.schedule:
#             if random.random() < 0.5:
#                 self.schedule[key] = global_best_schedule[key]
# # 3. Метод
#     def update_position(self) -> None:
#         key1, key2 = random.sample(list(self.schedule.keys()), 2)
#         self.schedule[key1], self.schedule[key2] = self.schedule[key2], self.schedule[key1]

# #  Фитнес-функция
# def fitness_function(schedule) -> int:
#     penalty = 0  #штраф 

#     for group in GROUPS:
#         course_counts = {course: 0 for course in COURSES}
#         for day in DAYS:
#             for period in range(PERIODS_PER_DAY):
#                 course = schedule[(day, period, group)]
#                 if course != 'Free': 
#                     course_counts[course] += 1 # курс

#         penalty += sum(abs(course_counts[course] - COURSES[course]) for course in COURSES) 

#     return -penalty

# # Основная функция PSO
# def pso():
#     particles = [Particle() for _ in range(NUM_PARTICLES)]
#     global_best_schedule = particles[0].schedule.copy()
#     global_best_value = float('-inf')
#     best_values = []

#     for iteration in range(MAX_ITERATIONS):
#         for particle in particles:
#             value = fitness_function(particle.schedule)
#             if value > particle.best_value:
#                 particle.best_value = value
#                 particle.best_schedule = particle.schedule.copy()
#             if value > global_best_value:
#                 global_best_value = value
#                 global_best_schedule = particle.schedule.copy()
#             particle.update_velocity(global_best_schedule)
#             particle.update_position()

#         best_values.append(global_best_value)
#         print(f"Iteration {iteration + 1}: Best Fitness = {global_best_value}")

#     return global_best_schedule, global_best_value, best_values

# # Вывод расписания
# def print_schedule(schedule) -> None:
#     print("\n📅 Optimized Schedule:")
#     for day in DAYS:
#         headers = ["Group"] + [f"{i+1}-hour" for i in range(PERIODS_PER_DAY)]
#         table = []
#         for group in GROUPS:
#             row = [group] + [schedule[(day, period, group)] for period in range(PERIODS_PER_DAY)]
#             table.append(row) 
#         print(f"\n📌 {day}")
#         print(table)
#         # print(tabulate(table, headers=headers, tablefmt="fancy_grid"))


# # Запуск алгоритма PSO
# best_schedule, best_value, best_values = pso()

# print_schedule(best_schedule)
# print(f"\n✅ Best fitness value: {best_value}")

# # График
# plt.plot(range(1, MAX_ITERATIONS + 1), best_values, marker='o', linestyle='-', color='b')
# plt.xlabel("Iterations")
# plt.ylabel("Best Fitness Value")
# plt.grid()
# plt.gca().invert_yaxis()
# plt.show()ffff

# ///////////////////////////////////////////////////////////////////////////////////
