# Movie Title + year, critic score, audience score 
movieList = [
    ("The Shawshank Redemption (1994)", 91, 98), ("The Godfather (1972)", 97, 98), ("The Dark Knight", 94, 94),
    ("Forrest Gump (1994)", 71, 95), ("Pulp Fiction (1994)", 92, 96), ("Fight Club (1999)", 79, 96),
    ("The Matrix (1999)", 83, 85), ("Seven (1995)", 83, 95), ("The Silence of the Lambs", 95, 95),
    ("Spider-Man: Into the Spider-Verse (2018)", 97, 94), ("The Shining", 83, 93), ("Full Metal Jacket (1987)", 90, 94),
    ("Batman & Robin (1997)", 11, 16), ("Venom (2018)", 30, 80), ("Transformers (2007)", 57, 85), 
    ("Scooby-Doo (2002)", 32, 40), ("Killer Klowns from Outer Space (1988)", 77, 60), ("Teenage Mutant Ninja Turtles (1990)", 42, 81),
    ("Step Brothers (2008)", 55, 69), ("Rise of the Planet of the Apes (2011)", 82, 77), ("Night of the Living Dead", 95, 87), 
    ("The Suicide Squad (2021)", 90, 82), ("Saw (2004)", 50, 84), ("Marvel's the Avengers (2012)", 91, 91), 
    ("Despicable Me (2010)", 80, 83), ("Spider-Man (2002)", 90, 67), ("Spider-Man 2 (2004)", 93, 82),
    ("Gremlins (1984)", 86, 78), ("Jaws (1975)", 97, 90), ("Hellraiser (1987)", 70, 73),
    ("The Hunger Games (2012)", 84, 81), ("Monty Python and the Holy Grail (1975)", 96, 95), ("Akira (1988)", 91, 90),
    ("The Truman Show (1998)", 94, 89), ("Get Out (2017)", 98, 86), ("No Country for Old Men (2007)", 93, 86), 
    ("The Thing (1983)", 85, 92), ("Do the Right Thing (1989)", 92, 89), ("Prisoners (2013)", 81, 87), 
    ("Kill Bill (2003)", 85, 81), ("Superbad (2007)", 88, 87), ("Friday (1995)", 76, 91), 
    ("Avatar (2009)", 82, 82), ("Transformers: Revenge of the Fallen (2009)", 20, 57), ("Jurassic Park (1993)", 91, 91),
    ("Jurassic World (2015)", 71, 78), ("Aquaman (2018)", 66, 72), ("Suicide Squad (2016)", 26, 58),
    ("Captain Marvel (2019)", 79, 45), ("Joker (2019)", 69, 88), ("The Super Mario Bros. Movie (2023)", 59, 95),
    ("Justice League (2017)", 39, 67), ("Zack Synder's Justice League (2021)", 72, 93), ("Jurassice World Dominion (2022)", 29, 77),
    ("Thor: Love and Thunder (2022)", 63, 76), ("Old (2021)", 50, 53), ("Watchmen (2009)", 65, 71),
    ("Star Wars: Episode I - the Phantom Menace (1999)", 52, 59), ("Star Wars: Episode IV Return of the Jedi (1983)", 83, 94), ("Bird Box (2018)", 64, 58)
]   

def length():
    return len(movieList)

def addMovie():
    title = input("Enter Movie Title (ex: 'Movie Title (Year released)'): ")
    critic = input("Enter Critic Score (enter percentage as a number ex: 23, 65, 92): ")
    audience = input("Enter Critic Score (enter percentage as a number ex: 23, 65, 92): ")
    movie = [title, critic, audience]
    movieList + movie
    return movieList