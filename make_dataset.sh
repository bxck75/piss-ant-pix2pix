
# from folder to pix2pix set and train/test
# usage :./make_dataset.sh <images folder> <epochs to train>
# it wil make a  <image_folder>_resize (resized pix2pix training set) and a <image_folder>_train (training metrics) beside the original folder
# index.html in the train folder has the evaluation of the training and test

# Resize source images
python tools/process.py --input_dir $1 --operation resize --output_dir /tmp/preprocess/_resized
# Create images with blank centers
python tools/process.py --input_dir /tmp/preprocess/_resized --operation blank --output_dir /tmp/preprocess/_blank
# Combine resized images with blanked images side by side
python tools/process.py --input_dir /tmp/preprocess/_resized --b_dir  /tmp/preprocess/_blank --operation combine --output_dir  /tmp/preprocess/_resized/_combined
# Split into train/val set
python tools/split.py --dir /tmp/preprocess/_resized/_combined
#echo $1/resized
sudo mkdir -p $1_resize
cp -rf /tmp/preprocess/_resized/_combined/ $1_resize/
#remove tmp files
sudo rm -r /tmp/preprocess
#sudo rm -r /tmp/preprocess_resized
#sudo rm -r /tmp/preprocess_resized_combined
#Training pix2pix
tensorboard --logdir=/root/Bureaublad/data/$1_train & chromium --no-sandbox http://debian:6006 & \
python pix2pix.py --mode train --output_dir $1_train --max_epochs $2 --input_dir $1_resize/preprocess/_resized/_combined/train --which_direction BtoA
#Test
tensorboard --logdir=/root/Bureaublad/data/$1_train & chromium --no-sandbox http://debian:6006 & \
result_url=`python pix2pix.py --mode test --output_dir $1_test --input_dir $1_resize/preprocess_resized_combined/val --checkpoint $1_train` & \
chromium $result_url




