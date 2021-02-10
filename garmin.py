def get_activities():
    from garminconnect import (
    Garmin,
    GarminConnectConnectionError,
    GarminConnectTooManyRequestsError,
    GarminConnectAuthenticationError,
    )       
    import datetime
    from datetime import date
    import numpy as np
    from matplotlib import pyplot as plt
    import pandas as pd

    client = Garmin("YOURUSERNAME", "YOURPASS")
    client.login()
    act=list(client.get_activities(0,100))
    distance=[]
    duration=[]
    elevation=[]
    avghr=[]
    vo2=[]
    date=[]
    for i in range(len(act)):
        distance.append(act[i]["distance"])
        duration.append(act[i]["duration"])
        elevation.append(act[i]["elevationGain"])
        avghr.append(act[i]["averageHR"])
        vo2.append(act[i]["vO2MaxValue"])
        date.append(act[i]["startTimeLocal"])
    
    # modifica distance
    for i in range(len(distance)):
        distance[i]=distance[i]/1000
    # modifica duration
    for i in range(len(duration)):
        duration[i]=duration[i]/60
    
    # Inverto le liste per ordine cronologico
    distance.reverse()
    duration .reverse()
    elevation.reverse()
    avghr.reverse()
    date.reverse()

    # Creazione df

    dict_act ={"distance":distance,"duration":duration,"elevation":elevation,
            "avghr":avghr,"vo2":vo2,"date":date}
    df_act=pd.DataFrame(dict_act)
    df_act["date"]=df_act["date"].apply(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S') )
    df_act["date"]= df_act["date"].apply(lambda x: x.date())
    return df_act
