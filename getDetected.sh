ROOT=.
IMGS=$ROOT/imgs/
RES=$ROOT/detec/

for dir in $(ls $IMGS);
do
	mkdir -p $RES$dir
	for path in $(ls "$IMGS$dir"/*);
	do
		(
			file=$(basename $path)
			res=$(./face_detection_imgs.py haarcascade_frontalface_default.xml $path); 
			echo $path $res;
			echo $path $res >> num_faces_detected.txt;
			if [[ "$res" -gt 0 ]];
			then 
				cp $path $RES$dir/$file;
			fi 
		) & 
	done;
	wait
done;
