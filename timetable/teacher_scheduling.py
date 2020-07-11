from ortools.linear_solver import pywraplp

D=[1,2,3,4,5] # Days
P=[1,2,3,4,5,6,7,8] # Periods in the day
K=["K1","K2","K3","K4","K5","K6","KM","KG"] #teachers. KM for music and KG for gym

#Courses taken by each grade G1, G2, G...
C_G1=["MAT1","LAN1","ENG1","CIE1","HIS1","PHY1","ART1","TEC1","MUS1","ORI1","REL1"]
C_G2=["MAT2","LAN2","ENG2","CIE2","HIS2","PHY2","ART2","TEC2","MUS2","ORI2","REL2"]
C_G3=["MAT3","LAN3","ENG3","CIE3","HIS3","PHY3","ART3","TEC3","MUS3","ORI3","REL3"]
C_G4=["MAT4","LAN4","ENG4","CIE4","HIS4","PHY4","ART4","TEC4","MUS4","ORI4","REL4"]
C_G5=["MAT5","LAN5","ENG5","CIE5","HIS5","PHY5","ART5","TEC5","MUS5","ORI5","REL5"]
C_G6=["MAT6","LAN6","ENG6","CIE6","HIS6","PHY6","ART6","TEC6","MUS6","ORI6","REL6"]
C_double=["PHY1","PHY2"] #courses forced to have two lectures per d
C = C_G1 + C_G2 + C_G3 + C_G4 + C_G5 + C_G6

hours ={"MAT1":10,
"LAN1":8,
"ENG1":3,
"CIE1":3,
"HIS1":3,
"PHY1":4,
"ART1":2,
"TEC1":1,
"MUS1":2,
"ORI1":1,
"REL1":2,
"MAT2":10,
"LAN2":8,
"ENG2":3,
"CIE2":3,
"HIS2":3,
"PHY2":4,
"ART2":2,
"TEC2":1,
"MUS2":2,
"ORI2":1,
"REL2":2,
"MAT3":10,
"LAN3":8,
"ENG3":3,
"CIE3":3,
"HIS3":3,
"PHY3":4,
"ART3":2,
"TEC3":1,
"MUS3":2,
"ORI3":1,
"REL3":2,
"MAT4":10,
"LAN4":8,
"ENG4":3,
"CIE4":3,
"HIS4":3,
"PHY4":4,
"ART4":2,
"TEC4":1,
"MUS4":2,
"ORI4":1,
"REL4":2,
"MAT5":8,
"LAN5":8,
"ENG5":3,
"CIE5":4,
"HIS5":4,
"PHY5":4,
"ART5":1,
"TEC5":2,
"MUS5":2,
"ORI5":1,
"REL5":2,
"MAT6":8,
"LAN6":8,
"ENG6":3,
"CIE6":4,
"HIS6":4,
"PHY6":4,
"ART6":1,
"TEC6":2,
"MUS6":2,
"ORI6":1,
"REL6":2}

contractHours = {"K1":40, "K2":40, "K3":40, "K4":40, "K5":40, "K6":40, "KM":20, "KG":30}

aptitude =  {"MAT1":{"K1":0,"K2":3,"K3":4,"K4":4,"K5":4,"K6":4,"KM":4,"KG":4},
"LAN1":{"K1":0,"K2":3,"K3":4,"K4":4,"K5":4,"K6":4,"KM":4,"KG":4},
"ENG1":{"K1":0,"K2":3,"K3":4,"K4":4,"K5":4,"K6":4,"KM":4,"KG":4},
"CIE1":{"K1":0,"K2":3,"K3":4,"K4":4,"K5":4,"K6":4,"KM":4,"KG":4},
"HIS1":{"K1":0,"K2":3,"K3":4,"K4":4,"K5":4,"K6":4,"KM":4,"KG":4},
"PHY1":{"K1":3,"K2":3,"K3":4,"K4":4,"K5":4,"K6":4,"KM":4,"KG":0},
"ART1":{"K1":0,"K2":3,"K3":4,"K4":4,"K5":4,"K6":4,"KM":4,"KG":4},
"TEC1":{"K1":0,"K2":3,"K3":4,"K4":4,"K5":4,"K6":4,"KM":4,"KG":4},
"MUS1":{"K1":3,"K2":3,"K3":4,"K4":4,"K5":4,"K6":4,"KM":0,"KG":4},
"ORI1":{"K1":0,"K2":3,"K3":4,"K4":4,"K5":4,"K6":4,"KM":4,"KG":4},
"REL1":{"K1":0,"K2":3,"K3":4,"K4":4,"K5":4,"K6":4,"KM":4,"KG":4},
"MAT2":{"K1":3,"K2":0,"K3":4,"K4":4,"K5":4,"K6":4,"KM":4,"KG":4},
"LAN2":{"K1":3,"K2":0,"K3":4,"K4":4,"K5":4,"K6":4,"KM":4,"KG":4},
"ENG2":{"K1":3,"K2":0,"K3":4,"K4":4,"K5":4,"K6":4,"KM":4,"KG":4},
"CIE2":{"K1":3,"K2":0,"K3":4,"K4":4,"K5":4,"K6":4,"KM":4,"KG":4},
"HIS2":{"K1":3,"K2":0,"K3":4,"K4":4,"K5":4,"K6":4,"KM":4,"KG":4},
"PHY2":{"K1":3,"K2":3,"K3":4,"K4":4,"K5":4,"K6":4,"KM":4,"KG":0},
"ART2":{"K1":3,"K2":0,"K3":4,"K4":4,"K5":4,"K6":4,"KM":4,"KG":4},
"TEC2":{"K1":3,"K2":0,"K3":4,"K4":4,"K5":4,"K6":4,"KM":4,"KG":4},
"MUS2":{"K1":3,"K2":3,"K3":4,"K4":4,"K5":4,"K6":4,"KM":0,"KG":4},
"ORI2":{"K1":3,"K2":0,"K3":4,"K4":4,"K5":4,"K6":4,"KM":4,"KG":4},
"REL2":{"K1":3,"K2":0,"K3":4,"K4":4,"K5":4,"K6":4,"KM":4,"KG":4},
"MAT3":{"K1":4,"K2":4,"K3":0,"K4":3,"K5":4,"K6":4,"KM":4,"KG":4},
"LAN3":{"K1":4,"K2":4,"K3":0,"K4":3,"K5":4,"K6":4,"KM":4,"KG":4},
"ENG3":{"K1":4,"K2":4,"K3":0,"K4":3,"K5":4,"K6":4,"KM":4,"KG":4},
"CIE3":{"K1":4,"K2":4,"K3":0,"K4":3,"K5":4,"K6":4,"KM":4,"KG":4},
"HIS3":{"K1":4,"K2":4,"K3":0,"K4":3,"K5":4,"K6":4,"KM":4,"KG":4},
"PHY3":{"K1":4,"K2":4,"K3":3,"K4":3,"K5":4,"K6":4,"KM":4,"KG":0},
"ART3":{"K1":4,"K2":4,"K3":0,"K4":3,"K5":4,"K6":4,"KM":4,"KG":4},
"TEC3":{"K1":4,"K2":4,"K3":0,"K4":3,"K5":4,"K6":4,"KM":4,"KG":4},
"MUS3":{"K1":4,"K2":4,"K3":3,"K4":3,"K5":4,"K6":4,"KM":0,"KG":4},
"ORI3":{"K1":4,"K2":4,"K3":0,"K4":3,"K5":4,"K6":4,"KM":4,"KG":4},
"REL3":{"K1":4,"K2":4,"K3":0,"K4":3,"K5":4,"K6":4,"KM":4,"KG":4},
"MAT4":{"K1":4,"K2":4,"K3":3,"K4":0,"K5":4,"K6":4,"KM":4,"KG":4},
"LAN4":{"K1":4,"K2":4,"K3":3,"K4":0,"K5":4,"K6":4,"KM":4,"KG":4},
"ENG4":{"K1":4,"K2":4,"K3":3,"K4":0,"K5":4,"K6":4,"KM":4,"KG":4},
"CIE4":{"K1":4,"K2":4,"K3":3,"K4":0,"K5":4,"K6":4,"KM":4,"KG":4},
"HIS4":{"K1":4,"K2":4,"K3":3,"K4":0,"K5":4,"K6":4,"KM":4,"KG":4},
"PHY4":{"K1":4,"K2":4,"K3":3,"K4":3,"K5":4,"K6":4,"KM":4,"KG":0},
"ART4":{"K1":4,"K2":4,"K3":3,"K4":0,"K5":4,"K6":4,"KM":4,"KG":4},
"TEC4":{"K1":4,"K2":4,"K3":3,"K4":0,"K5":4,"K6":4,"KM":4,"KG":4},
"MUS4":{"K1":4,"K2":4,"K3":3,"K4":3,"K5":4,"K6":4,"KM":0,"KG":4},
"ORI4":{"K1":4,"K2":4,"K3":3,"K4":0,"K5":4,"K6":4,"KM":4,"KG":4},
"REL4":{"K1":4,"K2":4,"K3":3,"K4":0,"K5":4,"K6":4,"KM":4,"KG":4},
"MAT5":{"K1":4,"K2":4,"K3":4,"K4":4,"K5":0,"K6":3,"KM":4,"KG":4},
"LAN5":{"K1":4,"K2":4,"K3":4,"K4":4,"K5":0,"K6":3,"KM":4,"KG":4},
"ENG5":{"K1":4,"K2":4,"K3":4,"K4":4,"K5":0,"K6":3,"KM":4,"KG":4},
"CIE5":{"K1":4,"K2":4,"K3":4,"K4":4,"K5":0,"K6":3,"KM":4,"KG":4},
"HIS5":{"K1":4,"K2":4,"K3":4,"K4":4,"K5":0,"K6":3,"KM":4,"KG":4},
"PHY5":{"K1":4,"K2":4,"K3":4,"K4":4,"K5":3,"K6":3,"KM":4,"KG":0},
"ART5":{"K1":4,"K2":4,"K3":4,"K4":4,"K5":0,"K6":3,"KM":4,"KG":4},
"TEC5":{"K1":4,"K2":4,"K3":4,"K4":4,"K5":0,"K6":3,"KM":4,"KG":4},
"MUS5":{"K1":4,"K2":4,"K3":4,"K4":4,"K5":3,"K6":3,"KM":0,"KG":4},
"ORI5":{"K1":4,"K2":4,"K3":4,"K4":4,"K5":0,"K6":3,"KM":4,"KG":4},
"REL5":{"K1":4,"K2":4,"K3":4,"K4":4,"K5":0,"K6":3,"KM":4,"KG":4},
"MAT6":{"K1":4,"K2":4,"K3":4,"K4":4,"K5":3,"K6":0,"KM":4,"KG":4},
"LAN6":{"K1":4,"K2":4,"K3":4,"K4":4,"K5":3,"K6":0,"KM":4,"KG":4},
"ENG6":{"K1":4,"K2":4,"K3":4,"K4":4,"K5":3,"K6":0,"KM":4,"KG":4},
"CIE6":{"K1":4,"K2":4,"K3":4,"K4":4,"K5":3,"K6":0,"KM":4,"KG":4},
"HIS6":{"K1":4,"K2":4,"K3":4,"K4":4,"K5":3,"K6":0,"KM":4,"KG":4},
"PHY6":{"K1":4,"K2":4,"K3":4,"K4":4,"K5":3,"K6":3,"KM":4,"KG":0},
"ART6":{"K1":4,"K2":4,"K3":4,"K4":4,"K5":3,"K6":0,"KM":4,"KG":4},
"TEC6":{"K1":4,"K2":4,"K3":4,"K4":4,"K5":3,"K6":0,"KM":4,"KG":4},
"MUS6":{"K1":4,"K2":4,"K3":4,"K4":4,"K5":3,"K6":3,"KM":0,"KG":4},
"ORI6":{"K1":4,"K2":4,"K3":4,"K4":4,"K5":3,"K6":0,"KM":4,"KG":4},
"REL6":{"K1":4,"K2":4,"K3":4,"K4":4,"K5":3,"K6":0,"KM":4,"KG":4}}

discomfort = {"K1":[[4,0,0,0,0],
[4,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,4]],
"K2":[[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,4,0,0],
[0,0,4,0,4]],
"K3":[[4,4,4,4,4],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,4]],
"K4":[[4,4,4,4,4],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,4]],
"K5":[[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,4]],
"K6":[[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[4,0,0,0,0],
[4,0,0,0,4]],
"KM":[[4,4,4,4,4],
[4,4,4,4,4],
[4,4,4,4,4],
[4,4,4,4,4],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,4]],
"KG":[[0,0,4,0,0],
[0,0,4,0,0],
[0,0,4,0,0],
[0,0,4,0,0],
[0,0,4,0,0],
[0,0,4,0,0],
[0,0,4,0,0],
[0,0,4,0,4]]}

solver = pywraplp.Solver('teacher_scheduling',pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

# Lectures
x = {}
for d in D:
    for p in P:
        for c in C:
            for k in K:
                x[d,p,c,k] = solver.IntVar(0,1,'')

# forces courses to be delivered by the same teacher
w1 = {}
for c in C:
    for k in K:
        w1[c,k] = solver.IntVar(0,1,'')

# Make sure that a teacher will not be scheduled in two classes at the same time
for d in D:
    for p in P:
        for k in K:
            solver.Add(solver.Sum([x[d,p,c,k] for c in C]) <= 1)

# Make sure that courses in the same group will not collide with each other
for d in D:
    for p in P:
            solver.Add(solver.Sum([x[d,p,c,k] for c in C_G1 for k in K]) <= 1)

for d in D:
    for p in P:
            solver.Add(solver.Sum([x[d,p,c,k] for c in C_G2 for k in K]) <= 1)

for d in D:
    for p in P:
            solver.Add(solver.Sum([x[d,p,c,k] for c in C_G3 for k in K]) <= 1)

for d in D:
    for p in P:
            solver.Add(solver.Sum([x[d,p,c,k] for c in C_G4 for k in K]) <= 1)

for d in D:
    for p in P:
            solver.Add(solver.Sum([x[d,p,c,k] for c in C_G5 for k in K]) <= 1)

for d in D:
    for p in P:
            solver.Add(solver.Sum([x[d,p,c,k] for c in C_G6 for k in K]) <= 1)

# Make sure no more than 2 hours are scheduled per day for a given class
for d in D:
    for c in C:
            solver.Add(solver.Sum([x[d,p,c,k] for p in P for k in K]) <= 2)

# Make sure that the correct number of class hours is scheduled
for c in C:
    solver.Add(solver.Sum([x[d,p,c,k] for d in D for p in P for k in K]) == hours[c])

# Make sure techers do not teach more than their assigned number of hours by contract
for k in K:
    solver.Add(solver.Sum([x[d,p,c,k] for d in D for p in P for c in C]) <= contractHours[k])

# Make sure each course is only taught by one teacher
for c in C:
    for k in K:
        solver.Add(solver.Sum([x[d,p,c,k] for d in D for p in P]) == w1[c,k]*hours[c])

# Locked sessions that can not be changed. 
# solver.Add(x[1,1,'PHY2','KM'] + x[1,2,'PHY2','KM'] == 2) # Sí funciona pero está comentado

#TODO Following three constraints generate a syntax error
# Make sure that given courses have 2 or 0 periods each day
#Two_Lectures_per_day{d in D, c in C_double}:
#sum{p in P, k in K} x[d,p,c,k] = 2 or 0; #i hoped this would allow some days to have 2 and other 0
#ERROR: sum{d in D, k  >>> in  <<< K} (x[d,p,c,k] + x[d,p+1,c,k]) = 2;

# # Make sure that given courses do not have more than 1 lecture each day
# for d in D:
#     for c in C:
#         solver.Add(solver.Sum([x[d,p,c,k] for p in P for k in K]) <= 1)

# # Make sure that classes are taught in 2 hour segments when possible (excludes classes even number of hours)
# for k in K:
#     for p in P:
#         for c in {'MAT1','MAT2','MAT3','MAT4','MAT5','MAT6','LAN1','LAN2','LAN3','LAN4','LAN5','LAN6'}:
#             if(p != 8):    
#                 solver.Add(solver.Sum([x[d,p,c,k] + x[d,p+1,c,k] for d in D for k in K]) == 2)


#TODO create different types of classes? Some taught by teachers and others by aids
#TODO make sure that classes with more than one period per day are given at consecutive times
#TODO caso de clases de gimnasia para dos niveles en el mismo horario con el mismo profe
#TODO caso de dos o más asignaturas que se pueden dar juntas en el mismo horario

# Make sure that there is some day between lectures when possible (excludes classes with 4 or more hours per week)
for d in D:
    if (d != 5):
        for c in C:
            if(c not in {'MAT1','MAT2','MAT3','MAT4','MAT5','MAT6','LAN1','LAN2','LAN3','LAN4','LAN5','LAN6','PHY1','PHY2','PHY3','PHY4','PHY5','PHY6','CIE5','CIE6','HIS5','HIS6'}):
                solver.Add(solver.Sum([x[d,p,c,k] + x[d+1,p,c,k] for p in P for k in K]) <= 1)

# Objective
objective_terms = []
for d in D:
    for p in P:
        for c in C:
            for k in K:
                objective_terms.append(x[d,p,c,k]*(aptitude[c][k]+discomfort[k][p-1][d-1]))

solver.Minimize(solver.Sum(objective_terms))

# Solve
status = solver.Solve()

# Print solution.
if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
    print('Total cost = ', solver.Objective().Value(), '\n')
    for d in D:
        for p in P:
            for c in C:
                for k in K:
                    # Test if x[i,j] is 1 (with tolerance for floating point arithmetic).
                    if x[d,p,c,k].solution_value() > 0.5:
                        print(d, p, c, k, x[d,p,c,k].solution_value())
else:
    print("Problem Infeasible")
