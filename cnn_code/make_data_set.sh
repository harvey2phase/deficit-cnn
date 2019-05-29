for d in training_data/*/ ; do
    echo "$d"
done

ls |sort -R |tail -$N |while read file; do
    # Something involving $file, or you can leave
    # off the while to just get the filenames
done
