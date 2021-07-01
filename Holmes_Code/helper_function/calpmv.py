####################### Ref PMV ##################################
# https://github.com/CenterForTheBuiltEnvironment/pythermalcomfort/tree/master/examples

from pythermalcomfort.models import pmv_ppd
from pythermalcomfort.psychrometrics import v_relative
from pythermalcomfort.utilities import met_typical_tasks
from pythermalcomfort.utilities import clo_individual_garments, clo_typical_ensembles

def calpmv(tdb, rh):
    # input variables
    # tdb = dry-bulb air temperature, [$^{\circ}$C]
    # tr =  mean radiant temperature, [$^{\circ}$C]
    # v = average air speed, [m/s]

    tr = tdb
    v = 0.1

    activity = "Writing"
    met = met_typical_tasks[activity]
    # garments = ["Sweatpants", "T-shirt", "Shoes or sandals"]
    # icl = sum([clo_individual_garments[item] for item in garments])

    icl = clo_typical_ensembles["Trousers, long-sleeve shirt"]
    # calculate the relative air velocity
    vr = v_relative(v=v, met=met)

    # calculate PMV in accordance with the ASHRAE 55 2017
    results = pmv_ppd(tdb=tdb, tr=tr, vr=vr, rh=rh, met=met, clo=icl, standard="ASHRAE")

    return results['pmv']