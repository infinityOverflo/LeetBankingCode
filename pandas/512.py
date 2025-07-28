import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity_indexed = activity.groupby(["player_id"])

    return pd.DataFrame(activity_indexed["event_date"].min()).reset_index().rename(columns={"event_date":"first_login"})