CREATE TABLE IF NOT EXISTS MEMBERS
            (MEMBER_ID SERIAL PRIMARY KEY NOT NULL,
            FIRST_NAME TEXT NOT NULL,
            LAST_NAME TEXT NOT NULL,
	    	CARD_NO INT NOT NULL,
	    	HEIGHT INT NOT NULL,
	    	CURRWEIGHT INT NOT NULL,
            TARGWEIGHT INT NOT NULL,
            USERNAME TEXT UNIQUE NOT NULL);

CREATE TABLE IF NOT EXISTS TRAINERS
            (TRAINER_ID SERIAL PRIMARY KEY NOT NULL,
            FIRST_NAME TEXT NOT NULL,
            LAST_NAME TEXT NOT NULL,
	        RTINE TEXT NOT NULL,
            USERNAME TEXT UNIQUE NOT NULL);

CREATE TABLE IF NOT EXISTS SOLO_SESSION
            (TRAINER_ID INT NOT NULL,
            MEMBER_ID INT,
            DAYOFWEEK TEXT NOT NULL,
            STARTTIME TIME NOT NULL,
            ENDTIME TIME NOT NULL,
            ROOM_NO INT NOT NULL,
	        PAYEDOFF BOOLEAN);

CREATE TABLE IF NOT EXISTS GROUP_SESSION
            (TRAINER_ID INT NOT NULL,
            MEMBER_ID INT NOT NULL,
            DAYOFWEEK TEXT NOT NULL,
            STARTTIME TIME NOT NULL,
            ENDTIME TIME NOT NULL,
            ROOM_NO INT NOT NULL,
	        PAYEDOFF BOOLEAN);

CREATE TABLE IF NOT EXISTS ACCOUNTS
            (USERNAME TEXT UNIQUE NOT NULL,
            PASS TEXT NOT NULL,
            PERMS TEXT NOT NULL);

CREATE TABLE IF NOT EXISTS ROOMS
            (NUM INT PRIMARY KEY NOT NULL,
            TREADMILL BOOLEAN,
	        BENCHPRESS BOOLEAN,
            SQUATRACK BOOLEAN,
            ELLYPTICAL BOOLEAN);

CREATE TABLE IF NOT EXISTS ROOM_BOOKINGS (
    booking_id SERIAL PRIMARY KEY,
    room_no INT NOT NULL,
    day TEXT NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    purpose TEXT NOT NULL
);