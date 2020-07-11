# instructions
# go to [NEOS Server Gurobi](https://neos-server.org/neos/solvers/lp:Gurobi/AMPL.html)
# upload teachertt.mod in "Model"
# upload datatt.dat in "Data"
# upload commandstt in "Commands"

set K; # teachers
set D; # Days
set P; # Periods
set C_G1; # Courses taken by G1
set C_G2; # Courses taken by G2
set C_G3; # Courses taken by G3
set C_G4; # Courses taken by G4
set C_G5; # Courses taken by G5
set C_G6; # Courses taken by G6
set C_double; #courses forced to have two lectures per day
set C := C_G1 union C_G2 union C_G3 union C_G4 union C_G5 union C_G6; # All courses

param contractHours{K}; #Teaching hours by contract 
param hours{C}; #Required number of hours for each course 
param aptitude{C,K}; # Ability to dictate a class
param discomfort{D,K,P}; # Disconfort for teaching at given times
# param discomfort{k in K, P[k], 1..T}

var x{D,P,C,K} binary; # Lectures
var w1{C,K} binary; # forces courses to be delivered by the same teacher

# Object function
# This is the function that should be adjusted to include "availability"
minimize f: sum{d in D, p in P, c in C, k in K} x[d,p,c,k]*aptitude[c,k] + sum{d in D, p in P, c in C, k in K} x[d,p,c,k]*discomfort[d,k,p];

subject to
# Make sure that a teacher will not be scheduled in two classes at the same time
Teacher_collision{d in D, p in P, k in K}:
sum{c in C} (x[d,p,c,k]) <= 1;

# Make sure that courses in the same group will not collide with each other
Course_collision_G1{d in D, p in P, k in K}:
sum{c in C_G1} (x[d,p,c,k]) <= 1;

Course_collision_G2{d in D, p in P, k in K}:
sum{c in C_G2} (x[d,p,c,k]) <= 1;

Course_collision_G3{d in D, p in P, k in K}:
sum{c in C_G3} (x[d,p,c,k]) <= 1;

Course_collision_G4{d in D, p in P, k in K}:
sum{c in C_G4} (x[d,p,c,k]) <= 1;

Course_collision_G5{d in D, p in P, k in K}:
sum{c in C_G5} (x[d,p,c,k]) <= 1;

Course_collision_G6{d in D, p in P, k in K}:
sum{c in C_G6} (x[d,p,c,k]) <= 1;

# Make sure that the correct number of class hours is scheduled
Class_hours{c in C}:
sum{d in D, p in P, k in K} x[d,p,c,k] = hours[c];

# Make sure techers do not teach more than their assigned number of hours by contract
Teacher_hours{k in K}:
sum{d in D, p in P, c in C} x[d,p,c,k] <= contractHours[k];

# Make sure each course is only taught by one teacher
Same_teacher_course{c in C, k in K}:
sum{d in D, p in P} x[d,p,c,k] - w1[c,k]*hours[c] = 0;

#Locked sessions that cannot be changed
PHY2: x[1,1,'PHY2','KM'] + x[1,2,'PHY2','KM'] = 2; #Music teacher must teach GYM on monday and tuesday first and second block

#TODO Following three constraints generate a syntax error
# Make sure that given courses have 2 or 0 periods each day
#Two_Lectures_per_day{d in D, c in C_double}:
#sum{p in P, k in K} x[d,p,c,k] = 2 or 0; #i hoped this would allow some days to have 2 and other 0
#ERROR: sum{d in D, k  >>> in  <<< K} (x[d,p,c,k] + x[d,p+1,c,k]) = 2;

# Make sure that given courses do not have more than 1 lecture each day
#Lecture_limit{d in D, c in C}: sum{p in P, k in K} x[d,p,c,k] <= 1;

# Make sure that classes are taught in 2 hour segments when possible (excludes classes even number of hours)
#DoubleBlock{k in K, p in P diff {8}, c in {'MAT1','MAT2','MAT3','MAT4','MAT5','MAT6','LEN1','LEN2','LEN3','LEN4','LEN5','LEN6'}}:
#sum{d in D, k in K} (x[d,p,c,k] + x[d,p+1,c,k]) = 2; #ERROR: sum{d in D, k  >>> in  <<< K} (x[d,p,c,k] + x[d,p+1,c,k]) = 2;

# Make sure that there is some day between lectures when possible (excludes classes with 4 or more hours per week)
#Sparse{d in D diff {5}, c in C diff {'MAT1','MAT2','MAT3','MAT4','MAT5','MAT6','LEN1','LEN2','LEN3','LEN4','LEN5','LEN6','PHY1','PHY2','PHY3','PHY4','PHY5','PHY6','CIE5','CIE6','HIS5','HIS6'}}:
#sum{p in P, k in K} (x[d,p,c,k] + x[d+1,p,c,k]) <= 1;