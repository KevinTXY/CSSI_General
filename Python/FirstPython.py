from random import randint
tasks = ['my homework', 'the job', 'my code', 'the race', 'my grocery shopping', 'the marathon']
excuses = ["I fell and couldn't get up.", 'had to help rescue Matt Damon from outer space.', '''was kidnapped and
questioned by the NSA.''', 'accidentally took the magic school bus instead of the pace.', 'got caught in deadly acid rain.', '''
was attacked by a band of savages.''', "was abducted by a strange man in a blue policebox.", "took an arrow to the knee."]
def rint(list):
    return randint(0,len(list) - 1)
print ("I did not complete %s because I %s") % (tasks[rint(tasks)], excuses[rint(excuses)])
# name = raw_input('Enter Your Name: ')
# print ("Hello %s") % (name)
# adj1 = raw_input('Enter an Adjective: ')
# vb1 = raw_input('Enter a Verb: ')
# noun1 = raw_input('Enter a Noun: ')
# print ('The %s, brown fox %s the lazy %s.') % (adj1, vb1, noun1)
