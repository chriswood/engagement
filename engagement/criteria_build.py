import sys
import os
    
class CriteriaBuild:
    '''
        Takes a 2 dimensional array of criteria with weights
        ('opens' => 20, 'clicks' => 30, 'shares' => 10)
        calculate the total of the weights,
        normalize and generate the corresponding values
    '''
    def __init__(self, criteria):
        self.weight_total = 0
        self.data = {}
        self.scores = {}
        self.accuracy = 2
        
        print('Your given criteria are')
        for crit in criteria:
            self.weight_total += criteria[crit]
            print('Name: %s Weight: %s' %(crit, str(criteria[crit])))
           
        print('This gives a total range of 0 to %s' %(self.weight_total))
        print('Normalizing....')
        self._build_normalized_data(criteria)
        
    def generate_score(self, crit_list, user_data):
        """
            Returns a dictionary of users and their corresponding scores
            for the given data set.
        """
        for user in user_data:
            score = 0
            for resp_tuple in user_data[user]:
                for order, crit in enumerate(crit_list):
                    score += self.data[crit] * resp_tuple[order]
            #We have the total for each event. We could weight each event as well,
            #for now they are all even.
            score = round(score/float(len(resp_list)), self.accuracy)
                
            self.scores[user] = score
        
    def _build_normalized_data(self, criteria):
        for crit in criteria:
            try:
                n_value = round(float(criteria[crit])/float(self.weight_total) * 100, self.accuracy)
            except ZeroDivisionError, e: #only chuck norris
                n_value = 0
            self.data[crit] = n_value