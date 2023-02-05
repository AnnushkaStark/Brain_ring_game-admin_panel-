

class Question(object):
    text = str()
    asnwer = str()
    level = int()

    def set_new(self, text, answer, level):
        self.text = text
        self.answer = answer
        self.level = level

    def get_level(self):
        return self.level
    def get_text(self):
        return self.text
    def get_answer(self):
        return self.answer

questions = []
fisrt_question = Question()
fisrt_question.set_new("Согласно одной несерьезной новости, на открытии "
                        "нового корпуса роддома президент... Что сделал? "
                        "Ответьте двумя словами, начинающимися с одной и той "
                        "же буквы.", 'Перерезал пуповину', 1)
second_question = Question()
second_question.set_new('В одном из интервью этот уроженец Мурома возмущался: \"Зачем они показывают такое по всем программам?\", \"... Ужасы, драки и убийства!\", \"Я бы не позволил своим детям и близко подходить к этому аппарату!\". Назовите его фамилию.', 'Зворыкин', 2)

questions.append(fisrt_question)
questions.append(second_question)




