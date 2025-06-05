# QUESTION 1: SOCIAL MEDIA POST ANALYZER

# In the dynamic world of social media, users often want to analyze the impact of their posts. Your
# task is to create a Python program that helps users track and analyze their social media posts.
# Implement a solution that includes the following classes:

# 1. Post class: This class should represent an individual social media post and should be
# initialized with the following attributes:
# ● username (string): The username of the person making the post.
# ● content (string): The content of the post.
# ● timestamp (string): The timestamp when the post was made.

# 2. User class: This class should represent a social media user and should be initialized with
# the following attributes:
# ● username (string): The username of the user.
# ● posts (list): A list to store instances of the `Post` class.
# The User class should provide the following methods:
# ● add_post(post): Adds a new post to the user's list of posts.
# ● display_post_history(): Iterates through the list of posts and displays information
# about each post in a readable format. Print details such as the username, content, and
# timestamp of each post.

# 3. Analyzer class: This class should be responsible for analyzing the impact of social media
# posts. It should be initialized with a list of User instances. The Analyzer class should provide
# the following methods:
# ● calculate_user_engagement(username): Takes a username as input and calculates
# the total engagement (e.g., the number posts)

class Post:
    def __init__(self,username,content,timestamp):
        self.username=username
        self.content=content
        self.timestamp=timestamp

    
class User:
    def __init__ (self,username):
        self.username=username
        self.posts=[]

    def add_post(self,post):
        self.posts.append(post)

    def display_post_history(self):
        display=""
        for post in self.posts:
            display+=f'{post.username}\t'
            display+=f'{post.content}\t'
            display+=f'{post.timestamp}\t'
            display+='\n'
        
class Analyzer:
    def __init__ (self,users):
        self.users=users
    def calculate_user_engagement(self,username):
        for user in self.users:
            if user.username==username:
                return f"User Engagement for {username}: {len(user.posts)}"


def main():
# Create instances of User representing different social media users
    user1 = User("Alice")
    user2 = User("Bob")
# Create instances of Post representing different social media posts
    post1 = Post("Alice", "Feeling excited about the weekend!", "2023-01-01 10:00:00")
    post2 = Post("Bob", "Just finished reading a great book.", "2023-01-02 15:30:00")
    post3 = Post("Alice", "Cooked a delicious meal today.", "2023-01-03 18:45:00")
# Create an instance of Analyzer
    social_media_analyzer = Analyzer([user1, user2])
# Add posts to users
    user1.add_post(post1)
    user2.add_post(post2)
    user1.add_post(post3)
# Display post history for each user
    user1.display_post_history()
    user2.display_post_history()
# Calculate and print user engagement for a specific user
    print("\nUser Engagement for Alice:", social_media_analyzer.calculate_user_engagement("Alice"))

main()


# QUESTION 2: SESAME STREET

# In the colorful world of Sesame Street, each character brings unique qualities and personalities.
# Your task is to create a Python program that helps fans analyze and understand their favorite
# Sesame Street characters. Implement a solution that includes the following classes:


# 1. Character class:
# This class should represent an individual Sesame Street character and should be
# initialized with the following attributes:
# ● name (string): The name of the character.
# ● species (string): The species of the character (e.g., monster, bird, grouch).
# ● color (string): The color associated with the character (e.g., red, yellow,
# green).
# ● description (string): A brief description of the character's personality or
# traits.

# 2. Episode class:
# This class should represent a Sesame Street episode and should be initialized with the
# following attributes:
# ● title (string): The title of the episode.
# ● air_date (string): The air date of the episode.
# ● characters (list): A list to store instances of the Character class representing
# characters featured in the episode.

# The Episode class should provide the following methods:
# ● add_character(character): Adds a new character to the list of characters
# featured in the episode.

# ● display_characters(): Iterates through the list of characters and displays
# information about each character in a readable format, including the name, species,
# color, and description.

# 3. Analyzer class:
# This class should be responsible for analyzing Sesame Street episodes and characters.
# It should be initialized with a list of Episode instances.
# The Analyzer class should provide the following methods:

# ● find_episodes_with_character(character_name): Takes a character's name
# as input and returns a list of episode titles featuring that character.
# ● find_characters_in_episode(episode_title): Takes an episode title as input
# and returns a list of characters featured in that episode.


class Character:
    def __init__(self,name,species,color,description):
        self.name=name
        self.species=species
        self.color=color
        self.description=description

    def get_name(self):
        return self.name
    
    def get_species(self):
        return self.species
    
    def get_color(self):
        return self.color
    
    def get_description(self):
        return self.description

    def __str__(self):
        return f"{self.name} ({self.species}, {self.color}): {self.description}"
    
class Episode:
    def __init__(self,title,airdate):
        self.title=title
        self.airdate=airdate
        self.characters=[]

    def get_characters(self):
        return self.characters
    
    def get_title(self):
        return self.title

    def add_character(self,character):
        self.characters.append(character)

    def display_characters(self):
        display=""
        for character in self.characters:
            display+=f'{character.get_name()}:{character.get_species()}:{character.get_color()}:{character.get_description()}'
        return display
    
    
class Analyzer:
    def __init__(self,episodes):
        self.episodes=episodes

    def find_episodes_with_character(self,character_name):
        episodelist=[]
        for episode in self.episodes:
            for character in episode.get_characters():
                if character.get_name() == character_name:
                    episodelist.append(episode.title)
        return episodelist


    def find_characters_in_episode(self,episode_title): 
        characterlist=[]
        for episode in self.episodes:
            if episode_title==episode.get_title():
                for character in episode.get_characters():
                    characterlist.append(character.name)
        return characterlist
        
            
def main():
# Create Character instances
    big_bird = Character("Big Bird", "Bird", "Yellow", "Friendly and curious.")
    oscar = Character("Oscar the Grouch", "Grouch", "Green", "Grumpy and loves trash.")
# Create Episode instances and add characters
    episode1 = Episode("Welcome to Sesame Street", "2024-04-01")
    episode1.add_character(big_bird)
    episode1.add_character(oscar)
# Display characters in the episode
    episode1.display_characters()
# Create Analyzer instance
    analyzer = Analyzer([episode1])
# Find episodes featuring a character
    big_bird_episodes = analyzer.find_episodes_with_character("Big Bird")
    print("Episodes featuring Big Bird:", big_bird_episodes)
# Find characters in an episode
    episode_characters = analyzer.find_characters_in_episode("Welcome to Sesame Street")
    print("Characters in 'Welcome to Sesame Street':", episode_characters)
main()

            

#HOMEWORK 10 QUESTIONS 

        

# Problem 01: Tools Of The Trade

# The whole point of this assignment is to simulate two musicians having a battle (think Scott Pilgrim
# vs The World's bass battle). To do this, we're going to create two classes, an Instrument class
# (i.e. their instrument of choice) and the Musician class (i.e. the musician using the instrument).
# Let's start with Instrument class, since this one is simpler.'


# 1.1: Creating Instrument Objects:
# Start with the initializer method, which will accept three parameters from the user:
# Table 1: Attributes of the Instrument class. Make sure the spelling of your attributes matches those given
# here. You can assume that the user will always enter a valid value for strength.
# If you implement your initializer method correctly, your Instrument objects should behave as follows:
# def main():
# fender_vi = Instrument("VI Bass", "Fender", 0.99)
# print(fender_vi.model)
# print(fender_vi.brand)
# print(fender_vi.strength)
# main()
# Output:
# VI Bass
# Fender
# 0.99


# 1.2: Printing Instrument Objects:
# Here, your goal is to simply make sure that the following behavior occurs when printing objects of the
# Instrument class:
# fender_vi = Instrument("VI Bass", "Fender", 0.99)
# four_double_o_one = Instrument("4001C64 Bass", "Rickenbacker", 0.856)
# print(fender_vi)
# print(four_double_o_one)
# Output:
# Fender VI Bass (99.0 / 100 strength)
# Rickenbacker 4001C64 Bass (85.6 / 100 strength)




# 1.3: The does_break() Method:
# This method will do the following:
# ● If a randomly-generated float value from 0.0 to 1.0 (inclusive) is smaller than 1/2 of the
# strength attribute of this Instrument object, does_break() will return True, meaning the
# instrument has broken.
# ● Otherwise, return False, meaning the instrument has stood the test of time and not broken.
# That is, the stronger an Instrument object is, the more likely it is to break.
# Consider the following possible sample behavior:
# def main():
# danelectro = Instrument("Stock '59", "Danelectro", 0.25)
# number_of_tests = 100
# number_of_breaks = 0
# # I'm testing does_break() 100 times and keeping track of how many times it breaks
# for i in range(number_of_tests):
# if danelectro.does_break():
# number_of_breaks += 1
# percentage = (number_of_breaks / number_of_tests) * 100
# print(f"The {danelectro.model} broke {round(percentage)}% of the time in {number_of_tests} tests!")
# main()
# Possible output:
# The Stock '59 broke 16% of the time in 100 tests!
# Please make sure you understand and have gotten it to work perfectly before moving on to the next
# part, as we'll be making use of Instrument objects.
import random
class Instrument:
    def __init__(self,model,brand,strength):
        self.model=model
        self.brand=brand
        self.strength=strength
    
    def getmodel(self):
        return self.model
    
    def getbrand(self):
        return self.brand
    
    def getstrength(self):
        return self.strength
    
    def doesbreak(self):
        breakcount=0
        for i in range(0,100):
            breakstate=False
            randomtension=random.uniform(0,1)
            if randomtension < 0.5*float(self.getstrength()):
                breakstate=True
            if breakstate==True:
                breakcount+=1
        if breakcount>50:
            return True
        else:
            return False
 
    def __str__(self):
        return f'{self.brand} {self.model} ({self.strength} / 100 strength)'
    

class Musician:
    def __init__(self,stage_name,instruments):
        self.stage_name=stage_name
        self.instruments=instruments
        self.number_of_instruments=len(self.instruments)

    def getstagename(self):
        return self.stage_name
    
    def getinstrulength(self):
        return self.number_of_instruments
    
    def getinstrumentlist(self):
        return self.instruments

    def __str__ (self):
        formattedinstru=""
        for instrument in self.instruments:
            formattedinstru+=instrument.__str__()
            formattedinstru+="\n"

        return f'{self.stage_name}\n{self.number_of_instruments}\n{formattedinstru}'

    def pick_instrument(self,instrumentindex="None"):
        try:
            if instrumentindex=="None":
                return "None"
            else:
                return self.instruments[instrumentindex].__str__()
        
        except IndexError: 
            return self.instruments[-1].__str__()
        
def get_name_of_battle_winners(musician1,musician2):
    randomhalf=random.randint(1,2)
    if musician1.getinstrulength()==0 and musician2.getinstrulength==0:
        return "No contest"
    elif musician1.getinstrulength()==0:
        return musician2 + "is the winner"
    elif musician2.getinstrulength()==0:
        return musician1 + "is the winner"

    instru1index=random.randint(0,musician1.getinstrulength()-1)
    instru2index=random.randint(0,musician2.getinstrulength()-1)

    instru1=musician1.getinstrumentlist()[instru1index]
    instru2=musician2.getinstrumentlist()[instru2index]
    
    print(f'{musician1.getstagename()} chose {instru1}')
    print(f'{musician2.getstagename()} chose {instru2}')

    if instru1.getstrength()>instru2.getstrength():
        if instru1.doesbreak()==True:
            return "Winner is " + musician2.getstagename()
        else:
            return "Winner is " + musician1.getstagename()
    elif instru2.getstrength()>instru1.getstrength():
        if instru2.doesbreak()==True:
            return "Winner is " + musician1.getstagename()
        else:
            return "Winner is " + musician2.getstagename()
    else: 
        if randomhalf==1:
            return "Winner is " + musician1.getstagename()
        else:
            return "Winner is " + musician2.getstagename()

def main():
    newinstru1=Instrument("Grand Piano","Mozart",0.1)
    newinstru2=Instrument("Guitar","Philips",0.5)
    newinstru3=Instrument("Electric Piano","Belly",0.8)
    newinstru4=Instrument("Drum Set","Koby",0.99)
    musician1instru=[newinstru1,newinstru2,newinstru3,newinstru4]
    musician1=Musician("Eddie",musician1instru)
    musician2=Musician("Bobby",musician1instru)
    print(musician1)
    print(newinstru1.doesbreak())
    musician1.pick_instrument(1)
    print(get_name_of_battle_winners(musician1,musician2))
    
main()





