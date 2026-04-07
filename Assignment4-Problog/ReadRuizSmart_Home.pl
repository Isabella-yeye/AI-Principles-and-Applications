% Assignment 4: ProbLog Program

% Probabilistic Facts
0.05::faulty_motion_sensor(living_room).
0.05::faulty_motion_sensor(hallway).
0.02::faulty_light_sensor.
0.03::faulty_temp_sensor.
0.01::faulty_thermostat.
0.01::power_failure.

% Normal conditions 
0.6::movement(living_room).
0.5::movement(hallway).
0.7::light_switch_on.
0.8::desired_heating.

% Rules for observations
motion_detected(Room) :- 
    not(faulty_motion_sensor(Room)), 
    movement(Room).

light_on :- 
    not(faulty_light_sensor), 
    light_switch_on.

heating_on :- 
    desired_heating,
    not(faulty_thermostat), 
    not(power_failure).

temp_reading_ok :- 
    not(faulty_temp_sensor).

incorrect_temp_reading :- 
    faulty_temp_sensor.

% Possible cause for fault
no_motion_detected(Room) :-
    not(motion_detected(Room)).

no_light :-
    not(light_on).

no_heating :-
    not(heating_on).

heating_failure_due_to_thermostat :- 
    faulty_thermostat.

heating_failure_due_to_power :- 
    power_failure.

light_off_due_to_power :- 
    power_failure.

% Evidence (Observations)
evidence(motion_detected(living_room), false).
evidence(light_on, false).

% Queries
query(faulty_motion_sensor(living_room)).
query(faulty_motion_sensor(hallway)).
query(faulty_light_sensor).
query(faulty_thermostat).
query(power_failure).