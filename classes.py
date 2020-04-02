class Term:
    
    def __init__(self, term_itself, comment, links, page=False):
        #self.species = 'term'
        self.term = term_itself
        self.comment = comment
        self.links = links.split(';')
        self.page = int(page) if page else None


class Meme:
    
    def __init__(self, meme_url, explanation, page=False):
        #self.species = 'meme'
        self.meme = meme_url
        self.explanation = explanation
        self.page = int(page) if page else None
    
    #def __str__(self):
    #    return 'meme'

class Problem:
    
    def __init__(self, text, solution_link, page=False):
        #self.species = 'problem'
        self.problem = text
        self.solution_link = solution_link
        self.page = int(page) if page else None


class QRLink:
    
    def __init__(self, link, explanation, page=False):
        #self.species = 'qr link'
        self.qr_link = link
        self.explanation = explanation
        self.page = int(page) if page else None


class Note:
    def __init__(self, a, page=False): 
        #self.species = 'note'
        self.note = a
        self.page = int(page) if page else None


class Study:
    
    def __init__(self, problem, data):
        #self.species = 'study'
        self.problem = problem
        self.data = data.split(';')


class Interview:
    
    def __init__(self, name, questions, time, place):
        #self.species = 'interview'
        self.name = name
        self.questions = questions
        self.time = time
        self.place = place