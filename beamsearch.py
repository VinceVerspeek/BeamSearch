import queue
import pandas as pd

data_file = 'Web_Analytics_Nov_2018_final.csv'
data_delimiter = ';'

data = pd.read_csv(data_file, delimiter = data_delimiter)

result_set_size = int
beam_depth = int
beam_width = 3 #amount of most likely possible follow-ups
bins = int

def main(data, result_set_size, beam_depth, beam_width):
    beam_search(data, result_set_size, beam_depth, beam_width)

def beam_search(dt, q, d, w):
    candidate_queue = queue.Queue()
    candidate_queue.put([])
    result_set = queue.PriorityQueue(q)

    for level in range(0, d):
        beam = queue.PriorityQueue(w)
        while not candidate_queue.empty:
            seed = candidate_queue.get()
            set = generate_desc(seed)
            for desc in set :
                quality = quality_measure(desc)
                if check_conditions(desc) :
                    result_set.put((desc, quality)) #niet zeker of dit met priority is
                    beam.put((desc, quality))
        while not beam.empty():
            candidate_queue.put(beam.get())
    return result_set


def generate_desc(seed):



def quality_measure():

def check_conditions(desc):