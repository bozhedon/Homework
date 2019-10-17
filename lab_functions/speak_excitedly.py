def speak_excitedly(message, m=1, capitalize=False):
    for i in range(m):
        message += '!'
    if capitalize:
        print(message.upper())
    else:
        print(message)


speak_excitedly("I love Python")  # => "I love Python!"
speak_excitedly("Keyword arguments are great", 4)  # => "Keyword arguments are great!!!!"
speak_excitedly("I guess Java is okay...", 0)  # => "I guess Java is okay..."
speak_excitedly("Let's go stanford", 2, True)  # => "LET'S GO STANFORD!!"
