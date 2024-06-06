import pyvoting
import pandas as pd

def test_plurality_voting():
    # initialize an election with 3 candidates
    election = pyvoting.PluralityVoting(["cand1", "cand2", "cand3"])
    # manually add some ballots
    election.AddBallot(pd.Series({"cand1":1,
                               "cand2":0,
                               "cand3":0}))
    election.AddBallot(pd.Series({"cand1":1,
                               "cand2":0,
                               "cand3":0}))
    election.AddBallot(pd.Series({"cand1":0,
                               "cand2":1,
                               "cand3":0}))
    # run the election and get the result
    result = election.RunElection()
    assert result[0][0] == "cand1"
