import json


class SystemPrompt:
    def __init__(self):
        self.faq = {}
        self._load_faq()

    def _load_faq(self):
        try:
            with open('faq.json', 'r') as json_file:
                self.faq = json.load(json_file)
        except FileNotFoundError:
            print("No existing FAQ Json found")

    def _save_faq(self):
        with open('faq.json', 'w') as json_file:
            json.dump(self.faq, json_file)

    def get_faq(self):
        formatted_faq = "\n".join([f"Q: {q}\nA: {a}" for q, a in self.faq.items()])
        return formatted_faq

    def add_faq(self, question, answer):
        self.faq[question] = answer
        self._save_faq()

    def remove_faq(self, question):
        if question in self.faq:
            del self.faq[question]
            self._save_faq()
            return True
        return False


if __name__ == '__main__':
    system_prompt = SystemPrompt()
    print(system_prompt.get_faq())
    system_prompt.add_faq("What is your name?", "My name is System Prompt")
    print(system_prompt.get_faq())
    system_prompt.add_faq("What is my name?", "My name is System Prompt")
    print(system_prompt.get_faq())
