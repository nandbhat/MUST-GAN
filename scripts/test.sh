# pose transfer
python test.py --dataroot /mnt/hdd0/nandan/active/must-gan/MUST-GAN/datasets \
                --pairLst /mnt/hdd0/nandan/active/must-gan/MUST-GAN/datasets/fashion-resize-pairs-test.csv \
                --checkpoints_dir /mnt/hdd0/nandan/active/must-gan/MUST-GAN/check_points \
                --results_dir ./results \
                --name MUST-GAN/ \
                --model MUST --phase test --dataset_mode keypoint --norm instance \
                --batchSize 1 --resize_or_crop no --gpu_ids 0 --BP_input_nc 19 \
                --which_model_netG MUST \
                --which_epoch 157 \

