class TRIAL:
    def __init__(self,subject,value):
        self.subject=subject
        self.value=value
    
    def get_subject(self):
        return self.subject
    
    def set_subject(self,subject):
        self.subject=subject
    
    def get_value(self):
        return self.subject
    
    def set_value(self,value):
        self.value=value
        
    def __str__(self):
        return f"({self.subject},{self.value})"
    
    def __le__(self,xyz):
        if self.name<=xyz.name:
            return True
        else:
            return False
        
    def __gt__(self,xyz):
        if self.name>xyz.name:
            return True
        else:
            return False
        
        
def main():
    student1=TRIAL("MATH",24)
    student1.set_subject("PHYSICS")
    student1.set_value("30")

    print(student1)

main()
    


QUESTION 1:

class Post:
    def __init__ (self,u,c,t):
        self.username=u
        self.content=c
        self.timestamp=t

class User:
    def __init__(self,u):
        self.username=u
        self.post=[]

    def add_post(self,post):
        self.posts.append(post)
    
    def display_post_history(self):
        print(f"{self.username} post history:")
        for posts in self.post:
            print(f"{self.name} - Content: {posts} -- {self.timestampp}")

def main():
    user1=User("Alice")
    user2=User("Bob")


main()
