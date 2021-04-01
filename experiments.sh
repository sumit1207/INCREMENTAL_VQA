#!/usr/bin/env bash

#yes/no + other -> number  // done check log_run_68234422



#yes/no + number -> other  check log number_yes_no
python3 run.py --RUN='train' \
    --SPLIT='train' \
    --MAX_EPOCH=13 \
    --GPU='2' \
    --VERSION='number_yes_no' 



#number + other -> yes/no
# python3 run.py --RUN='train' \
#     --SPLIT='train' \
#     --MAX_EPOCH=13 \
#     --GPU='2' \
#     --VERSION='number_yes_no'    


# // need to make changes in load_data file to include answer of corresponding types.


# python3 run.py \
#     --RUN='val' \
#     --CKPT_V='88684954' \
#     --CKPT_E=39 \
#     --GPU='2' 