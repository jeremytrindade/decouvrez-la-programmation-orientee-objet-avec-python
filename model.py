class Agent:
    
    def say_hello(self, first_name):
        return "Bien le bonjour " + first_name + " !"


agent = Agent()
print(agent.say_hello("Celine"))