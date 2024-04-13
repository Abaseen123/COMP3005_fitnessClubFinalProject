INSERT INTO MEMBERS (first_name, last_name, card_no, height, currweight, targweight, username)
VALUES 
('talha', 'ather', 123456789, 200, 100, 120, 'talha123'),
('abaseen', 'ahmadzai', 987654321, 153, 50, 80, 'abaseen123');


INSERT INTO TRAINERS (first_name, last_name, rtine, username)
VALUES 
('LeBron', 'James', '5km Run, 50 push ups, 50 sit ups, 50 squats, 50 lunges', 'lebron123'),
('Tom', 'Brady', '1km Run, 100 push ups, 100 sit ups, 70 squats, 70 lunges', 'tom123'),
('Cristiano', 'Ronaldo', '7km Run, 30 push ups, 30 sit ups, 30 squats, 30 lunges', 'cristiano123');

INSERT INTO SOLO_SESSION (trainer_id, member_id, dayofweek, starttime, endtime, room_no, payedoff)
VALUES
(1, 0, 'Monday', '09:00:00', '12:00:00', 200, NULL),
(2, 0, 'Tuesday', '13:00:00', '16:00:00', 204, NULL),
(3, 0, 'Wednesday', '17:00:00', '20:00:00', 203, NULL),
(1, 0, 'Saturday', '10:00:00', '13:00:00', 200, NULL);

INSERT INTO GROUP_SESSION (trainer_id, member_id, dayofweek, starttime, endtime, room_no, payedoff)
VALUES
(1, 0, 'Thursday', '09:00:00', '12:00:00', 201, NULL),
(2, 0, 'Friday', '13:00:00', '16:00:00', 202, NULL),
(3, 0, 'Saturday', '17:00:00', '20:00:00', 205, NULL),
(3, 0, 'Sunday', '14:00:00', '17:00:00', 205, NULL);

INSERT INTO ACCOUNTS (username, pass, perms)
VALUES
('talha123', '12345', 'Members'),
('abaseen123', '12345', 'Members'),
('lebron123', '12345', 'Trainers'),
('tom123', '12345', 'Trainers'),
('cristiano123', '12345', 'Trainers'),
('admin', '12345', 'Admin');

INSERT INTO ROOMS (num, treadmill, benchpress, squatrack, ellyptical)
VALUES
(200, TRUE, TRUE, TRUE, FALSE),
(201, TRUE, TRUE, TRUE, TRUE),
(202, FALSE, TRUE, TRUE, TRUE),
(203, FALSE, TRUE, TRUE, TRUE),
(204, FALSE, TRUE, TRUE, TRUE),
(205, TRUE, TRUE, TRUE, FALSE);