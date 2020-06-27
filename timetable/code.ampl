set D; # Days
set P; # Periods
set C_GU1; # Courses taken by GU students first year
set C_GU2; # Courses taken by GU students second year
set C_EM1; # Courses taken by EM students first year
set C_EM2; # Courses taken by EM students second year
set C_adv; # Other courses that should not collide
set C_others; # All other courses
set C_g; # Set with courses that have their exercises splitted into small groups
set C := C_GU1 union C_GU2 union C_EM1 union C_EM2 union C_adv union C_others;
# All courses
set R_ex; # Exercise rooms
set R_lec; # Lecture rooms
set R_com; # Computer rooms
set R := R_ex union R_lec union R_com; # All rooms

param s{C}; # Course size
param m{R}; # Room capacity
param n_com{C}; # Number of computer labs
param n_lec{C}; # Number of lectures
param n_ex{C}; # Number of excercises
param g{C}; # Number of groups for exercises

var x{D,P,C,R} binary; # Lectures
var y{D,P,C,R} binary; # Excercises
var z{D,P,C,R} binary; # Computer labs
var w1{C,R} binary; # Help variable to force lectures to be in the same room
var w2{C,R} binary; # Help variable to force excercises to be in the same room

# Object function
minimize f: sum{d in D, c in C, r in R} (x[d,1,c,r] + x[d,3,c,r] + 4*x[d,4,c,r] + 3*y[d,1,c,r] + y[d,2,c,r] + 2*y[d,4,c,r] + 3*z[d,1,c,r] + z[d,2,c,r] + 2*z[d,4,c,r]) + sum{c in C, r in R} 5*(x[1,1,c,r] + y[1,1,c,r] + z[1,1,c,r] + x[5,4,c,r] + y[5,4,c,r] + z[5,4,c,r]);

subject to
# Make sure that the classes fits in the rooms
Room_capacity_lec{d in D, p in P, c in C, r in R_lec}:
x[d,p,c,r]*s[c] <= m[r];

Room_capacity_ex{d in D, p in P, c in C, r in R_ex}:
0.8*y[d,p,c,r]*s[c]/g[c] <= m[r];

Room_capacity_com{d in D, p in P, c in C, r in R_com}:
z[d,p,c,r]*s[c] <= m[r];

# Make sure that two courses will not be scheduled in the same room at the same time
Room_collision{d in D, p in P, r in R}:
sum{c in C} (x[d,p,c,r] + y[d,p,c,r] + z[d,p,c,r]) <= 1;

# Make sure that courses in the same group will not collide with each other
Course_collision_GU1{d in D, p in P}:
sum{c in C_GU1, r in R} (x[d,p,c,r] + y[d,p,c,r]/g[c] + z[d,p,c,r]) <= 1;

Course_collision_GU2{d in D, p in P}:
sum{c in C_GU2, r in R} (x[d,p,c,r] + y[d,p,c,r]/g[c] + z[d,p,c,r]) <= 1;

Course_collision_EM1{d in D, p in P}:
sum{c in C_EM1, r in R} (x[d,p,c,r] + y[d,p,c,r]/g[c] + z[d,p,c,r]) <= 1;

Course_collision_EM2{d in D, p in P}:
sum{c in C_EM2, r in R} (x[d,p,c,r] + y[d,p,c,r]/g[c] + z[d,p,c,r]) <= 1;

Course_collision_adv{d in D, p in P}:
sum{c in C_adv, r in R} (x[d,p,c,r]) <= 1;

# Make sure that the other courses will not collide with themselves
Course_collision_others{d in D, p in P, c in C_others}:
sum{r in R} (x[d,p,c,r] + y[d,p,c,r]/g[c] + z[d,p,c,r]) <= 1;

# Make sure that the correct number of lectures, exercises,
and computerlabs is scheduled
Lecture_sessions{c in C}:
sum{d in D, p in P, r in R_lec} x[d,p,c,r] = n_lec[c];
Excercise_sessions{c in C}:
sum{d in D, p in P, r in R_ex} y[d,p,c,r] = n_ex[c]*g[c];
Computer_sessions{c in C}:
sum{d in D, p in P, r in R_com} z[d,p,c,r] = n_com[c];

# Make sure that there is some day between lectures when possible
Sparse{d in D diff {5}, c in C diff {'MMG800','LGMA10','MMGK11','MMGL31','MMGF30'}}:
sum{p in P, r in R} (x[d,p,c,r] + x[d+1,p,c,r]) <= 1;

# Forces the lectures for each course to be scheduled in the same room
Same_room_lec{c in C, r in R_lec}:
sum{d in D, p in P} x[d,p,c,r] - w1[c,r]*n_lec[c] = 0;

# Forces the exercises for each course to be scheduled in the same room
Same_room_ex1{c in C diff C_g, r in R_ex}:
sum{d in D, p in P} y[d,p,c,r] - w2[c,r]*n_ex[c] = 0;

Same_room_ex2{c in C_g, r1 in R_ex, r2 in R_ex}:
sum{d in D, p in P} (y[d,p,c,r1] + y[d,p,c,r2])
- w2[c,r1]*n_ex[c] - w2[c,r2]*n_ex[c] = 0;

# Forces exercises to be scheduled directly after lectures
# Works for courses that have number of lectures >= number of exercises
Ex_after_lec{d in D, p in P diff {1}, c in C diff{'MSG830','LGMA10'}}: 
sum{r in R_lec} (y[d,p,c,r]/g[c] - x[d,p-1,c,r]) <= 0;

# Make sure that courses does not have more than 1 lecture each day
Lecture_limit{d in D, c in C}: sum{p in P, r in R} x[d,p,c,r] <= 1;

# The same for exercises
Excercise_limit1{d in D, c in C diff (C_g union {'MMGL31','LGMA10'})}: sum{p in P, r in R} y[d,p,c,r] <= 1;

Excercise_limit2{d in D}: sum{p in P, r in R} y[d,p,'MMGL31',r] <= 2;

# The same for computerlabs
Computer_limit{d in D, c in C diff {'MSG830'}}:
sum{p in P, r in R} z[d,p,c,r] <= 1;

# Locked sessions that can not be changed
MMG300: x[2,2,'MMG300','Pascal'] + y[2,3,'MMG300','MVH12'] + x[4,2,'MMG300','Pascal'] + y[4,3,'MMG300','MVH12'] = 4;

MVG300: x[1,3,'MVG300','Euler'] + z[1,4,'MVG300','MVF22'] + x[3,3,'MVG300','Euler'] + z[3,4,'MVG300','MVF22'] + x[5,3,'MVG300','Euler'] + z[5,4,'MVG300','MVF22'] = 6;

LGMA10: x[2,3,'LGMA10','Pascal'] + x[4,3,'LGMA10','Pascal'] + x[1,3,'LGMA10','Pascal'] + x[5,3,'LGMA10','Pascal'] + y[1,1,'LGMA10','MVF31'] + y[1,2,'LGMA10','MVF31'] + y[2,1,'LGMA10','MVF31'] + y[2,2,'LGMA10','MVF31'] + y[4,1,'LGMA10','MVF31'] + y[4,2,'LGMA10','MVF31'] + y[5,1,'LGMA10','MVF31'] + y[5,2,'LGMA10','MVF31'] = 12;

MSG830: x[2,2,'MSG830','Euler'] + x[4,3,'MSG830','Euler'] + y[3,2,'MSG830','MVF33']
+ z[2,3,'MSG830','MVF22'] + z[2,4,'MSG830','MVF22'] = 5;

MMGF30: x[2,2,'MMGF30','MVF23'] + x[3,3,'MMGF30','MVF23'] + x[5,2,'MMGF30','MVF23'] = 3;

