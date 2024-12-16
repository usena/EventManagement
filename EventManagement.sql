-- Create the database
DROP DATABASE IF EXISTS EventManagement;
CREATE DATABASE EventManagement;
USE EventManagement;

-- Creating CateringType Table
CREATE TABLE CateringType(
	CateringTypeID		INT AUTO_INCREMENT 			PRIMARY KEY,
    CateringType		VARCHAR(50)					NOT NULL,
    CateringStandard	ENUM('Standard', 'Premium')	DEFAULT 'Standard',
    CateringDesc		VARCHAR(250)				NOT NULL,
    ContainAllergens	BOOLEAN						NOT NULL,
    CateringPrice		DECIMAL(10,2)				NOT NULL
);

-- Creating Venue Table
CREATE TABLE Venue (
    VenueID 		INT AUTO_INCREMENT 	PRIMARY KEY,
	VenueName 		VARCHAR(255)		NOT NULL,
    VenueAddress 	VARCHAR(255)		NOT NULL,
    VenueType 		ENUM('Indoor', 'Outdoor')	NOT NULL,
    VenuePhone 		VARCHAR(20)			NOT NULL,
    VenueEmail 		VARCHAR(100)		,
    VenueCapacity 	INT					NOT NULL,
    VenuePrice 		DECIMAL(10, 2)		NOT NULL
);

-- Creating User Table
CREATE TABLE `User` (
    UserID 			INT AUTO_INCREMENT 	PRIMARY KEY,
    UserName 		VARCHAR(255)		NOT NULL,
    UserLName 		VARCHAR(255)		NOT NULL,
    UserPhone 		VARCHAR(20)			NOT NULL,
    UserEmail 		VARCHAR(100)
);

-- Creating Organizer Table
CREATE TABLE Organizer (
    OrganizerID 	INT AUTO_INCREMENT 	PRIMARY KEY,
    OrganizerName 	VARCHAR(255)		NOT NULL,
    OrganizerLName 	VARCHAR(255)		NOT NULL,
    OrganizerPhone 	VARCHAR(20)			NOT NULL,
    OrganizerEmail 	VARCHAR(100)		NOT NULL
);

-- Creating Event Table
CREATE TABLE `Event` (
    EventID 		INT AUTO_INCREMENT	PRIMARY KEY,
    EventName 		VARCHAR(255) 		NOT NULL,
    EventType 		ENUM('Wedding', 'Birthday Party', 'Conference', 'Seminar', 'Other')	NOT NULL,
    EventDetails 	TEXT				,
    EventDate		DATE 				NOT NULL,
    EventCapacity	INT					NOT NULL,
    VenueID			INT 				NOT NULL,
    CateringTypeID	INT 				NOT NULL,
    UserID			INT 				NOT NULL,
    OrganizerID		INT					DEFAULT 0,
    FOREIGN KEY (VenueID) REFERENCES Venue(VenueID) ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (CateringTypeID) REFERENCES CateringType(CateringTypeID) ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (UserID) REFERENCES `User`(UserID) ON UPDATE CASCADE,
    FOREIGN KEY (OrganizerID) REFERENCES Organizer(OrganizerID)	ON UPDATE CASCADE ON DELETE SET NULL
);

-- Creating Invitation Table
CREATE TABLE Invitation (
    InvitationID 	INT AUTO_INCREMENT 	PRIMARY KEY,
    Attend			BOOLEAN				NOT NULL,
    EventID			INT 				NOT NULL,
    UserID			INT 				NOT NULL,
    FOREIGN KEY (EventID) REFERENCES `Event`(EventID)	ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (UserID) REFERENCES `User`(UserID)		ON UPDATE CASCADE ON DELETE CASCADE
);

-- Creating Transaction_Bill Table
CREATE TABLE Transaction_Bill (
    BillID 			INT AUTO_INCREMENT 		PRIMARY KEY,
    BillPrice 		DECIMAL(10, 2) 			NOT NULL,
    EventID			INT 					NOT NULL,
    FOREIGN KEY (EventID) REFERENCES `Event`(EventID)	ON UPDATE CASCADE ON DELETE CASCADE
);

-- Add Constraints to Ensure No Overlapping Dates for the Same Venue and Package
ALTER TABLE `Event`
ADD CONSTRAINT unique_venue_date UNIQUE (VenueID, EventDate);

DELIMITER $$

CREATE TRIGGER OnUserDelete
AFTER DELETE ON `User`-- Trigger executes after a delete operation on the parent table
FOR EACH ROW
BEGIN
    -- Update all rows in UserActions where the foreign key matches the deleted UserID
    UPDATE `Event`
    SET UserID = 0
    WHERE UserID = OLD.UserID;
END$$

DELIMITER ;

DELIMITER $$

CREATE TRIGGER after_event_insert
AFTER INSERT ON Event
FOR EACH ROW
BEGIN
    DECLARE total_price DECIMAL(10, 2);

    -- Calculate the total price
    SELECT 
        (c.CateringPrice + v.VenuePrice + 500000) 
    INTO 
        total_price
    FROM 
        CateringType c
    JOIN 
        Venue v ON NEW.VenueID = v.VenueID
    WHERE 
        c.CateringTypeID = NEW.CateringTypeID;

    -- Insert the bill record
    INSERT INTO Transaction_Bill (BillPrice, EventID) 
    VALUES (total_price, NEW.EventID);
END$$

DELIMITER ;

-- Insert data into CateringType
INSERT INTO CateringType (CateringType, CateringStandard, CateringDesc, ContainAllergens, CateringPrice) 
VALUES 
    ('Wedding Catering', 'Premium', 'Premium wedding catering package', FALSE, 2500000.00);

-- Insert data into Venue
INSERT INTO Venue (VenueName, VenueAddress, VenueType, VenuePhone, VenueEmail, VenueCapacity, VenuePrice) 
VALUES 
    ('Grand Ballroom', '123 Main St', 'Indoor', '123-456-7890', 'info@venue.com', 500, 7500000.00);

-- Insert data into User
INSERT INTO `User` (UserName, UserLName, UserPhone, UserEmail)
VALUES 
    ('John', 'Doe', '123-456-7890', 'john.doe@example.com');

-- Insert data into Event
INSERT INTO Event (EventName, EventType, EventDetails, EventDate, EventCapacity, VenueID, CateringTypeID, UserID)
VALUES 
    ('Wedding Party', 'Wedding', 'Elegant wedding celebration', '2024-12-25', 200, 1, 1, 1);

