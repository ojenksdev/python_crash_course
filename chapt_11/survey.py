class AnonymousSurvey():
    """Collect anonymous answers to survey questions"""

    def __init__(self, question):
        """Store a question, and prepare to store responses"""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_results(self):
        """Show all the results that have been given."""
        print("Survey Results:")
        for response in self.responses:
            print(" -" + response)
            
    
