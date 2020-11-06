
-- Creates the user table
CREATE TABLE "user"
(
    user_id integer NOT NULL,
    first_name character varying(20) NOT NULL,
    last_name character varying(20) NOT NULL,
    email character varying(50) NOT NULL,
    password character varying(30) NOT NULL,
    steps integer NOT NULL,
    points integer NOT NULL,
    PRIMARY KEY (user_id)
);



-- Inserts user data into the user table
INSERT INTO public.user(user_id, first_name, last_name, email, password, steps, points) VALUES (1, 'User1', 'GetFit', 'user1@usc.edu', 'fitness123', 500, 50);
INSERT INTO public.user(user_id, first_name, last_name, email, password, steps, points) VALUES (2, 'User2', 'LovesFit', 'user2@gmail.com', 'fitness123', 5000, 500);
INSERT INTO public.user(user_id, first_name, last_name, email, password, steps, points) VALUES (3, 'User3', 'Fitness', 'user3@yahoo.com', 'fitness123', 100, 0);
INSERT INTO public.user(user_id, first_name, last_name, email, password, steps, points) VALUES (4, 'User4', 'Running', 'user4@aol.com', 'fitness123', 10000, 1000);

INSERT INTO public.user(user_id, first_name, last_name, email, password, steps, points) VALUES (5, 'Jared', 'Stigter', 'jstigter@usc.edu', 'fitness123', 10000, 1000);
INSERT INTO public.user(user_id, first_name, last_name, email, password, steps, points) VALUES (6, 'Gabe', 'Dalessandro', 'gdalessa@usc.edu', 'fitness123', 20000, 1000);
INSERT INTO public.user(user_id, first_name, last_name, email, password, steps, points) VALUES (7, 'Carson', 'Greengrove', 'cgreengrove@usc.edu', 'fitness123', 50000, 1000);
INSERT INTO public.user(user_id, first_name, last_name, email, password, steps, points) VALUES (8, 'Elissa', 'Perdue', 'eperdue@usc.edu', 'fitness123', 23000, 1000);
INSERT INTO public.user(user_id, first_name, last_name, email, password, steps, points) VALUES (9, 'TJ', 'Ram', 'tram@usc.edu', 'fitness123', 32000, 1000);
INSERT INTO public.user(user_id, first_name, last_name, email, password, steps, points) VALUES (10, 'Christian', 'Barrett', 'cbarrett@usc.edu', 'fitness123', 40000, 1000);
INSERT INTO public.user(user_id, first_name, last_name, email, password, steps, points) VALUES (11, 'Amy', 'Cosgrove', 'acosgrove@usc.edu', 'fitness123', 40000, 1500);



-- Creates the bet table
CREATE TABLE bet
(
    bet_id integer NOT NULL,
    bet_owner_user_id integer NOT NULL,
    title character varying(50) NOT NULL,
    description character varying(160) NOT NULL,
    steps_wagered integer NOT NULL,
    date_created date NOT NULL,
    active boolean NOT NULL,
    achieved_goal boolean NOT NULL,
    PRIMARY KEY (bet_id),
    CONSTRAINT bet_owner_user_id FOREIGN KEY (bet_owner_user_id)
        REFERENCES public.user (user_id)
);




-- Inserts a bet created by a user into the bets table

-- Active Bets
INSERT INTO public.bet(bet_id, bet_owner_user_id, title, description, steps_wagered, date_created, active, achieved_goal) VALUES
    (1, 1, 'Bet1', '1500 steps in a week', 1500, CURRENT_DATE, TRUE, FALSE);

INSERT INTO public.bet(bet_id, bet_owner_user_id, title, description, steps_wagered, date_created, active, achieved_goal) VALUES
    (2, 7, 'Getting Active', '2500 steps in a week', 2500, CURRENT_DATE, TRUE, FALSE);

INSERT INTO public.bet(bet_id, bet_owner_user_id, title, description, steps_wagered, date_created, active, achieved_goal) VALUES
    (3, 7, 'Pushing Myself', '50000 steps in a month', 50000, CURRENT_DATE, TRUE, FALSE);

INSERT INTO public.bet(bet_id, bet_owner_user_id, title, description, steps_wagered, date_created, active, achieved_goal) VALUES
    (4, 8, 'Running 2 miles', '4500 steps in a day', 4500, CURRENT_DATE, TRUE, FALSE);




-- Finished Bets
    -- achieved their goal
INSERT INTO public.bet(bet_id, bet_owner_user_id, title, description, steps_wagered, date_created, active, achieved_goal) VALUES
    (5, 1, 'Bet2', '500 steps in a day', 500, CURRENT_DATE, FALSE, TRUE);

INSERT INTO public.bet(bet_id, bet_owner_user_id, title, description, steps_wagered, date_created, active, achieved_goal) VALUES
    (6, 1, 'Bet3', '5000 steps in 2 days', 5000, CURRENT_DATE, FALSE, TRUE);

INSERT INTO public.bet(bet_id, bet_owner_user_id, title, description, steps_wagered, date_created, active, achieved_goal) VALUES
    (7, 11, 'New Habits', '50000 steps in a week', 50000, CURRENT_DATE, FALSE, TRUE);

INSERT INTO public.bet(bet_id, bet_owner_user_id, title, description, steps_wagered, date_created, active, achieved_goal) VALUES
    (8, 11, 'Running a mile', '3500 steps in a day', 3500, CURRENT_DATE, FALSE, TRUE);


    -- did not meet their goal
INSERT INTO public.bet(bet_id, bet_owner_user_id, title, description, steps_wagered, date_created, active, achieved_goal) VALUES
    (9, 11, 'Running a marathon', '35000 steps in a day', 3500, CURRENT_DATE, FALSE, FALSE);

INSERT INTO public.bet(bet_id, bet_owner_user_id, title, description, steps_wagered, date_created, active, achieved_goal) VALUES
    (10, 11, 'Walking in the morning', '3000 steps in a day', 3500, CURRENT_DATE, FALSE, FALSE);

INSERT INTO public.bet(bet_id, bet_owner_user_id, title, description, steps_wagered, date_created, active, achieved_goal) VALUES
    (11, 11, 'Completing a half marathon', '17500 steps in a day', 17500, CURRENT_DATE, FALSE, FALSE);






-- Creates user_bets table
CREATE TABLE public.user_bets
(
    user_bet_id integer NOT NULL,
    user_id integer NOT NULL,
    bet_id integer NOT NULL,
    amount_bet integer NOT NULL,
    betting_against boolean NOT NULL,
    PRIMARY KEY (user_bet_id),
    CONSTRAINT user_id FOREIGN KEY (user_id)
        REFERENCES public."user" (user_id) MATCH SIMPLE,
    CONSTRAINT bet_id FOREIGN KEY (bet_id)
        REFERENCES public.bet (bet_id)
);



-- Inserts a bet that is either for or against the bet created by another user
-- betting against
    -- Explaination: user2 is betting against user1's bet. TRUE says user2 does not think user1 will reach the goal
INSERT INTO public.user_bets(user_bet_id, user_id, bet_id, amount_bet, betting_against) VALUES (1, 2, 1, 100, TRUE);

INSERT INTO public.user_bets(user_bet_id, user_id, bet_id, amount_bet, betting_against) VALUES (2, 4, 1, 100, TRUE);

INSERT INTO public.user_bets(user_bet_id, user_id, bet_id, amount_bet, betting_against) VALUES (3, 3, 4, 200, TRUE);


-- betting for
    -- Explaination: user3 is betting for user1's bet. FALSE says user3 thinks user1 will reach the goal
INSERT INTO public.user_bets(user_bet_id, user_id, bet_id, amount_bet, betting_against) VALUES (4, 3, 1, 100, FALSE);

INSERT INTO public.user_bets(user_bet_id, user_id, bet_id, amount_bet, betting_against) VALUES (5, 3, 3, 100, FALSE);

INSERT INTO public.user_bets(user_bet_id, user_id, bet_id, amount_bet, betting_against) VALUES (6, 2, 9, 100, FALSE);

INSERT INTO public.user_bets(user_bet_id, user_id, bet_id, amount_bet, betting_against) VALUES (7, 2, 10, 200, FALSE);

INSERT INTO public.user_bets(user_bet_id, user_id, bet_id, amount_bet, betting_against) VALUES (8, 2, 11, 300, FALSE);




-- ========== QUERIES ==========
/* List of all the queries needed in the app
1. retrieve all active bets for a user
2. retrieve all users who bet against a specific bet
3. retrieve all users who bet that the goal would be completed
4. List all the bets a user has won (bet correctly)
5. List the bets a user has made where they achieved their goal
6. List the bets a user has made where they did not achieve their goal
7. total amount a user has won
8. total amount a user has lost
*/



-- 1. retrieve all active bets for a user
SELECT public.user.user_id, public.user.first_name, public.bet.title, public.bet.active
FROM public.user
    INNER JOIN public.bet ON public.bet.bet_owner_user_id = public.user.user_id
WHERE public.user.user_id = 1 AND public.bet.active = TRUE;


-- 2. retrieve all users who bet against a specific bet
SELECT public.user_bets.user_bet_id, public.bet.title, public.user_bets.user_id, public.user.first_name, public.user_bets.betting_against
FROM public.user_bets
    INNER JOIN public.bet ON public.bet.bet_id = public.user_bets.bet_id
    INNER JOIN public.user ON public.user_bets.user_id = public.user.user_id
WHERE
    public.user_bets.betting_against = TRUE AND
    public.bet.title = 'Bet1';
    
    
-- 3. retrieve all users who bet the goal would be completed
SELECT public.user_bets.user_bet_id, public.bet.title, public.user_bets.user_id, public.user.first_name, public.user_bets.betting_against
FROM public.user_bets
    INNER JOIN public.bet ON public.bet.bet_id = public.user_bets.bet_id
    INNER JOIN public.user ON public.user_bets.user_id = public.user.user_id
WHERE
    public.user_bets.betting_against = FALSE AND
    public.bet.title = 'Bet1';


-- 4. List all the bets a user has won (bet correctly)
SELECT public.user_bets.user_bet_id, public.user_bets.user_id, public.user.first_name, public.bet.title, public.user_bets.amount_bet, 
    public.user_bets.betting_against, public.bet.achieved_goal
FROM public.user_bets
    INNER JOIN public.bet ON public.bet.bet_id = public.user_bets.bet_id
    INNER JOIN public.user ON public.user_bets.user_id = public.user.user_id
WHERE
    public.bet.active = FALSE AND
    (public.user_bets.betting_against = FALSE AND public.bet.achieved_goal = TRUE) OR
    (public.user_bets.betting_against = TRUE AND public.bet.achieved_goal = FALSE);
    -- AND public.user.user_id = 1;


-- 5. List the bets a user has made where they achieved their goal
SELECT public.user.user_id, public.user.first_name, public.bet.title, public.bet.achieved_goal
FROM public.bet
    INNER JOIN public.user ON public.user.user_id = public.bet.bet_owner_user_id
WHERE
    public.bet.active = FALSE AND
    public.bet.achieved_goal = TRUE;


-- 6. List the bets a user has made where they did not achieve their goal
SELECT public.user.user_id, public.user.first_name, public.bet.title, public.bet.achieved_goal
FROM public.bet
    INNER JOIN public.user ON public.user.user_id = public.bet.bet_owner_user_id
WHERE
    public.bet.active = FALSE AND
    public.bet.achieved_goal = FALSE;


-- 7. total amount a user has won
SELECT public.user_bets.user_bet_id, public.user_bets.user_id, public.user.first_name, public.bet.title, public.user_bets.amount_bet, 
    public.user_bets.betting_against, public.bet.achieved_goal
FROM public.user_bets
    INNER JOIN public.bet ON public.bet.bet_id = public.user_bets.bet_id
    INNER JOIN public.user ON public.user_bets.user_id = public.user.user_id
WHERE
    public.bet.active = FALSE AND
    (public.user_bets.betting_against = FALSE AND public.bet.achieved_goal = TRUE) OR
    (public.user_bets.betting_against = TRUE AND public.bet.achieved_goal = FALSE);
    -- AND public.user.user_id = 1;







