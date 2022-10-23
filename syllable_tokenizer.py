
import sys
import nltk

text = """
She sat there not knowing how much her life would change
He joined her unaware beauty and breath can be so strange 

Echoing practiced word to get the intonation right
In the dark and still he whispered "I have to kiss you tonight"


Frozen and unsure Her face and neck flushed
...Finally that Easter friend was a man rushed 
Touched, rushed, crushed, hushed 

Against red leather it all felt so right
In his driveway - I have to kiss you tonight


Only the crazy would start this during school 
But No one had told him that fool's rule

The middle of exams, grad schools height
Oh well, we're here, i have to kiss you tonight 


He and and others had known for so long
And he hopes you feel it with every song 

He'd held it back with a professional might
But damn the job - i have to kiss you tonight 


Around the world his heart she carrie-d
Far from settled down but happily married 

Fast forward through the bumps and fights
As we lay down together - i have to kiss you tonight
"""

text = [r.strip() for r in text.split('\n') if len(r.strip()) > 0]

tokenizer = nltk.SyllableTokenizer()

for line in text: #open(sys[1], 'r'):
    tokens = tokenizer.tokenize(line)
    print(line)
    print(tokens)