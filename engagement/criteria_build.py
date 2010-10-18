import sys
import os
    
class CriteriaBuild:
    '''
        Take a 2 dimensional array of criteria with weights
        ('opens' => 20, 'clicks' => 30, 'shares' => 10)
        calculate the total of the weights
        normalize and generate the corresponding values
    '''
    def __init__(self, criteria):
        self.weight_total = 0
        self.data = {}
        self.accuracy = 2
        
        print('Your given criteria are')
        for crit in criteria:
            self.weight_total += criteria[crit]
            print('Name: %s Weight: %s' %(crit, str(criteria[crit])))
           
        print('This gives a total range of 0 to %s' %(self.weight_total))
        print('Normalizing....')
        self._build_normalized_data(criteria)
        
    def generate_score(self, user_data):
        score = 0
        for event_response in user_data:
            score += self.data['clicks'] * event_response[0]
            score += self.data['opens'] * event_response[1]
            score += self.data['shares'] * event_response[2]
        return(score)
        
    def _build_normalized_data(self, criteria):
        for crit in criteria:
            n_value = round(float(criteria[crit])/float(self.weight_total) * 100, self.accuracy)
            #self.data.append({crit : n_value})
            self.data[crit] = n_value