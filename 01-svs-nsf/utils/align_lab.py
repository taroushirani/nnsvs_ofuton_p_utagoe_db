import os

from glob import glob
from os.path import join, basename, splitext
from nnmnkwii.io import hts
from fastdtw import fastdtw
import sys
import config
from util import prep_ph2num, ph2numeric

# Get rough alignment between
# 1) ofuton_p_utagoe_db's mono-phone labels and
# 2) generated labels by sinsy

ph2num = prep_ph2num()

sinsy_files = sorted(glob(join(config.out_dir, "sinsy_mono_round/*.lab")))
ofuton_p_utagoe_db_files = sorted(glob(join(config.out_dir, "mono_label_round/*.lab")))

dst_dir = join(config.out_dir, "mono_dtw")
os.makedirs(dst_dir, exist_ok=True)

excludes = []
for (path1, path2) in zip(sinsy_files, ofuton_p_utagoe_db_files):
    lab_sinsy = hts.load(path1)
    lab_ofuton_p_utagoe_db = hts.load(path2)
    name = basename(path1)
    if name in excludes:
        print("Skip!", name)
        continue

    # align two labels roughly based on the phoneme labels
    d, path = fastdtw(ph2numeric(lab_sinsy.contexts,ph2num),
        ph2numeric(lab_ofuton_p_utagoe_db.contexts, ph2num), radius=len(lab_ofuton_p_utagoe_db))

    # Edit sinsy labels with hand-annontated aligments
    for x, y in path:
        lab_sinsy.start_times[x] = lab_ofuton_p_utagoe_db.start_times[y]
        lab_sinsy.end_times[x] = lab_ofuton_p_utagoe_db.end_times[y]
    with open(join(dst_dir, name), "w") as of:
        of.write(str(lab_sinsy))
    print(name, d)

sys.exit(0)
