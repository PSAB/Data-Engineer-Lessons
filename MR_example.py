'''
This program runs a MapReduce job on songplays.txt: 
Counting the amount of each unique song

To use, run in terminal: 
python MR_example.py songplays.txt
'''

from mrjob.job import MRJob

class MRSongCount(MRJob):

    # The map step: each line in the txt file is read as a key, value pair
    # Since the text file only contains the song name, it can be 
    # interpreted as having a value but no key. _ will represent the key.

    def mapper(self, _, song):
        # output each line as a tuple of (song_names, 1)
        yield(song, 1)

    # The reduce step: combine all tuples with the same key
    # in this case, the key is the song name, the value is 1. 
    # then sum all the values of the tuple, which will give the 
    # total unique song plays:

    def reducer(self, key, values):
        yield (key, sum(values))
    
if __name__ == "__main__":
    MRSongCount.run()