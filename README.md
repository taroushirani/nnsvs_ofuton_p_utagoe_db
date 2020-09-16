# nnsvs_ofuton_p_utagoe_db

[NNSVS](https://github.com/r9y9/nnsvs) recipe of OFUTON_P singing voice database (49 songs, 46 original songs + 3 key-changed songs). 
Almost all codes are derived from [kiritan_singing](https://github.com/r9y9/kiritan_singing).

## Requirements
- nnsvs
- pysinsy
- nnmnkwii
- librosa
- soundfile
- scipy
- numpy
- tqdm
- jaconv

## How to use
Due to the licensing issue, this recipe does not include data nor helper scripts for downloading automatically. First of all, you need to get OFUTON_P_UTAGOE_DB.zip from [おふとんP歌声DB配布所](https://sites.google.com/view/oftn-utagoedb/%E3%83%9B%E3%83%BC%E3%83%A0) (the terms of service are written in Japanese). Next, clone this repository and change `db_root` in `00-svs-world/run.sh` according to your environment. Then move to `00-svs-world` directory and run:

    run.sh --stage 0 --stop-stage 6

The directory structure made by this recipe is the same as kiritan_singing does.

## Sample code
- [Jupyter Notebook](https://gist.github.com/taroushirani/82ec3493dba0aa02e3965625c4c575b3) (Google Colaboratory, comments are written in Japanese)

## Resources

- おふとんP歌声DB配布所: https://sites.google.com/view/oftn-utagoedb/%E3%83%9B%E3%83%BC%E3%83%A0 (Japanese)
