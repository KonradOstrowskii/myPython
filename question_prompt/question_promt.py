from Questions import Question
question_promts = [
    "Who created the cryptocurrency Bitcoin?\n (a) Satoshi Nakamoto \n (b) Vitalik Buterin \n (c) Anonymous\n ",
    "What is the opposite of 'HOLDING' (slang term)?\n (a)Panic Selling\n (b)Acuumulate after TGE \n (c)Dont selling\n ",
    "After Bitcoin, Ether which are the biggest crypto coins\n (a) Binance_Coin\n (b) Shiba-Inu\n (c) Tether\n",
    "What is maximum circulation of Bitcoin\n (a) Unlimited\n (b) 21mln\n (c) 100mln\n"]


questions = [
    Question(question_promts[0], "a"),
    Question(question_promts[1], "a"),
    Question(question_promts[2], "c"),
    Question(question_promts[3], "b"),


]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got ", str(score), "/", str(len(questions)), "Correct")


run_test(questions)
