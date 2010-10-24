import sys
import os
from engagement.graphing.utilities import EE_convert
    
class CriteriaBuild:
    '''
        Takes a 2 dimensional array of criteria with weights
        ('opens' => 20, 'clicks' => 30, 'shares' => 10)
        calculate the total of the weights,
        normalize and generate the corresponding values
    '''
    def __init__(self, criteria, scale):
        self.weight_total = 0
        self.data = {}
        self.scores = {}
        self.ind_event_results = {}
        self.accuracy = 1
        self.encoded_str = ''
        self.scale = scale
        
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
            for the given data set. This would be used to pick the top people from
            a query, or to rank people for whatever reason, rather than the chart
            which requires individual event values.
        """
        for user in user_data:
            score = 0
            for resp_tuple in user_data[user]:
                for order, crit in enumerate(crit_list):
                    score += self.data[crit] * resp_tuple[order]
            #We have the total for each event. We could weight each event as well,
            #for now they are all even.
            score = round(score/float(len(user_data[user])), self.accuracy)
                
            self.scores[user] = score
            
    def build_chart_values(self, user_list, crit_list, user_data):
        """
            Similar to gerneate score, but this needs to just build
            event response for each user, in a chart ready format.
        """

        #First build the labeled dictionary for use with chart labels,
        #mouseovers, etc...
        for user in user_data:
            event_dict = {}
            for resp_tuple in user_data[user]:
                for order, crit in enumerate(crit_list):
                    if crit not in event_dict.keys():
                        event_dict[crit] = 0
                    event_dict[crit] += round((self.data[crit] * resp_tuple[order])/float(len(user_data[user])), self.accuracy)
            
            self.ind_event_results[user] = event_dict

        #Then the encoded string to display the bars...
        #user1_crit1 + user2_crit1 + user3_crit1...
        for crit in crit_list:
            for user in user_list:
                self.encoded_str += EE_convert(self.ind_event_results[user][crit] * self.scale)
            self.encoded_str += ','
        print(self.ind_event_results)
        #Then the string of users
        self.users = '|'.join(user_list)
        #events...
        self.crit = '|'.join(crit_list)

    def _build_normalized_data(self, criteria):
        for crit in criteria:
            try:
                n_value = round(float(criteria[crit])/float(self.weight_total) * 100, self.accuracy)
            except ZeroDivisionError, e: #only chuck norris
                n_value = 0
            self.data[crit] = n_value