"""

"""
import numpy as np
import pytest
import plotcounts
from collections import Counter
import countwords
import collate

#---------------------------------------------------------
def test_alpha():
    """
    Test the calculation of the alpha parameter.

    The test word counts satisfy the relationship,
      r = cf**(-1/alpha), where
      r : rank,
      f : word count, and
      c : constant of proportionality.

    To generate test word counts for an expected 
    alpha of 1.0, a maximum word frequency of 600
    is used(i.e. c=600 and r ranges from 1 to 600)
    """
    max_freq = 600
    counts = np.floor(max_freq / np.arange(1, max_freq + 1))
    actual_alpha = plotcounts.get_power_law_params(counts)
    expected_alpha = pytest.approx(1.0, abs=0.01)
    assert actual_alpha == expected_alpha

#----------------------------------------------------------
def test_word_count():
    """
    Test the counting of words.

    The example poem is Night, by William Blake.
    """

    night_poem_counts = {'the': 6, 'in': 3, 'silent': 2, 'and': 2, 'sun': 1, 
          'descending': 1,  'west': 1, 'evening': 1, 'star': 1, 'does': 1, 
          'shine': 1, 'birds': 1, 'are': 1, 'their': 1, 'nest': 1, 
          'i': 1, 'must': 1, 'seek': 1, 'for': 1, 'mine': 1, 
          'moon': 1, 'like': 1, 'a': 1, 'flower': 1, 'heaven\'s': 1,  
          'high': 1, 'bower': 1, 'with': 1, 'delight': 1, 'sits': 1, 
          'smiles': 1, 'on': 1, 'night': 1}
    expected_result = Counter(night_poem_counts)
    with open('test_data/Night.txt', 'r') as reader:
        actual_result = countwords.count_words(reader)
    assert actual_result == expected_result

#----------------------------------------------------------
def test_integration():
    """
    Test the full word count to alpha parameter workflow.
    """

    with open('test_data/random_words.txt', 'r') as reader:
        word_counts_dict = countwords.count_words(reader)
    counts_array = np.array(list(word_counts_dict.values()))
    actual_alpha = plotcounts.get_power_law_params(counts_array)
    expected_alpha = pytest.approx(1.0, abs=0.01)
    assert actual_alpha == expected_alpha

#-----------------------------------------------------------
def test_regression():
    """
    Regression test for Dracula.
    """

    with open('data/dracula.txt', 'r') as reader:
        word_counts_dict = countwords.count_words(reader)
    counts_array = np.array(list(word_counts_dict.values()))
    actual_alpha = plotcounts.get_power_law_params(counts_array)
    expected_alpha = pytest.approx(1.087, abs=0.001)
    assert actual_alpha == expected_alpha

#-----------------------------------------------------------
def test_not_csv_erros():
    """
    csv-error handling test. 
    """ 
    #fixtures
    fname = 'data/dracula.txt'
    word_counts = Counter()
    #test
    with pytest.raises(OSError):
        collate.process_file(fname, word_counts)

#-----------------------------------------------------------
def test_file_not_found_error():
    """
    Error handling test when file does not exist.
    """
    #fixtures
    fname = 'no_file.csv'
    word_counts = Counter()
    #test
    with pytest.raises(FileNotFoundError):
        collate.process_file(fname, word_counts)
