
class Ranking():
    """ Class that handles the scoring and ordering of a ParseResult list """

    def rank_and_sort(self, parseResult_list, search_term):
        """
        Params(ParseResult[list], search_term[string])
            loops through the list scoring each item based on the URL (PDF or HTML file)
            and adds a "score" attribute to the ParseResult object and then returns a
            sorted list based on the score
        """
        for link in parseResult_list:
            self.rank(link, search_term)

        parseResult_list.sort(key=lambda x: x.score, reverse=True)
        return parseResult_list

    def rank(self, pr, search_term):
        """ Routes the ranking depending on what type of URL it is """
        url = pr.url.lower()
        if (url.endswith('.htm') or url.endswith('.html')):
            self.rank_html(pr, search_term)
        elif (url.endswith('.pdf')):
            self.rank_pdf(pr, search_term)
        else:
            print("No ranking available for document type:", pr.url)

    def rank_html(self, pr, search_term):
        score = 0
        if (pr.title != None and pr.title.find(search_term) > -1):
            score += 5
        if (pr.keywords != None and pr.keywords.find(search_term) > -1):
            score += 4
        if (pr.description != None and pr.description.find(search_term) > -1):
            score += 3
        if (pr.h1 != None and pr.h1.find(search_term) > -1):
            score += 3
        if (pr.h2 != None and pr.h2.find(search_term) > -1):
            score += 2
        if (pr.h3 != None and pr.h3.find(search_term) > -1):
            score += 1
        score += pr.content.count(search_term)
        pr.score = score
        # TODO should we add a value for words that are in the url itself ???

    def rank_pdf(self, pr, search_term):
        score = 0
        if (pr.title != None and pr.title.find(search_term) > -1):
            score += 5
        score += pr.content.count(search_term)
        pr.score = score
        # TODO should we add a value for words that are in the url itself ???