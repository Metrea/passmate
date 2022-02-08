INSERT INTO events_category_level1
VALUES
(1, 'Theme Park'),
(2, 'Zoo'),
(3, 'Attraction'),
(4, 'Aquarium'),
(5, 'Museum'),
(6, 'Water Park'),
(7, 'Family Fun');


INSERT INTO events_category_level2
VALUES
(1,'Amusement Park',1),
(2,'Boardwalk Park',1),
(3,'Midwat Attraction',3),
(4,'Aquarium',4),
(5,'Zoo',2),
(6,'History Museum',5),
(7,'Go Kart',3),
(8,'Water Park',6),
(9,'Trampoline Park/Gymnatics',7);

INSERT INTO public.events_event(id, city_code, city_desc, country_code, country_desc, event_desc, event_id, geo_data, category_level1_id, category_level2_id, event_status, event_type)
	VALUES 
(1, 'chi', 'chi place 1', 'us', 'United States of America', 'Five Day Park Hopper Ticket', '9XW', '{"latitude": 35.961,"longitude": -112.1365}', 1, 1, 'live', 'simple_ticket'),
(2, 'chi', 'chi place 2', 'us', 'United States of America', 'Imperial Helicopter Tour', 'DP9', '{"latitude": 35.961,"longitude": -112.1365}', 1, 2, 'live', 'simple_ticket'),
(3, 'chi', 'chi place 3', 'us', 'United States of America', 'Ingressoland - Any Day', '1D7B8', '{"latitude": 28.3451302,"longitude": -81.5748225}', 2, 5, 'live', 'simple_ticket'),
(4, 'chi', 'chi place 4', 'us', 'United States of America', 'North Canyon Helicopter Tour', 'DPB', '{"latitude": 35.961,"longitude": -112.1365}', 3, 7, 'live', 'simple_ticket'),
(5, 'chi', 'chi place 5', 'us', 'United States of America', 'Seven day Parkhopper', '9XX', '{"latitude": 35.961,"longitude": -112.1365}', 6, 8, 'live', 'simple_ticket'),
(6, 'chi', 'chi place 6', 'us', 'United States of America', 'Two day Parkhopper', '9XY', '{"latitude": 35.961,"longitude": -112.1365}', 7, 9, 'live', 'simple_ticket');
