class question:
    def __init__(self, promt, answer):
        self.promt = promt
        self.answer = answer

question_promts = [
    "1.What is the name of the weak zone of the earth’s crust?\n(a)Seismic  (b)Cosmic\n(c)Formic  (d)Anaemic\n\n",
    "2.Which latitude runs through the center of the Earth?\n(a)Tropic of Cancer  (b)Equator\n(c)Prime Meridian  (d)Arctic Circle\n\n"
]

questions = [
    question(question_promts[0], "a"),
    question(question_promts[1], "b"),

]

def run_test(questions):
    points = 0
    for qstn in questions:
        answer = input(qstn.promt)
        if answer == qstn.answer:
            points += 1
    print(f"You got {points}/{len(questions)} Correct.")

run_test(questions)
