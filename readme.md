```shell
CUDE_VISIBLE_DEVICES=3 nohup python train.py dmfb -i=1 --chip_size=10 --drop_num=4 --n_step=100 --fov=7 --block_num=0 --version=0.2 > ./log/20230315test1 2>&1 &
```



```shell
 python3 evaluate.py dmfb --evaluate_task=100 --drop_num=4 --fov=7 --chip_size=10 --block_num=1 --show
```

```shell
CUDE_VISIBLE_DEVICES=3 nohup python train.py dmfb -i=1 --chip_size=10 --drop_num=4 --n_step=100 --fov=7 --block_num=0 --version=0.2 > ./log/20230502testv02 2>&1 &
```

```shell
nohup python train.py dmfb -i=1 --chip_size=10 --drop_num=2 --n_step=100 --fov=7 --block_num=0 --model_dir="./model0.8" --result_dir="./TrainResult0.8" --version=0.2 > ./log/20230519test-2-08 2>&1 &
nohup python train.py dmfb -i=1 --chip_size=10 --drop_num=3 --n_step=100 --fov=7 --block_num=0 --model_dir="./model0.8" --result_dir="./TrainResult0.8" --version=0.2 > ./log/20230519test-3-08 2>&1 &
nohup python train.py dmfb -i=1 --chip_size=10 --drop_num=4 --n_step=100 --fov=7 --block_num=0 --model_dir="./model0.8" --result_dir="./TrainResult0.8" --version=0.2 > ./log/20230519test-4-08 2>&1 &
nohup python train.py dmfb -i=1 --chip_size=10 --drop_num=2 --n_step=100 --fov=7 --block_num=0 --model_dir="./model0.6" --result_dir="./TrainResult0.6" --version=0.2 > ./log/20230519test-2-06 2>&1 &
nohup python train.py dmfb -i=1 --chip_size=10 --drop_num=3 --n_step=100 --fov=7 --block_num=0 --model_dir="./model0.6" --result_dir="./TrainResult0.6" --version=0.2 > ./log/20230519test-3-06 2>&1 &
nohup python train.py dmfb -i=1 --chip_size=10 --drop_num=4 --n_step=100 --fov=7 --block_num=0 --model_dir="./model0.6" --result_dir="./TrainResult0.6" --version=0.2 > ./log/20230519test-4-06 2>&1 &
nohup python train.py dmfb -i=1 --chip_size=10 --drop_num=2 --n_step=100 --fov=7 --block_num=0 --model_dir="./model0.4" --result_dir="./TrainResult0.4" --version=0.2 > ./log/20230519test-2-04 2>&1 &
nohup python train.py dmfb -i=1 --chip_size=10 --drop_num=3 --n_step=100 --fov=7 --block_num=0 --model_dir="./model0.4" --result_dir="./TrainResult0.4" --version=0.2 > ./log/20230519test-3-04 2>&1 &
nohup python train.py dmfb -i=1 --chip_size=10 --drop_num=4 --n_step=100 --fov=7 --block_num=0 --model_dir="./model0.4" --result_dir="./TrainResult0.4" --version=0.2 > ./log/20230519test-4-04 2>&1 &
nohup python train.py dmfb -i=1 --chip_size=10 --drop_num=2 --n_step=100 --fov=7 --block_num=0 --model_dir="./model0.2" --result_dir="./TrainResult0.2" --version=0.2 > ./log/20230519test-2-02 2>&1 &
nohup python train.py dmfb -i=1 --chip_size=10 --drop_num=3 --n_step=100 --fov=7 --block_num=0 --model_dir="./model0.2" --result_dir="./TrainResult0.2" --version=0.2 > ./log/20230519test-3-02 2>&1 &
nohup python train.py dmfb -i=1 --chip_size=10 --drop_num=4 --n_step=100 --fov=7 --block_num=0 --model_dir="./model0.2" --result_dir="./TrainResult0.2" --version=0.2 > ./log/20230519test-4-02 2>&1 &
```

