#echo Test for version 0.1
#python3 evaDegre.py dmfb --load_model_name 1_ --model_dir=./prev_model --evaluate_epoch=100 --evaluate_task=20 --version=0.1 --per-degrade=0.1 --chip_size=10 --fov=7 --drop_num=2
#python3 evaDegre.py dmfb --load_model_name 1_ --model_dir=./prev_model --evaluate_epoch=100 --evaluate_task=20 --version=0.1 --per-degrade=0.1 --chip_size=10 --fov=7 --drop_num=3
#python3 evaDegre.py dmfb --load_model_name 1_ --model_dir=./prev_model --evaluate_epoch=100 --evaluate_task=20 --version=0.1 --per-degrade=0.1 --chip_size=10 --fov=7 --drop_num=4
#echo Test for version 0.2
#python3 evaDegre.py dmfb --load_model_name 1_ --model_dir=./model --evaluate_epoch=100 --evaluate_task=20 --version=0.2 --per-degrade=0.1 --chip_size=10 --fov=7 --drop_num=2
#python3 evaDegre.py dmfb --load_model_name 1_ --model_dir=./model --evaluate_epoch=100 --evaluate_task=20 --version=0.2 --per-degrade=0.1 --chip_size=10 --fov=7 --drop_num=3
#python3 evaDegre.py dmfb --load_model_name 1_ --model_dir=./model --evaluate_epoch=100 --evaluate_task=20 --version=0.2 --per-degrade=0.1 --chip_size=10 --fov=7 --drop_num=4
echo Test for 2 droplet
python3 evaDegre.py dmfb --load_model_name 1_ --model_dir=./_model0.2 --evaluate_epoch=100 --evaluate_task=20 --version=0.2 --per-degrade=0.1 --chip_size=10 --fov=7 --drop_num=2 --heal_init=0.2
python3 evaDegre.py dmfb --load_model_name 1_ --model_dir=./_model0.4 --evaluate_epoch=100 --evaluate_task=20 --version=0.2 --per-degrade=0.1 --chip_size=10 --fov=7 --drop_num=2 --heal_init=0.4
python3 evaDegre.py dmfb --load_model_name 1_ --model_dir=./_model0.6 --evaluate_epoch=100 --evaluate_task=20 --version=0.2 --per-degrade=0.1 --chip_size=10 --fov=7 --drop_num=2 --heal_init=0.6
python3 evaDegre.py dmfb --load_model_name 1_ --model_dir=./_model0.8 --evaluate_epoch=100 --evaluate_task=20 --version=0.2 --per-degrade=0.1 --chip_size=10 --fov=7 --drop_num=2 --heal_init=0.8