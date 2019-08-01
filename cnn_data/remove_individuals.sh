dir="e4_age80/corhort1"
num_to_move=88

ls $dir | sort -R | tail -$num_to_move | while read file; do

    rm $dir/$file

done
