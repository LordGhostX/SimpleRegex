import re

# SimpleRegex class
# contains all module functions
class SimpleRegex():
    def __init__(self, text=None):
        self.text = text

    def email(self, text=None, mode="e"):
        # if no text is given use the one used to initialize the class
        if text == None:
            text = self.text

        # email regex
        regex = r'[\w\.-]+@[\w\.-]+'

        # SimpleRegex return modes
        # valid modes are 'e' and 'v'
        if mode == "e":
            # extraction mode
            # returns every occurence of search
            all_mails = re.findall(regex, text)
            return all_mails
        if mode == "v":
            # validation mode
            # checks if a given text matches the search
            is_email = re.match(regex, text)
            return is_email
