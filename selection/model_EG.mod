set STUDENTS;   # origins
set COURSES;   # destinations
set BLOCK_A;
set BLOCK_B;
set BLOCK_C;

param seats {COURSES} >= 0;   # amounts required at destinations

   check: sum {i in STUDENTS} 1 <= sum {j in COURSES} seats[j];

param ranking {STUDENTS,COURSES} >= 0;   # shipment costs per unit
var Asignacion {STUDENTS,COURSES} >= 0;    # units to be shipped

minimize Total_Cost:
   sum {i in STUDENTS, j in COURSES} ranking[i,j] * Asignacion[i,j];

subject to BloqueA {i in STUDENTS}:
   sum {j in BLOCK_A} Asignacion[i,j] = 1;

subject to BloqueB {i in STUDENTS}:
   sum {j in BLOCK_B} Asignacion[i,j] = 1;

subject to Deportivos {i in STUDENTS}:
   sum {j in BLOCK_C} Asignacion[i,j] = 1;

subject to O_cero {i in STUDENTS, j in COURSES}: Asignacion[i,j] >= 0;
subject to O_uno {i in STUDENTS, j in COURSES}: Asignacion[i,j] <= 1;

subject to Demand {j in COURSES}:
   sum {i in STUDENTS} Asignacion[i,j] <= seats[j];